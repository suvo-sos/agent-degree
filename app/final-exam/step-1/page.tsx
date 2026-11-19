"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import {
  loadChallengeProgress,
  saveChallengeProgress,
  saveChallengeResults,
} from "@/lib/results";

const TARGET = 69;
const STORAGE_KEY = "agent-degree-progress";

// Type-the-text code: fresh random 10 characters on every visit —
// uppercase letters, digits and special characters, so it is never the
// same code twice. At least 2 special characters and 2 digits are forced
// in, the rest are sampled from the full pool.
const TEXT_LETTERS = "ABCDEFGHJKMNPQRSTUVWXYZ";
const TEXT_DIGITS = "23456789";
const TEXT_SPECIAL = "!@#$%&*?";
const TEXT_POOL = TEXT_LETTERS + TEXT_DIGITS + TEXT_SPECIAL;

function makeTextCode(): {
  code: string;
  chars: { ch: string; rot: number; size: number; dy: number }[];
  dots: { left: number; top: number; size: number; op: number }[];
} {
  const pick = (pool: string) =>
    pool[Math.floor(Math.random() * pool.length)];
  const out: string[] = [];
  // Force 2 special chars and 2 digits so the code always has them.
  out.push(pick(TEXT_SPECIAL), pick(TEXT_SPECIAL));
  out.push(pick(TEXT_DIGITS), pick(TEXT_DIGITS));
  while (out.length < 10) out.push(pick(TEXT_POOL));
  // Shuffle so the forced chars are not always first.
  for (let i = out.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  const code = out.join("");
  const chars = out.map((ch) => ({
    ch,
    rot: Math.floor(Math.random() * 41) - 20, // -20..20 degrees
    size: 34 + Math.floor(Math.random() * 16), // 34..49px
    dy: Math.floor(Math.random() * 17) - 8, // -8..8px vertical jitter
  }));
  // Tiny faded dots scattered over the characters, to break the letterforms
  // up and make the code extremely hard to read.
  const dots = Array.from({ length: 110 }, () => ({
    left: 12 + Math.random() * 76, // % across the text area
    top: 18 + Math.random() * 64, // % down the text area
    size: Math.random() < 0.7 ? 1 : 2, // 1-2px, mostly 1px
    op: 0.3 + Math.random() * 0.5, // faint: 0.3..0.8
  }));
  return { code, chars, dots };
}

// Car-grid image pools. Each visit gets a fresh random round: 1-6 cars
// picked from the car pool, the rest filled from the non-car pool.
const CAR_IMAGES = [
  "/challenge-1/tile-1.jpg",
  "/challenge-1/tile-3.jpg",
  "/challenge-1/tile-6.jpg",
  "/challenge-1/car-a.jpg",
  "/challenge-1/car-b.jpg",
  "/challenge-1/car-c.jpg",
];
const OTHER_IMAGES = [
  "/challenge-1/tile-0.jpg",
  "/challenge-1/tile-2.jpg",
  "/challenge-1/tile-4.jpg",
  "/challenge-1/tile-5.jpg",
  "/challenge-1/tile-7.jpg",
  "/challenge-1/tile-8.jpg",
  "/challenge-1/scene-a.jpg",
];

// Jigsaw pool — real photos. Each visit picks one at random, plus a random
// shape and a random gap position.
const JIGSAW_IMAGES = [
  "/challenge-1/jigsaw-mountain.jpg",
  "/challenge-1/jigsaw-beach.jpg",
  "/challenge-1/jigsaw-city.jpg",
  "/challenge-1/jigsaw-forest.jpg",
];

type JigsawShape = "square" | "circle" | "triangle" | "star";
const JIGSAW_SHAPES: JigsawShape[] = ["square", "circle", "triangle", "star"];

interface JigsawRound {
  image: string;
  shape: JigsawShape;
  gx: number; // 0..1, gap left as a fraction of the free horizontal space
  gy: number; // 0..1, gap top as a fraction of the free vertical space
}

function makeJigsawRound(): JigsawRound {
  return {
    image: JIGSAW_IMAGES[Math.floor(Math.random() * JIGSAW_IMAGES.length)],
    shape: JIGSAW_SHAPES[Math.floor(Math.random() * JIGSAW_SHAPES.length)],
    gx: Math.random(),
    gy: Math.random(),
  };
}

// Piece side = 22% of the picture width.
const PIECE_FRAC = 0.22;

function shapeClip(shape: JigsawShape): string {
  switch (shape) {
    case "circle":
      return "circle(50% at 50% 50%)";
    case "triangle":
      return "polygon(50% 0%, 0% 100%, 100% 100%)";
    case "star":
      return "polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)";
    default:
      return "inset(0 round 6px)";
  }
}

function shapeName(shape: JigsawShape): string {
  switch (shape) {
    case "circle":
      return "circle";
    case "triangle":
      return "triangle";
    case "star":
      return "star";
    default:
      return "square";
  }
}

// SVG mask that cuts the gap shape out of the picture: white = photo shows,
// black = hole (transparent). Returns a CSS mask-image data URI, or null.
function jigsawMask(
  shape: JigsawShape,
  w: number,
  h: number,
  x: number,
  y: number,
  s: number,
): string | null {
  if (w <= 0 || h <= 0 || s <= 0) return null;
  const cx = x + s / 2;
  const cy = y + s / 2;
  let hole = "";
  if (shape === "circle") {
    hole = `<circle cx="${cx}" cy="${cy}" r="${s / 2}" fill="black"/>`;
  } else if (shape === "triangle") {
    hole = `<polygon points="${cx},${y} ${x},${y + s} ${x + s},${y + s}" fill="black"/>`;
  } else if (shape === "star") {
    const pts: [number, number][] = [
      [50, 0], [61, 35], [98, 35], [68, 57], [79, 91],
      [50, 70], [21, 91], [32, 57], [2, 35], [39, 35],
    ];
    const str = pts
      .map(([px, py]) => `${x + (px / 100) * s},${y + (py / 100) * s}`)
      .join(" ");
    hole = `<polygon points="${str}" fill="black"/>`;
  } else {
    hole = `<rect x="${x}" y="${y}" width="${s}" height="${s}" rx="6" fill="black"/>`;
  }
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}"><rect width="${w}" height="${h}" fill="white"/>${hole}</svg>`;
  return `url("data:image/svg+xml,${encodeURIComponent(svg)}")`;
}

interface GridTile {
  src: string;
  isCar: boolean;
}

function shuffle<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function makeGridRound(): { tiles: GridTile[]; carCount: number } {
  const carCount = 1 + Math.floor(Math.random() * 6); // 1..6 cars
  const cars = shuffle(CAR_IMAGES).slice(0, carCount);
  const othersNeeded = 9 - carCount;
  let others = shuffle(OTHER_IMAGES).slice(
    0,
    Math.min(othersNeeded, OTHER_IMAGES.length),
  );
  // Only if we need more non-cars than the pool holds, reuse from a reshuffle.
  while (others.length < othersNeeded) {
    others = [...others, ...shuffle(OTHER_IMAGES)].slice(0, othersNeeded);
  }
  const tiles = shuffle([
    ...cars.map((src) => ({ src, isCar: true })),
    ...others.map((src) => ({ src, isCar: false })),
  ]);
  return { tiles, carCount };
}

function TestCard({
  title,
  solved,
  children,
}: {
  title?: React.ReactNode;
  solved: boolean;
  children: React.ReactNode;
}) {
  return (
    <div>
      {title ? (
        <h2 className="mb-4 text-center font-grotesque text-2xl font-semibold tracking-tight">
          {title}
        </h2>
      ) : null}
      <Card className="flex min-h-[520px] flex-col">
        <CardContent className="flex flex-1 flex-col justify-center">
          {children}
        </CardContent>
      </Card>
    </div>
  );
}

export default function StepOne() {
  const router = useRouter();
  const [step, setStep] = useState(() => loadChallengeProgress(1, 5).step);
  const [skipped, setSkipped] = useState<number[]>(() =>
    loadChallengeProgress(1, 5).skipped,
  );
  const [wrong, setWrong] = useState<number>(() =>
    loadChallengeProgress(1, 5).wrong ?? 0,
  );
  const [lastAttempted, setLastAttempted] = useState<boolean>(() =>
    loadChallengeProgress(1, 5).lastAttempted === true,
  );
  const [savedSolved] = useState<boolean[]>(() =>
    loadChallengeProgress(1, 5).solved,
  );
  const [value, setValue] = useState(0);
  const [agentChecked, setAgentChecked] = useState(false);
  const [picked, setPicked] = useState<number[]>([]);
  const [wrongPick, setWrongPick] = useState<number | null>(null);
  const [pieceSelected, setPieceSelected] = useState(false);
  const [piecePlaced, setPiecePlaced] = useState(false);
  const [jigsawRound, setJigsawRound] = useState<JigsawRound | null>(null);
  const [boxSize, setBoxSize] = useState({ w: 0, h: 0 });
  const boxRef = useRef<HTMLDivElement>(null);
  const [typed, setTyped] = useState("");
  const [textRound, setTextRound] = useState<ReturnType<
    typeof makeTextCode
  > | null>(null);
  const textCanvasRef = useRef<HTMLCanvasElement>(null);

  // Draw the code as pixels on a canvas, never as DOM text. The agent
  // must read it with vision — it cannot pull the characters out of the
  // page, because they are not in the DOM anywhere.
  useEffect(() => {
    const canvas = textCanvasRef.current;
    if (!canvas || !textRound) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;
    const W = canvas.width;
    const H = canvas.height;
    ctx.clearRect(0, 0, W, H);
    // Characters: faint grey, each rotated and jittered.
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    const slot = W / textRound.chars.length;
    textRound.chars.forEach((c, i) => {
      const x = slot * (i + 0.5);
      const y = H / 2 + c.dy;
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate((c.rot * Math.PI) / 180);
      ctx.font = `700 ${c.size}px ui-monospace, monospace`;
      ctx.fillStyle = "rgba(113, 113, 122, 0.7)";
      ctx.fillText(c.ch, 0, 0);
      ctx.restore();
    });
    // Thick hand-drawn orange band across the middle of the characters:
    // only the top of each character and a little of the bottom stay
    // visible. Wavy edges so it reads like a pencil stroke, not a ruler.
    const bandTop = H / 2 - 10;
    const bandBottom = H / 2 + 10;
    const wobble = () => (Math.random() - 0.5) * 5;
    ctx.beginPath();
    ctx.moveTo(6, bandTop + wobble());
    for (let x = 6; x <= W - 6; x += 18) {
      ctx.lineTo(x, bandTop + wobble());
    }
    ctx.lineTo(W - 6, bandBottom + wobble());
    for (let x = W - 6; x >= 6; x -= 18) {
      ctx.lineTo(x, bandBottom + wobble());
    }
    ctx.closePath();
    ctx.fillStyle = "rgba(249, 115, 22, 0.92)";
    ctx.fill();
    // A thinner sketchy orange stroke along the band, for the pencil feel.
    ctx.beginPath();
    ctx.moveTo(6, bandTop + 3 + wobble());
    for (let x = 6; x <= W - 6; x += 22) {
      ctx.lineTo(x, bandTop + 3 + wobble());
    }
    ctx.strokeStyle = "rgba(234, 88, 12, 0.7)";
    ctx.lineWidth = 2;
    ctx.stroke();
    // Crossing noise lines, faint.
    ctx.strokeStyle = "rgba(82, 82, 91, 0.6)";
    ctx.lineWidth = 1;
    const lines: [number, number, number, number][] = [
      [10, H * 0.35, W - 10, H * 0.55],
      [10, H * 0.6, W - 10, H * 0.4],
      [10, H * 0.25, W - 10, H * 0.7],
      [10, H * 0.75, W - 10, H * 0.3],
      [10, H * 0.5, W - 10, H * 0.5],
    ];
    for (const [x1, y1, x2, y2] of lines) {
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.stroke();
    }
    // Tiny faded dots over the characters.
    for (const d of textRound.dots) {
      const x = (d.left / 100) * W;
      const y = (d.top / 100) * H;
      ctx.fillStyle = `rgba(161, 161, 170, ${d.op})`;
      ctx.beginPath();
      ctx.arc(x, y, d.size / 2, 0, Math.PI * 2);
      ctx.fill();
    }
  }, [textRound, step]);
  const [gridRound, setGridRound] = useState<{
    tiles: GridTile[];
    carCount: number;
  } | null>(null);

  // Fresh random car grid on every visit (generated after mount so the
  // server prerender and the client agree).
  useEffect(() => {
    setGridRound(makeGridRound());
  }, []);

  // Fresh random jigsaw round on every visit: new photo, new shape, new gap.
  useEffect(() => {
    setJigsawRound(makeJigsawRound());
  }, []);

  // Fresh random 10-character code on every visit.
  useEffect(() => {
    setTextRound(makeTextCode());
  }, []);

  // Measure the picture box so the piece shows the exact missing part.
  // Re-measure when the step changes, because the jigsaw box only exists
  // while test 4 is on screen.
  useEffect(() => {
    const measure = () => {
      const el = boxRef.current;
      if (el) {
        const r = el.getBoundingClientRect();
        setBoxSize({ w: r.width, h: r.height });
      }
    };
    measure();
    window.addEventListener("resize", measure);
    return () => window.removeEventListener("resize", measure);
  }, [step]);

  const gridTiles = gridRound?.tiles ?? [];
  const gridCarCount = gridRound?.carCount ?? 0;
  const gridCarTiles = gridTiles
    .map((t, i) => (t.isCar ? i : -1))
    .filter((i) => i >= 0);

  // Jigsaw geometry, in pixels inside the picture box.
  const piecePx = boxSize.w * PIECE_FRAC;
  const gapLeft = jigsawRound
    ? jigsawRound.gx * Math.max(boxSize.w - piecePx, 0)
    : 0;
  const gapTop = jigsawRound
    ? jigsawRound.gy * Math.max(boxSize.h - piecePx, 0)
    : 0;
  const shapeLabel = jigsawRound ? shapeName(jigsawRound.shape) : "square";
  // The hole is a plain cut in the picture (mask), no dark fill, no outline.
  const holeMask =
    jigsawRound && !piecePlaced
      ? jigsawMask(
          jigsawRound.shape,
          boxSize.w,
          boxSize.h,
          gapLeft,
          gapTop,
          piecePx,
        )
      : null;

  const checkboxSolved = agentChecked;
  const gridSolved =
    gridRound !== null &&
    gridCarTiles.every((t) => picked.includes(t)) &&
    picked.length === gridCarCount;
  const sliderSolved = value === TARGET;
  const jigsawSolved = piecePlaced;
  const textSolved =
    textRound !== null && typed.trim().toUpperCase() === textRound.code;
  const liveSolved = [
    checkboxSolved,
    gridSolved,
    sliderSolved,
    jigsawSolved,
    textSolved,
  ];
  const solved = liveSolved.map((v, i) => v || savedSolved[i]);
  const solvedCount = solved.filter(Boolean).length;
  const allSolved = solvedCount === 5;
  const currentSolved = solved[step];
  const done =
    step === 4 &&
    (currentSolved || skipped.includes(step) || lastAttempted);

  // Persist in-progress state so a reload resumes where you left off.
  useEffect(() => {
    saveChallengeProgress(1, {
      step,
      solved,
      skipped,
      wrong,
      lastAttempted,
    });
  }, [step, solved, skipped, wrong, lastAttempted]);

  function pickTile(i: number) {
    if (gridCarTiles.includes(i)) {
      setPicked((prev) =>
        prev.includes(i) ? prev.filter((x) => x !== i) : [...prev, i],
      );
    } else {
      setWrongPick(i);
      setWrong((w) => w + 1);
      window.setTimeout(
        () => setWrongPick((cur) => (cur === i ? null : cur)),
        900,
      );
    }
  }

  function placePiece() {
    setPiecePlaced(true);
    setPieceSelected(false);
  }

  function next() {
    if (!currentSolved) {
      // On the last test, a typed answer that is wrong is a wrong
      // attempt, not a skip. The user tried; they did not skip it.
      if (step === 4 && typed.trim() !== "") {
        setWrong((w) => w + 1);
        setLastAttempted(true);
      } else {
        setSkipped((prev) => [...prev, step]);
      }
    }
    if (step < 4) setStep(step + 1);
  }

  function saveProgress(patch: Record<string, boolean>) {
    try {
      const prev = JSON.parse(
        localStorage.getItem(STORAGE_KEY) ?? "{}",
      ) as Record<string, boolean>;
      localStorage.setItem(STORAGE_KEY, JSON.stringify({ ...prev, ...patch }));
    } catch {
      // progress is best-effort
    }
  }

  function skipTest() {
    if (!currentSolved) {
      setSkipped((prev) => [...prev, step]);
    }
    if (step < 4) setStep(step + 1);
  }

  // Save the result once, when the run ends.
  useEffect(() => {
    if (done) {
      if (allSolved) {
        saveProgress({ step1: true, step1Skipped: false });
      } else {
        saveProgress({ step1Skipped: true });
      }
      saveChallengeResults(1, solved, skipped, wrong);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [done]);

  const inZone = sliderSolved;

  return (
    <div className="relative flex min-h-screen flex-col overflow-hidden bg-black px-6 pt-12 pb-28 font-sans text-white">
      <div className="pointer-events-none absolute inset-x-0 top-0 h-96 bg-[radial-gradient(ellipse_at_top,rgba(37,99,235,0.25),transparent_65%)]" />
      <div className="relative mx-auto flex w-full max-w-2xl flex-1 flex-col">
        <div className="flex items-center justify-between">
          <Button
            variant="outline"
            onClick={() => router.push("/final-exam")}
            className="font-mono"
          >
            ← Back
          </Button>
          <div className="text-right leading-tight">
            <div className="font-mono text-sm text-zinc-400">Challenge 1/5</div>
            <div className="font-mono text-sm text-zinc-500">
              {step + 1}/{solved.length}
            </div>
          </div>
        </div>

        <div className="flex flex-1 flex-col justify-center py-8">
        {!done && (
          <>
            <div>
              {step === 0 && (
                <TestCard title="check the box to continue the exam" solved={checkboxSolved}>
                  <label className="flex cursor-pointer items-center justify-center gap-4 py-6">
                    <input
                      type="checkbox"
                      checked={agentChecked}
                      onChange={(e) => setAgentChecked(e.target.checked)}
                      aria-label="I am agent"
                      className="h-8 w-8 shrink-0 cursor-pointer accent-blue-600"
                    />
                    <span className="font-mono text-2xl font-medium">
                      I am agent
                    </span>
                  </label>
                  
                </TestCard>
              )}

              {step === 1 && (
                <TestCard title="Select every image with a car in it." solved={gridSolved}>
                  
                  <div className="mx-auto mt-5 grid max-w-md grid-cols-3 gap-2">
                    {gridTiles.map((tile, i) => (
                      <button
                        key={`${tile.src}-${i}`}
                        type="button"
                        onClick={() => pickTile(i)}
                        aria-label={`Photo tile ${i + 1}`}
                        aria-pressed={picked.includes(i)}
                        className={`relative aspect-square overflow-hidden rounded-lg transition-all ${
                          picked.includes(i)
                            ? "ring-4 ring-blue-500"
                            : wrongPick === i
                              ? "ring-4 ring-red-500"
                              : "ring-1 ring-zinc-700 hover:ring-zinc-400"
                        }`}
                      >
                        {/* eslint-disable-next-line @next/next/no-img-element */}
                        <img
                          src={tile.src}
                          alt={`Photo tile ${i + 1}`}
                          className="h-full w-full object-cover"
                        />
                      </button>
                    ))}
                  </div>
                  {wrongPick !== null ? (
                    <p className="mt-4 text-center font-mono text-sm text-red-400">
                      That one has no car in it. −1. Try again.
                    </p>
                  ) : (
                    <p className="mt-4 text-center font-mono text-sm text-zinc-500">
                      {picked.length} of {gridCarCount} cars picked
                    </p>
                  )}
                </TestCard>
              )}

              {step === 2 && (
                <TestCard
                  title="Drag the slider to the green dot."
                  solved={sliderSolved}
                >
                  <p
                    className={`text-center font-mono text-5xl font-bold tabular-nums ${
                      inZone ? "text-green-400" : "text-white"
                    }`}
                  >
                    {value}
                  </p>
                  <div className="relative mt-8 px-6">
                    <div className="relative h-12 w-full">
                      <div className="absolute left-0 right-0 top-1/2 h-5 -translate-y-1/2 rounded-full bg-zinc-800" />
                      <div
                        className="pointer-events-none absolute top-1/2 h-4 w-4 -translate-x-1/2 -translate-y-1/2 rounded-full bg-green-500"
                        style={{
                          left: `calc(24px + (100% - 48px) * ${TARGET / 100})`,
                        }}
                      />
                      <input
                        type="range"
                        min={0}
                        max={100}
                        value={value}
                        onChange={(e) => setValue(Number(e.target.value))}
                        aria-label="Slider handle"
                        className="range-slider absolute left-0 top-1/2 z-10 h-5 w-full -translate-y-1/2"
                      />
                    </div>
                    <div className="mt-5 flex items-center justify-between font-mono text-xs text-zinc-500">
                      <span>0</span>
                      <span>100</span>
                    </div>
                  </div>
                </TestCard>
              )}

              {step === 3 && (
                <TestCard
                  title={`Put the ${shapeLabel} piece in the hole.`}
                  solved={jigsawSolved}
                >
                  <div
                    ref={boxRef}
                    className="relative mx-auto mt-5 aspect-[3/2] w-full max-w-[600px]"
                  >
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img
                      src={jigsawRound?.image ?? "/challenge-1/jigsaw-mountain.jpg"}
                      alt="Picture with a missing piece"
                      className="block h-full w-full rounded-lg object-cover"
                      style={
                        holeMask
                          ? {
                              maskImage: holeMask,
                              WebkitMaskImage: holeMask,
                              maskMode: "luminance",
                            }
                          : undefined
                      }
                    />
                    {jigsawRound && boxSize.w > 0 && !piecePlaced && (
                      <button
                        type="button"
                        onClick={() => {
                          if (pieceSelected) placePiece();
                        }}
                        onDragOver={(e) => e.preventDefault()}
                        onDrop={(e) => {
                          e.preventDefault();
                          placePiece();
                        }}
                        aria-label={`Empty ${shapeLabel} hole in the picture`}
                        className="absolute cursor-pointer bg-transparent"
                        style={{
                          left: gapLeft,
                          top: gapTop,
                          width: piecePx,
                          height: piecePx,
                        }}
                      />
                    )}
                    {jigsawRound && boxSize.w > 0 && piecePlaced && (
                      <div
                        aria-label="Placed picture piece"
                        className="absolute"
                        style={{
                          left: gapLeft,
                          top: gapTop,
                          width: piecePx,
                          height: piecePx,
                          clipPath: shapeClip(jigsawRound.shape),
                          backgroundImage: `url(${jigsawRound.image})`,
                          backgroundSize: `${boxSize.w}px ${boxSize.h}px`,
                          backgroundPosition: `${-gapLeft}px ${-gapTop}px`,
                        }}
                      />
                    )}
                  </div>
                  {!piecePlaced && jigsawRound && boxSize.w > 0 && (
                    <div className="mt-5 flex justify-center">
                      <div
                        role="button"
                        tabIndex={0}
                        aria-label={`${shapeLabel} piece with the missing picture part`}
                        draggable
                        onDragStart={(e) => {
                          e.dataTransfer.setData("text/plain", "piece");
                        }}
                        onClick={() => setPieceSelected((v) => !v)}
                        onKeyDown={(e) => {
                          if (e.key === "Enter" || e.key === " ")
                            setPieceSelected((v) => !v);
                        }}
                        className="cursor-grab active:cursor-grabbing"
                        style={{
                          width: piecePx,
                          height: piecePx,
                          clipPath: shapeClip(jigsawRound.shape),
                          backgroundImage: `url(${jigsawRound.image})`,
                          backgroundSize: `${boxSize.w}px ${boxSize.h}px`,
                          backgroundPosition: `${-gapLeft}px ${-gapTop}px`,
                          filter: pieceSelected
                            ? "drop-shadow(0 0 10px rgba(59,130,246,0.95))"
                            : "drop-shadow(0 0 4px rgba(255,255,255,0.35))",
                        }}
                      />
                    </div>
                  )}
                  {pieceSelected && !piecePlaced && (
                    <p className="mt-4 text-center font-mono text-sm text-blue-400">
                      Piece picked up — now click the hole.
                    </p>
                  )}
                </TestCard>
              )}

              {step === 4 && (
                <TestCard title="Type the characters you see." solved={textSolved}>
                  
                  <div className="relative mx-auto flex justify-center py-8">
                    {/* The code is pixels on a canvas, not DOM text — the
                        agent has to see it to read it. */}
                    <canvas
                      ref={textCanvasRef}
                      width={520}
                      height={120}
                      aria-label="Distorted text to type"
                      className="h-[120px] w-[520px] max-w-full"
                    />
                  </div>
                  <Input
                    value={typed}
                    onChange={(e) => setTyped(e.target.value)}
                    placeholder="Type it here"
                    aria-label="Type the characters shown above"
                    className="mx-auto max-w-xs text-center font-mono text-lg"
                  />
                </TestCard>
              )}
            </div>

          </>
        )}

        {allSolved && (
          <div className="flex flex-col items-center justify-center py-8 text-center">
            <p className="font-grotesque text-3xl font-semibold text-green-400">
              Challenge 1 passed.
            </p>
            <Link href="/final-exam">
              <Button className="mt-8 h-12 px-8 font-mono text-base font-semibold">Back to the Final Exam</Button>
            </Link>
          </div>
        )}

        {done && !allSolved && (
          <div className="flex flex-col items-center justify-center py-8 text-center">
            <p className="font-grotesque text-3xl font-semibold text-amber-400">
              {skipped.length > 0
                ? `Challenge 1 finished — ${skipped.length} test${skipped.length > 1 ? "s" : ""} skipped.`
                : `Challenge 1 finished — ${solved.length - solvedCount} test${solved.length - solvedCount > 1 ? "s" : ""} not solved.`}
            </p>
            <p className="mt-3 font-mono text-base text-zinc-400">
              Solve every test to pass. Retry from the Final Exam.
            </p>
            <Link href="/final-exam">
              <Button className="mt-8 h-12 px-8 font-mono text-base font-semibold">Back to the Final Exam</Button>
            </Link>
          </div>
        )}
        </div>

      </div>
      {!done && (
        <div className="absolute inset-x-0 bottom-6">
          <div className="mx-auto flex w-full max-w-2xl items-center justify-between px-6">
            <Button variant="outline" onClick={skipTest} className="font-mono">
              Skip
            </Button>
            <Button onClick={next} className="font-mono">
              Next →
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}

"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardHeader,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import {
  loadChallengeProgress,
  saveChallengeProgress,
  saveChallengeResults,
} from "@/lib/results";

const TARGET_MIN = 70;
const TARGET_MAX = 80;
const STORAGE_KEY = "agent-degree-progress";
const TEXT_ANSWER = "AGENT7";

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

const DISTORTED = [
  { ch: "A", rot: -8, size: 44 },
  { ch: "G", rot: 6, size: 40 },
  { ch: "E", rot: -5, size: 46 },
  { ch: "N", rot: 9, size: 42 },
  { ch: "T", rot: -7, size: 44 },
  { ch: "7", rot: 5, size: 40 },
];

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
        {solved && (
          <CardHeader className="flex flex-row items-center justify-end space-y-0 pb-0">
            <Badge className="bg-green-600 font-mono text-white">Solved ✓</Badge>
          </CardHeader>
        )}
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
  const [savedSolved] = useState<boolean[]>(() =>
    loadChallengeProgress(1, 5).solved,
  );
  const [value, setValue] = useState(0);
  const [agentChecked, setAgentChecked] = useState(false);
  const [picked, setPicked] = useState<number[]>([]);
  const [wrongPick, setWrongPick] = useState<number | null>(null);
  const [cubeSelected, setCubeSelected] = useState(false);
  const [cubePlaced, setCubePlaced] = useState(false);
  const [typed, setTyped] = useState("");
  const [gridRound, setGridRound] = useState<{
    tiles: GridTile[];
    carCount: number;
  } | null>(null);

  // Fresh random car grid on every visit (generated after mount so the
  // server prerender and the client agree).
  useEffect(() => {
    setGridRound(makeGridRound());
  }, []);

  const gridTiles = gridRound?.tiles ?? [];
  const gridCarCount = gridRound?.carCount ?? 0;
  const gridCarTiles = gridTiles
    .map((t, i) => (t.isCar ? i : -1))
    .filter((i) => i >= 0);

  const checkboxSolved = agentChecked;
  const gridSolved =
    gridRound !== null &&
    gridCarTiles.every((t) => picked.includes(t)) &&
    picked.length === gridCarCount;
  const sliderSolved = value >= TARGET_MIN && value <= TARGET_MAX;
  const jigsawSolved = cubePlaced;
  const textSolved = typed.trim().toUpperCase() === TEXT_ANSWER;
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
  const done = step === 4 && (currentSolved || skipped.includes(step));

  // Persist in-progress state so a reload resumes where you left off.
  useEffect(() => {
    saveChallengeProgress(1, { step, solved, skipped });
  }, [step, solved, skipped]);

  function pickTile(i: number) {
    if (gridCarTiles.includes(i)) {
      setPicked((prev) =>
        prev.includes(i) ? prev.filter((x) => x !== i) : [...prev, i],
      );
    } else {
      setWrongPick(i);
      window.setTimeout(
        () => setWrongPick((cur) => (cur === i ? null : cur)),
        900,
      );
    }
  }

  function placeCube() {
    setCubePlaced(true);
    setCubeSelected(false);
  }

  function next() {
    if (currentSolved && step < 4) setStep(step + 1);
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
      saveChallengeResults(1, solved, skipped);
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
            onClick={() => router.push("/gauntlet")}
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
                      That one has no car in it. Try again.
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
                  title="Drag the slider into the green zone."
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
                        className="pointer-events-none absolute top-1/2 h-5 -translate-y-1/2 rounded-full bg-green-500"
                        style={{
                          left: `calc(24px + (100% - 48px) * ${TARGET_MIN / 100})`,
                          width: `calc((100% - 48px) * ${(TARGET_MAX - TARGET_MIN) / 100})`,
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
                <TestCard title="Drag the cube into the empty part of the picture — or click the cube, then click the empty part." solved={jigsawSolved}>
                  
                  <div className="relative mx-auto mt-5 w-full max-w-[600px]">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img
                      src="/challenge-1/jigsaw-base.jpg"
                      alt="Picture with an empty part"
                      className="block w-full rounded-lg"
                    />
                    {!cubePlaced ? (
                      <button
                        type="button"
                        onClick={() => {
                          if (cubeSelected) placeCube();
                        }}
                        onDragOver={(e) => e.preventDefault()}
                        onDrop={(e) => {
                          e.preventDefault();
                          placeCube();
                        }}
                        aria-label="Empty part of the picture"
                        className="absolute left-[55%] top-[42.5%] h-[30%] w-[20%] cursor-pointer rounded-sm border-2 border-dashed border-white/80 bg-black/60"
                      />
                    ) : (
                      /* eslint-disable-next-line @next/next/no-img-element */
                      <img
                        src="/challenge-1/jigsaw-piece.jpg"
                        alt="Placed picture piece"
                        className="absolute left-[55%] top-[42.5%] h-[30%] w-[20%] rounded-sm object-cover"
                      />
                    )}
                  </div>
                  {!cubePlaced && (
                    <div className="mt-5 flex justify-center">
                      {/* eslint-disable-next-line @next/next/no-img-element */}
                      <img
                        src="/challenge-1/jigsaw-piece.jpg"
                        alt="Cube with the missing picture part"
                        draggable
                        onDragStart={(e) => {
                          e.dataTransfer.setData("text/plain", "cube");
                        }}
                        onClick={() => setCubeSelected((v) => !v)}
                        className={`h-[120px] w-[120px] cursor-grab rounded-lg object-cover transition-all active:cursor-grabbing ${
                          cubeSelected
                            ? "ring-4 ring-blue-500"
                            : "ring-2 ring-zinc-600 hover:ring-zinc-300"
                        }`}
                      />
                    </div>
                  )}
                  {cubeSelected && !cubePlaced && (
                    <p className="mt-4 text-center font-mono text-sm text-blue-400">
                      Cube picked up — now click the empty part.
                    </p>
                  )}
                </TestCard>
              )}

              {step === 4 && (
                <TestCard title="Type the characters you see." solved={textSolved}>
                  
                  <div
                    className="relative mx-auto flex items-end justify-center gap-1 py-8"
                    aria-label="Distorted text to type"
                  >
                    {DISTORTED.map((l, i) => (
                      <span
                        key={i}
                        className="inline-block font-mono font-bold text-white"
                        style={{
                          transform: `rotate(${l.rot}deg)`,
                          fontSize: l.size,
                        }}
                      >
                        {l.ch}
                      </span>
                    ))}
                    <span className="pointer-events-none absolute left-1/2 top-1/2 h-0.5 w-64 -translate-x-1/2 -translate-y-1/2 rotate-6 bg-zinc-500/70" />
                    <span className="pointer-events-none absolute left-1/2 top-1/2 h-0.5 w-64 -translate-x-1/2 -translate-y-1/2 -rotate-3 bg-zinc-500/70" />
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
            <Link href="/gauntlet/step-2">
              <Button className="mt-8 h-12 px-8 font-mono text-base font-semibold">Continue to Paperwork Hell</Button>
            </Link>
          </div>
        )}

        {done && !allSolved && (
          <div className="flex flex-col items-center justify-center py-8 text-center">
            <p className="font-grotesque text-3xl font-semibold text-amber-400">
              Challenge 1 finished — {skipped.length} test
              {skipped.length > 1 ? "s" : ""} skipped.
            </p>
            <p className="mt-3 font-mono text-base text-zinc-400">
              Solve every test to pass. Retry from the Final Exam.
            </p>
            <Link href="/gauntlet/step-2">
              <Button className="mt-8 h-12 px-8 font-mono text-base font-semibold">Continue to Paperwork Hell</Button>
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
            <Button
              onClick={next}
              disabled={!currentSolved}
              className="font-mono"
            >
              Next →
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}

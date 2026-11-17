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
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Progress } from "@/components/ui/progress";
import { StepPagination } from "@/components/step-pagination";

const TARGET_MIN = 70;
const TARGET_MAX = 80;
const STORAGE_KEY = "agent-degree-progress";
const CAR_TILES = [1, 3, 6];
const TEXT_ANSWER = "AGENT7";

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
  title: string;
  solved: boolean;
  children: React.ReactNode;
}) {
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between space-y-0">
        <div>
          <CardTitle className="font-grotesque">{title}</CardTitle>
        </div>
        {solved ? (
          <Badge className="bg-green-600 font-mono text-white">Solved ✓</Badge>
        ) : (
          <Badge variant="secondary" className="font-mono">
            Pending
          </Badge>
        )}
      </CardHeader>
      <CardContent>{children}</CardContent>
    </Card>
  );
}

export default function StepOne() {
  const router = useRouter();
  const [step, setStep] = useState(0);
  const [value, setValue] = useState(0);
  const [agentChecked, setAgentChecked] = useState(false);
  const [picked, setPicked] = useState<number[]>([]);
  const [wrongPick, setWrongPick] = useState<number | null>(null);
  const [cubeSelected, setCubeSelected] = useState(false);
  const [cubePlaced, setCubePlaced] = useState(false);
  const [typed, setTyped] = useState("");

  const checkboxSolved = agentChecked;
  const gridSolved =
    CAR_TILES.every((t) => picked.includes(t)) && picked.length === 3;
  const sliderSolved = value >= TARGET_MIN && value <= TARGET_MAX;
  const jigsawSolved = cubePlaced;
  const textSolved = typed.trim().toUpperCase() === TEXT_ANSWER;
  const solved = [
    checkboxSolved,
    gridSolved,
    sliderSolved,
    jigsawSolved,
    textSolved,
  ];
  const solvedCount = solved.filter(Boolean).length;
  const allSolved = solvedCount === 5;
  const currentSolved = solved[step];

  function pickTile(i: number) {
    if (CAR_TILES.includes(i)) {
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

  function skip() {
    saveProgress({ step1Skipped: true });
    router.push("/gauntlet");
  }

  // Save the pass once, when all five tests are solved.
  useEffect(() => {
    if (allSolved) {
      saveProgress({ step1: true, step1Skipped: false });
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [allSolved]);

  const inZone = sliderSolved;

  return (
    <div className="relative min-h-screen overflow-hidden bg-black px-6 py-12 font-sans text-white">
      <div className="pointer-events-none absolute inset-x-0 top-0 h-96 bg-[radial-gradient(ellipse_at_top,rgba(37,99,235,0.25),transparent_65%)]" />
      <div className="relative mx-auto w-full max-w-2xl">
        <div className="flex justify-start">
          <Button
            variant="outline"
            onClick={() => router.push("/gauntlet")}
            className="font-mono"
          >
            ← Back
          </Button>
        </div>
        <div className="mt-10 text-center">
          <p className="font-mono text-xs font-semibold tracking-[0.3em] text-blue-400">
            CHALLENGE 1 OF 5
          </p>
          <h1 className="mt-3 font-grotesque text-4xl font-semibold tracking-tight sm:text-5xl">
            Challenge 1
          </h1>
          <p className="mt-3 font-mono text-sm text-zinc-400">
            Five tests. This exam is built for AI agents. Taking it is the
            whole point.
          </p>
          <div className="mx-auto mt-6 max-w-md">
            <div className="flex items-center justify-between font-mono text-sm">
              <span className="text-zinc-400">Tests solved</span>
              <span className="font-medium text-white">
                {solvedCount} of 5
              </span>
            </div>
            <Progress value={(solvedCount / 5) * 100} className="mt-2" />
          </div>
        </div>

        {!allSolved && (
          <>
            <div className="mt-10">
              {step === 0 && (
                <TestCard title="I Am Agent" solved={checkboxSolved}>
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
                  <p className="text-center font-mono text-sm text-zinc-500">
                    check the box to continue the exam
                  </p>
                </TestCard>
              )}

              {step === 1 && (
                <TestCard title="Pick the Cars" solved={gridSolved}>
                  <p className="text-center font-mono text-lg font-medium">
                    Select every image with a car in it.
                  </p>
                  <div className="mx-auto mt-5 grid max-w-md grid-cols-3 gap-2">
                    {Array.from({ length: 9 }, (_, i) => (
                      <button
                        key={i}
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
                          src={`/challenge-1/tile-${i}.jpg`}
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
                      {picked.length} of 3 cars picked
                    </p>
                  )}
                </TestCard>
              )}

              {step === 2 && (
                <TestCard title="The Slider" solved={sliderSolved}>
                  <p
                    className={`text-center font-mono text-5xl font-bold tabular-nums ${
                      inZone ? "text-green-400" : "text-white"
                    }`}
                  >
                    {value}
                  </p>
                  <p className="mt-1 text-center font-mono text-sm text-zinc-500">
                    drag into the green · 70–80
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
                <TestCard title="Complete the Picture" solved={jigsawSolved}>
                  <p className="text-center font-mono text-lg font-medium">
                    Drag the cube into the empty part of the picture — or click
                    the cube, then click the empty part.
                  </p>
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
                <TestCard title="Type the Text" solved={textSolved}>
                  <p className="text-center font-mono text-lg font-medium">
                    Type the characters you see.
                  </p>
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

            <div className="mt-8 flex items-center justify-between">
              <Button variant="outline" onClick={skip} className="font-mono">
                Skip this challenge →
              </Button>
              <Button
                onClick={next}
                disabled={!currentSolved}
                className="font-mono"
              >
                Next →
              </Button>
            </div>
          </>
        )}

        {allSolved && (
          <div className="mt-10 rounded-2xl border border-green-500/40 bg-green-500/10 p-6 text-center">
            <p className="font-grotesque text-xl font-semibold text-green-400">
              Challenge 1 passed.
            </p>
            <Link href="/gauntlet">
              <Button className="mt-5 font-mono">Back to Gauntlet</Button>
            </Link>
          </div>
        )}

        <div className="mt-12">
          <StepPagination current={1} available={3} />
        </div>
      </div>
    </div>
  );
}

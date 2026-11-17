"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Progress } from "@/components/ui/progress";

const TARGET_MIN = 70;
const TARGET_MAX = 80;
const STORAGE_KEY = "agent-degree-progress";
const MATH_ANSWER = "14";
const BUTTON_OPTIONS = ["Cancel", "Delete", "Continue", "Submit"];

export default function StepOne() {
  const router = useRouter();
  const [value, setValue] = useState(0);
  const [buttonPressed, setButtonPressed] = useState<string | null>(null);
  const [math, setMath] = useState("");
  const trackRef = useRef<HTMLDivElement>(null);

  const sliderSolved = value >= TARGET_MIN && value <= TARGET_MAX;
  const buttonSolved = buttonPressed === "Continue";
  const mathSolved = math.trim() === MATH_ANSWER;
  const solvedCount = [sliderSolved, buttonSolved, mathSolved].filter(
    Boolean,
  ).length;
  const allSolved = solvedCount === 3;

  function valueFromClientX(clientX: number) {
    const track = trackRef.current;
    if (!track) return 0;
    const rect = track.getBoundingClientRect();
    const ratio = (clientX - rect.left) / rect.width;
    return Math.max(0, Math.min(100, Math.round(ratio * 100)));
  }

  function onHandlePointerDown(e: React.PointerEvent<HTMLDivElement>) {
    e.preventDefault();
    const handle = e.currentTarget;
    handle.setPointerCapture(e.pointerId);
    const move = (ev: PointerEvent) => setValue(valueFromClientX(ev.clientX));
    const up = () => {
      handle.removeEventListener("pointermove", move);
      handle.removeEventListener("pointerup", up);
    };
    handle.addEventListener("pointermove", move);
    handle.addEventListener("pointerup", up);
  }

  function onTrackPointerDown(e: React.PointerEvent<HTMLDivElement>) {
    setValue(valueFromClientX(e.clientX));
  }

  function onHandleKeyDown(e: React.KeyboardEvent<HTMLDivElement>) {
    if (e.key === "ArrowRight" || e.key === "ArrowUp") {
      e.preventDefault();
      setValue((v) => Math.min(100, v + 1));
    } else if (e.key === "ArrowLeft" || e.key === "ArrowDown") {
      e.preventDefault();
      setValue((v) => Math.max(0, v - 1));
    } else if (e.key === "PageUp") {
      e.preventDefault();
      setValue((v) => Math.min(100, v + 10));
    } else if (e.key === "PageDown") {
      e.preventDefault();
      setValue((v) => Math.max(0, v - 10));
    } else if (e.key === "Home") {
      e.preventDefault();
      setValue(0);
    } else if (e.key === "End") {
      e.preventDefault();
      setValue(100);
    }
  }

  function pressButton(label: string) {
    setButtonPressed(label);
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

  // Save the pass once, when all three trials are solved.
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
        <div className="text-center">
          <p className="text-xs font-semibold tracking-[0.3em] text-blue-400">
            STEP 1 OF 5 · THE GAUNTLET
          </p>
          <h1 className="mt-3 text-4xl font-semibold tracking-tight sm:text-5xl">
            Slide Into the Green
          </h1>
          <p className="mx-auto mt-3 max-w-md text-base text-zinc-400">
            Three trials. Solve them all, or skip the step.
          </p>
          <p className="mx-auto mt-2 max-w-md text-sm text-zinc-500">
            This exam is built for AI agents. Taking it is the whole point.
          </p>
          <div className="mx-auto mt-6 max-w-md">
            <div className="flex items-center justify-between text-sm">
              <span className="text-zinc-400">Trials solved</span>
              <span className="font-medium text-white">
                {solvedCount} of 3
              </span>
            </div>
            <Progress value={(solvedCount / 3) * 100} className="mt-2" />
          </div>
        </div>

        <div className="mt-10 space-y-5">
          {/* Trial 1 — slider */}
          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0">
              <div>
                <CardTitle>Trial 1 · The Slider</CardTitle>
                <CardDescription>
                  Set the slider inside the green zone.
                </CardDescription>
              </div>
              {sliderSolved ? (
                <Badge className="bg-green-600 text-white">Solved ✓</Badge>
              ) : (
                <Badge variant="secondary">Pending</Badge>
              )}
            </CardHeader>
            <CardContent>
              <p
                className={`text-center text-5xl font-bold tabular-nums ${
                  inZone ? "text-green-400" : "text-white"
                }`}
              >
                {value}
              </p>
              <p className="mt-1 text-center text-sm text-zinc-500">
                drag it into the green
              </p>
              <div className="relative mt-8 px-6">
                <div
                  ref={trackRef}
                  onPointerDown={onTrackPointerDown}
                  className="relative h-5 w-full cursor-pointer rounded-full bg-zinc-800"
                >
                  <div
                    className="absolute top-0 h-full rounded-full bg-green-500"
                    style={{
                      left: `${TARGET_MIN}%`,
                      width: `${TARGET_MAX - TARGET_MIN}%`,
                    }}
                  />
                  <div
                    role="slider"
                    aria-label="Slider handle"
                    aria-valuemin={0}
                    aria-valuemax={100}
                    aria-valuenow={value}
                    tabIndex={0}
                    onPointerDown={onHandlePointerDown}
                    onKeyDown={onHandleKeyDown}
                    className="absolute top-1/2 h-12 w-12 -translate-x-1/2 -translate-y-1/2 cursor-grab rounded-full border-4 border-white bg-blue-600 shadow-xl shadow-blue-600/30 active:cursor-grabbing"
                    style={{ left: `${value}%` }}
                  />
                </div>
                <div className="mt-5 flex items-center justify-between text-xs text-zinc-500">
                  <span>0</span>
                  <span>← drag →</span>
                  <span>100</span>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Trial 2 — press the right button */}
          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0">
              <div>
                <CardTitle>Trial 2 · Press the Right Button</CardTitle>
                <CardDescription>
                  Four buttons. Only one is the right one.
                </CardDescription>
              </div>
              {buttonSolved ? (
                <Badge className="bg-green-600 text-white">Solved ✓</Badge>
              ) : (
                <Badge variant="secondary">Pending</Badge>
              )}
            </CardHeader>
            <CardContent>
              <p className="text-center text-lg font-medium">
                Press the button that says <span className="text-blue-400">Continue</span>.
              </p>
              <div className="mt-5 flex flex-wrap items-center justify-center gap-3">
                {BUTTON_OPTIONS.map((label) => (
                  <Button
                    key={label}
                    variant={
                      buttonPressed === label ? "default" : "outline"
                    }
                    onClick={() => pressButton(label)}
                  >
                    {label}
                  </Button>
                ))}
              </div>
              {buttonPressed !== null && !buttonSolved && (
                <p className="mt-4 text-center text-sm text-red-400">
                  Wrong button — that was {buttonPressed}. Try again.
                </p>
              )}
            </CardContent>
          </Card>

          {/* Trial 3 — maths */}
          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0">
              <div>
                <CardTitle>Trial 3 · Quick Maths</CardTitle>
                <CardDescription>
                  One question. No calculator needed.
                </CardDescription>
              </div>
              {mathSolved ? (
                <Badge className="bg-green-600 text-white">Solved ✓</Badge>
              ) : (
                <Badge variant="secondary">Pending</Badge>
              )}
            </CardHeader>
            <CardContent>
              <p className="text-center text-2xl font-semibold">
                What is 8 + 6?
              </p>
              <Input
                value={math}
                onChange={(e) => setMath(e.target.value)}
                inputMode="numeric"
                placeholder="Your answer"
                aria-label="Answer to 8 plus 6"
                className="mx-auto mt-4 max-w-xs text-center text-lg"
              />
            </CardContent>
          </Card>
        </div>

        {allSolved && (
          <div className="mt-8 rounded-2xl border border-green-500/40 bg-green-500/10 p-6 text-center">
            <p className="text-xl font-semibold text-green-400">
              Step 1 passed — all three trials solved.
            </p>
            <p className="mt-2 text-sm text-zinc-400">Step 2 unlocks next.</p>
            <Link href="/gauntlet">
              <Button className="mt-5">Back to Gauntlet</Button>
            </Link>
          </div>
        )}

        <div className="mt-10 text-center">
          <Button variant="outline" onClick={skip}>
            Skip this step →
          </Button>
          <p className="mt-3 text-sm text-zinc-500">
            Skipping means no pass for this step. The degree needs all five
            passed.
          </p>
          <div className="mt-6">
            <Link
              href="/gauntlet"
              className="text-sm text-blue-400 hover:text-blue-300"
            >
              ← Back to Gauntlet
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

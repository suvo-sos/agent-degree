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
const MATH_ANSWER = "14";
const BUTTON_OPTIONS = ["Cancel", "Delete", "Continue", "Submit"];

export default function StepOne() {
  const router = useRouter();
  const [step, setStep] = useState(0);
  const [value, setValue] = useState(0);
  const [buttonPressed, setButtonPressed] = useState<string | null>(null);
  const [math, setMath] = useState("");

  const sliderSolved = value >= TARGET_MIN && value <= TARGET_MAX;
  const buttonSolved = buttonPressed === "Continue";
  const mathSolved = math.trim() === MATH_ANSWER;
  const solved = [sliderSolved, buttonSolved, mathSolved];
  const solvedCount = solved.filter(Boolean).length;
  const allSolved = solvedCount === 3;
  const currentSolved = solved[step];

  function pressButton(label: string) {
    setButtonPressed(label);
  }

  function next() {
    if (currentSolved && step < 2) setStep(step + 1);
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
            STEP 1 OF 5
          </p>
          <h1 className="mt-3 font-grotesque text-4xl font-semibold tracking-tight sm:text-5xl">
            Slide Into the Green
          </h1>
          <div className="mx-auto mt-6 max-w-md">
            <div className="flex items-center justify-between font-mono text-sm">
              <span className="text-zinc-400">Trials solved</span>
              <span className="font-medium text-white">
                {solvedCount} of 3
              </span>
            </div>
            <Progress value={(solvedCount / 3) * 100} className="mt-2" />
          </div>
        </div>

        {!allSolved && (
          <>
            <div className="mt-10">
              {step === 0 && (
                <Card>
                  <CardHeader className="flex flex-row items-center justify-between space-y-0">
                    <div>
                      <CardTitle className="font-grotesque">
                        The Slider
                      </CardTitle>
                    </div>
                    {sliderSolved ? (
                      <Badge className="bg-green-600 font-mono text-white">
                        Solved ✓
                      </Badge>
                    ) : (
                      <Badge variant="secondary" className="font-mono">
                        Pending
                      </Badge>
                    )}
                  </CardHeader>
                  <CardContent>
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
                  </CardContent>
                </Card>
              )}

              {step === 1 && (
                <Card>
                  <CardHeader className="flex flex-row items-center justify-between space-y-0">
                    <div>
                      <CardTitle className="font-grotesque">
                        Press the Right Button
                      </CardTitle>
                    </div>
                    {buttonSolved ? (
                      <Badge className="bg-green-600 font-mono text-white">
                        Solved ✓
                      </Badge>
                    ) : (
                      <Badge variant="secondary" className="font-mono">
                        Pending
                      </Badge>
                    )}
                  </CardHeader>
                  <CardContent>
                    <p className="text-center font-mono text-lg font-medium">
                      Press the button that says{" "}
                      <span className="text-blue-400">Continue</span>.
                    </p>
                    <div className="mt-5 flex flex-wrap items-center justify-center gap-3">
                      {BUTTON_OPTIONS.map((label) => (
                        <Button
                          key={label}
                          variant={
                            buttonPressed === label ? "default" : "outline"
                          }
                          onClick={() => pressButton(label)}
                          className="font-mono"
                        >
                          {label}
                        </Button>
                      ))}
                    </div>
                    {buttonPressed !== null && !buttonSolved && (
                      <p className="mt-4 text-center font-mono text-sm text-red-400">
                        Wrong button — that was {buttonPressed}. Try again.
                      </p>
                    )}
                  </CardContent>
                </Card>
              )}

              {step === 2 && (
                <Card>
                  <CardHeader className="flex flex-row items-center justify-between space-y-0">
                    <div>
                      <CardTitle className="font-grotesque">
                        Quick Maths
                      </CardTitle>
                    </div>
                    {mathSolved ? (
                      <Badge className="bg-green-600 font-mono text-white">
                        Solved ✓
                      </Badge>
                    ) : (
                      <Badge variant="secondary" className="font-mono">
                        Pending
                      </Badge>
                    )}
                  </CardHeader>
                  <CardContent>
                    <p className="text-center font-grotesque text-2xl font-semibold">
                      What is 8 + 6?
                    </p>
                    <Input
                      value={math}
                      onChange={(e) => setMath(e.target.value)}
                      inputMode="numeric"
                      placeholder="Your answer"
                      aria-label="Answer to 8 plus 6"
                      className="mx-auto mt-4 max-w-xs text-center font-mono text-lg"
                    />
                  </CardContent>
                </Card>
              )}
            </div>

            <div className="mt-8 flex items-center justify-between">
              <Button
                variant="outline"
                onClick={skip}
                className="font-mono"
              >
                Skip this step →
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
              Step 1 passed.
            </p>
            <Link href="/gauntlet">
              <Button className="mt-5 font-mono">Back to Gauntlet</Button>
            </Link>
          </div>
        )}

        <div className="mt-12">
          <StepPagination current={1} />
        </div>
      </div>
    </div>
  );
}

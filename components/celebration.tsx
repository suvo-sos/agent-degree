"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import confetti from "canvas-confetti";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import {
  CHALLENGE_NAMES,
  TEST_NAMES,
  certificateImageFor,
  computeScore,
  finishTimer,
  formatDuration,
  getResults,
  getTimer,
  gradeFor,
  isFinalExamComplete,
  testStatus,
  timerElapsedMs,
  type ResultsMap,
} from "@/lib/results";

// The iconic finish: white page, confetti for 3 seconds, "Congratulations",
// then the full review — every test, marks, grade, and the certificate.
// `celebrate` plays the 3s confetti intro (used right after the last test).
// `current` is the just-finished challenge's results, passed in directly
// so the review includes them before the save effect has run.
export function Celebration({
  celebrate = false,
  current,
}: {
  celebrate?: boolean;
  current?: { challenge: number; solved: boolean[]; skipped: number[]; wrong?: number };
}) {
  const [phase, setPhase] = useState<"confetti" | "results">(
    celebrate ? "confetti" : "results",
  );
  const [stored, setStored] = useState<ResultsMap>({});
  const [timerMs, setTimerMs] = useState<number | null>(null);

  useEffect(() => {
    setStored(getResults());
    // Stop the Final Exam clock once every challenge is done.
    if (isFinalExamComplete()) finishTimer();
    setTimerMs(timerElapsedMs(getTimer()));
  }, []);

  useEffect(() => {
    if (!celebrate) return;
    confetti({ particleCount: 160, spread: 100, origin: { y: 0.6 } });
    const interval = window.setInterval(() => {
      confetti({
        particleCount: 40,
        angle: 60,
        spread: 60,
        origin: { x: 0, y: 0.7 },
      });
      confetti({
        particleCount: 40,
        angle: 120,
        spread: 60,
        origin: { x: 1, y: 0.7 },
      });
    }, 250);
    const t = window.setTimeout(() => {
      window.clearInterval(interval);
      setPhase("results");
    }, 3000);
    return () => {
      window.clearInterval(interval);
      window.clearTimeout(t);
    };
  }, [celebrate]);

  const results: ResultsMap = current
    ? {
        ...stored,
        [current.challenge]: {
          solved: current.solved,
          skipped: current.skipped,
          wrong: current.wrong ?? 0,
        },
      }
    : stored;

  const { total, solved, wrong, score, pct } = computeScore(results);
  const { grade, label } = gradeFor(pct);
  const hasResults = total > 0;

  if (phase === "confetti") {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center bg-white px-6 font-sans text-black">
        <h1 className="text-center font-grotesque text-6xl font-semibold tracking-tight sm:text-7xl">
          Congratulations
        </h1>
        <p className="mt-4 text-center font-mono text-lg text-zinc-600">
          You finished the Final Exam.
        </p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-white px-6 py-12 font-sans text-black">
      <div className="mx-auto w-full max-w-2xl">
        <div className="text-center">
          <p className="font-mono text-xs font-semibold tracking-[0.3em] text-blue-600">
            AGENT DEGREE — RESULTS
          </p>
          <h1 className="mt-3 font-grotesque text-4xl font-semibold tracking-tight sm:text-5xl">
            Congratulations
          </h1>
          <p className="mt-3 font-mono text-sm text-zinc-600">
            You finished the Final Exam. Here is how you did.
          </p>
        </div>

        {!hasResults ? (
          <div className="mt-10 rounded-2xl border border-zinc-200 p-6 text-center">
            <p className="font-mono text-sm text-zinc-600">
              No results yet. Finish the Final Exam first.
            </p>
            <Link href="/final-exam">
              <Button className="mt-5 font-mono">Go to the Final Exam</Button>
            </Link>
          </div>
        ) : (
          <>
            <div className="mt-10 space-y-4">
              {[1, 2, 3, 4, 5].map((n) => {
                const names = TEST_NAMES[n] ?? [];
                const count =
                  results[n]?.solved.length ?? names.length;
                return (
                  <Card key={n}>
                    <CardHeader className="flex flex-row items-center justify-between space-y-0">
                      <CardTitle className="font-grotesque">
                        Challenge {n} — {CHALLENGE_NAMES[n]}
                      </CardTitle>
                      <Badge variant="secondary" className="font-mono">
                        {results[n]?.solved.filter(Boolean).length ?? 0}/
                        {count} correct
                      </Badge>
                    </CardHeader>
                    <CardContent>
                      {Array.from({ length: count }, (_, i) => {
                        const status = testStatus(n, i, results);
                        const name = names[i] ?? `Test ${i + 1}`;
                        return (
                          <div
                            key={i}
                            className="flex items-center justify-between border-b border-zinc-100 py-2 font-mono text-sm last:border-0"
                          >
                            <span>
                              Test {i + 1} — {name}
                            </span>
                            {status === "solved" && (
                              <span className="font-semibold text-green-600">
                                ✓ Correct
                              </span>
                            )}
                            {status === "skipped" && (
                              <span className="font-semibold text-amber-600">
                                Skipped
                              </span>
                            )}
                            {status === "unsolved" && (
                              <span className="font-semibold text-red-600">
                                ✗ Not solved
                              </span>
                            )}
                          </div>
                        );
                      })}
                    </CardContent>
                  </Card>
                );
              })}
            </div>

            <div className="mt-10 rounded-2xl border border-zinc-200 p-6 text-center">
              <p className="font-mono text-sm text-zinc-600">Marks</p>
              <p className="mt-2 font-grotesque text-4xl font-semibold">
                {score} / {total}
              </p>
              <p className="mt-1 font-mono text-sm text-zinc-600">
                {solved} correct
                {wrong > 0 ? ` · −${wrong} for wrong answers` : ""}
              </p>
              <p className="mt-1 font-mono text-sm text-zinc-600">
                {pct}% correct
              </p>
              <Progress value={pct} className="mx-auto mt-4 max-w-md" />
              <p className="mt-6 font-grotesque text-6xl font-semibold">
                {grade}
              </p>
              <p className="mt-1 font-mono text-sm text-zinc-600">{label}</p>
              {timerMs !== null && (
                <p className="mt-4 font-mono text-sm text-zinc-600">
                  Completed in {formatDuration(timerMs)}
                </p>
              )}
            </div>

            {/* The award, last: the framed certificate for the grade earned. */}
            <div className="mt-10 text-center">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={certificateImageFor(grade)}
                alt={`Agent Degree certificate, grade ${grade}`}
                className="mx-auto w-full max-w-sm rounded-lg"
              />
              <a
                href={certificateImageFor(grade)}
                download="agent-degree-certificate.png"
                className="mt-6 inline-flex h-11 items-center justify-center rounded-full bg-blue-600 px-6 font-mono text-sm font-semibold text-white transition-colors hover:bg-blue-500"
              >
                Download certificate
              </a>
            </div>

            <div className="mt-8 text-center">
              <Link href="/final-exam">
                <Button variant="outline" className="font-mono">
                  Back to the Final Exam
                </Button>
              </Link>
            </div>
          </>
        )}
      </div>
    </div>
  );
}

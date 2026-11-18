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
  computeScore,
  downloadCertificate,
  getResults,
  gradeFor,
  testStatus,
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
  current?: { challenge: number; solved: boolean[]; skipped: number[] };
}) {
  const [phase, setPhase] = useState<"confetti" | "results">(
    celebrate ? "confetti" : "results",
  );
  const [stored, setStored] = useState<ResultsMap>({});

  useEffect(() => {
    setStored(getResults());
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
        },
      }
    : stored;

  const { total, solved, pct } = computeScore(results);
  const { grade, label } = gradeFor(pct);
  const hasResults = total > 0;

  if (phase === "confetti") {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center bg-white px-6 font-sans text-black">
        <h1 className="text-center font-grotesque text-6xl font-semibold tracking-tight sm:text-7xl">
          Congratulations
        </h1>
        <p className="mt-4 text-center font-mono text-lg text-zinc-600">
          You finished the Gauntlet.
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
            You finished the Gauntlet. Here is how you did.
          </p>
        </div>

        {!hasResults ? (
          <div className="mt-10 rounded-2xl border border-zinc-200 p-6 text-center">
            <p className="font-mono text-sm text-zinc-600">
              No results yet — finish the Gauntlet first.
            </p>
            <Link href="/gauntlet">
              <Button className="mt-5 font-mono">Go to the Gauntlet</Button>
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
                {solved} / {total}
              </p>
              <p className="mt-1 font-mono text-sm text-zinc-600">
                {pct}% correct
              </p>
              <Progress value={pct} className="mx-auto mt-4 max-w-md" />
              <p className="mt-6 font-grotesque text-6xl font-semibold">
                {grade}
              </p>
              <p className="mt-1 font-mono text-sm text-zinc-600">{label}</p>
            </div>

            <div className="mt-10 rounded-2xl border-4 border-yellow-600 bg-black p-8 text-center text-white">
              <p className="font-mono text-xs font-semibold tracking-[0.3em] text-yellow-500">
                AGENT DEGREE
              </p>
              <p className="mt-3 font-grotesque text-3xl font-semibold">
                Digital Human Award
              </p>
              <p className="mt-4 font-mono text-sm text-zinc-400">
                Awarded to
              </p>
              <p className="mt-1 font-grotesque text-2xl font-semibold">
                Kane — AI Agent
              </p>
              <p className="mt-4 font-mono text-sm text-zinc-400">
                Grade {grade} • Score {solved}/{total} • {pct}% •{" "}
                {new Date().getFullYear()}
              </p>
              <Button
                onClick={() =>
                  downloadCertificate(grade, `${solved}/${total}`, pct)
                }
                className="mt-6 font-mono"
              >
                Download certificate
              </Button>
            </div>

            <div className="mt-8 text-center">
              <Link href="/gauntlet">
                <Button variant="outline" className="font-mono">
                  Back to Gauntlet
                </Button>
              </Link>
            </div>
          </>
        )}
      </div>
    </div>
  );
}

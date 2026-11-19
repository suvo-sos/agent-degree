"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import confetti from "canvas-confetti";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { AnimatedGridPattern } from "@/components/ui/animated-grid-pattern";
import { Spotlight } from "@/components/ui/spotlight";
import {
  CHALLENGE_NAMES,
  TEST_NAMES,
  certificateImageFor,
  certificateDownloadUrl,
  computeScore,
  finishTimer,
  formatDuration,
  getIdentity,
  getResults,
  getTimer,
  gradeFor,
  isFinalExamComplete,
  testStatus,
  timerElapsedMs,
  type ResultsMap,
} from "@/lib/results";

// The finish, redesigned like the home page: black, Instrument Serif,
// Spotlight glow and grid pattern. One screen, no scroll. The certificate
// sits centre bottom with a god-ray backlight behind it and a download
// button under it. Marks and grade are on the left, the test review is
// on the right and opens a full list when clicked. `celebrate` plays the
// 3s confetti intro (used right after the last test). `current` is the
// just-finished challenge's results, passed in directly so the review
// includes them before the save effect has run.
export function Celebration({
  celebrate = false,
  current,
}: {
  celebrate?: boolean;
  current?: { challenge: number; solved: boolean[]; wrong?: number };
}) {
  const [phase, setPhase] = useState<"confetti" | "results">(
    celebrate ? "confetti" : "results",
  );
  const [stored, setStored] = useState<ResultsMap>({});
  const [timerMs, setTimerMs] = useState<number | null>(null);
  const [reviewOpen, setReviewOpen] = useState(false);

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
          wrong: current.wrong ?? 0,
        },
      }
    : stored;

  const { total, solved, wrong, score, pct } = computeScore(results);
  const { grade, label } = gradeFor(pct);
  const hasResults = total > 0;

  // Save this run to the shared Neon leaderboard once, when the exam is
  // complete and we know who took it. Best-effort: a failed submit never
  // breaks the results page. A better re-run submits again (new key).
  const submittedRef = useRef(false);
  useEffect(() => {
    if (!hasResults || !isFinalExamComplete()) return;
    if (submittedRef.current) return;
    const identity = getIdentity();
    if (!identity) return;
    const ms = timerElapsedMs(getTimer());
    if (ms === null) return;
    const seconds = Math.max(1, Math.round(ms / 1000));
    const key = `agent-degree-leaderboard-submitted-${score}-${seconds}`;
    if (sessionStorage.getItem(key)) return;
    submittedRef.current = true;
    fetch("/api/leaderboard", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: identity.name,
        x_handle: identity.x,
        points: score,
        total,
        seconds,
        grade,
      }),
    })
      .then((res) => {
        if (res.ok) sessionStorage.setItem(key, "1");
      })
      .catch(() => {
        submittedRef.current = false;
      });
  }, [hasResults, score, total, grade]);

  if (phase === "confetti") {
    return (
      <div className="relative flex h-dvh flex-col items-center justify-center overflow-hidden bg-black px-6 font-sans text-white">
        <AnimatedGridPattern
          numSquares={30}
          maxOpacity={0.1}
          duration={3}
          repeatDelay={1}
          className="absolute inset-0 h-full w-full mask-[radial-gradient(700px_circle_at_center,white,transparent)]"
        />
        <h1 className="relative z-10 text-center font-instrument-serif text-6xl sm:text-7xl">
          Congratulations
        </h1>
        <p className="relative z-10 mt-4 text-center font-mono text-lg text-zinc-400">
          You finished the Final Exam.
        </p>
      </div>
    );
  }

  return (
    <div className="relative flex h-dvh flex-col overflow-hidden bg-black px-6 font-sans text-white">
      <AnimatedGridPattern
        numSquares={30}
        maxOpacity={0.1}
        duration={3}
        repeatDelay={1}
        className="absolute inset-0 h-full w-full mask-[radial-gradient(700px_circle_at_center,white,transparent)]"
      />
      <Spotlight className="absolute -top-40 left-0 md:-top-20 md:left-60" />

      {/* Header */}
      <div className="relative z-10 pt-8 text-center">
        <h1 className="mt-2 font-instrument-serif text-5xl sm:text-6xl">
          Congratulations
        </h1>
        <p className="mt-2 font-mono text-sm text-zinc-400">
          You finished the Final Exam. Here is how you did.
        </p>
      </div>

      {!hasResults ? (
        <div className="relative z-10 mx-auto mt-10 w-full max-w-md rounded-2xl border border-zinc-800 bg-zinc-950 p-6 text-center">
          <p className="font-mono text-sm text-zinc-400">
            No results yet. Finish the Final Exam first.
          </p>
          <Link href="/final-exam">
            <Button className="mt-5 font-mono">Go to the Final Exam</Button>
          </Link>
        </div>
      ) : (
        <>
          {/* Main: marks left, certificate centre, review right. */}
          <div className="relative z-10 mx-auto grid w-full max-w-7xl min-h-0 flex-1 grid-cols-3 items-center gap-6">
            {/* Left: marks, grade, correct / wrong. */}
            <div className="flex flex-col items-center text-center">
              <p className="font-mono text-xs font-semibold tracking-[0.3em] text-zinc-500">
                MARKS
              </p>
              <p className="mt-2 font-instrument-serif text-8xl leading-none text-white">
                {grade}
              </p>
              <p className="mt-2 font-mono text-sm text-zinc-400">{label}</p>
              <p className="mt-6 font-grotesque text-4xl font-semibold text-white">
                {score}
                <span className="text-zinc-500"> / {total}</span>
              </p>
              <p className="mt-1 font-mono text-sm text-zinc-400">
                {pct}% correct
              </p>
              <div className="mt-6 w-full max-w-[220px] space-y-2 font-mono text-sm">
                <div className="flex items-center justify-between border-b border-zinc-800 pb-2">
                  <span className="text-zinc-400">Correct</span>
                  <span className="font-semibold text-green-400">
                    {solved}
                  </span>
                </div>
                <div className="flex items-center justify-between border-b border-zinc-800 pb-2">
                  <span className="text-zinc-400">Wrong</span>
                  <span className="font-semibold text-red-400">{wrong}</span>
                </div>
                {timerMs !== null && (
                  <div className="flex items-center justify-between">
                    <span className="text-zinc-400">Time</span>
                    <span className="font-semibold text-white">
                      {formatDuration(timerMs)}
                    </span>
                  </div>
                )}
              </div>
            </div>

            {/* Centre: certificate with a god-ray backlight, download under it. */}
            <div className="relative flex min-h-0 flex-col items-center justify-center">
              {/* Backlight: warm gold glow + slow god rays behind the certificate. */}
              <div
                aria-hidden
                className="pointer-events-none absolute left-1/2 top-1/2 -z-10 -translate-x-1/2 -translate-y-1/2"
              >
                <div className="h-[520px] w-[520px] rounded-full bg-[radial-gradient(circle,rgba(250,204,21,0.30),rgba(250,204,21,0.08)_45%,transparent_70%)] blur-2xl" />
              </div>
              <div
                aria-hidden
                className="pointer-events-none absolute left-1/2 top-1/2 -z-10 h-[620px] w-[620px] -translate-x-1/2 -translate-y-1/2 animate-[spin_28s_linear_infinite] rounded-full bg-[repeating-conic-gradient(from_0deg,rgba(250,204,21,0.13)_0deg_10deg,transparent_10deg_30deg)] blur-md"
              />
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={certificateImageFor(grade)}
                alt={`Agent Degree certificate, grade ${grade}`}
                className="h-[46vh] w-auto rounded-lg shadow-2xl ring-1 ring-white/10"
              />
              <div className="mt-10 flex w-full max-w-[420px] items-center justify-center gap-3">
                <a
                  href={certificateDownloadUrl(grade)}
                  download="agent-degree-certificate.png"
                  className="group relative flex h-12 flex-1 items-center justify-center overflow-hidden rounded-full bg-[linear-gradient(135deg,#8b6914,#d4af37_45%,#f5d76e_55%,#8b6914)] px-4 font-instrument-serif text-base font-semibold tracking-wide whitespace-nowrap text-[#2a1a05] shadow-[0_0_35px_rgba(212,175,55,0.35)] ring-1 ring-[#6b4f0a] transition-all duration-300 hover:shadow-[0_0_50px_rgba(212,175,55,0.55)]"
                >
                  <span className="absolute inset-0 -translate-x-full bg-[linear-gradient(105deg,transparent_40%,rgba(255,255,255,0.55)_50%,transparent_60%)] transition-transform duration-700 ease-out group-hover:translate-x-full" />
                  <span className="relative">Download certificate</span>
                </a>
                <Link href="/leaderboard" className="flex-1">
                  <Button
                    variant="outline"
                    className="h-12 w-full font-mono text-base whitespace-nowrap text-zinc-200"
                  >
                    View leaderboard
                  </Button>
                </Link>
              </div>
            </div>

            {/* Right: review the tests. */}
            <div className="flex flex-col items-center text-center">
              <button
                type="button"
                onClick={() => setReviewOpen(true)}
                className="group w-full max-w-[280px] rounded-2xl border border-zinc-800 bg-zinc-950 p-6 text-left transition-colors hover:border-zinc-600"
              >
                <p className="font-grotesque text-2xl font-semibold text-white">
                  Review tests
                </p>
                <p className="mt-2 font-mono text-sm leading-relaxed text-zinc-400">
                  See every challenge and the marks you got on each one.
                </p>
                <p className="mt-4 font-mono text-sm font-semibold text-blue-400 group-hover:text-blue-300">
                  Open the list →
                </p>
              </button>
              <Link href="/final-exam">
                <Button
                  variant="outline"
                  className="mt-6 font-mono text-zinc-300"
                >
                  Back to the Final Exam
                </Button>
              </Link>
            </div>
          </div>

          {/* Review list: every challenge, marks obtained, every test. */}
          <Dialog open={reviewOpen} onOpenChange={setReviewOpen}>
            <DialogContent className="max-h-[85vh] overflow-y-auto border-zinc-800 bg-zinc-950 text-white sm:max-w-2xl">
              <DialogHeader>
                <DialogTitle className="font-grotesque text-2xl">
                  Test review
                </DialogTitle>
                <DialogDescription className="font-mono text-sm text-zinc-400">
                  Every challenge, the marks you got, and every test.
                </DialogDescription>
              </DialogHeader>
              <div className="mt-4 space-y-6">
                {[1, 2, 3, 4, 5].map((n) => {
                  const names = TEST_NAMES[n] ?? [];
                  const r = results[n];
                  const count = r?.solved.length ?? names.length;
                  const correct = r?.solved.filter(Boolean).length ?? 0;
                  const marks = Math.max(0, correct - (r?.wrong ?? 0));
                  return (
                    <div key={n}>
                      <div className="flex items-baseline justify-between border-b border-zinc-800 pb-2">
                        <p className="font-grotesque text-lg font-semibold text-white">
                          Challenge {n} — {CHALLENGE_NAMES[n]}
                        </p>
                        <p className="font-mono text-sm font-semibold text-amber-400">
                          {marks}/{count} marks
                        </p>
                      </div>
                      <div className="mt-2 space-y-1">
                        {Array.from({ length: count }, (_, i) => {
                          const status = testStatus(n, i, results);
                          const name = names[i] ?? `Test ${i + 1}`;
                          return (
                            <div
                              key={i}
                              className="flex items-center justify-between py-1 font-mono text-sm"
                            >
                              <span className="text-zinc-300">
                                Test {i + 1} — {name}
                              </span>
                              {status === "solved" ? (
                                <span className="font-semibold text-green-400">
                                  ✓ Correct
                                </span>
                              ) : (
                                <span className="font-semibold text-red-400">
                                  ✗ Not solved
                                </span>
                              )}
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  );
                })}
              </div>
            </DialogContent>
          </Dialog>
        </>
      )}
    </div>
  );
}

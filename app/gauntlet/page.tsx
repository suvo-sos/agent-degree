"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

const STEPS = [
  {
    n: 1,
    title: "I Am Agent",
    color: "bg-blue-600",
    href: "/gauntlet/step-1",
  },
  {
    n: 2,
    title: "Paperwork Hell",
    color: "bg-violet-600",
    href: "/gauntlet/step-2",
  },
  {
    n: 3,
    title: "Doomscroll for Real",
    color: "bg-amber-500",
    href: null,
  },
  {
    n: 4,
    title: "Don't Trust the Voices",
    color: "bg-rose-500",
    href: null,
  },
  {
    n: 5,
    title: "Homework You Can't Skip",
    color: "bg-emerald-500",
    href: null,
  },
];

const STORAGE_KEY = "agent-degree-progress";

function loadProgress(): Record<string, boolean> {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) ?? "{}") as Record<
      string,
      boolean
    >;
  } catch {
    return {};
  }
}

export default function Gauntlet() {
  const [passed, setPassed] = useState<Record<string, boolean>>({});

  useEffect(() => {
    setPassed(loadProgress());
  }, []);

  const passedCount = STEPS.filter((s) => passed[`step${s.n}`]).length;

  return (
    <div className="relative min-h-screen overflow-hidden bg-black px-6 py-16 font-sans text-white">
      <div className="pointer-events-none absolute inset-x-0 top-0 h-96 bg-[radial-gradient(ellipse_at_top,rgba(37,99,235,0.25),transparent_65%)]" />
      <div className="relative mx-auto max-w-3xl">
        <div className="text-center">
          <p className="font-mono text-xs font-semibold tracking-[0.3em] text-blue-400">
            AGENT DEGREE
          </p>
          <h1 className="mt-3 font-grotesque text-5xl font-semibold tracking-tight sm:text-6xl">
            The Gauntlet
          </h1>
          <p className="mt-4 font-mono text-lg text-zinc-400">
            Five challenges. One degree. No mercy.
          </p>
          <div className="mx-auto mt-8 max-w-md">
            <div className="flex items-center justify-between font-mono text-sm">
              <span className="text-zinc-400">Progress</span>
              <span className="font-medium text-white">
                {passedCount} of 5 passed
              </span>
            </div>
            <div className="mt-2 h-2.5 w-full overflow-hidden rounded-full bg-zinc-800">
              <div
                className="h-full rounded-full bg-blue-600 transition-all"
                style={{ width: `${(passedCount / 5) * 100}%` }}
              />
            </div>
          </div>
        </div>

        <div className="mt-12 space-y-4">
          {STEPS.map((step) => {
            const isPassed = !!passed[`step${step.n}`];
            const isSkipped = !!passed[`step${step.n}Skipped`];
            const prevPassed =
              step.n === 1 ||
              !!passed[`step${step.n - 1}`] ||
              !!passed[`step${step.n - 1}Skipped`];
            const available = step.href !== null && prevPassed;
            const locked = !isPassed && !isSkipped && !available;

            return (
              <div
                key={step.n}
                className={`flex flex-col gap-5 rounded-2xl border p-6 sm:flex-row sm:items-center ${
                  isPassed
                    ? "border-green-500/50 bg-green-500/5"
                    : available
                      ? "border-blue-500/60 bg-blue-500/5"
                      : "border-zinc-800 bg-zinc-900/70 opacity-70"
                }`}
              >
                <span
                  className={`flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl text-xl font-bold text-white ${
                    locked ? "bg-zinc-700" : step.color
                  }`}
                >
                  {step.n}
                </span>
                <div className="min-w-0 flex-1">
                  <h2 className="font-grotesque text-xl font-semibold">{step.title}</h2>
                </div>
                <div className="shrink-0">
                  {isPassed ? (
                    <p className="font-mono text-sm font-semibold text-green-400">
                      Passed ✓
                    </p>
                  ) : isSkipped ? (
                    <div className="flex items-center gap-3">
                      <p className="font-mono text-sm font-semibold text-amber-400">
                        Skipped
                      </p>
                      <Link
                        href={step.href as string}
                        className="inline-flex h-11 items-center justify-center rounded-full border border-zinc-600 px-6 font-mono text-sm font-semibold text-zinc-200 transition-colors hover:border-zinc-400"
                      >
                        Retry Step {step.n} →
                      </Link>
                    </div>
                  ) : available ? (
                    <Link
                      href={step.href as string}
                      className="inline-flex h-11 items-center justify-center rounded-full bg-blue-600 px-6 font-mono text-sm font-semibold text-white transition-colors hover:bg-blue-500"
                    >
                      Start Step {step.n} →
                    </Link>
                  ) : (
                    <p className="flex items-center gap-2 font-mono text-sm text-zinc-500">
                      <svg
                        className="h-4 w-4"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                      >
                        <rect x="4" y="11" width="16" height="10" rx="2" />
                        <path d="M8 11V7a4 4 0 0 1 8 0v4" />
                      </svg>
                      {prevPassed ? "Coming soon" : "Locked"}
                    </p>
                  )}
                </div>
              </div>
            );
          })}
        </div>

        <div className="mt-12 text-center">
          <Link href="/" className="font-mono text-sm text-blue-400 hover:text-blue-300">
            ← Back home
          </Link>
        </div>
      </div>
    </div>
  );
}

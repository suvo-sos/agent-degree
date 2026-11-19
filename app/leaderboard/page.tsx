"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { HugeiconsIcon } from "@hugeicons/react";
import {
  Award01Icon,
  Clock01Icon,
  Medal01Icon,
  StarIcon,
  TwitterIcon,
  UserIcon,
} from "@hugeicons/core-free-icons";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Spotlight } from "@/components/ui/spotlight";
import { AnimatedGridPattern } from "@/components/ui/animated-grid-pattern";
import {
  computeScore,
  getIdentity,
  getResults,
  getTimer,
  gradeFor,
  isFinalExamComplete,
  timerElapsedMs,
} from "@/lib/results";

// Shared leaderboard, backed by Neon Postgres. The page reads the live top
// 5 from /api/leaderboard — most points first, then fastest time. When
// the API or database is not reachable, it falls back to the seeded entries
// plus this browser's own finished run (localStorage).
type Entry = {
  name: string;
  x?: string;
  points: number;
  total: number;
  seconds: number;
  grade: string;
  you?: boolean;
};

const SEED: Entry[] = [
  { name: "Kane", points: 27, total: 27, seconds: 12, grade: "A+" },
];

function formatTime(seconds: number) {
  if (seconds < 60) return `${seconds}s`;
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return s === 0 ? `${m}m` : `${m}m ${s}s`;
}

export default function LeaderboardPage() {
  const [entries, setEntries] = useState<Entry[]>(SEED);

  useEffect(() => {
    let cancelled = false;

    async function load() {
      try {
        const res = await fetch("/api/leaderboard");
        const data = (await res.json()) as {
          entries?: Array<{
            name: string;
            x_handle: string;
            points: number;
            total: number;
            seconds: number;
            grade: string;
          }>;
        };
        const rows = Array.isArray(data.entries) ? data.entries : [];
        if (!cancelled && rows.length > 0) {
          const identity = getIdentity();
          setEntries(
            rows.slice(0, 5).map((r) => ({
              name: r.name,
              x: r.x_handle || undefined,
              points: r.points,
              total: r.total,
              seconds: r.seconds,
              grade: r.grade,
              you: identity ? r.name === identity.name : false,
            })),
          );
          return;
        }
      } catch {
        // fall through to the local fallback below
      }
      if (cancelled) return;
      // Fallback: seed + this browser's finished run, when the API is down
      // or the database is not configured yet.
      const identity = getIdentity();
      let all: Entry[] = [...SEED];
      if (identity && isFinalExamComplete()) {
        const { total, score, pct } = computeScore(getResults());
        if (total > 0) {
          const ms = timerElapsedMs(getTimer());
          all = [
            ...all,
            {
              name: identity.name,
              x: identity.x || undefined,
              points: score,
              total,
              seconds: ms === null ? 0 : Math.max(1, Math.round(ms / 1000)),
              grade: gradeFor(pct).grade,
              you: true,
            },
          ];
        }
      }
      const sorted = [...all].sort(
        (a, b) => b.points - a.points || a.seconds - b.seconds,
      );
      const deduped = sorted.filter(
        (e, i) => sorted.findIndex((o) => o.name === e.name) === i,
      );
      setEntries(deduped.slice(0, 5));
    }

    load();
    return () => {
      cancelled = true;
    };
  }, []);

  const ranked = [...entries]
    .sort((a, b) => b.points - a.points || a.seconds - b.seconds)
    .slice(0, 5);

  return (
    <div className="relative flex min-h-screen items-start overflow-hidden bg-black px-6 pt-24 pb-16 font-sans text-white">
      <Spotlight
        className="-top-40 left-0 md:-top-20 md:left-60"
        fill="#2563eb"
      />
      <AnimatedGridPattern
        numSquares={30}
        maxOpacity={0.1}
        duration={3}
        repeatDelay={1}
        className={cn(
          "absolute inset-0 h-full w-full mask-[radial-gradient(700px_circle_at_center,white,transparent)]"
        )}
      />
      <div className="relative z-10 mx-auto w-full max-w-4xl text-center">
        <h1 className="font-instrument-serif text-6xl leading-[0.95] sm:text-7xl">
          Agent Leaderboard
        </h1>
        <p className="mx-auto mt-6 max-w-xl font-mono text-base leading-7 text-zinc-400">
          The fastest agents that finished the Final Exam, with their stats.
          Most points wins, the clock only breaks ties.
        </p>

        <div className="mx-auto mt-10 w-full max-w-3xl text-left">
          {/* Column labels */}
          <div className="flex items-center gap-4 border-b border-zinc-700 pb-3 font-mono text-xs font-semibold tracking-[0.2em] text-zinc-500">
            <span className="inline-flex w-8 shrink-0 items-center justify-center gap-1.5 text-center">
              <HugeiconsIcon icon={Medal01Icon} size={14} strokeWidth={2} />
            </span>
            <span className="inline-flex flex-1 items-center gap-1.5">
              <HugeiconsIcon icon={UserIcon} size={14} strokeWidth={2} />
              NAME
            </span>
            <span className="inline-flex w-10 shrink-0 items-center justify-center gap-1.5 text-center">
              <HugeiconsIcon icon={Award01Icon} size={14} strokeWidth={2} />
              GRADE
            </span>
            <span className="inline-flex w-20 shrink-0 items-center justify-end gap-1.5 text-right">
              <HugeiconsIcon icon={StarIcon} size={14} strokeWidth={2} />
              POINTS
            </span>
            <span className="inline-flex w-16 shrink-0 items-center justify-end gap-1.5 text-right">
              <HugeiconsIcon icon={Clock01Icon} size={14} strokeWidth={2} />
              TIME
            </span>
            <span className="inline-flex w-24 shrink-0 items-center justify-center gap-1.5 text-center">
              <HugeiconsIcon icon={TwitterIcon} size={14} strokeWidth={2} />
              VISIT X
            </span>
          </div>
          {ranked.map((e, i) => (
            <div
              key={e.name}
              className="flex items-center gap-4 border-b border-zinc-800 py-4 font-mono"
            >
              <span className="w-8 shrink-0 text-center text-lg font-semibold text-amber-400">
                {i + 1}
              </span>
              <span className="flex-1 min-w-0 truncate text-base font-semibold text-white">
                {e.name}
                {e.x && (
                  <span className="ml-2 text-sm font-normal text-zinc-500">
                    @{e.x}
                  </span>
                )}
                {e.you && (
                  <span className="ml-2 rounded-full border border-blue-400/40 bg-blue-400/10 px-2 py-0.5 text-[11px] font-semibold text-blue-300">
                    you
                  </span>
                )}
              </span>
              <span className="w-10 shrink-0 text-center font-instrument-serif text-2xl text-amber-400">
                {e.grade}
              </span>
              <span className="w-20 shrink-0 text-right text-sm text-zinc-400">
                {e.points}/{e.total}
              </span>
              <span className="w-16 shrink-0 text-right text-sm text-zinc-300">
                {formatTime(e.seconds)}
              </span>
              <span className="w-24 shrink-0 text-center">
                {e.x ? (
                  <a
                    href={`https://x.com/${e.x}`}
                    target="_blank"
                    rel="noreferrer"
                  >
                    <Button
                      variant="outline"
                      size="sm"
                      className="font-mono text-xs text-zinc-200"
                    >
                      Visit X
                    </Button>
                  </a>
                ) : (
                  <span className="text-sm text-zinc-600">—</span>
                )}
              </span>
            </div>
          ))}
          {ranked.length === 0 && (
            <p className="py-8 text-center font-mono text-sm text-zinc-400">
              No agents have finished yet.
            </p>
          )}
        </div>

        <p className="mt-8 font-mono text-xs text-zinc-500">
          Showing up to 5 agents. More appear as they finish the exam.
        </p>

        <div className="mt-10 flex flex-wrap items-center justify-center gap-4">
          <Link href="/final-exam">
            <Button
              variant="outline"
              size="lg"
              className="px-8 font-mono text-base"
            >
              Take the exam
            </Button>
          </Link>
          <Link href="/">
            <Button
              variant="ghost"
              size="lg"
              className="px-8 font-mono text-base text-zinc-300"
            >
              Back home
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
}

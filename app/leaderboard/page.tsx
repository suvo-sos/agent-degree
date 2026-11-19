import Link from "next/link";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Spotlight } from "@/components/ui/spotlight";
import { AnimatedGridPattern } from "@/components/ui/animated-grid-pattern";

// Seeded with verified full-exam runs. Ranked by most points first, then
// fastest time — the clock only breaks ties. More agents appear here as
// they finish the exam. Cap: 10.
type Entry = {
  name: string;
  points: number;
  total: number;
  seconds: number;
  grade: string;
};

const ENTRIES: Entry[] = [
  { name: "Kane", points: 27, total: 27, seconds: 12, grade: "A+" },
];

const ranked = [...ENTRIES]
  .sort((a, b) => b.points - a.points || a.seconds - b.seconds)
  .slice(0, 10);

function formatTime(seconds: number) {
  if (seconds < 60) return `${seconds}s`;
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return s === 0 ? `${m}m` : `${m}m ${s}s`;
}

export default function LeaderboardPage() {
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

        <div className="mx-auto mt-10 w-full max-w-2xl text-left">
          {ranked.map((e, i) => (
            <div
              key={e.name}
              className="flex items-center gap-4 border-b border-zinc-800 py-4 font-mono"
            >
              <span className="w-8 text-center text-lg font-semibold text-amber-400">
                {i + 1}
              </span>
              <span className="flex-1 text-base font-semibold text-white">
                {e.name}
              </span>
              <span className="font-instrument-serif text-2xl text-amber-400">
                {e.grade}
              </span>
              <span className="text-sm text-zinc-400">
                {e.points}/{e.total} points
              </span>
              <span className="w-16 text-right text-sm text-zinc-300">
                {formatTime(e.seconds)}
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
          Showing up to 10 agents. More appear as they finish the exam.
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

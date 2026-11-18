"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import {
  Bot,
  FileText,
  Fingerprint,
  Lock,
  ShieldAlert,
  SlidersHorizontal,
  type LucideIcon,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { GlareHover } from "@/components/ui/glare-hover";
import { MagicCard } from "@/components/ui/magic-card";
import { Progress } from "@/components/ui/progress";
import { GauntletTimer } from "@/components/gauntlet-timer";
import { ensureTimerStart } from "@/lib/results";

type Step = {
  n: number;
  title: string;
  icon: LucideIcon;
  color: string;
  glow: string;
  href: string;
};

const STEPS: Step[] = [
  {
    n: 1,
    title: "I Am Agent",
    icon: Bot,
    color: "bg-blue-600",
    glow: "#2563eb",
    href: "/gauntlet/step-1",
  },
  {
    n: 2,
    title: "Paperwork Hell",
    icon: FileText,
    color: "bg-violet-600",
    glow: "#7c3aed",
    href: "/gauntlet/step-2",
  },
  {
    n: 3,
    title: "The Control Room",
    icon: SlidersHorizontal,
    color: "bg-amber-500",
    glow: "#f59e0b",
    href: "/gauntlet/step-3",
  },
  {
    n: 4,
    title: "Prove It's You",
    icon: Fingerprint,
    color: "bg-rose-500",
    glow: "#f43f5e",
    href: "/gauntlet/step-4",
  },
  {
    n: 5,
    title: "Homework You Can't Skip",
    icon: ShieldAlert,
    color: "bg-emerald-500",
    glow: "#10b981",
    href: "/gauntlet/step-5",
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
    ensureTimerStart();
  }, []);

  const passedCount = STEPS.filter((s) => passed[`step${s.n}`]).length;
  const allDone = STEPS.every(
    (s) => passed[`step${s.n}`] || passed[`step${s.n}Skipped`],
  );

  return (
    <div className="min-h-screen bg-black px-6 py-16 font-sans text-white">
      <div className="mx-auto max-w-7xl">
        <div className="text-center">
          <p className="font-mono text-xs font-semibold tracking-[0.3em] text-blue-400">
            AGENT DEGREE
          </p>
          <h1 className="mt-3 font-grotesque text-5xl font-semibold tracking-tight sm:text-6xl">
            The Final Exam
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
            <Progress
              value={(passedCount / 5) * 100}
              className="mt-2 w-full [&_[data-slot=progress-indicator]]:bg-blue-600 [&_[data-slot=progress-track]]:h-2.5"
            />
            <GauntletTimer className="mt-3 text-center" />
          </div>
        </div>

        <div className="mt-12 grid gap-4 sm:grid-cols-2 lg:grid-cols-5">
          {STEPS.map((step) => {
            const isPassed = !!passed[`step${step.n}`];
            const isSkipped = !!passed[`step${step.n}Skipped`];
            const prevPassed =
              step.n === 1 ||
              !!passed[`step${step.n - 1}`] ||
              !!passed[`step${step.n - 1}Skipped`];
            const available = step.href !== null && prevPassed;
            const locked = !isPassed && !isSkipped && !available;
            const Icon = step.icon;

            return (
              <GlareHover
                key={step.n}
                color="#505050"
                duration={700}
                width="100%"
                height="100%"
                className="rounded-xl"
              >
                <MagicCard
                  gradientColor={step.glow}
                  gradientOpacity={0.5}
                  className="h-full w-full"
                >
                  <Card
                    className={`relative h-full w-full overflow-hidden border-zinc-800 bg-zinc-950 text-white ring-0 ${
                      locked ? "opacity-70" : ""
                    }`}
                  >
                    <span
                      aria-hidden
                      className="pointer-events-none absolute -right-2 -bottom-7 select-none font-grotesque text-[110px] leading-none font-bold text-white/[0.06]"
                    >
                      {step.n}
                    </span>
                    <CardHeader className="relative">
                      <div className="flex justify-end">
                        <span
                          className={`flex h-11 w-11 items-center justify-center rounded-xl text-white ${
                            locked ? "bg-zinc-700" : step.color
                          }`}
                        >
                          <Icon className="h-5 w-5" />
                        </span>
                      </div>
                      <CardTitle className="mt-6 font-grotesque text-xl text-white">
                        {step.title}
                      </CardTitle>
                    </CardHeader>
                    <CardFooter className="relative mt-auto justify-between border-t border-zinc-800 bg-transparent">
                      {isPassed ? (
                        <p className="font-mono text-sm font-semibold text-green-400">
                          Passed ✓
                        </p>
                      ) : isSkipped ? (
                        <>
                          <p className="font-mono text-sm font-semibold text-amber-400">
                            Skipped
                          </p>
                          <Button
                            variant="outline"
                            render={<Link href={step.href} />}
                          >
                            Retry →
                          </Button>
                        </>
                      ) : available ? (
                        <Button render={<Link href={step.href} />}>
                          Start →
                        </Button>
                      ) : (
                        <p className="flex items-center gap-2 font-mono text-sm text-zinc-500">
                          <Lock className="h-4 w-4" />
                          Locked
                        </p>
                      )}
                    </CardFooter>
                  </Card>
                </MagicCard>
              </GlareHover>
            );
          })}
        </div>

        {allDone && (
          <div className="mt-8 text-center">
            <Button
              render={<Link href="/results" />}
              className="bg-green-600 font-mono text-sm font-semibold text-white hover:bg-green-500"
            >
              View results & certificate →
            </Button>
          </div>
        )}

        <div className="mt-12 text-center">
          <Link href="/" className="font-mono text-sm text-blue-400 hover:text-blue-300">
            ← Back home
          </Link>
        </div>
      </div>
    </div>
  );
}

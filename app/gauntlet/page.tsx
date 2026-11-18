"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { Lock } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { GlareHover } from "@/components/ui/glare-hover";
import { MagicCard } from "@/components/ui/magic-card";
import { GauntletTimer } from "@/components/gauntlet-timer";
import { ensureTimerStart } from "@/lib/results";

type Step = {
  n: number;
  title: string;
  glow: string;
  href: string;
};

const STEPS: Step[] = [
  {
    n: 1,
    title: "I Am Agent",
    glow: "#2563eb",
    href: "/gauntlet/step-1",
  },
  {
    n: 2,
    title: "Paperwork Hell",
    glow: "#7c3aed",
    href: "/gauntlet/step-2",
  },
  {
    n: 3,
    title: "The Control Room",
    glow: "#f59e0b",
    href: "/gauntlet/step-3",
  },
  {
    n: 4,
    title: "Prove It's You",
    glow: "#f43f5e",
    href: "/gauntlet/step-4",
  },
  {
    n: 5,
    title: "Homework You Can't Skip",
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

  const allDone = STEPS.every(
    (s) => passed[`step${s.n}`] || passed[`step${s.n}Skipped`],
  );

  return (
    <div className="min-h-screen bg-black px-6 py-16 font-sans text-white">
      <div className="mx-auto max-w-7xl">
        <div className="text-center">
          <h1 className="font-grotesque text-5xl font-semibold tracking-tight sm:text-6xl">
            The Final Exam
          </h1>
          <GauntletTimer className="mt-8 text-center" />
        </div>

        <div className="mt-20 grid gap-3 sm:grid-cols-2 lg:grid-cols-5">
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
                    className={`relative h-full min-h-[300px] w-full overflow-hidden border-zinc-800 bg-zinc-950 text-white ring-0 ${
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
                      <CardTitle className="font-grotesque text-2xl text-white">
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

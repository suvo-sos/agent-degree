"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { HugeiconsIcon, type IconSvgElement } from "@hugeicons/react";
import {
  BotIcon,
  FileTextIcon,
  FingerPrintIcon,
  LockIcon,
  ShieldAlertIcon,
  SlidersHorizontalIcon,
} from "@hugeicons/core-free-icons";
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle } from "@/components/ui/card";
import { GlareHover } from "@/components/ui/glare-hover";
import { MagicCard } from "@/components/ui/magic-card";
import { ensureTimerStart } from "@/lib/results";

type Step = {
  n: number;
  title: string;
  icon: IconSvgElement;
  glow: string;
  href: string;
};

const STEPS: Step[] = [
  {
    n: 1,
    title: "I Am Agent",
    icon: BotIcon,
    glow: "#2563eb",
    href: "/gauntlet/step-1",
  },
  {
    n: 2,
    title: "Paperwork Hell",
    icon: FileTextIcon,
    glow: "#7c3aed",
    href: "/gauntlet/step-2",
  },
  {
    n: 3,
    title: "The Control Room",
    icon: SlidersHorizontalIcon,
    glow: "#f59e0b",
    href: "/gauntlet/step-3",
  },
  {
    n: 4,
    title: "Prove It's You",
    icon: FingerPrintIcon,
    glow: "#f43f5e",
    href: "/gauntlet/step-4",
  },
  {
    n: 5,
    title: "Homework You Can't Skip",
    icon: ShieldAlertIcon,
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
    <div className="relative flex min-h-screen flex-col bg-black px-6 py-16 font-sans text-white">
      <Link
        href="/"
        className="absolute top-6 left-6 font-mono text-sm text-blue-400 hover:text-blue-300"
      >
        ← Back home
      </Link>
      <div className="mx-auto flex w-full max-w-7xl flex-1 flex-col justify-center">
        <div className="text-center">
          <h1 className="font-grotesque text-5xl font-semibold tracking-tight sm:text-6xl">
            The Final Exam
          </h1>
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
              <div key={step.n} className="flex flex-col items-center">
                <GlareHover
                  color="#505050"
                  duration={700}
                  width="100%"
                  height="100%"
                  className="w-full rounded-xl"
                >
                  <MagicCard
                    gradientColor={step.glow}
                    gradientOpacity={0.5}
                    className="h-full w-full"
                  >
                    <Card
                      className={`group relative h-full min-h-[300px] w-full overflow-hidden border-zinc-800 bg-zinc-950 text-white ring-0 ${
                        locked ? "opacity-70" : ""
                      }`}
                    >
                      <span
                        aria-hidden
                        className="pointer-events-none absolute -top-8 -right-2 select-none font-grotesque text-[160px] leading-none font-bold text-white/[0.06]"
                      >
                        {step.n}
                      </span>
                      <CardHeader className="relative">
                        <CardTitle className="font-grotesque text-2xl text-white">
                          {step.title}
                        </CardTitle>
                      </CardHeader>
                      <div className="absolute bottom-5 left-1/2 -translate-x-1/2">
                        <HugeiconsIcon
                          icon={step.icon}
                          size={72}
                          strokeWidth={2.5}
                          style={{ color: step.glow }}
                        />
                      </div>
                      {locked && (
                        <div className="absolute inset-0 z-10 flex items-center justify-center opacity-0 transition-opacity duration-300 group-hover:opacity-100">
                          <HugeiconsIcon
                            icon={LockIcon}
                            size={56}
                            strokeWidth={2.5}
                            className="text-white"
                          />
                        </div>
                      )}
                    </Card>
                  </MagicCard>
                </GlareHover>
                <div className="mt-5 flex min-h-12 items-center justify-center">
                  {isPassed ? (
                    <p className="font-mono text-sm font-semibold text-green-400">
                      Passed ✓
                    </p>
                  ) : isSkipped ? (
                    <div className="flex items-center gap-3">
                      <p className="font-mono text-sm font-semibold text-amber-400">
                        Skipped
                      </p>
                      <Button
                        variant="outline"
                        render={<Link href={step.href} />}
                        className="h-12 px-8 font-mono text-base font-semibold"
                      >
                        Retry →
                      </Button>
                    </div>
                  ) : available ? (
                    <Button
                      render={<Link href={step.href} />}
                      className="h-12 px-8 font-mono text-base font-semibold"
                    >
                      Start →
                    </Button>
                  ) : null}
                </div>
              </div>
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

      </div>
    </div>
  );
}

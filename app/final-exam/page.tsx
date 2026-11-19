"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import { HugeiconsIcon, type IconSvgElement } from "@hugeicons/react";
import {
  BotIcon,
  FileTextIcon,
  FingerPrintIcon,
  LockKeyholeIcon,
  ShieldAlertIcon,
  SlidersHorizontalIcon,
} from "@hugeicons/core-free-icons";
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle } from "@/components/ui/card";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { GlareHover } from "@/components/ui/glare-hover";
import { MagicCard } from "@/components/ui/magic-card";
import { AnimatedBeam } from "@/components/ui/animated-beam";
import { ensureTimerStart, getResults } from "@/lib/results";

type Step = {
  n: number;
  title: string;
  icon: IconSvgElement;
  href: string;
};

const STEPS: Step[] = [
  {
    n: 1,
    title: "I Am Agent",
    icon: BotIcon,
    href: "/final-exam/step-1",
  },
  {
    n: 2,
    title: "Paperwork Hell",
    icon: FileTextIcon,
    href: "/final-exam/step-2",
  },
  {
    n: 3,
    title: "The Control Room",
    icon: SlidersHorizontalIcon,
    href: "/final-exam/step-3",
  },
  {
    n: 4,
    title: "Prove It's You",
    icon: FingerPrintIcon,
    href: "/final-exam/step-4",
  },
  {
    n: 5,
    title: "Homework You Can't Skip",
    icon: ShieldAlertIcon,
    href: "/final-exam/step-5",
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

export default function FinalExam() {
  const [passed, setPassed] = useState<Record<string, boolean>>({});
  const [marks, setMarks] = useState<Record<number, string>>({});
  const [rulesOpen, setRulesOpen] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);
  const titleRef = useRef<HTMLHeadingElement>(null);
  const cardRef1 = useRef<HTMLDivElement>(null);
  const cardRef2 = useRef<HTMLDivElement>(null);
  const cardRef3 = useRef<HTMLDivElement>(null);
  const cardRef4 = useRef<HTMLDivElement>(null);
  const cardRef5 = useRef<HTMLDivElement>(null);
  const cardRefs = [cardRef1, cardRef2, cardRef3, cardRef4, cardRef5];

  useEffect(() => {
    setPassed(loadProgress());
    ensureTimerStart();
    // Marks per completed challenge, from the saved results.
    const res = getResults();
    const m: Record<number, string> = {};
    for (const [key, r] of Object.entries(res)) {
      const n = Number(key);
      const solved = r.solved.filter(Boolean).length;
      const score = Math.max(0, solved - (r.wrong ?? 0));
      m[n] = `${score}/${r.solved.length}`;
    }
    setMarks(m);
    // Rules show only on the very first visit to this page. After that
    // (e.g. coming back after finishing a challenge) they stay hidden.
    try {
      if (!localStorage.getItem("agent-degree-rules-shown")) {
        localStorage.setItem("agent-degree-rules-shown", "1");
        setRulesOpen(true);
      }
    } catch {
      // storage is best-effort; if it fails, just show the rules
      setRulesOpen(true);
    }
  }, []);

  const allDone = STEPS.every(
    (s) => passed[`step${s.n}`] || passed[`step${s.n}Skipped`],
  );

  // Marks for a completed-but-not-passed challenge, e.g. "3/5".
  function challengeMarks(n: number): string {
    return marks[n] ?? "Completed";
  }

  return (
    <div
      ref={containerRef}
      className="relative flex min-h-screen flex-col bg-black px-6 py-16 font-sans text-white"
    >
      <Link
        href="/"
        className="absolute top-6 left-6 font-mono text-sm text-blue-400 hover:text-blue-300"
      >
        ← Back home
      </Link>
      <div className="mx-auto w-full max-w-7xl text-center">
        <h1
          ref={titleRef}
          className="font-grotesque text-5xl font-semibold tracking-tight sm:text-6xl"
        >
          The Final Exam
        </h1>
      </div>
      <div className="mx-auto flex w-full max-w-7xl flex-1 flex-col justify-center">
        <div className="mt-16 grid gap-3 sm:grid-cols-2 lg:grid-cols-5">
          {STEPS.map((step, idx) => {
            const isPassed = !!passed[`step${step.n}Passed`];
            // Completed = all tests resolved (solved or not). Old saves
            // used stepNSkipped for the same meaning.
            const isCompleted =
              !!passed[`step${step.n}`] || !!passed[`step${step.n}Skipped`];
            const prevCompleted =
              step.n === 1 ||
              !!passed[`step${step.n - 1}`] ||
              !!passed[`step${step.n - 1}Skipped`];
            const available = step.href !== null && prevCompleted;
            const locked = !isCompleted && !available;

            return (
              <div
                key={step.n}
                ref={cardRefs[idx]}
                className="flex flex-col items-center"
              >                <GlareHover
                  color="#505050"
                  duration={700}
                  width="100%"
                  height="100%"
                  className="w-full rounded-xl"
                >
                  <MagicCard
                    gradientColor="#262626"
                    gradientOpacity={0.5}
                    className="h-full w-full"
                  >
                    <Card
                      className={`group relative h-full min-h-[400px] w-full overflow-hidden border-zinc-800 bg-zinc-950 text-white ring-0 ${
                        locked ? "opacity-70" : ""
                      }`}
                    >
                      <span
                        aria-hidden
                        className="pointer-events-none absolute -top-8 -right-2 select-none font-grotesque text-[240px] leading-none font-bold text-white/[0.06]"
                      >
                        {step.n}
                      </span>
                      <CardHeader className="relative z-10">
                        <CardTitle className="font-grotesque text-2xl text-white">
                          {step.title}
                        </CardTitle>
                      </CardHeader>
                      <div className="absolute bottom-6 left-1/2 z-0 -translate-x-1/2">
                        <HugeiconsIcon
                          icon={step.icon}
                          size={140}
                          strokeWidth={0.5}
                          style={{ color: "#0070f3" }}
                        />
                      </div>
                      {locked && (
                        <div className="absolute inset-0 z-10 flex items-center justify-center opacity-0 transition-opacity duration-300 group-hover:opacity-100">
                          <HugeiconsIcon
                            icon={LockKeyholeIcon}
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
                  ) : isCompleted ? (
                    <p className="font-mono text-sm font-semibold text-amber-400">
                      {challengeMarks(step.n)}
                    </p>
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

      {STEPS.map((step, idx) => (
        <AnimatedBeam
          key={step.n}
          containerRef={containerRef}
          fromRef={titleRef}
          toRef={cardRefs[idx]}
          curvature={-50}
          startYOffset={30}
          endYOffset={-234}
          pathColor="#9c40ff"
          pathOpacity={0.15}
          gradientStartColor="#ffaa40"
          gradientStopColor="#9c40ff"
          delay={idx * 0.8}
          className="opacity-60"
        />
      ))}

      <Dialog open={rulesOpen} onOpenChange={setRulesOpen}>
        <DialogContent className="border-zinc-800 bg-zinc-950 text-white">
          <DialogHeader>
            <DialogTitle className="font-grotesque text-2xl">Rules</DialogTitle>
            <DialogDescription className="font-mono text-sm text-zinc-400">
              Read these before you start.
            </DialogDescription>
          </DialogHeader>
          <ul className="space-y-2 font-mono text-sm text-zinc-200">
            <li>5 challenges. Pass them all to earn the Digital Human degree.</li>
            <li>Each test is 1 mark. An unsolved test costs −1.</li>
            <li>A wrong answer costs −1.</li>
            <li>Next is always open, but an unsolved test lowers your mark.</li>
            <li>Reload any time. Your progress is saved.</li>
          </ul>
          <DialogFooter>
            <Button
              onClick={() => setRulesOpen(false)}
              className="font-mono"
            >
              Start the exam
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  );
}

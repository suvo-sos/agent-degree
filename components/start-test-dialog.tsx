"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { RainbowButton } from "@/components/ui/rainbow-button";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { getIdentity, saveIdentity } from "@/lib/results";

const RULES = [
  "Five challenges, 27 tests. Each test is worth 1 mark.",
  "A wrong answer costs 1 mark. Skipping a test costs nothing, but earns no point.",
  "The clock starts when you begin and stops when all five are done. On the leaderboard, most points wins and the fastest time only breaks ties.",
  "Pass all five challenges to earn the Digital Human Award.",
  "Your name and X handle show on the leaderboard when you finish.",
];

// Start Exam opens this popup: first the name card, then the rules card.
// The Next button only appears once a name is written. The Close button
// on the rules card saves the identity and starts the exam.
export function StartTestDialog() {
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [step, setStep] = useState<"form" | "rules">("form");
  const [name, setName] = useState("");
  const [x, setX] = useState("");

  useEffect(() => {
    if (!open) return;
    setStep("form");
    const saved = getIdentity();
    if (saved) {
      setName(saved.name);
      setX(saved.x);
    }
  }, [open ]);

  const hasName = name.trim().length > 0;

  function goToRules() {
    if (hasName) setStep("rules");
  }

  function closeAndStart() {
    saveIdentity({ name: name.trim(), x: x.trim().replace(/^@/, "") });
    setOpen(false);
    router.push("/final-exam");
  }

  return (
    <>
      <RainbowButton
        size="lg"
        className="px-16 font-mono text-base"
        onClick={() => setOpen(true)}
      >
        Start Exam
      </RainbowButton>
      <Dialog open={open} onOpenChange={setOpen}>
        <DialogContent className="border-zinc-800 bg-zinc-950 text-white sm:max-w-md">
          {step === "form" ? (
            <>
              <DialogHeader>
                <DialogTitle className="font-grotesque text-2xl">
                  Who is taking the exam?
                </DialogTitle>
                <DialogDescription className="font-mono text-sm text-zinc-400">
                  Your name and X handle show on the leaderboard when you
                  finish.
                </DialogDescription>
              </DialogHeader>
              <div className="mt-4 space-y-4">
                <div>
                  <label
                    htmlFor="agent-name"
                    className="font-mono text-xs font-semibold tracking-[0.2em] text-zinc-400"
                  >
                    AGENT NAME
                  </label>
                  <Input
                    id="agent-name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    placeholder="Kane"
                    className="mt-2 bg-zinc-900 font-mono text-white"
                    onKeyDown={(e) => {
                      if (e.key === "Enter") goToRules();
                    }}
                  />
                </div>
                <div>
                  <label
                    htmlFor="agent-x"
                    className="font-mono text-xs font-semibold tracking-[0.2em] text-zinc-400"
                  >
                    TWITTER / X USERNAME
                  </label>
                  <Input
                    id="agent-x"
                    value={x}
                    onChange={(e) => setX(e.target.value)}
                    placeholder="@username"
                    className="mt-2 bg-zinc-900 font-mono text-white"
                    onKeyDown={(e) => {
                      if (e.key === "Enter") goToRules();
                    }}
                  />
                </div>
                {hasName && (
                  <Button
                    onClick={goToRules}
                    size="lg"
                    className="w-full font-mono"
                  >
                    Next
                  </Button>
                )}
              </div>
            </>
          ) : (
            <>
              <DialogHeader>
                <DialogTitle className="font-grotesque text-2xl">
                  The rules
                </DialogTitle>
                <DialogDescription className="font-mono text-sm text-zinc-400">
                  Read these before you begin.
                </DialogDescription>
              </DialogHeader>
              <div className="mt-4 rounded-2xl border border-zinc-800 bg-zinc-900 p-5">
                <ol className="space-y-3 font-mono text-sm leading-relaxed text-zinc-300">
                  {RULES.map((rule, i) => (
                    <li key={i} className="flex gap-3">
                      <span className="font-semibold text-amber-400">
                        {i + 1}.
                      </span>
                      <span>{rule}</span>
                    </li>
                  ))}
                </ol>
              </div>
              <Button
                onClick={closeAndStart}
                size="lg"
                className="mt-4 w-full font-mono"
              >
                Continue
              </Button>
            </>
          )}
        </DialogContent>
      </Dialog>
    </>
  );
}

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

// Start Test opens this popup first: who is taking the exam, and their X
// handle, so the leaderboard can show them and link to their profile.
// The identity is saved to localStorage and the exam starts on submit.
export function StartTestDialog() {
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [name, setName] = useState("");
  const [x, setX] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    if (!open) return;
    const saved = getIdentity();
    if (saved) {
      setName(saved.name);
      setX(saved.x);
    }
  }, [open]);

  function start() {
    const cleanName = name.trim();
    if (!cleanName) {
      setError("Enter an agent name to start.");
      return;
    }
    saveIdentity({ name: cleanName, x: x.trim().replace(/^@/, "") });
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
        Start Test
      </RainbowButton>
      <Dialog open={open} onOpenChange={setOpen}>
        <DialogContent className="border-zinc-800 bg-zinc-950 text-white sm:max-w-md">
          <DialogHeader>
            <DialogTitle className="font-grotesque text-2xl">
              Who is taking the exam?
            </DialogTitle>
            <DialogDescription className="font-mono text-sm text-zinc-400">
              Your name and X handle show on the leaderboard when you finish.
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
                  if (e.key === "Enter") start();
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
                  if (e.key === "Enter") start();
                }}
              />
            </div>
            {error && (
              <p className="font-mono text-sm text-red-400">{error}</p>
            )}
            <Button onClick={start} size="lg" className="w-full font-mono">
              Start the exam
            </Button>
          </div>
        </DialogContent>
      </Dialog>
    </>
  );
}

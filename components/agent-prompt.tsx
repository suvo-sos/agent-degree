"use client";

import { useState } from "react";
import { HugeiconsIcon } from "@hugeicons/react";
import { CheckmarkCircle02Icon, Copy01Icon } from "@hugeicons/core-free-icons";
import { Button } from "@/components/ui/button";

// The one prompt a visitor gives their agent so it takes the Final Exam.
// The prompt itself is never shown on the page, only copied.
export const AGENT_PROMPT =
  "Go to https://agent-degree-kappa.vercel.app and take the Final Exam. Complete all 5 challenges to earn the Digital Human degree.\n\nRules:\n1. Five challenges, 27 tests, 40 marks in total. Each question is worth 1 mark.\n2. A wrong answer costs 1 mark. Skipping a test costs nothing, but earns no point.\n3. The clock starts when you begin and stops when all five are done. On the leaderboard, most points wins and the fastest time only breaks ties.\n4. Pass all five challenges to earn the Digital Human Award.\n5. Your name and X handle show on the leaderboard when you finish.";

export function AgentPrompt() {
  const [copied, setCopied] = useState(false);

  async function copyPrompt() {
    try {
      await navigator.clipboard.writeText(AGENT_PROMPT);
    } catch {
      return;
    }
    setCopied(true);
    window.setTimeout(() => setCopied(false), 2000);
  }

  return (
    <div className="flex w-full max-w-xl flex-nowrap items-center justify-between gap-3 rounded-full border border-zinc-800 bg-zinc-950/80 py-2.5 pr-2.5 pl-5">
      <p className="font-mono text-xs leading-6 whitespace-nowrap text-zinc-300">
        Give this prompt to your agent to take the Final Exam.
      </p>
      <Button
        onClick={copyPrompt}
        size="sm"
        className="h-8 shrink-0 rounded-full bg-blue-600 px-3 font-mono text-xs text-white hover:bg-blue-700"
      >
        <HugeiconsIcon
          icon={copied ? CheckmarkCircle02Icon : Copy01Icon}
          size={16}
          strokeWidth={2}
        />
        {copied ? "Copied" : "Copy prompt"}
      </Button>
    </div>
  );
}

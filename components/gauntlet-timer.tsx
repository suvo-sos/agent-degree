"use client";

import { useEffect, useState } from "react";
import {
  ensureTimerStart,
  formatDuration,
  getTimer,
  timerElapsedMs,
  type GauntletTimer,
} from "@/lib/results";

// Live Gauntlet clock. Ticks every second while the exam is running,
// freezes on the final time once the Gauntlet is complete.
// Mounting this anywhere in the exam also starts the clock (first open).
export function GauntletTimer({ className = "" }: { className?: string }) {
  const [timer, setTimer] = useState<GauntletTimer | null>(null);

  useEffect(() => {
    ensureTimerStart();
    setTimer(getTimer());
    const id = window.setInterval(() => {
      const t = getTimer();
      setTimer(t);
      if (t?.end !== null && t?.end !== undefined) {
        window.clearInterval(id);
      }
    }, 1000);
    return () => window.clearInterval(id);
  }, []);

  const elapsed = timerElapsedMs(timer);
  if (elapsed === null) return null;
  const finished = timer?.end !== null && timer?.end !== undefined;

  return (
    <p className={`font-mono text-sm text-zinc-400 ${className}`}>
      {finished ? "Completed in" : "Time"} {formatDuration(elapsed)}
    </p>
  );
}

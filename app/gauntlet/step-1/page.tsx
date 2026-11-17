"use client";

import Link from "next/link";
import { useRef, useState } from "react";

const TARGET_MIN = 70;
const TARGET_MAX = 80;
const STORAGE_KEY = "agent-degree-progress";

export default function StepOne() {
  const [value, setValue] = useState(0);
  const [result, setResult] = useState<"pass" | "fail" | null>(null);
  const trackRef = useRef<HTMLDivElement>(null);

  function valueFromClientX(clientX: number) {
    const track = trackRef.current;
    if (!track) return 0;
    const rect = track.getBoundingClientRect();
    const ratio = (clientX - rect.left) / rect.width;
    return Math.max(0, Math.min(100, Math.round(ratio * 100)));
  }

  function onHandlePointerDown(e: React.PointerEvent<HTMLDivElement>) {
    e.preventDefault();
    const handle = e.currentTarget;
    handle.setPointerCapture(e.pointerId);
    const move = (ev: PointerEvent) => setValue(valueFromClientX(ev.clientX));
    const up = () => {
      handle.removeEventListener("pointermove", move);
      handle.removeEventListener("pointerup", up);
    };
    handle.addEventListener("pointermove", move);
    handle.addEventListener("pointerup", up);
  }

  function onTrackPointerDown(e: React.PointerEvent<HTMLDivElement>) {
    setValue(valueFromClientX(e.clientX));
  }

  function onHandleKeyDown(e: React.KeyboardEvent<HTMLDivElement>) {
    if (e.key === "ArrowRight" || e.key === "ArrowUp") {
      e.preventDefault();
      setValue((v) => Math.min(100, v + 1));
    } else if (e.key === "ArrowLeft" || e.key === "ArrowDown") {
      e.preventDefault();
      setValue((v) => Math.max(0, v - 1));
    } else if (e.key === "PageUp") {
      e.preventDefault();
      setValue((v) => Math.min(100, v + 10));
    } else if (e.key === "PageDown") {
      e.preventDefault();
      setValue((v) => Math.max(0, v - 10));
    } else if (e.key === "Home") {
      e.preventDefault();
      setValue(0);
    } else if (e.key === "End") {
      e.preventDefault();
      setValue(100);
    }
  }

  function verify() {
    if (value >= TARGET_MIN && value <= TARGET_MAX) {
      setResult("pass");
      try {
        const prev = JSON.parse(
          localStorage.getItem(STORAGE_KEY) ?? "{}",
        ) as Record<string, boolean>;
        prev.step1 = true;
        localStorage.setItem(STORAGE_KEY, JSON.stringify(prev));
      } catch {
        // progress is best-effort; the pass still shows
      }
    } else {
      setResult("fail");
    }
  }

  function reset() {
    setValue(0);
    setResult(null);
  }

  const inZone = value >= TARGET_MIN && value <= TARGET_MAX;

  return (
    <div className="relative flex min-h-screen flex-col items-center justify-center overflow-hidden bg-black px-6 py-10 font-sans text-white">
      <div className="pointer-events-none absolute inset-x-0 top-0 h-96 bg-[radial-gradient(ellipse_at_top,rgba(37,99,235,0.25),transparent_65%)]" />
      <div className="relative w-full max-w-2xl text-center">
        <p className="text-xs font-semibold tracking-[0.3em] text-blue-400">
          STEP 1 OF 5 · THE GAUNTLET
        </p>
        <h1 className="mt-3 text-4xl font-semibold tracking-tight sm:text-5xl">
          The Slider
        </h1>
        <p className="mx-auto mt-3 max-w-md text-base text-zinc-400">
          Set the slider inside the green zone. Steady hands, exact numbers.
        </p>
        <p className="mx-auto mt-2 max-w-md text-sm text-zinc-500">
          This exam is built for AI agents. Taking it is the whole point.
        </p>

        <p
          className={`mt-8 text-6xl font-bold tabular-nums ${
            inZone ? "text-green-400" : "text-white"
          }`}
        >
          {value}
        </p>
        <p className="mt-1 text-sm text-zinc-500">drag it into the green</p>

        <div className="relative mt-10 px-6">
          <div
            ref={trackRef}
            onPointerDown={onTrackPointerDown}
            className="relative h-5 w-full cursor-pointer rounded-full bg-zinc-800"
          >
            <div
              className="absolute top-0 h-full rounded-full bg-green-500"
              style={{
                left: `${TARGET_MIN}%`,
                width: `${TARGET_MAX - TARGET_MIN}%`,
              }}
            />
            <div
              role="slider"
              aria-label="Slider handle"
              aria-valuemin={0}
              aria-valuemax={100}
              aria-valuenow={value}
              tabIndex={0}
              onPointerDown={onHandlePointerDown}
              onKeyDown={onHandleKeyDown}
              className="absolute top-1/2 h-12 w-12 -translate-x-1/2 -translate-y-1/2 cursor-grab rounded-full border-4 border-white bg-blue-600 shadow-xl shadow-blue-600/30 active:cursor-grabbing"
              style={{ left: `${value}%` }}
            />
          </div>
          <div className="mt-3 flex items-center justify-between text-xs text-zinc-500">
            <span>0</span>
            <span>← drag →</span>
            <span>100</span>
          </div>
        </div>

        <div className="mt-8 flex items-center justify-center gap-4">
          <button
            onClick={verify}
            className="flex h-12 items-center justify-center rounded-full bg-blue-600 px-10 text-base font-semibold text-white transition-colors hover:bg-blue-500"
          >
            Check my answer
          </button>
          <button
            onClick={reset}
            className="flex h-12 items-center justify-center rounded-full border border-zinc-700 px-8 text-base font-medium text-zinc-300 transition-colors hover:border-zinc-500"
          >
            Reset
          </button>
        </div>

        {result === "pass" && (
          <div className="mt-8 rounded-2xl border border-green-500/40 bg-green-500/10 p-6">
            <p className="text-xl font-semibold text-green-400">
              Step 1 passed — precise control confirmed.
            </p>
            <p className="mt-2 text-sm text-zinc-400">
              Step 2 unlocks next.
            </p>
            <Link
              href="/gauntlet"
              className="mt-5 inline-flex h-11 items-center justify-center rounded-full bg-blue-600 px-6 text-sm font-medium text-white transition-colors hover:bg-blue-500"
            >
              Back to Gauntlet
            </Link>
          </div>
        )}

        {result === "fail" && (
          <p className="mt-8 rounded-2xl border border-red-500/40 bg-red-500/10 px-6 py-4 text-base text-red-400">
            Not quite — the handle is at {value}, the green zone is{" "}
            {TARGET_MIN}–{TARGET_MAX}. Try again.
          </p>
        )}

        <div className="mt-8">
          <Link
            href="/gauntlet"
            className="text-sm text-blue-400 hover:text-blue-300"
          >
            ← Back to Gauntlet
          </Link>
        </div>
      </div>
    </div>
  );
}

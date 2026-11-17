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

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-black px-6 py-16 font-sans text-white">
      <div className="w-full max-w-2xl text-center">
        <p className="text-sm text-zinc-500">Step 1 of 5</p>
        <h1 className="mt-3 text-4xl font-semibold tracking-tight sm:text-5xl">
          The Slider
        </h1>
        <p className="mx-auto mt-4 max-w-md text-lg text-zinc-400">
          Drag the handle into the green zone to prove you can move like a
          human.
        </p>

        <p className="mt-10 text-5xl font-semibold tabular-nums">{value}</p>
        <p className="mt-2 text-sm text-zinc-500">
          Green zone: {TARGET_MIN}–{TARGET_MAX}
        </p>

        <div
          ref={trackRef}
          onPointerDown={onTrackPointerDown}
          className="relative mt-6 h-3 w-full cursor-pointer rounded-full bg-zinc-800"
        >
          <div
            className="absolute top-0 h-full rounded-full bg-green-500/70"
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
            className="absolute top-1/2 h-9 w-9 -translate-x-1/2 -translate-y-1/2 cursor-grab rounded-full border-2 border-white bg-blue-600 shadow-lg active:cursor-grabbing"
            style={{ left: `${value}%` }}
          />
        </div>

        <div className="mt-10 flex items-center justify-center gap-4">
          <button
            onClick={verify}
            className="flex h-12 items-center justify-center rounded-full bg-blue-600 px-8 text-base font-medium text-white transition-colors hover:bg-blue-500"
          >
            Verify
          </button>
          <button
            onClick={reset}
            className="flex h-12 items-center justify-center rounded-full border border-zinc-700 px-8 text-base font-medium text-zinc-300 transition-colors hover:border-zinc-500"
          >
            Reset
          </button>
        </div>

        {result === "pass" && (
          <div className="mt-10 rounded-2xl border border-green-500/40 bg-green-500/10 p-6">
            <p className="text-xl font-semibold text-green-400">
              Step 1 passed — you move like a human.
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
          <p className="mt-10 text-base text-red-400">
            Not quite — the handle is at {value}, the green zone is{" "}
            {TARGET_MIN}–{TARGET_MAX}. Try again.
          </p>
        )}

        <div className="mt-10">
          <Link
            href="/gauntlet"
            className="text-sm text-blue-400 hover:text-blue-300"
          >
            Back to Gauntlet
          </Link>
        </div>
      </div>
    </div>
  );
}

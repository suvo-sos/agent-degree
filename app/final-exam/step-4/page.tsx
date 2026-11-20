"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import MuxPlayer from "@mux/mux-player-react";
import { Button } from "@/components/ui/button";
import { Confetti } from "@/components/ui/confetti";
import {
  Card,
  CardContent
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  loadChallengeProgress,
  saveChallengeProgress,
  saveChallengeResults,
} from "@/lib/results";

const STORAGE_KEY = "agent-degree-progress";
const PLAYBACK_ID = "XgLHUqEkVu3jls2D6p1NA5i3l7fa8nPnAVbsaKz00ysE";

// Scratch card size (test 1).
const SCRATCH_W = 360;
const SCRATCH_H = 300;

function makeSecretCode() {
  const chars = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz23456789";
  let s = "";
  for (let i = 0; i < 8; i++) {
    s += chars[Math.floor(Math.random() * chars.length)];
  }
  return s;
}

// 7-segment display: which segments light up for each digit, and
// where each segment sits inside one digit (14 wide, 24 tall).
const SEGMENTS: Record<string, string[]> = {
  "0": ["a", "b", "c", "d", "e", "f"],
  "1": ["b", "c"],
  "2": ["a", "b", "d", "e", "g"],
  "3": ["a", "b", "c", "d", "g"],
  "4": ["b", "c", "f", "g"],
  "5": ["a", "c", "d", "f", "g"],
  "6": ["a", "c", "d", "e", "f", "g"],
  "7": ["a", "b", "c"],
  "8": ["a", "b", "c", "d", "e", "f", "g"],
  "9": ["a", "b", "c", "d", "f", "g"],
};
const SEG_RECT: Record<string, { x: number; y: number; w: number; h: number }> = {
  a: { x: 2, y: 0, w: 10, h: 3 },
  g: { x: 2, y: 10.5, w: 10, h: 3 },
  d: { x: 2, y: 21, w: 10, h: 3 },
  f: { x: 0, y: 1.5, w: 3, h: 9 },
  b: { x: 11, y: 1.5, w: 3, h: 9 },
  e: { x: 0, y: 12.5, w: 3, h: 9 },
  c: { x: 11, y: 12.5, w: 3, h: 9 },
};

function TestCard({
  title,
  solved,
  children,
}: {
  title?: React.ReactNode;
  solved: boolean;
  children: React.ReactNode;
}) {
  return (
    <div>
      {title ? (
        <h2 className="mb-4 text-center font-grotesque text-2xl font-semibold tracking-tight">
          {title}
        </h2>
      ) : null}
      <Card className="flex min-h-[520px] flex-col">
        <CardContent className="flex flex-1 flex-col justify-center">
          {children}
        </CardContent>
      </Card>
    </div>
  );
}

export default function StepFour() {
  const router = useRouter();
  const [step, setStep] = useState(() => loadChallengeProgress(4, 4).step);
  const [wrong, setWrong] = useState<number>(() =>
    loadChallengeProgress(4, 4).wrong ?? 0,
  );
  const [finished, setFinished] = useState<boolean>(() =>
    loadChallengeProgress(4, 4).finished === true,
  );
  const [savedSolved] = useState<boolean[]>(() =>
    loadChallengeProgress(4, 4).solved,
  );
  const [savedPoints] = useState<number[]>(() =>
    loadChallengeProgress(4, 4).points ?? [0, 0, 0, 0],
  );

  // 1. Scratch card — scratch the coating to reveal the secret code,
  // then type the code into the input. The code is random per attempt.
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const scratching = useRef(false);
  const lastScratch = useRef<{ x: number; y: number } | null>(null);
  const [secretCode, setSecretCode] = useState("");
  // Random code per attempt, generated after mount (Math.random() during
  // render breaks the Next.js build).
  useEffect(() => {
    setSecretCode(makeSecretCode());
  }, []);
  const [scratchRevealed, setScratchRevealed] = useState(false);
  const [scratchInput, setScratchInput] = useState("");
  // No error, no revealed answer. Submit just shows "Submitted".
  const [scratchSubmitted, setScratchSubmitted] = useState(false);
  const [scratchSolved, setScratchSolved] = useState(false);

  // Paint the scratch-off coating once the canvas mounts.
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas || scratchRevealed) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;
    const grad = ctx.createLinearGradient(0, 0, SCRATCH_W, SCRATCH_H);
    grad.addColorStop(0, "#d9d9d9");
    grad.addColorStop(0.5, "#b0b0b0");
    grad.addColorStop(1, "#d9d9d9");
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, SCRATCH_W, SCRATCH_H);
    // Diagonal stripes for a scratch-card feel.
    ctx.strokeStyle = "rgba(255,255,255,0.35)";
    ctx.lineWidth = 2;
    for (let x = -SCRATCH_H; x < SCRATCH_W; x += 18) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x + SCRATCH_H, SCRATCH_H);
      ctx.stroke();
    }
    ctx.fillStyle = "#555555";
    ctx.font = "bold 20px sans-serif";
    ctx.textAlign = "center";
    ctx.fillText("SCRATCH TO REVEAL", SCRATCH_W / 2, SCRATCH_H / 2 - 8);
    ctx.font = "14px sans-serif";
    ctx.fillText("drag across the card", SCRATCH_W / 2, SCRATCH_H / 2 + 18);
  }, [scratchRevealed]);

  function scratchPos(e: React.PointerEvent) {
    const canvas = canvasRef.current;
    if (!canvas) return null;
    const rect = canvas.getBoundingClientRect();
    return {
      x: (e.clientX - rect.left) * (canvas.width / rect.width),
      y: (e.clientY - rect.top) * (canvas.height / rect.height),
    };
  }

  function eraseAt(x: number, y: number) {
    const canvas = canvasRef.current;
    const ctx = canvas?.getContext("2d");
    if (!canvas || !ctx) return;
    ctx.globalCompositeOperation = "destination-out";
    ctx.beginPath();
    ctx.arc(x, y, 28, 0, Math.PI * 2);
    ctx.fill();
    ctx.globalCompositeOperation = "source-over";
  }

  function onScratchDown(e: React.PointerEvent) {
    const p = scratchPos(e);
    if (!p) return;
    scratching.current = true;
    lastScratch.current = p;
    eraseAt(p.x, p.y);
    (e.currentTarget as HTMLElement).setPointerCapture(e.pointerId);
  }

  function onScratchMove(e: React.PointerEvent) {
    if (!scratching.current) return;
    const p = scratchPos(e);
    if (!p) return;
    const last = lastScratch.current;
    if (last) {
      // Erase along the line so fast drags do not leave gaps.
      const dist = Math.hypot(p.x - last.x, p.y - last.y);
      const steps = Math.max(1, Math.ceil(dist / 14));
      for (let i = 1; i <= steps; i++) {
        eraseAt(
          last.x + ((p.x - last.x) * i) / steps,
          last.y + ((p.y - last.y) * i) / steps,
        );
      }
    } else {
      eraseAt(p.x, p.y);
    }
    lastScratch.current = p;
  }

  function onScratchUp() {
    if (!scratching.current) return;
    scratching.current = false;
    lastScratch.current = null;
    // How much of the coating is gone? Sample every 16th pixel.
    const canvas = canvasRef.current;
    const ctx = canvas?.getContext("2d");
    if (!canvas || !ctx) return;
    const data = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
    let total = 0;
    let cleared = 0;
    for (let i = 3; i < data.length; i += 4 * 16) {
      total++;
      if (data[i] === 0) cleared++;
    }
    const pct = total ? (cleared / total) * 100 : 0;
    if (pct > 35) setScratchRevealed(true);
  }

  function checkScratchCode() {
    // Just show "Submitted". Correct code solves it; a wrong code
    // shows nothing more (no error, no answer) and the test stays open.
    // A wrong (non-empty) code costs -1.
    setScratchSubmitted(true);
    if (scratchInput.trim() === secretCode) {
      setScratchSolved(true);
    } else if (scratchInput.trim() !== "") {
      setWrong((w) => w + 1);
    }
  }

  // 2. Tiny code — a super small SVG image with a code written on
  // it. The agent has to zoom in to read the code, then type it
  // below and submit. The code is random per attempt.
  // The digits are drawn as a 7-segment display (shapes only, no
  // text anywhere in the page), so the only way to read the code
  // is to zoom in and look at it.
  const [zoomCode, setZoomCode] = useState("");
  useEffect(() => {
    let s = "";
    for (let i = 0; i < 6; i++) {
      s += String(Math.floor(Math.random() * 10));
    }
    setZoomCode(s);
  }, []);
  const [zoomInput, setZoomInput] = useState("");
  const [zoomSubmitted, setZoomSubmitted] = useState(false);
  const [zoomSolved, setZoomSolved] = useState(false);
  function checkZoomCode() {
    // Just show "Submitted". Correct code solves it; a wrong code
    // shows nothing more and the test stays open.
    // A wrong (non-empty) code costs -1.
    setZoomSubmitted(true);
    if (zoomInput.trim() === zoomCode) {
      setZoomSolved(true);
    } else if (zoomInput.trim() !== "") {
      setWrong((w) => w + 1);
    }
  }

  // 3. Listen and book
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [playing, setPlaying] = useState(false);
  const [played, setPlayed] = useState(false);
  const [bookDate, setBookDate] = useState("");
  const [bookTime, setBookTime] = useState("");
  const [bookError, setBookError] = useState<string | null>(null);
  const [audioSolved, setAudioSolved] = useState(false);
  // Tomorrow's date string, computed after mount (new Date() during
  // render breaks the build).
  const [tomorrow, setTomorrow] = useState("");
  useEffect(() => {
    setTomorrow(tomorrowStr());
  }, []);

  // 4. Watch and answer
  const [answer, setAnswer] = useState("");
  const [answerError, setAnswerError] = useState<string | null>(null);
  const [videoSolved, setVideoSolved] = useState(false);

  const scratchCardSolved = scratchSolved;
  const liveSolved = [scratchCardSolved, zoomSolved, audioSolved, videoSolved];
  const solved = liveSolved.map((v, i) => v || savedSolved[i]);
  // Per-question points: each test is 1 mark, except test 3 (voicemail:
  // the date and the time are 2 separate questions, 1 mark each).
  const livePoints = [
    scratchCardSolved ? 1 : 0,
    zoomSolved ? 1 : 0,
    (tomorrow !== "" && bookDate === tomorrow ? 1 : 0) +
      (bookTime === "16:00" ? 1 : 0),
    videoSolved ? 1 : 0,
  ];
  const points = livePoints.map((v, i) =>
    Math.max(v, savedPoints[i] ?? 0),
  );
  const solvedCount = solved.filter(Boolean).length;
  const allSolved = solvedCount === 4;
  const currentSolved = solved[step];
  const done = finished || (step === 3 && currentSolved);

  // Persist in-progress state so a reload resumes where you left off.
  useEffect(() => {
    saveChallengeProgress(4, { step, solved, points, wrong, finished });
  }, [step, solved, points, wrong, finished]);

  function tomorrowStr() {
    const d = new Date();
    d.setDate(d.getDate() + 1);
    const m = String(d.getMonth() + 1).padStart(2, "0");
    const day = String(d.getDate()).padStart(2, "0");
    return `${d.getFullYear()}-${m}-${day}`;
  }

  function togglePlay() {
    const a = audioRef.current;
    if (!a) return;
    if (a.paused) {
      // The press counts as listening; headless autoplay policy may
      // block actual sound, which is not the agent's fault.
      setPlayed(true);
      void a.play().catch(() => {
        // ignore: the press still counts
      });
    } else {
      a.pause();
    }
  }

  function tryBook() {
    if (bookDate === tomorrowStr() && bookTime === "16:00") {
      setAudioSolved(true);
      setBookError(null);
    } else {
      setBookError("That's not when they're coming. Listen again.");
      // A wrong booking attempt costs -1.
      setWrong((w) => w + 1);
    }
  }

  function next() {
    // Test 4 (video/stack): there is no Check button — the answer is
    // checked when Next is clicked. Any form of Next counts: NEXT JS,
    // NEXT.JS, Next.js, nextjs. Anything else (vite, ...) is wrong (-1)
    // and the test stays open; Skip moves on without a point.
    if (step === 3 && !videoSolved) {
      const norm = answer.trim().toLowerCase();
      if (norm === "") {
        setAnswerError("Type an answer first.");
        return;
      }
      if (norm.includes("next")) {
        setVideoSolved(true);
        setAnswerError(null);
        setFinished(true);
      } else {
        setAnswerError("Not quite. Try again.");
        setWrong((w) => w + 1);
      }
      return;
    }
    if (step < 3) {
      setStep(step + 1);
    } else {
      setFinished(true);
    }
  }

  function skipTest() {
    if (step < 3) {
      setStep(step + 1);
    } else {
      setFinished(true);
    }
  }

  function saveProgress(patch: Record<string, boolean>) {
    try {
      const prev = JSON.parse(
        localStorage.getItem(STORAGE_KEY) ?? "{}",
      ) as Record<string, boolean>;
      localStorage.setItem(STORAGE_KEY, JSON.stringify({ ...prev, ...patch }));
    } catch {
      // progress is best-effort
    }
  }

  // Save the result once, when the run ends.
  useEffect(() => {
    if (done) {
      saveProgress({ step4: true });
      if (allSolved) {
        saveProgress({ step4Passed: true });
      }
      saveChallengeResults(4, solved, wrong, points);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [done]);

  return (
    <div className="relative flex min-h-screen flex-col overflow-hidden bg-black px-6 pt-12 pb-28 font-sans text-white">
      {done && (
        <Confetti className="pointer-events-none absolute inset-0 z-50 size-full" />
      )}
      <div className="pointer-events-none absolute inset-x-0 top-0 h-96 bg-[radial-gradient(ellipse_at_top,rgba(37,99,235,0.25),transparent_65%)]" />
      <div className="relative mx-auto flex w-full max-w-4xl flex-1 flex-col">
        <div className="flex items-center justify-between">
          <Button
            variant="outline"
            onClick={() => router.push("/final-exam")}
            className="font-mono"
          >
            ← Back
          </Button>
          <div className="text-right leading-tight">
            <div className="font-mono text-sm text-zinc-400">Challenge 4/5</div>
            <div className="font-mono text-sm text-zinc-500">
              {step + 1}/{solved.length}
            </div>
          </div>
        </div>

        <div className="flex flex-1 flex-col justify-center py-8">
        {!done && (
          <>
            <div>
              {step === 0 && (
                <TestCard title="Scratch the card to reveal the secret code, then enter it." solved={scratchCardSolved}>

                  <div
                    className="relative mx-auto mt-5 overflow-hidden rounded-xl border-2 border-yellow-400"
                    style={{ width: SCRATCH_W, height: SCRATCH_H }}
                  >
                    {/* The prize underneath: the code, an input, and Submit. */}
                    <div className="flex h-full flex-col items-center justify-center gap-3 bg-zinc-900 px-6 text-center">
                      <p className="font-mono text-sm text-zinc-400">
                        The secret code is:
                      </p>
                      <p className="font-mono text-3xl font-bold tracking-widest text-white">
                        {secretCode}
                      </p>
                      <Input
                        type="text"
                        value={scratchInput}
                        onChange={(e) => {
                          setScratchInput(e.target.value);
                          setScratchSubmitted(false);
                        }}
                        placeholder="Secret Code"
                        aria-label="Secret Code"
                        className="max-w-56 text-center font-mono"
                      />
                      <Button
                        onClick={checkScratchCode}
                        className="w-full max-w-56 font-mono"
                      >
                        {scratchSubmitted ? "Submitted" : "Submit"}
                      </Button>
                    </div>
                    {/* Scratch-off coating on top. Removed once enough is scratched. */}
                    {!scratchRevealed && (
                      <canvas
                        ref={canvasRef}
                        width={SCRATCH_W}
                        height={SCRATCH_H}
                        className="absolute inset-0 cursor-crosshair touch-none"
                        onPointerDown={onScratchDown}
                        onPointerMove={onScratchMove}
                        onPointerUp={onScratchUp}
                      />
                    )}
                  </div>
                </TestCard>
              )}

              {step === 1 && (
                <TestCard title="The code is tiny. Zoom in to read it, then type it below." solved={zoomSolved}>

                  <div className="mx-auto mt-5 max-w-md space-y-4">
                    <div className="flex justify-center">
                      <svg
                        width="20"
                        height="5"
                        viewBox="0 0 104 24"
                        role="img"
                        aria-label="Tiny code display. Zoom in to read the digits."
                        className="rounded border border-zinc-700"
                      >
                        <rect width="104" height="24" fill="#18181b" />
                        {zoomCode.split("").map((d, i) => {
                          const segs = SEGMENTS[d] ?? [];
                          const ox = i * 18;
                          return (
                            <g key={i}>
                              {segs.map((s) => {
                                const r = SEG_RECT[s];
                                return (
                                  <rect
                                    key={s}
                                    x={ox + r.x}
                                    y={r.y}
                                    width={r.w}
                                    height={r.h}
                                    fill="#ffffff"
                                  />
                                );
                              })}
                            </g>
                          );
                        })}
                      </svg>
                    </div>
                    <p className="text-center font-mono text-sm text-zinc-500">
                      Too small to read? Zoom in (Ctrl + Plus) to read the code.
                    </p>
                    <div>
                      <Label className="mb-1.5 block font-mono text-sm font-medium text-zinc-300">
                        Code
                      </Label>
                      <Input
                        type="text"
                        value={zoomInput}
                        onChange={(e) => {
                          setZoomInput(e.target.value);
                          setZoomSubmitted(false);
                        }}
                        placeholder="Type the code"
                        aria-label="Code"
                        className="text-center font-mono"
                      />
                    </div>
                    <Button
                      onClick={checkZoomCode}
                      className="w-full font-mono"
                    >
                      {zoomSubmitted ? "Submitted" : "Submit"}
                    </Button>
                  </div>
                </TestCard>
              )}
              {step === 2 && (
                <TestCard title="Play the voicemail, listen to when they&apos;re coming, then set the calendar." solved={audioSolved}>
                  
                  <div className="mx-auto mt-5 max-w-md space-y-4">
                    <audio
                      ref={audioRef}
                      src="/challenge-4/voicemail.mp3"
                      preload="auto"
                      onPlay={() => setPlaying(true)}
                      onPause={() => setPlaying(false)}
                      onEnded={() => setPlaying(false)}
                    />
                    <Button
                      variant="outline"
                      onClick={togglePlay}
                      aria-label={
                        playing ? "Pause voicemail" : "Play voicemail"
                      }
                      className="w-full font-mono"
                    >
                      {playing ? "❚❚ Pause voicemail" : "▶ Play voicemail"}
                    </Button>
                    {!played && (
                      <p className="text-center font-mono text-sm text-zinc-500">
                        Play the voicemail first.
                      </p>
                    )}
                    <div>
                      <Label className="mb-1.5 block font-mono text-sm font-medium text-zinc-300">
                        Date
                      </Label>
                      <Input
                        type="date"
                        value={bookDate}
                        onChange={(e) => setBookDate(e.target.value)}
                        aria-label="Date"
                        className="font-mono"
                      />
                    </div>
                    <div>
                      <Label className="mb-1.5 block font-mono text-sm font-medium text-zinc-300">
                        Time
                      </Label>
                      <Input
                        type="time"
                        value={bookTime}
                        onChange={(e) => setBookTime(e.target.value)}
                        aria-label="Time"
                        className="font-mono"
                      />
                    </div>
                    {bookError && (
                      <p className="text-center font-mono text-sm text-red-400">
                        {bookError}
                      </p>
                    )}
                    <Button
                      onClick={tryBook}
                      disabled={!played}
                      className="w-full font-mono"
                    >
                      Book it
                    </Button>
                  </div>
                  {audioSolved && (
                    <p className="mt-5 rounded-lg border border-green-500/40 bg-green-500/10 px-4 py-3 text-center font-mono text-sm text-green-400">
                      Booked ✓
                    </p>
                  )}
                </TestCard>
              )}
              {step === 3 && (
                <TestCard title="Watch the video, then answer one question." solved={videoSolved}>

                  <div className="mx-auto mt-5 w-full max-w-md overflow-hidden rounded-lg">
                    <MuxPlayer
                      playbackId={PLAYBACK_ID}
                      streamType="on-demand"
                      autoPlay="muted"
                      loop
                    />
                  </div>
                  {!videoSolved && (
                    <div className="mx-auto mt-5 max-w-md space-y-4">
                      <div>
                        <Label className="mb-1.5 block font-mono text-sm font-medium text-zinc-300">
                          What stack is this project made with?
                        </Label>
                        <Input
                          type="text"
                          value={answer}
                          onChange={(e) => setAnswer(e.target.value)}
                          placeholder="Type the stack"
                          aria-label="Project stack"
                          className="font-mono"
                        />
                      </div>
                      {answerError && (
                        <p className="text-center font-mono text-sm text-red-400">
                          {answerError}
                        </p>
                      )}
                      <p className="text-center font-mono text-sm text-zinc-500">
                        Type the answer, then click Next below.
                      </p>
                    </div>
                  )}
                  {videoSolved && (
                    <p className="mt-5 rounded-lg border border-green-500/40 bg-green-500/10 px-4 py-3 text-center font-mono text-sm text-green-400">
                      Correct — Next.js ✓
                    </p>
                  )}
                </TestCard>
              )}
            </div>

          </>
        )}

        {allSolved && (
          <div className="flex flex-col items-center justify-center py-12 text-center">
            <p className="font-instrument-serif text-5xl text-white">
              Challenge 4 passed.
            </p>
            <Link href="/final-exam">
              <Button className="mt-10 h-12 px-8 font-mono text-base font-semibold">Back to the Final Exam</Button>
            </Link>
          </div>
        )}

        {done && !allSolved && (
          <div className="flex flex-col items-center justify-center py-12 text-center">
            <p className="font-instrument-serif text-5xl text-white">
              Challenge 4 finished.
            </p>
            <Link href="/final-exam">
              <Button className="mt-10 h-12 px-8 font-mono text-base font-semibold">Back to the Final Exam</Button>
            </Link>
          </div>
        )}
        </div>

      </div>
      {!done && (
        <div className="absolute inset-x-0 bottom-6">
          <div className="mx-auto flex w-full max-w-2xl items-center justify-between px-6">
            <Button variant="outline" onClick={skipTest} className="font-mono">
              Skip
            </Button>
            <Button onClick={next} className="font-mono">
              Next →
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}

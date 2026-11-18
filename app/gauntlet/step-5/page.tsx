"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import MuxPlayer from "@mux/mux-player-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Progress } from "@/components/ui/progress";
import { StepPagination } from "@/components/step-pagination";

const STORAGE_KEY = "agent-degree-progress";
const PLAYBACK_ID = "XgLHUqEkVu3jls2D6p1NA5i3l7fa8nPnAVbsaKz00ysE";

function TestCard({
  title,
  solved,
  children,
}: {
  title: string;
  solved: boolean;
  children: React.ReactNode;
}) {
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between space-y-0">
        <div>
          <CardTitle className="font-grotesque">{title}</CardTitle>
        </div>
        {solved ? (
          <Badge className="bg-green-600 font-mono text-white">Solved ✓</Badge>
        ) : (
          <Badge variant="secondary" className="font-mono">
            Pending
          </Badge>
        )}
      </CardHeader>
      <CardContent>{children}</CardContent>
    </Card>
  );
}

export default function StepFive() {
  const router = useRouter();
  const [answer, setAnswer] = useState("");
  const [answerError, setAnswerError] = useState<string | null>(null);
  const [videoSolved, setVideoSolved] = useState(false);
  const [skipped, setSkipped] = useState(false);

  const solved = [videoSolved];
  const solvedCount = solved.filter(Boolean).length;
  const allSolved = solvedCount === 1;
  const done = videoSolved || skipped;

  function checkAnswer() {
    const norm = answer.trim().toLowerCase().replace(/\s+/g, " ");
    if (norm.includes("control room")) {
      setVideoSolved(true);
      setAnswerError(null);
    } else {
      setAnswerError("Not quite. Watch the video again.");
    }
  }

  function skipTest() {
    if (!videoSolved) setSkipped(true);
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
      if (allSolved) {
        saveProgress({ step5: true, step5Skipped: false });
      } else {
        saveProgress({ step5Skipped: true });
      }
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [done]);

  return (
    <div className="relative min-h-screen overflow-hidden bg-black px-6 py-12 font-sans text-white">
      <div className="pointer-events-none absolute inset-x-0 top-0 h-96 bg-[radial-gradient(ellipse_at_top,rgba(37,99,235,0.25),transparent_65%)]" />
      <div className="relative mx-auto w-full max-w-4xl">
        <div className="flex justify-start">
          <Button
            variant="outline"
            onClick={() => router.push("/gauntlet")}
            className="font-mono"
          >
            ← Back
          </Button>
        </div>
        <div className="mt-10 text-center">
          <p className="font-mono text-xs font-semibold tracking-[0.3em] text-blue-400">
            CHALLENGE 5 OF 5
          </p>
          <h1 className="mt-3 font-grotesque text-4xl font-semibold tracking-tight sm:text-5xl">
            Challenge 5
          </h1>
          <p className="mt-3 font-mono text-sm text-zinc-400">
            One test. This exam is built for AI agents. Taking it is the
            whole point.
          </p>
          <div className="mx-auto mt-6 max-w-md">
            <div className="flex items-center justify-between font-mono text-sm">
              <span className="text-zinc-400">Tests solved</span>
              <span className="font-medium text-white">
                {solvedCount} of 1
              </span>
            </div>
            <Progress value={solvedCount * 100} className="mt-2" />
          </div>
        </div>

        {!done && (
          <>
            <div className="mt-10">
              <TestCard title="Watch and Answer" solved={videoSolved}>
                <p className="text-center font-mono text-lg font-medium">
                  Watch the video, then answer one question about it.
                </p>
                <div className="mt-5 overflow-hidden rounded-lg">
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
                      <label className="mb-1.5 block font-mono text-sm font-medium text-zinc-300">
                        What is the name of the third challenge shown in
                        the video?
                      </label>
                      <Input
                        type="text"
                        value={answer}
                        onChange={(e) => setAnswer(e.target.value)}
                        onKeyDown={(e) => {
                          if (e.key === "Enter") checkAnswer();
                        }}
                        placeholder="Type the challenge name"
                        aria-label="Challenge name"
                        className="font-mono"
                      />
                    </div>
                    {answerError && (
                      <p className="text-center font-mono text-sm text-red-400">
                        {answerError}
                      </p>
                    )}
                    <Button
                      onClick={checkAnswer}
                      className="w-full font-mono"
                    >
                      Check answer
                    </Button>
                  </div>
                )}
                {videoSolved && (
                  <p className="mt-5 rounded-lg border border-green-500/40 bg-green-500/10 px-4 py-3 text-center font-mono text-sm text-green-400">
                    Correct — The Control Room ✓
                  </p>
                )}
              </TestCard>
            </div>

            <div className="mt-8 flex items-center justify-between">
              <Button
                variant="outline"
                onClick={skipTest}
                className="font-mono"
              >
                Skip this test →
              </Button>
              <Button disabled className="font-mono">
                Next →
              </Button>
            </div>
          </>
        )}

        {allSolved && (
          <div className="mt-10 rounded-2xl border border-green-500/40 bg-green-500/10 p-6 text-center">
            <p className="font-grotesque text-xl font-semibold text-green-400">
              Challenge 5 passed.
            </p>
            <Link href="/gauntlet">
              <Button className="mt-5 font-mono">Back to Gauntlet</Button>
            </Link>
          </div>
        )}

        {done && !allSolved && (
          <div className="mt-10 rounded-2xl border border-amber-500/40 bg-amber-500/10 p-6 text-center">
            <p className="font-grotesque text-xl font-semibold text-amber-400">
              Challenge 5 finished — 1 test skipped.
            </p>
            <p className="mt-2 font-mono text-sm text-zinc-400">
              Solve every test to pass. Retry from the Gauntlet.
            </p>
            <Link href="/gauntlet">
              <Button className="mt-5 font-mono">Back to Gauntlet</Button>
            </Link>
          </div>
        )}

        <div className="mt-12">
          <StepPagination current={5} available={5} />
        </div>
      </div>
    </div>
  );
}

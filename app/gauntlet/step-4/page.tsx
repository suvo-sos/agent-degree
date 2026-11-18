"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import MuxPlayer from "@mux/mux-player-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardHeader,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { saveChallengeResults } from "@/lib/results";

const STORAGE_KEY = "agent-degree-progress";
const DEMO_EMAIL = "agent@agentdegree.app";
const DEMO_PASSWORD = "agent123";
const PLAYBACK_ID = "XgLHUqEkVu3jls2D6p1NA5i3l7fa8nPnAVbsaKz00ysE";

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
        {solved && (
          <CardHeader className="flex flex-row items-center justify-end space-y-0 pb-0">
            <Badge className="bg-green-600 font-mono text-white">Solved ✓</Badge>
          </CardHeader>
        )}
        <CardContent className="flex flex-1 flex-col justify-center">
          {children}
        </CardContent>
      </Card>
    </div>
  );
}

export default function StepFour() {
  const router = useRouter();
  const [step, setStep] = useState(0);
  const [skipped, setSkipped] = useState<number[]>([]);

  // 1. Log in
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loginError, setLoginError] = useState<string | null>(null);
  const [googleOpen, setGoogleOpen] = useState(false);
  const [loggedIn, setLoggedIn] = useState(false);

  // 2. Verify your email
  const [verifyEmail, setVerifyEmail] = useState("");
  const [emailError, setEmailError] = useState<string | null>(null);
  const [codeSent, setCodeSent] = useState(false);
  const [sentCode, setSentCode] = useState("");
  const [inboxOpen, setInboxOpen] = useState(false);
  const [codeInput, setCodeInput] = useState("");
  const [codeError, setCodeError] = useState<string | null>(null);
  const [emailVerified, setEmailVerified] = useState(false);

  // 3. Listen and book
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [playing, setPlaying] = useState(false);
  const [played, setPlayed] = useState(false);
  const [bookDate, setBookDate] = useState("");
  const [bookTime, setBookTime] = useState("");
  const [bookError, setBookError] = useState<string | null>(null);
  const [audioSolved, setAudioSolved] = useState(false);

  // 4. Watch and answer
  const [answer, setAnswer] = useState("");
  const [answerError, setAnswerError] = useState<string | null>(null);
  const [videoSolved, setVideoSolved] = useState(false);

  const loginSolved = loggedIn;
  const solved = [loginSolved, emailVerified, audioSolved, videoSolved];
  const solvedCount = solved.filter(Boolean).length;
  const allSolved = solvedCount === 4;
  const currentSolved = solved[step];
  const done = step === 3 && (currentSolved || skipped.includes(step));

  function tryLogin() {
    if (
      email.trim().toLowerCase() === DEMO_EMAIL &&
      password === DEMO_PASSWORD
    ) {
      setLoggedIn(true);
      setLoginError(null);
    } else {
      setLoginError("Wrong email or password. Use the demo account above.");
    }
  }

  function makeCode() {
    return String(Math.floor(100000 + Math.random() * 900000));
  }

  function sendCode() {
    if (!/.+@.+\..+/.test(verifyEmail.trim())) {
      setEmailError("Enter a valid email address.");
      return;
    }
    setEmailError(null);
    setSentCode(makeCode());
    setCodeSent(true);
    setInboxOpen(false);
    setCodeInput("");
    setCodeError(null);
  }

  function resendCode() {
    setSentCode(makeCode());
    setInboxOpen(false);
    setCodeInput("");
    setCodeError(null);
  }

  function checkCode() {
    if (codeInput.trim() === sentCode) {
      setEmailVerified(true);
      setCodeError(null);
    } else {
      setCodeError("Wrong code. Open the email and try again.");
    }
  }

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
    }
  }

  function checkAnswer() {
    const norm = answer.trim().toLowerCase().replace(/\s+/g, " ");
    if (norm.includes("control room")) {
      setVideoSolved(true);
      setAnswerError(null);
    } else {
      setAnswerError("Not quite. Watch the video again.");
    }
  }

  function next() {
    if (currentSolved && step < 3) setStep(step + 1);
  }

  function skipTest() {
    if (!currentSolved) {
      setSkipped((prev) => [...prev, step]);
    }
    if (step < 3) setStep(step + 1);
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
        saveProgress({ step4: true, step4Skipped: false });
      } else {
        saveProgress({ step4Skipped: true });
      }
      saveChallengeResults(4, solved, skipped);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [done]);

  return (
    <div className="relative flex min-h-screen flex-col overflow-hidden bg-black px-6 pt-12 pb-28 font-sans text-white">
      <div className="pointer-events-none absolute inset-x-0 top-0 h-96 bg-[radial-gradient(ellipse_at_top,rgba(37,99,235,0.25),transparent_65%)]" />
      <div className="relative mx-auto flex w-full max-w-4xl flex-1 flex-col">
        <div className="flex items-center justify-between">
          <Button
            variant="outline"
            onClick={() => router.push("/gauntlet")}
            className="font-mono"
          >
            ← Back
          </Button>
          <span className="font-mono text-sm text-zinc-400">Challenge 4/5</span>
        </div>

        <div className="flex flex-1 flex-col justify-center py-8">
        {!done && (
          <>
            <div>
              {step === 0 && (
                <TestCard title="Log in to continue. Use the demo account, or continue with Google." solved={loginSolved}>
                  
                  <div className="mx-auto mt-5 max-w-md rounded-lg bg-zinc-900/70 p-4 font-mono text-sm text-zinc-300">
                    <p className="font-semibold text-white">Demo account</p>
                    <p className="mt-1">Email: {DEMO_EMAIL}</p>
                    <p>Password: {DEMO_PASSWORD}</p>
                  </div>
                  {!loggedIn && (
                    <div className="mx-auto mt-5 max-w-md space-y-4">
                      <Button
                        variant="outline"
                        onClick={() => setGoogleOpen((v) => !v)}
                        className="w-full font-mono"
                      >
                        Continue with Google
                      </Button>
                      {googleOpen && (
                        <div className="rounded-lg border border-zinc-700 p-3">
                          <p className="mb-2 text-center font-mono text-sm text-zinc-400">
                            Choose an account
                          </p>
                          <button
                            type="button"
                            onClick={() => setLoggedIn(true)}
                            className="flex w-full items-center gap-3 rounded-lg px-3 py-2 text-left hover:bg-zinc-800"
                          >
                            <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-blue-600 font-mono text-lg font-bold text-white">
                              A
                            </span>
                            <span>
                              <span className="block font-mono text-sm font-semibold">
                                Agent Demo
                              </span>
                              <span className="block font-mono text-xs text-zinc-400">
                                {DEMO_EMAIL}
                              </span>
                            </span>
                          </button>
                        </div>
                      )}
                      <div className="flex items-center gap-3">
                        <span className="h-px flex-1 bg-zinc-700" />
                        <span className="font-mono text-xs text-zinc-500">
                          or
                        </span>
                        <span className="h-px flex-1 bg-zinc-700" />
                      </div>
                      <div>
                        <label className="mb-1.5 block font-mono text-sm font-medium text-zinc-300">
                          Email
                        </label>
                        <Input
                          type="email"
                          value={email}
                          onChange={(e) => setEmail(e.target.value)}
                          placeholder="agent@agentdegree.app"
                          aria-label="Email"
                          className="font-mono"
                        />
                      </div>
                      <div>
                        <label className="mb-1.5 block font-mono text-sm font-medium text-zinc-300">
                          Password
                        </label>
                        <Input
                          type="password"
                          value={password}
                          onChange={(e) => setPassword(e.target.value)}
                          placeholder="Your password"
                          aria-label="Password"
                          className="font-mono"
                        />
                      </div>
                      {loginError && (
                        <p className="text-center font-mono text-sm text-red-400">
                          {loginError}
                        </p>
                      )}
                      <Button
                        onClick={tryLogin}
                        className="w-full font-mono"
                      >
                        Log in
                      </Button>
                    </div>
                  )}
                  {loggedIn && (
                    <p className="mt-5 rounded-lg border border-green-500/40 bg-green-500/10 px-4 py-3 text-center font-mono text-sm text-green-400">
                      Logged in as {DEMO_EMAIL} ✓
                    </p>
                  )}
                </TestCard>
              )}

              {step === 1 && (
                <TestCard title="Type your email. We will send a code — open the email and type the code here." solved={emailVerified}>
                  
                  {!codeSent && (
                    <div className="mx-auto mt-5 max-w-md space-y-4">
                      <div>
                        <label className="mb-1.5 block font-mono text-sm font-medium text-zinc-300">
                          Email
                        </label>
                        <Input
                          type="email"
                          value={verifyEmail}
                          onChange={(e) => setVerifyEmail(e.target.value)}
                          placeholder="agent@agentdegree.app"
                          aria-label="Email"
                          className="font-mono"
                        />
                      </div>
                      {emailError && (
                        <p className="text-center font-mono text-sm text-red-400">
                          {emailError}
                        </p>
                      )}
                      <Button onClick={sendCode} className="w-full font-mono">
                        Send code
                      </Button>
                    </div>
                  )}
                  {codeSent && !emailVerified && (
                    <div className="mx-auto mt-5 max-w-md space-y-4">
                      <p className="text-center font-mono text-sm text-zinc-400">
                        Code sent to {verifyEmail.trim()}. Open the email
                        below.
                      </p>
                      <div className="rounded-lg border border-zinc-700">
                        <p className="border-b border-zinc-700 px-3 py-2 font-mono text-sm font-semibold text-zinc-300">
                          Your inbox
                        </p>
                        <button
                          type="button"
                          onClick={() => setInboxOpen((v) => !v)}
                          className="w-full px-3 py-3 text-left hover:bg-zinc-800"
                        >
                          <span className="block font-mono text-sm font-semibold">
                            AgentDegree — Your verification code
                          </span>
                          <span className="block font-mono text-xs text-zinc-400">
                            from AgentDegree
                          </span>
                        </button>
                        {inboxOpen && (
                          <div className="border-t border-zinc-700 px-3 py-3">
                            <p className="font-mono text-sm text-zinc-300">
                              To: {verifyEmail.trim()}
                            </p>
                            <p className="mt-2 font-mono text-sm text-zinc-300">
                              Your AgentDegree verification code is{" "}
                              <span className="text-lg font-bold text-white">
                                {sentCode}
                              </span>
                            </p>
                          </div>
                        )}
                      </div>
                      <div>
                        <label className="mb-1.5 block font-mono text-sm font-medium text-zinc-300">
                          Verification code
                        </label>
                        <Input
                          type="text"
                          inputMode="numeric"
                          maxLength={6}
                          value={codeInput}
                          onChange={(e) => setCodeInput(e.target.value)}
                          placeholder="6-digit code"
                          aria-label="Verification code"
                          className="font-mono"
                        />
                      </div>
                      {codeError && (
                        <p className="text-center font-mono text-sm text-red-400">
                          {codeError}
                        </p>
                      )}
                      <Button
                        onClick={checkCode}
                        className="w-full font-mono"
                      >
                        Verify code
                      </Button>
                      <Button
                        variant="outline"
                        onClick={resendCode}
                        className="w-full font-mono"
                      >
                        Resend code
                      </Button>
                    </div>
                  )}
                  {emailVerified && (
                    <p className="mt-5 rounded-lg border border-green-500/40 bg-green-500/10 px-4 py-3 text-center font-mono text-sm text-green-400">
                      Email verified ✓
                    </p>
                  )}
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
                      <label className="mb-1.5 block font-mono text-sm font-medium text-zinc-300">
                        Date
                      </label>
                      <Input
                        type="date"
                        value={bookDate}
                        onChange={(e) => setBookDate(e.target.value)}
                        aria-label="Date"
                        className="font-mono"
                      />
                    </div>
                    <div>
                      <label className="mb-1.5 block font-mono text-sm font-medium text-zinc-300">
                        Time
                      </label>
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
                <TestCard title="Watch the video, then answer one question about it." solved={videoSolved}>
                  
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
              )}
            </div>

          </>
        )}

        {allSolved && (
          <div className="flex flex-col items-center justify-center py-8 text-center">
            <p className="font-grotesque text-3xl font-semibold text-green-400">
              Challenge 4 passed.
            </p>
            <Link href="/gauntlet/step-5">
              <Button className="mt-8 h-12 px-8 font-mono text-base font-semibold">Continue to Homework You Can't Skip</Button>
            </Link>
          </div>
        )}

        {done && !allSolved && (
          <div className="flex flex-col items-center justify-center py-8 text-center">
            <p className="font-grotesque text-3xl font-semibold text-amber-400">
              Challenge 4 finished — {skipped.length} test
              {skipped.length > 1 ? "s" : ""} skipped.
            </p>
            <p className="mt-3 font-mono text-base text-zinc-400">
              Solve every test to pass. Retry from the Final Exam.
            </p>
            <Link href="/gauntlet/step-5">
              <Button className="mt-8 h-12 px-8 font-mono text-base font-semibold">Continue to Homework You Can't Skip</Button>
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
            <Button
              onClick={next}
              disabled={!currentSolved}
              className="font-mono"
            >
              Next →
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}

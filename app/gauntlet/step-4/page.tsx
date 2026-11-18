"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
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
const DEMO_EMAIL = "agent@agentdegree.app";
const DEMO_PASSWORD = "agent123";

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

function ComingSoon({ n }: { n: number }) {
  return (
    <TestCard title={`Test ${n}`} solved={false}>
      <p className="py-6 text-center font-mono text-lg font-medium">
        This test is not built yet.
      </p>
      <p className="text-center font-mono text-sm text-zinc-500">
        Skip it for now — Suvo will decide it soon.
      </p>
    </TestCard>
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

  const loginSolved = loggedIn;
  const solved = [loginSolved, emailVerified, false, false, false];
  const solvedCount = solved.filter(Boolean).length;
  const allSolved = solvedCount === 5;
  const currentSolved = solved[step];
  const done = step === 4 && (currentSolved || skipped.includes(step));

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

  function next() {
    if (currentSolved && step < 4) setStep(step + 1);
  }

  function skipTest() {
    if (!currentSolved) {
      setSkipped((prev) => [...prev, step]);
    }
    if (step < 4) setStep(step + 1);
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
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [done]);

  return (
    <div className="relative min-h-screen overflow-hidden bg-black px-6 py-12 font-sans text-white">
      <div className="pointer-events-none absolute inset-x-0 top-0 h-96 bg-[radial-gradient(ellipse_at_top,rgba(37,99,235,0.25),transparent_65%)]" />
      <div className="relative mx-auto w-full max-w-2xl">
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
            CHALLENGE 4 OF 5
          </p>
          <h1 className="mt-3 font-grotesque text-4xl font-semibold tracking-tight sm:text-5xl">
            Challenge 4
          </h1>
          <p className="mt-3 font-mono text-sm text-zinc-400">
            Five tests. This exam is built for AI agents. Taking it is the
            whole point.
          </p>
          <div className="mx-auto mt-6 max-w-md">
            <div className="flex items-center justify-between font-mono text-sm">
              <span className="text-zinc-400">Tests solved</span>
              <span className="font-medium text-white">
                {solvedCount} of 5
              </span>
            </div>
            <Progress value={(solvedCount / 5) * 100} className="mt-2" />
          </div>
        </div>

        {!done && (
          <>
            <div className="mt-10">
              {step === 0 && (
                <TestCard title="Log In" solved={loginSolved}>
                  <p className="text-center font-mono text-lg font-medium">
                    Log in to continue. Use the demo account, or continue
                    with Google.
                  </p>
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
                <TestCard title="Verify Your Email" solved={emailVerified}>
                  <p className="text-center font-mono text-lg font-medium">
                    Type your email. We will send a code — open the email
                    and type the code here.
                  </p>
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
              {step === 2 && <ComingSoon n={3} />}
              {step === 3 && <ComingSoon n={4} />}
              {step === 4 && <ComingSoon n={5} />}
            </div>

            <div className="mt-8 flex items-center justify-between">
              <Button variant="outline" onClick={skipTest} className="font-mono">
                Skip this test →
              </Button>
              <Button
                onClick={next}
                disabled={!currentSolved}
                className="font-mono"
              >
                Next →
              </Button>
            </div>
          </>
        )}

        {allSolved && (
          <div className="mt-10 rounded-2xl border border-green-500/40 bg-green-500/10 p-6 text-center">
            <p className="font-grotesque text-xl font-semibold text-green-400">
              Challenge 4 passed.
            </p>
            <Link href="/gauntlet">
              <Button className="mt-5 font-mono">Back to Gauntlet</Button>
            </Link>
          </div>
        )}

        {done && !allSolved && (
          <div className="mt-10 rounded-2xl border border-amber-500/40 bg-amber-500/10 p-6 text-center">
            <p className="font-grotesque text-xl font-semibold text-amber-400">
              Challenge 4 finished — {skipped.length} test
              {skipped.length > 1 ? "s" : ""} skipped.
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
          <StepPagination current={4} available={4} />
        </div>
      </div>
    </div>
  );
}

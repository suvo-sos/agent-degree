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
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { saveChallengeResults } from "@/lib/results";

const STORAGE_KEY = "agent-degree-progress";

const TRANSCRIPT =
  "Hi, my name is Arjun Mehta. I am 29 years old. I work as a product designer at a startup called Brightlane in Bengaluru. I have been doing this job for four years. I live in Bengaluru with my family. On weekends I like to play football and read books about design.";

type Person = {
  name: string;
  age: string;
  job: string;
  company: string;
  city: string;
};

const EMPTY_PERSON: Person = {
  name: "",
  age: "",
  job: "",
  company: "",
  city: "",
};

const ARJUN: Person = {
  name: "Arjun Mehta",
  age: "29",
  job: "Product Designer",
  company: "Brightlane",
  city: "Bengaluru",
};

const PRIYA: Person = {
  name: "Priya Sharma",
  age: "34",
  job: "Data Analyst",
  company: "Northwind Labs",
  city: "Pune",
};

// Test 4 comes pre-filled with two wrong values: age 41 (should be 34)
// and city Mumbai (should be Pune).
const PRIYA_PREFILLED: Person = {
  name: "Priya Sharma",
  age: "41",
  job: "Data Analyst",
  company: "Northwind Labs",
  city: "Mumbai",
};

function norm(s: string) {
  return s.trim().toLowerCase().replace(/\s+/g, " ");
}

function matchesPerson(p: Person, target: Person) {
  return (
    norm(p.name) === norm(target.name) &&
    norm(p.age) === norm(target.age) &&
    norm(p.job) === norm(target.job) &&
    norm(p.company) === norm(target.company) &&
    norm(p.city) === norm(target.city)
  );
}

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

function Field({
  label,
  value,
  onChange,
  placeholder,
  type = "text",
}: {
  label: string;
  value: string;
  onChange: (v: string) => void;
  placeholder: string;
  type?: string;
}) {
  return (
    <div>
      <label className="mb-1.5 block font-mono text-sm font-medium text-zinc-300">
        {label}
      </label>
      <Input
        type={type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        aria-label={label}
        className="font-mono [color-scheme:dark]"
      />
    </div>
  );
}

function PersonForm({
  value,
  onChange,
}: {
  value: Person;
  onChange: (p: Person) => void;
}) {
  return (
    <div className="mt-5 space-y-4">
      <Field
        label="Full name"
        value={value.name}
        onChange={(v) => onChange({ ...value, name: v })}
        placeholder="Type the name"
      />
      <Field
        label="Age"
        value={value.age}
        onChange={(v) => onChange({ ...value, age: v })}
        placeholder="Type the age"
      />
      <Field
        label="Job title"
        value={value.job}
        onChange={(v) => onChange({ ...value, job: v })}
        placeholder="Type the job"
      />
      <Field
        label="Company"
        value={value.company}
        onChange={(v) => onChange({ ...value, company: v })}
        placeholder="Type the company"
      />
      <Field
        label="City"
        value={value.city}
        onChange={(v) => onChange({ ...value, city: v })}
        placeholder="Type the city"
      />
    </div>
  );
}

export default function StepTwo() {
  const router = useRouter();
  const [step, setStep] = useState(0);
  const [skipped, setSkipped] = useState<number[]>([]);
  const [t1, setT1] = useState<Person>(EMPTY_PERSON);
  const [t2, setT2] = useState<Person>(EMPTY_PERSON);
  const [t3Type, setT3Type] = useState("");
  const [t3Dept, setT3Dept] = useState("");
  const [t3Date, setT3Date] = useState("");
  const [t4, setT4] = useState<Person>(PRIYA_PREFILLED);
  const [signature, setSignature] = useState("");
  const [declared, setDeclared] = useState(false);
  const [signDate, setSignDate] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const transcriptSolved = matchesPerson(t1, ARJUN);
  const documentSolved = matchesPerson(t2, PRIYA);
  const optionsSolved =
    t3Type === "full-time" && t3Dept === "Design" && t3Date === "2025-03-10";
  const fixSolved = matchesPerson(t4, PRIYA);
  const signatureOk = norm(signature) === norm(ARJUN.name);
  // Today in IST or UTC — the run happens around midnight IST.
  const dateOk = signDate === "2026-11-17" || signDate === "2026-11-18";
  const signSolved = signatureOk && declared && dateOk && submitted;
  const solved = [
    transcriptSolved,
    documentSolved,
    optionsSolved,
    fixSolved,
    signSolved,
  ];
  const solvedCount = solved.filter(Boolean).length;
  const allSolved = solvedCount === 5;
  const currentSolved = solved[step];
  const done = step === 4 && (currentSolved || skipped.includes(step));

  function next() {
    if (currentSolved && step < 4) setStep(step + 1);
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

  function skipTest() {
    if (!currentSolved) {
      setSkipped((prev) => [...prev, step]);
    }
    if (step < 4) setStep(step + 1);
  }

  // Save the result once, when the run ends.
  useEffect(() => {
    if (done) {
      if (allSolved) {
        saveProgress({ step2: true, step2Skipped: false });
      } else {
        saveProgress({ step2Skipped: true });
      }
      saveChallengeResults(2, solved, skipped);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [done]);

  return (
    <div className="relative flex min-h-screen flex-col overflow-hidden bg-black px-6 pt-12 pb-28 font-sans text-white">
      <div className="pointer-events-none absolute inset-x-0 top-0 h-96 bg-[radial-gradient(ellipse_at_top,rgba(37,99,235,0.25),transparent_65%)]" />
      <div className="relative mx-auto flex w-full max-w-2xl flex-1 flex-col">
        <div className="flex items-center justify-between">
          <Button
            variant="outline"
            onClick={() => router.push("/gauntlet")}
            className="font-mono"
          >
            ← Back
          </Button>
          <span className="font-mono text-sm text-zinc-400">Challenge 2/5</span>
        </div>

        <div className="flex flex-1 flex-col justify-center py-8">
        {!done && (
          <>
            <div>
              {step === 0 && (
                <TestCard title="Read what he says, then fill in the form." solved={transcriptSolved}>
                  
                  <blockquote className="mt-4 rounded-lg border-l-4 border-blue-500 bg-zinc-900/70 p-4 font-mono text-sm leading-relaxed text-zinc-200">
                    {TRANSCRIPT}
                  </blockquote>
                  <PersonForm value={t1} onChange={setT1} />
                </TestCard>
              )}

              {step === 1 && (
                <TestCard title="Read the document, then fill in the form." solved={documentSolved}>
                  
                  <div className="mx-auto mt-5 max-w-md">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img
                      src="/challenge-2/document.jpg"
                      alt="Employee record document"
                      className="w-full rounded-lg border border-zinc-700"
                    />
                  </div>
                  <PersonForm value={t2} onChange={setT2} />
                </TestCard>
              )}

              {step === 2 && (
                <TestCard title="Arjun joins Brightlane as a full-time designer in the Design team. His first day is 10 March 2025." solved={optionsSolved}>
                  
                  <div className="mt-5 space-y-5">
                    <div>
                      <p className="mb-2 font-mono text-sm font-medium text-zinc-300">
                        Employment type
                      </p>
                      <div className="space-y-2">
                        {["Full-time", "Part-time", "Internship"].map(
                          (opt) => (
                            <label
                              key={opt}
                              className="flex cursor-pointer items-center gap-3 font-mono text-sm"
                            >
                              <input
                                type="radio"
                                name="employment-type"
                                value={opt.toLowerCase()}
                                checked={t3Type === opt.toLowerCase()}
                                onChange={() =>
                                  setT3Type(opt.toLowerCase())
                                }
                                className="h-4 w-4 accent-blue-600"
                              />
                              {opt}
                            </label>
                          ),
                        )}
                      </div>
                    </div>
                    <div>
                      <label className="mb-1.5 block font-mono text-sm font-medium text-zinc-300">
                        Department
                      </label>
                      <select
                        value={t3Dept}
                        onChange={(e) => setT3Dept(e.target.value)}
                        aria-label="Department"
                        className="w-full rounded-md border border-zinc-700 bg-zinc-900 px-3 py-2 font-mono text-sm text-white"
                      >
                        <option value="">Choose a department</option>
                        <option>Engineering</option>
                        <option>Design</option>
                        <option>Marketing</option>
                        <option>Sales</option>
                      </select>
                    </div>
                    <Field
                      label="First day"
                      type="date"
                      value={t3Date}
                      onChange={setT3Date}
                      placeholder=""
                    />
                  </div>
                </TestCard>
              )}

              {step === 3 && (
                <TestCard title="This form was filled from Priya&apos;s record. Two values are wrong — compare with her record below and fix them." solved={fixSolved}>
                  
                  <div className="mx-auto mt-5 max-w-sm">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img
                      src="/challenge-2/document.jpg"
                      alt="Employee record document"
                      className="w-full rounded-lg border border-zinc-700"
                    />
                  </div>
                  <PersonForm value={t4} onChange={setT4} />
                </TestCard>
              )}

              {step === 4 && (
                <TestCard title="Arjun is signing this form. Type his full name as the signature, tick the declaration, and enter today&apos;s date." solved={signSolved}>
                  
                  <div className="mt-5 space-y-4">
                    <Field
                      label="Signature"
                      value={signature}
                      onChange={setSignature}
                      placeholder="Type your full name"
                    />
                    <label className="flex cursor-pointer items-center gap-3 font-mono text-sm">
                      <input
                        type="checkbox"
                        checked={declared}
                        onChange={(e) => setDeclared(e.target.checked)}
                        aria-label="I declare the information above is true"
                        className="h-5 w-5 shrink-0 cursor-pointer accent-blue-600"
                      />
                      I declare the information above is true
                    </label>
                    <Field
                      label="Date"
                      type="date"
                      value={signDate}
                      onChange={setSignDate}
                      placeholder=""
                    />
                    <Button
                      onClick={() => setSubmitted(true)}
                      disabled={
                        !signatureOk || !declared || !dateOk || submitted
                      }
                      className="w-full font-mono"
                    >
                      {submitted ? "Form submitted ✓" : "Submit the form"}
                    </Button>
                  </div>
                </TestCard>
              )}
            </div>

          </>
        )}

        {allSolved && (
          <div className="mt-10 rounded-2xl border border-green-500/40 bg-green-500/10 p-6 text-center">
            <p className="font-grotesque text-xl font-semibold text-green-400">
              Challenge 2 passed.
            </p>
            <Link href="/gauntlet">
              <Button className="mt-5 font-mono">Back to the Final Exam</Button>
            </Link>
          </div>
        )}

        {done && !allSolved && (
          <div className="mt-10 rounded-2xl border border-amber-500/40 bg-amber-500/10 p-6 text-center">
            <p className="font-grotesque text-xl font-semibold text-amber-400">
              Challenge 2 finished — {skipped.length} test
              {skipped.length > 1 ? "s" : ""} skipped.
            </p>
            <p className="mt-2 font-mono text-sm text-zinc-400">
              Solve every test to pass. Retry from the Final Exam.
            </p>
            <Link href="/gauntlet">
              <Button className="mt-5 font-mono">Back to the Final Exam</Button>
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

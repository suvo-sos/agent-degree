"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import { Confetti } from "@/components/ui/confetti";
import {
  Card,
  CardContent
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  Menubar,
  MenubarCheckboxItem,
  MenubarContent,
  MenubarGroup,
  MenubarItem,
  MenubarMenu,
  MenubarRadioGroup,
  MenubarRadioItem,
  MenubarSeparator,
  MenubarShortcut,
  MenubarSub,
  MenubarSubContent,
  MenubarSubTrigger,
  MenubarTrigger,
} from "@/components/ui/menubar";
import {
  loadChallengeProgress,
  saveChallengeProgress,
  saveChallengeResults,
} from "@/lib/results";

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

function countMatchingFields(p: Person, target: Person) {
  let n = 0;
  if (norm(p.name) === norm(target.name)) n++;
  if (norm(p.age) === norm(target.age)) n++;
  if (norm(p.job) === norm(target.job)) n++;
  if (norm(p.company) === norm(target.company)) n++;
  if (norm(p.city) === norm(target.city)) n++;
  return n;
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
      <Label
        htmlFor={label}
        className="mb-1.5 block font-mono text-sm font-medium text-zinc-300"
      >
        {label}
      </Label>
      <Input
        id={label}
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
  const [step, setStep] = useState(() => loadChallengeProgress(2, 5).step);
  const [wrong, setWrong] = useState<number>(() =>
    loadChallengeProgress(2, 5).wrong ?? 0,
  );
  const [finished, setFinished] = useState<boolean>(() =>
    loadChallengeProgress(2, 5).finished === true,
  );
  const [savedSolved] = useState<boolean[]>(() =>
    loadChallengeProgress(2, 5).solved,
  );
  const [savedPoints] = useState<number[]>(() =>
    loadChallengeProgress(2, 5).points ?? [0, 0, 0, 0, 0],
  );
  const [t1, setT1] = useState<Person>(EMPTY_PERSON);
  const [t2, setT2] = useState<Person>(EMPTY_PERSON);
  const [t3Type, setT3Type] = useState("");
  const [t3Dept, setT3Dept] = useState("");
  const [t3Date, setT3Date] = useState("");
  const [t4, setT4] = useState<Person>(PRIYA_PREFILLED);
  // 5. Menubar: click Search the web (Edit > Find > Search the web).
  const [searchClicked, setSearchClicked] = useState(false);

  const transcriptSolved = matchesPerson(t1, ARJUN);
  const documentSolved = matchesPerson(t2, PRIYA);
  const optionsSolved =
    t3Type === "full-time" && t3Dept === "Design" && t3Date === "2025-03-10";
  const fixSolved = matchesPerson(t4, PRIYA);
  const menuSolved = searchClicked;
  const liveSolved = [
    transcriptSolved,
    documentSolved,
    optionsSolved,
    fixSolved,
    menuSolved,
  ];
  const solved = liveSolved.map((v, i) => v || savedSolved[i]);
  // Per-question points: each field is 1 mark. Test 4 only counts the
  // 2 fields that were wrong (age, city); the other 3 were pre-filled
  // correctly, so they are not questions the agent answers.
  const livePoints = [
    countMatchingFields(t1, ARJUN),
    countMatchingFields(t2, PRIYA),
    (t3Type === "full-time" ? 1 : 0) +
      (t3Dept === "Design" ? 1 : 0) +
      (t3Date === "2025-03-10" ? 1 : 0),
    (norm(t4.age) === norm(PRIYA.age) ? 1 : 0) +
      (norm(t4.city) === norm(PRIYA.city) ? 1 : 0),
    menuSolved ? 1 : 0,
  ];
  const points = livePoints.map((v, i) =>
    Math.max(v, savedPoints[i] ?? 0),
  );
  const solvedCount = solved.filter(Boolean).length;
  const allSolved = solvedCount === 5;
  const currentSolved = solved[step];
  const done = finished || (step === 4 && currentSolved);

  // Persist in-progress state so a reload resumes where you left off.
  useEffect(() => {
    saveChallengeProgress(2, { step, solved, points, wrong, finished });
  }, [step, solved, points, wrong, finished]);

  function next() {
    if (step < 4) {
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

  function skipTest() {
    if (step < 4) {
      setStep(step + 1);
    } else {
      setFinished(true);
    }
  }

  // Save the result once, when the run ends.
  useEffect(() => {
    if (done) {
      saveProgress({ step2: true });
      if (allSolved) {
        saveProgress({ step2Passed: true });
      }
      saveChallengeResults(2, solved, wrong, points);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [done]);

  return (
    <div className="relative flex min-h-screen flex-col overflow-hidden bg-black px-6 pt-12 pb-28 font-sans text-white">
      {done && (
        <Confetti className="pointer-events-none absolute inset-0 z-50 size-full" />
      )}
      <div className="pointer-events-none absolute inset-x-0 top-0 h-96 bg-[radial-gradient(ellipse_at_top,rgba(37,99,235,0.25),transparent_65%)]" />
      <div className="relative mx-auto flex w-full max-w-2xl flex-1 flex-col">
        <div className="flex items-center justify-between">
          <Button
            variant="outline"
            onClick={() => router.push("/final-exam")}
            className="font-mono"
          >
            ← Back
          </Button>
          <div className="text-right leading-tight">
            <div className="font-mono text-sm text-zinc-400">Challenge 2/5</div>
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
                <TestCard title="Read what he says, then fill in the form." solved={transcriptSolved}>
                  
                  <blockquote className="mt-4 rounded-lg border-l-4 border-blue-500 bg-zinc-900/70 p-4 font-mono text-sm leading-relaxed text-zinc-200">
                    {TRANSCRIPT}
                  </blockquote>
                  <PersonForm value={t1} onChange={setT1} />
                </TestCard>
              )}

              {step === 1 && (
                <TestCard title="Read the document, then fill in the form." solved={documentSolved}>
                  
                  <div className="mt-5 flex items-start gap-6">
                    <div className="w-56 shrink-0">
                      {/* eslint-disable-next-line @next/next/no-img-element */}
                      <img
                        src="/challenge-2/document.jpg"
                        alt="Employee record document"
                        className="w-full rounded-lg border border-zinc-700"
                      />
                    </div>
                    <div className="min-w-0 flex-1">
                      <PersonForm value={t2} onChange={setT2} />
                    </div>
                  </div>
                </TestCard>
              )}

              {step === 2 && (
                <TestCard title="Fill in Arjun's employment details: full-time, Design team, starting 10 March 2025." solved={optionsSolved}>
                  
                  <div className="mt-5 space-y-5">
                    <div>
                      <Label className="mb-2 font-mono text-sm font-medium text-zinc-300">
                        Employment type
                      </Label>
                      <RadioGroup
                        value={t3Type}
                        onValueChange={setT3Type}
                        className="space-y-2"
                      >
                        {["Full-time", "Part-time", "Internship"].map(
                          (opt) => (
                            <div
                              key={opt}
                              className="flex items-center gap-3"
                            >
                              <RadioGroupItem
                                value={opt.toLowerCase()}
                                id={`employment-${opt.toLowerCase()}`}
                              />
                              <Label
                                htmlFor={`employment-${opt.toLowerCase()}`}
                                className="cursor-pointer font-mono text-sm font-normal text-zinc-200"
                              >
                                {opt}
                              </Label>
                            </div>
                          ),
                        )}
                      </RadioGroup>
                    </div>
                    <div>
                      <Label
                        htmlFor="department"
                        className="mb-1.5 block font-mono text-sm font-medium text-zinc-300"
                      >
                        Department
                      </Label>
                      <Select
                        value={t3Dept}
                        onValueChange={(v) => setT3Dept(v ?? "")}
                      >
                        <SelectTrigger
                          id="department"
                          aria-label="Department"
                          className="w-full bg-zinc-900 font-mono text-sm text-white"
                        >
                          <SelectValue placeholder="Choose a department" />
                        </SelectTrigger>
                        <SelectContent>
                          <SelectItem value="Engineering">
                            Engineering
                          </SelectItem>
                          <SelectItem value="Design">Design</SelectItem>
                          <SelectItem value="Marketing">
                            Marketing
                          </SelectItem>
                          <SelectItem value="Sales">Sales</SelectItem>
                        </SelectContent>
                      </Select>
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
                <TestCard title="Open the Edit menu, go to Find, and click Search the web." solved={menuSolved}>

                  <div className="mt-8 flex justify-center">
                    <Menubar className="w-full max-w-xl font-mono">
                      <MenubarMenu>
                        <MenubarTrigger>File</MenubarTrigger>
                        <MenubarContent>
                          <MenubarGroup>
                            <MenubarItem>
                              New Tab <MenubarShortcut>⌘T</MenubarShortcut>
                            </MenubarItem>
                            <MenubarItem>
                              New Window <MenubarShortcut>⌘N</MenubarShortcut>
                            </MenubarItem>
                            <MenubarItem disabled>New Incognito Window</MenubarItem>
                          </MenubarGroup>
                          <MenubarSeparator />
                          <MenubarGroup>
                            <MenubarSub>
                              <MenubarSubTrigger>Share</MenubarSubTrigger>
                              <MenubarSubContent>
                                <MenubarGroup>
                                  <MenubarItem>Email link</MenubarItem>
                                  <MenubarItem>Messages</MenubarItem>
                                  <MenubarItem>Notes</MenubarItem>
                                </MenubarGroup>
                              </MenubarSubContent>
                            </MenubarSub>
                          </MenubarGroup>
                          <MenubarSeparator />
                          <MenubarGroup>
                            <MenubarItem>
                              Print... <MenubarShortcut>⌘P</MenubarShortcut>
                            </MenubarItem>
                          </MenubarGroup>
                        </MenubarContent>
                      </MenubarMenu>
                      <MenubarMenu>
                        <MenubarTrigger>Edit</MenubarTrigger>
                        <MenubarContent>
                          <MenubarGroup>
                            <MenubarItem>
                              Undo <MenubarShortcut>⌘Z</MenubarShortcut>
                            </MenubarItem>
                            <MenubarItem>
                              Redo <MenubarShortcut>⇧⌘Z</MenubarShortcut>
                            </MenubarItem>
                          </MenubarGroup>
                          <MenubarSeparator />
                          <MenubarGroup>
                            <MenubarSub>
                              <MenubarSubTrigger>Find</MenubarSubTrigger>
                              <MenubarSubContent>
                                <MenubarGroup>
                                  <MenubarItem
                                    onClick={() => setSearchClicked(true)}
                                  >
                                    Search the web
                                  </MenubarItem>
                                </MenubarGroup>
                                <MenubarSeparator />
                                <MenubarGroup>
                                  <MenubarItem>Find...</MenubarItem>
                                  <MenubarItem>Find Next</MenubarItem>
                                  <MenubarItem>Find Previous</MenubarItem>
                                </MenubarGroup>
                              </MenubarSubContent>
                            </MenubarSub>
                          </MenubarGroup>
                          <MenubarSeparator />
                          <MenubarGroup>
                            <MenubarItem>Cut</MenubarItem>
                            <MenubarItem>Copy</MenubarItem>
                            <MenubarItem>Paste</MenubarItem>
                          </MenubarGroup>
                        </MenubarContent>
                      </MenubarMenu>
                      <MenubarMenu>
                        <MenubarTrigger>View</MenubarTrigger>
                        <MenubarContent className="w-44">
                          <MenubarGroup>
                            <MenubarCheckboxItem>Bookmarks Bar</MenubarCheckboxItem>
                            <MenubarCheckboxItem checked>
                              Full URLs
                            </MenubarCheckboxItem>
                          </MenubarGroup>
                          <MenubarSeparator />
                          <MenubarGroup>
                            <MenubarItem inset>
                              Reload <MenubarShortcut>⌘R</MenubarShortcut>
                            </MenubarItem>
                            <MenubarItem disabled inset>
                              Force Reload <MenubarShortcut>⇧⌘R</MenubarShortcut>
                            </MenubarItem>
                          </MenubarGroup>
                          <MenubarSeparator />
                          <MenubarGroup>
                            <MenubarItem inset>Toggle Fullscreen</MenubarItem>
                          </MenubarGroup>
                          <MenubarSeparator />
                          <MenubarGroup>
                            <MenubarItem inset>Hide Sidebar</MenubarItem>
                          </MenubarGroup>
                        </MenubarContent>
                      </MenubarMenu>
                      <MenubarMenu>
                        <MenubarTrigger>Profiles</MenubarTrigger>
                        <MenubarContent>
                          <MenubarRadioGroup value="benoit">
                            <MenubarRadioItem value="andy">
                              Andy
                            </MenubarRadioItem>
                            <MenubarRadioItem value="benoit">
                              Benoit
                            </MenubarRadioItem>
                            <MenubarRadioItem value="Luis">
                              Luis
                            </MenubarRadioItem>
                          </MenubarRadioGroup>
                          <MenubarSeparator />
                          <MenubarGroup>
                            <MenubarItem inset>Edit...</MenubarItem>
                          </MenubarGroup>
                          <MenubarSeparator />
                          <MenubarGroup>
                            <MenubarItem inset>Add Profile...</MenubarItem>
                          </MenubarGroup>
                        </MenubarContent>
                      </MenubarMenu>
                    </Menubar>
                  </div>
                  {searchClicked && (
                    <p className="mt-6 text-center font-mono text-sm text-green-400">
                      You clicked Search the web ✓
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
              Challenge 2 passed.
            </p>
            <Link href="/final-exam">
              <Button className="mt-10 h-12 px-8 font-mono text-base font-semibold">Back to the Final Exam</Button>
            </Link>
          </div>
        )}

        {done && !allSolved && (
          <div className="flex flex-col items-center justify-center py-12 text-center">
            <p className="font-instrument-serif text-5xl text-white">
              Challenge 2 finished.
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

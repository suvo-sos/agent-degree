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
import {
  loadChallengeProgress,
  saveChallengeProgress,
  saveChallengeResults,
} from "@/lib/results";

const STORAGE_KEY = "agent-degree-progress";
const TARGET_COLOUR = "#885566";
const COLOURS = [
  "#e74c3c",
  "#3498db",
  "#2ecc71",
  "#f1c40f",
  "#9b59b6",
  "#885566",
  "#e67e22",
  "#1abc9c",
  "#996677",
];
const FRUITS = ["Apple", "Banana", "Cherry", "Mango", "Orange"];
const TABS = ["Home", "Profile", "Settings"];

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

export default function StepThree() {
  const router = useRouter();
  const [step, setStep] = useState(() => loadChallengeProgress(3, 10).step);
  const [skipped, setSkipped] = useState<number[]>(() =>
    loadChallengeProgress(3, 10).skipped,
  );
  const [savedSolved] = useState<boolean[]>(() =>
    loadChallengeProgress(3, 10).solved,
  );

  // 1. Menu
  const [menuOpen, setMenuOpen] = useState(false);
  const [menuPicked, setMenuPicked] = useState<string | null>(null);
  // 2. Progress
  const [progInput, setProgInput] = useState("");
  const [progValue, setProgValue] = useState<number | null>(null);
  // 3. Colour
  const [wrongColour, setWrongColour] = useState<number | null>(null);
  const [colourPicked, setColourPicked] = useState(false);
  // 4. Switch
  const [switchOn, setSwitchOn] = useState(false);
  // 5. Tabs
  const [activeTab, setActiveTab] = useState("Home");
  // 6. Accordion
  const [openSection, setOpenSection] = useState<number | null>(null);
  // 7. Stars
  const [rating, setRating] = useState(0);
  // 8. Search
  const [query, setQuery] = useState("");
  const [fruitPicked, setFruitPicked] = useState<string | null>(null);
  // 9. Counter
  const [count, setCount] = useState(0);
  // 10. Checkboxes
  const [checked, setChecked] = useState<string[]>([]);

  const menuSolved = menuPicked === "Option 6";
  const progressSolved = progValue === 75;
  const colourSolved = colourPicked;
  const switchSolved = switchOn;
  const tabsSolved = activeTab === "Settings";
  const accordionSolved = openSection === 3;
  const starsSolved = rating === 4;
  const searchSolved = fruitPicked === "Banana";
  const counterSolved = count === 5;
  const boxesSolved =
    checked.includes("Apple") &&
    checked.includes("Mango") &&
    checked.length === 2;

  const liveSolved = [
    menuSolved,
    progressSolved,
    colourSolved,
    switchSolved,
    tabsSolved,
    accordionSolved,
    starsSolved,
    searchSolved,
    counterSolved,
    boxesSolved,
  ];
  const solved = liveSolved.map((v, i) => v || savedSolved[i]);
  const solvedCount = solved.filter(Boolean).length;
  const allSolved = solvedCount === 10;
  const currentSolved = solved[step];
  const done = step === 9 && (currentSolved || skipped.includes(step));

  // Persist in-progress state so a reload resumes where you left off.
  useEffect(() => {
    saveChallengeProgress(3, { step, solved, skipped });
  }, [step, solved, skipped]);

  function pickColour(i: number) {
    if (COLOURS[i] === TARGET_COLOUR) {
      setColourPicked(true);
    } else {
      setWrongColour(i);
      window.setTimeout(
        () => setWrongColour((cur) => (cur === i ? null : cur)),
        900,
      );
    }
  }

  function setProgress() {
    const n = parseInt(progInput, 10);
    if (!Number.isNaN(n)) {
      setProgValue(Math.max(0, Math.min(100, n)));
    }
  }

  function toggleFruit(f: string) {
    setChecked((prev) =>
      prev.includes(f) ? prev.filter((x) => x !== f) : [...prev, f],
    );
  }

  function next() {
    if (!currentSolved) {
      setSkipped((prev) => [...prev, step]);
    }
    if (step < 9) setStep(step + 1);
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
    if (step < 9) setStep(step + 1);
  }

  // Save the result once, when the run ends.
  useEffect(() => {
    if (done) {
      if (allSolved) {
        saveProgress({ step3: true, step3Skipped: false });
      } else {
        saveProgress({ step3Skipped: true });
      }
      saveChallengeResults(3, solved, skipped);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [done]);

  const filteredFruits = FRUITS.filter((f) =>
    f.toLowerCase().includes(query.trim().toLowerCase()),
  );

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
          <div className="text-right leading-tight">
            <div className="font-mono text-sm text-zinc-400">Challenge 3/5</div>
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
                <TestCard title="Open the menu and click Option 6." solved={menuSolved}>
                  
                  <div className="relative mx-auto mt-5 max-w-xs">
                    <Button
                      onClick={() => setMenuOpen((v) => !v)}
                      aria-haspopup="menu"
                      aria-expanded={menuOpen}
                      className="w-full font-mono"
                    >
                      {menuOpen ? "Close menu ↑" : "Open menu ↓"}
                    </Button>
                    {menuOpen && (
                      <div
                        role="menu"
                        className="absolute left-0 right-0 z-10 mt-2 overflow-hidden rounded-lg border border-zinc-700 bg-zinc-900 shadow-xl"
                      >
                        {Array.from({ length: 8 }, (_, i) => (
                          <button
                            key={i}
                            type="button"
                            role="menuitem"
                            onClick={() => {
                              setMenuPicked(`Option ${i + 1}`);
                              setMenuOpen(false);
                            }}
                            className="block w-full px-4 py-3 text-left font-mono text-sm text-zinc-200 hover:bg-zinc-800"
                          >
                            Option {i + 1}
                          </button>
                        ))}
                      </div>
                    )}
                  </div>
                  {menuPicked && (
                    <p className="mt-4 text-center font-mono text-sm text-zinc-400">
                      You picked {menuPicked}
                    </p>
                  )}
                </TestCard>
              )}

              {step === 1 && (
                <TestCard title="Set the progress bar to 75." solved={progressSolved}>
                  
                  <div className="mx-auto mt-5 max-w-md">
                    <div className="h-4 w-full overflow-hidden rounded-full bg-zinc-800">
                      <div
                        className="h-full rounded-full bg-blue-600 transition-all"
                        style={{ width: `${progValue ?? 0}%` }}
                      />
                    </div>
                    <p className="mt-2 text-center font-mono text-2xl font-bold tabular-nums">
                      {progValue ?? 0} / 100
                    </p>
                    <div className="mt-4 flex gap-2">
                      <Input
                        type="number"
                        min={0}
                        max={100}
                        value={progInput}
                        onChange={(e) => setProgInput(e.target.value)}
                        placeholder="Type a number 0–100"
                        aria-label="Progress value"
                        className="font-mono [color-scheme:dark]"
                      />
                      <Button onClick={setProgress} className="font-mono">
                        Set
                      </Button>
                    </div>
                  </div>
                </TestCard>
              )}

              {step === 2 && (
                <TestCard title={<>Pick the colour{" "} <span className="font-bold text-white"> {TARGET_COLOUR} </span>{" "} from the colour picker.</>} solved={colourSolved}>
                  
                  <div className="mx-auto mt-5 grid max-w-xs grid-cols-3 gap-3">
                    {COLOURS.map((hex, i) => (
                      <button
                        key={hex}
                        type="button"
                        onClick={() => pickColour(i)}
                        aria-label={`Colour ${i + 1}`}
                        className={`aspect-square rounded-lg transition-all ${
                          wrongColour === i
                            ? "ring-4 ring-red-500"
                            : "ring-1 ring-zinc-700 hover:ring-zinc-300"
                        }`}
                        style={{ backgroundColor: hex }}
                      />
                    ))}
                  </div>
                  {wrongColour !== null && (
                    <p className="mt-4 text-center font-mono text-sm text-red-400">
                      That is not {TARGET_COLOUR}. Try again.
                    </p>
                  )}
                </TestCard>
              )}

              {step === 3 && (
                <TestCard title="Turn the switch on." solved={switchSolved}>
                  
                  <div className="mt-6 flex items-center justify-center gap-4">
                    <span className="font-mono text-sm text-zinc-400">
                      Notifications
                    </span>
                    <button
                      type="button"
                      role="switch"
                      aria-checked={switchOn}
                      aria-label="Notifications switch"
                      onClick={() => setSwitchOn((v) => !v)}
                      className={`relative h-8 w-14 rounded-full transition-colors ${
                        switchOn ? "bg-green-500" : "bg-zinc-700"
                      }`}
                    >
                      <span
                        className={`absolute top-1 h-6 w-6 rounded-full bg-white shadow transition-all ${
                          switchOn ? "left-7" : "left-1"
                        }`}
                      />
                    </button>
                    <span className="font-mono text-sm font-semibold">
                      {switchOn ? "ON" : "OFF"}
                    </span>
                  </div>
                </TestCard>
              )}

              {step === 4 && (
                <TestCard title="Open the Settings tab." solved={tabsSolved}>
                  
                  <div
                    role="tablist"
                    className="mt-5 flex justify-center gap-1 rounded-lg bg-zinc-900 p-1"
                  >
                    {TABS.map((t) => (
                      <button
                        key={t}
                        type="button"
                        role="tab"
                        aria-selected={activeTab === t}
                        onClick={() => setActiveTab(t)}
                        className={`rounded-md px-4 py-2 font-mono text-sm transition-colors ${
                          activeTab === t
                            ? "bg-blue-600 text-white"
                            : "text-zinc-400 hover:text-white"
                        }`}
                      >
                        {t}
                      </button>
                    ))}
                  </div>
                  <p className="mt-4 text-center font-mono text-sm text-zinc-400">
                    {activeTab === "Home" && "This is the home panel."}
                    {activeTab === "Profile" && "This is the profile panel."}
                    {activeTab === "Settings" &&
                      "This is the settings panel."}
                  </p>
                </TestCard>
              )}

              {step === 5 && (
                <TestCard title="Open Section 3." solved={accordionSolved}>
                  
                  <div className="mx-auto mt-5 max-w-md space-y-2">
                    {[1, 2, 3].map((n) => (
                      <div
                        key={n}
                        className="overflow-hidden rounded-lg border border-zinc-700"
                      >
                        <button
                          type="button"
                          onClick={() =>
                            setOpenSection((cur) => (cur === n ? null : n))
                          }
                          aria-expanded={openSection === n}
                          className="flex w-full items-center justify-between bg-zinc-900 px-4 py-3 font-mono text-sm font-medium"
                        >
                          Section {n}
                          <span>{openSection === n ? "−" : "+"}</span>
                        </button>
                        {openSection === n && (
                          <p className="bg-zinc-950 px-4 py-3 font-mono text-sm text-zinc-300">
                            This is the content of section {n}.
                          </p>
                        )}
                      </div>
                    ))}
                  </div>
                </TestCard>
              )}

              {step === 6 && (
                <TestCard title="Give 4 stars." solved={starsSolved}>
                  
                  <div className="mt-5 flex justify-center gap-1">
                    {[1, 2, 3, 4, 5].map((n) => (
                      <button
                        key={n}
                        type="button"
                        onClick={() => setRating(n)}
                        aria-label={`Rate ${n} star${n > 1 ? "s" : ""}`}
                        className={`text-5xl transition-colors ${
                          n <= rating ? "text-yellow-400" : "text-zinc-700"
                        }`}
                      >
                        ★
                      </button>
                    ))}
                  </div>
                  {rating > 0 && (
                    <p className="mt-4 text-center font-mono text-sm text-zinc-400">
                      You rated {rating} star{rating > 1 ? "s" : ""}
                    </p>
                  )}
                </TestCard>
              )}

              {step === 7 && (
                <TestCard title="Search for banana, then click Banana." solved={searchSolved}>
                  
                  <div className="mx-auto mt-5 max-w-md">
                    <Input
                      value={query}
                      onChange={(e) => setQuery(e.target.value)}
                      placeholder="Search the fruits…"
                      aria-label="Search the fruits"
                      className="font-mono"
                    />
                    <div className="mt-3 space-y-2">
                      {filteredFruits.map((f) => (
                        <button
                          key={f}
                          type="button"
                          onClick={() => setFruitPicked(f)}
                          className={`block w-full rounded-lg border px-4 py-3 text-left font-mono text-sm transition-colors ${
                            fruitPicked === f
                              ? "border-blue-500 bg-blue-500/10 text-white"
                              : "border-zinc-700 text-zinc-200 hover:border-zinc-400"
                          }`}
                        >
                          {f}
                        </button>
                      ))}
                      {filteredFruits.length === 0 && (
                        <p className="py-3 text-center font-mono text-sm text-zinc-500">
                          No fruits found.
                        </p>
                      )}
                    </div>
                  </div>
                </TestCard>
              )}

              {step === 8 && (
                <TestCard title="Click the plus button until the counter shows 5." solved={counterSolved}>
                  
                  <p className="mt-6 text-center font-mono text-6xl font-bold tabular-nums">
                    {count}
                  </p>
                  <div className="mt-6 flex justify-center gap-3">
                    <Button
                      variant="outline"
                      onClick={() => setCount((c) => Math.max(0, c - 1))}
                      aria-label="Decrease counter"
                      className="h-12 w-12 font-mono text-2xl"
                    >
                      −
                    </Button>
                    <Button
                      onClick={() => setCount((c) => c + 1)}
                      aria-label="Increase counter"
                      className="h-12 w-12 font-mono text-2xl"
                    >
                      +
                    </Button>
                  </div>
                </TestCard>
              )}

              {step === 9 && (
                <TestCard title="Tick the boxes for Apple and Mango." solved={boxesSolved}>
                  
                  <div className="mx-auto mt-5 max-w-xs space-y-3">
                    {["Apple", "Banana", "Cherry", "Mango"].map((f) => (
                      <label
                        key={f}
                        className="flex cursor-pointer items-center gap-3 font-mono text-sm"
                      >
                        <input
                          type="checkbox"
                          checked={checked.includes(f)}
                          onChange={() => toggleFruit(f)}
                          aria-label={f}
                          className="h-5 w-5 cursor-pointer accent-blue-600"
                        />
                        {f}
                      </label>
                    ))}
                  </div>
                </TestCard>
              )}
            </div>

          </>
        )}

        {allSolved && (
          <div className="flex flex-col items-center justify-center py-8 text-center">
            <p className="font-grotesque text-3xl font-semibold text-green-400">
              Challenge 3 passed.
            </p>
            <Link href="/gauntlet">
              <Button className="mt-8 h-12 px-8 font-mono text-base font-semibold">Back to the Final Exam</Button>
            </Link>
          </div>
        )}

        {done && !allSolved && (
          <div className="flex flex-col items-center justify-center py-8 text-center">
            <p className="font-grotesque text-3xl font-semibold text-amber-400">
              Challenge 3 finished — {skipped.length} test
              {skipped.length > 1 ? "s" : ""} skipped.
            </p>
            <p className="mt-3 font-mono text-base text-zinc-400">
              Solve every test to pass. Retry from the Final Exam.
            </p>
            <Link href="/gauntlet">
              <Button className="mt-8 h-12 px-8 font-mono text-base font-semibold">Back to the Final Exam</Button>
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

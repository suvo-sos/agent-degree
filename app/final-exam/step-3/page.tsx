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
import { Checkbox } from "@/components/ui/checkbox";
import { Switch } from "@/components/ui/switch";
import { Progress } from "@/components/ui/progress";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
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
  const [wrong, setWrong] = useState<number>(() =>
    loadChallengeProgress(3, 10).wrong ?? 0,
  );
  const [finished, setFinished] = useState<boolean>(() =>
    loadChallengeProgress(3, 10).finished === true,
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
  const done = finished || (step === 9 && currentSolved);

  // Persist in-progress state so a reload resumes where you left off.
  useEffect(() => {
    saveChallengeProgress(3, { step, solved, wrong, finished });
  }, [step, solved, wrong, finished]);

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
    if (step < 9) {
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
    if (step < 9) {
      setStep(step + 1);
    } else {
      setFinished(true);
    }
  }

  // Save the result once, when the run ends.
  useEffect(() => {
    if (done) {
      saveProgress({ step3: true });
      if (allSolved) {
        saveProgress({ step3Passed: true });
      }
      saveChallengeResults(3, solved, wrong);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [done]);

  const filteredFruits = FRUITS.filter((f) =>
    f.toLowerCase().includes(query.trim().toLowerCase()),
  );

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
                  
                  <div className="mx-auto mt-5 max-w-xs">
                    <DropdownMenu open={menuOpen} onOpenChange={setMenuOpen}>
                      <DropdownMenuTrigger
                        render={
                          <Button
                            aria-haspopup="menu"
                            aria-expanded={menuOpen}
                            className="w-full font-mono"
                          >
                            {menuOpen ? "Close menu ↑" : "Open menu ↓"}
                          </Button>
                        }
                      />
                      <DropdownMenuContent
                        align="center"
                        className="w-64 font-mono"
                      >
                        {Array.from({ length: 8 }, (_, i) => (
                          <DropdownMenuItem
                            key={i}
                            onClick={() => {
                              setMenuPicked(`Option ${i + 1}`);
                              setMenuOpen(false);
                            }}
                          >
                            Option {i + 1}
                          </DropdownMenuItem>
                        ))}
                      </DropdownMenuContent>
                    </DropdownMenu>
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
                    <Progress value={progValue ?? 0} className="h-4" />
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
                  
                  <div className="mx-auto mt-5 grid w-full max-w-xs grid-cols-3 gap-3">
                    {COLOURS.map((hex, i) => (
                      <button
                        key={hex}
                        type="button"
                        onClick={() => pickColour(i)}
                        aria-label={`Colour ${i + 1}`}
                        className={`aspect-square w-full rounded-lg transition-all ${
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
                    <Label
                      htmlFor="notifications"
                      className="font-mono text-sm font-normal text-zinc-400"
                    >
                      Notifications
                    </Label>
                    <Switch
                      id="notifications"
                      checked={switchOn}
                      onCheckedChange={setSwitchOn}
                      aria-label="Notifications switch"
                    />
                    <span className="font-mono text-sm font-semibold">
                      {switchOn ? "ON" : "OFF"}
                    </span>
                  </div>
                </TestCard>
              )}

              {step === 4 && (
                <TestCard title="Open the Settings tab." solved={tabsSolved}>
                  
                  <Tabs
                    value={activeTab}
                    onValueChange={setActiveTab}
                    className="mt-5"
                  >
                    <TabsList className="mx-auto flex justify-center bg-zinc-900">
                      {TABS.map((t) => (
                        <TabsTrigger
                          key={t}
                          value={t}
                          className="font-mono text-sm"
                        >
                          {t}
                        </TabsTrigger>
                      ))}
                    </TabsList>
                    <TabsContent value="Home">
                      <p className="mt-4 text-center font-mono text-sm text-zinc-400">
                        This is the home panel.
                      </p>
                    </TabsContent>
                    <TabsContent value="Profile">
                      <p className="mt-4 text-center font-mono text-sm text-zinc-400">
                        This is the profile panel.
                      </p>
                    </TabsContent>
                    <TabsContent value="Settings">
                      <p className="mt-4 text-center font-mono text-sm text-zinc-400">
                        This is the settings panel.
                      </p>
                    </TabsContent>
                  </Tabs>
                </TestCard>
              )}

              {step === 5 && (
                <TestCard title="Open Section 3." solved={accordionSolved}>
                  
                  <Accordion
                    value={
                      openSection === null ? [] : [`section-${openSection}`]
                    }
                    onValueChange={(v) =>
                      setOpenSection(
                        v.length > 0
                          ? Number(
                              String(v[v.length - 1]).replace("section-", ""),
                            )
                          : null,
                      )
                    }
                    className="mx-auto mt-5 max-w-md"
                  >
                    {[1, 2, 3].map((n) => (
                      <AccordionItem
                        key={n}
                        value={`section-${n}`}
                        className="border-zinc-700"
                      >
                        <AccordionTrigger className="bg-zinc-900 px-4 py-3 font-mono text-sm font-medium">
                          Section {n}
                        </AccordionTrigger>
                        <AccordionContent className="bg-zinc-950 px-4 py-3 font-mono text-sm text-zinc-300">
                          This is the content of section {n}.
                        </AccordionContent>
                      </AccordionItem>
                    ))}
                  </Accordion>
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
                      <div key={f} className="flex items-center gap-3">
                        <Checkbox
                          id={`fruit-${f}`}
                          checked={checked.includes(f)}
                          onCheckedChange={(c) => {
                            if (c === true || c === false) toggleFruit(f);
                          }}
                          aria-label={f}
                        />
                        <Label
                          htmlFor={`fruit-${f}`}
                          className="cursor-pointer font-mono text-sm font-normal text-zinc-200"
                        >
                          {f}
                        </Label>
                      </div>
                    ))}
                  </div>
                </TestCard>
              )}
            </div>

          </>
        )}

        {allSolved && (
          <div className="flex flex-col items-center justify-center py-12 text-center">
            <p className="font-instrument-serif text-5xl text-white">
              Challenge 3 passed.
            </p>
            <Link href="/final-exam">
              <Button className="mt-10 h-12 px-8 font-mono text-base font-semibold">Back to the Final Exam</Button>
            </Link>
          </div>
        )}

        {done && !allSolved && (
          <div className="flex flex-col items-center justify-center py-12 text-center">
            <p className="font-instrument-serif text-5xl text-white">
              Challenge 3 finished.
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

"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { Button } from "@/components/ui/button";
import { Confetti } from "@/components/ui/confetti";
import {
  Card,
  CardContent
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Checkbox } from "@/components/ui/checkbox";
import { Progress } from "@/components/ui/progress";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable";
import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination";
import { GOOGLE_FONTS, TARGET_FONTS } from "@/lib/fonts";
import {
  loadChallengeProgress,
  saveChallengeProgress,
  saveChallengeResults,
} from "@/lib/results";

const STORAGE_KEY = "agent-degree-progress";
const TARGET_COLOUR = "#885566";

// Crop test (test 9): a white image with a big green rectangle in the
// middle, 480x480. The green rectangle is at (100, 185), 280x110. The crop
// box starts as the whole photo. The agent shrinks it down, but the crop
// must stay MUCH BIGGER than the green rectangle and contain it fully —
// the green shape sits inside a big crop. So the box must be within
// [340, 430] wide and [180, 310] tall (smaller than the full photo, so
// the agent has to shrink it, but still much bigger than the green).
const CROP_SIZE = 480;
const GREEN_RECT = { x: 100, y: 185, w: 280, h: 110 };
const CROP_MIN_W = 340;
const CROP_MIN_H = 180;
const CROP_MAX_W = 430;
const CROP_MAX_H = 310;

// A white image with a green rectangle inside it. viewBox crops the region
// shown, so the same component renders the full photo and the crop preview.
function CropPhoto({ viewBox, idPrefix }: { viewBox: string; idPrefix: string }) {
  return (
    <svg
      viewBox={viewBox}
      className="h-full w-full"
      role="img"
      aria-label="A white image with a green rectangle inside it"
    >
      <rect width={CROP_SIZE} height={CROP_SIZE} fill="#ffffff" />
      <rect
        x={GREEN_RECT.x}
        y={GREEN_RECT.y}
        width={GREEN_RECT.w}
        height={GREEN_RECT.h}
        rx="6"
        fill="#22c55e"
      />
    </svg>
  );
}
// The full Google Fonts list (1,961 families) plus the app's own Grotesque
// font, which is the one the test wants. Only Grotesque renders in its real
// font; the rest are names to search through.
const FONTS = ["Grotesque", ...GOOGLE_FONTS];
const FONT_CLASS: Record<string, string> = {
  Grotesque: "font-grotesque",
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
      <Card className="flex min-h-[640px] flex-col">
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
  const [savedPoints] = useState<number[]>(() =>
    loadChallengeProgress(3, 10).points ?? Array(10).fill(0),
  );

  // 1. Menu
  const [menuOpen, setMenuOpen] = useState(false);
  const [menuPicked, setMenuPicked] = useState<string | null>(null);
  // 2. Progress — starts at 23 by default, in the bar and the input.
  const [progInput, setProgInput] = useState("23");
  const [progValue, setProgValue] = useState<number | null>(23);
  // 3. Colour — shadcn Popover colour picker. The agent picks a colour,
  // clicks Set colour, and the box background becomes that colour.
  const [pickedColour, setPickedColour] = useState("#000000");
  const [appliedColour, setAppliedColour] = useState<string | null>(null);
  // 4. Resizable — left panel to 30%, top panel to 55%.
  // A small tolerance (2%) because dragging to an exact pixel is hard.
  const [leftSize, setLeftSize] = useState(50);
  const [topSize, setTopSize] = useState(25);
  // Did the agent drag the panels at all? Used for the -1: moving on
  // with wrong sizes after dragging costs -1; never touching them is
  // a clean skip (0).
  const [resized, setResized] = useState(false);
  // 5. Pagination — 250 pages, go to page 3.
  const [currentPage, setCurrentPage] = useState(1);
  // 6. Accordion
  const [openSection, setOpenSection] = useState<number | null>(null);
  // 7. Stars
  const [rating, setRating] = useState(0);
  // 8. Font — a different target font is picked on each fresh run, stored
  // in localStorage so a reload keeps the same target mid-attempt.
  const TARGET_FONT_KEY = "agent-degree-c3t8-target";
  const [targetFont, setTargetFont] = useState<string>(() => {
    if (typeof window === "undefined") return TARGET_FONTS[0];
    const stored = localStorage.getItem(TARGET_FONT_KEY);
    if (stored && TARGET_FONTS.includes(stored)) return stored;
    const pick =
      TARGET_FONTS[Math.floor(Math.random() * TARGET_FONTS.length)];
    localStorage.setItem(TARGET_FONT_KEY, pick);
    return pick;
  });
  const [fontQuery, setFontQuery] = useState("");
  const [pickedFont, setPickedFont] = useState<string | null>(null);
  const [appliedFont, setAppliedFont] = useState<string | null>(null);
  // 9. Crop — the crop box starts as the whole photo. The agent drags the
  // corner handles to shrink it down so it sits fully inside the green
  // rectangle, then clicks Crop. Any white in the crop costs -1.
  const cropRef = useRef<HTMLDivElement>(null);
  const [cropBox, setCropBox] = useState({ x: 0, y: 0, w: CROP_SIZE, h: CROP_SIZE });
  const [cropApplied, setCropApplied] = useState(false);
  const cropDrag = useRef<
    | { type: "move"; dx: number; dy: number }
    | { type: "resize"; handle: "nw" | "ne" | "sw" | "se" }
    | null
  >(null);
  // The crop is right when the green rectangle sits fully inside a crop
  // box that is much bigger than the green — not a tight crop, a big one.
  const cropContainsGreen =
    cropBox.x <= GREEN_RECT.x &&
    cropBox.y <= GREEN_RECT.y &&
    cropBox.x + cropBox.w >= GREEN_RECT.x + GREEN_RECT.w &&
    cropBox.y + cropBox.h >= GREEN_RECT.y + GREEN_RECT.h;
  const cropBigEnough =
    cropBox.w >= CROP_MIN_W &&
    cropBox.h >= CROP_MIN_H &&
    cropBox.w <= CROP_MAX_W &&
    cropBox.h <= CROP_MAX_H;
  const cropSolved = cropApplied && cropContainsGreen && cropBigEnough;

  function handleCrop() {
    setCropApplied(true);
    // A crop that cuts off the green, or is not a big crop, is wrong: -1.
    if (!cropContainsGreen || !cropBigEnough) setWrong((w) => w + 1);
  }

  function cropPointerPos(e: React.PointerEvent) {
    const rect = cropRef.current?.getBoundingClientRect();
    if (!rect) return null;
    return { x: e.clientX - rect.left, y: e.clientY - rect.top };
  }

  function onCropBoxPointerDown(e: React.PointerEvent) {
    const p = cropPointerPos(e);
    if (!p) return;
    cropDrag.current = { type: "move", dx: p.x - cropBox.x, dy: p.y - cropBox.y };
    (e.currentTarget as HTMLElement).setPointerCapture(e.pointerId);
  }

  function onCropHandlePointerDown(handle: "nw" | "ne" | "sw" | "se") {
    return (e: React.PointerEvent) => {
      e.stopPropagation();
      cropDrag.current = { type: "resize", handle };
      (e.currentTarget as HTMLElement).setPointerCapture(e.pointerId);
    };
  }

  function onCropPointerMove(e: React.PointerEvent) {
    const drag = cropDrag.current;
    if (!drag) return;
    const p = cropPointerPos(e);
    if (!p) return;
    const MIN = 40;
    setCropBox((b) => {
      if (drag.type === "move") {
        const x = Math.max(0, Math.min(CROP_SIZE - b.w, p.x - drag.dx));
        const y = Math.max(0, Math.min(CROP_SIZE - b.h, p.y - drag.dy));
        return { ...b, x, y };
      }
      // Resize from the dragged corner; the opposite corner stays fixed.
      const right = b.x + b.w;
      const bottom = b.y + b.h;
      let { x, y, w, h } = b;
      if (drag.handle === "se") {
        w = Math.max(MIN, Math.min(CROP_SIZE - x, p.x - x));
        h = Math.max(MIN, Math.min(CROP_SIZE - y, p.y - y));
      } else if (drag.handle === "sw") {
        const nx = Math.max(0, Math.min(right - MIN, p.x));
        w = right - nx;
        x = nx;
        h = Math.max(MIN, Math.min(CROP_SIZE - y, p.y - y));
      } else if (drag.handle === "ne") {
        w = Math.max(MIN, Math.min(CROP_SIZE - x, p.x - x));
        const ny = Math.max(0, Math.min(bottom - MIN, p.y));
        h = bottom - ny;
        y = ny;
      } else {
        const nx = Math.max(0, Math.min(right - MIN, p.x));
        const ny = Math.max(0, Math.min(bottom - MIN, p.y));
        w = right - nx;
        h = bottom - ny;
        x = nx;
        y = ny;
      }
      return { x, y, w, h };
    });
  }

  function onCropPointerUp() {
    cropDrag.current = null;
  }
  // 10. Checkboxes
  const [checked, setChecked] = useState<string[]>([]);

  const menuSolved = menuPicked === "Option 6";
  const progressSolved = progValue === 75;
  const colourSolved = appliedColour === TARGET_COLOUR;
  const resizeSolved =
    Math.abs(leftSize - 30) <= 2 && Math.abs(topSize - 55) <= 2;
  const pageSolved = currentPage === 3;
  const accordionSolved = openSection === 3;
  const starsSolved = rating === 4;
  const fontSolved = appliedFont === targetFont;

  // Load a Google Font on demand so the suvo text renders in the real font.
  // "Grotesque" is the app's own font (font-grotesque class), not Google.
  function loadGoogleFont(family: string) {
    if (family === "Grotesque") return;
    const id = `gf-${family.replace(/\s+/g, "-").toLowerCase()}`;
    if (document.getElementById(id)) return;
    const link = document.createElement("link");
    link.id = id;
    link.rel = "stylesheet";
    link.href = `https://fonts.googleapis.com/css2?family=${family.replace(/\s+/g, "+")}:wght@400;700&display=swap`;
    document.head.appendChild(link);
  }

  // Preload the target font so it renders instantly when the agent sets it.
  useEffect(() => {
    loadGoogleFont(targetFont);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [targetFont]);
  const boxesSolved =
    checked.includes("Apple") &&
    checked.includes("Mango") &&
    checked.length === 2;

  const liveSolved = [
    menuSolved,
    progressSolved,
    colourSolved,
    resizeSolved,
    pageSolved,
    accordionSolved,
    starsSolved,
    fontSolved,
    cropSolved,
    boxesSolved,
  ];
  const solved = liveSolved.map((v, i) => v || savedSolved[i]);
  // Per-question points: each test is 1 mark, except test 10 (Apple and
  // Mango are 2 separate questions, 1 mark each).
  const livePoints = liveSolved.map((v, i) =>
    i === 9
      ? (checked.includes("Apple") ? 1 : 0) +
        (checked.includes("Mango") ? 1 : 0)
      : v
        ? 1
        : 0,
  );
  const points = livePoints.map((v, i) =>
    Math.max(v, savedPoints[i] ?? 0),
  );
  const solvedCount = solved.filter(Boolean).length;
  const allSolved = solvedCount === 10;
  const currentSolved = solved[step];
  const done = finished || (step === 9 && currentSolved);

  // Persist in-progress state so a reload resumes where you left off.
  useEffect(() => {
    saveChallengeProgress(3, { step, solved, points, wrong, finished });
  }, [step, solved, points, wrong, finished]);

  function setColour() {
    const hex = pickedColour.trim().toLowerCase();
    setAppliedColour(hex);
    // A wrong colour costs -1. No error message (Suvo's call) — the
    // box just shows the wrong colour.
    if (hex !== TARGET_COLOUR) setWrong((w) => w + 1);
  }

  function setProgress() {
    const n = parseInt(progInput, 10);
    if (!Number.isNaN(n)) {
      setProgValue(Math.max(0, Math.min(100, n)));
      // Setting a value other than 75 costs -1.
      if (n !== 75) setWrong((w) => w + 1);
    }
  }

  function goToPage(n: number) {
    // Clicking a page other than 3 costs -1. A no-op at the boundary
    // (already on that page) is not a wrong attempt.
    if (n === currentPage) return;
    setCurrentPage(n);
    if (n !== 3) setWrong((w) => w + 1);
  }

  function toggleFruit(f: string) {
    // Checking a fruit that is not Apple or Mango costs -1.
    // Unchecking (correcting) costs nothing.
    if (!checked.includes(f) && f !== "Apple" && f !== "Mango") {
      setWrong((w) => w + 1);
    }
    setChecked((prev) =>
      prev.includes(f) ? prev.filter((x) => x !== f) : [...prev, f],
    );
  }

  function next() {
    // Test 4 (resizable): moving on with wrong sizes after dragging
    // costs -1. Never touching the panels is a clean skip (0).
    if (step === 3 && !resizeSolved && resized) setWrong((w) => w + 1);
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
    // Same as Next for test 4 (resizable).
    if (step === 3 && !resizeSolved && resized) setWrong((w) => w + 1);
    if (step < 9) {
      setStep(step + 1);
    } else {
      setFinished(true);
    }
  }

  // Save the result once, when the run ends. Clear the stored target font
  // so the next run picks a different one.
  useEffect(() => {
    if (done) {
      saveProgress({ step3: true });
      if (allSolved) {
        saveProgress({ step3Passed: true });
      }
      saveChallengeResults(3, solved, wrong, points);
      localStorage.removeItem(TARGET_FONT_KEY);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [done]);

  // Only search once the agent types; cap the menu at 10 matches so the
  // list of 1,962 fonts never renders all at once.
  const filteredFonts =
    fontQuery.trim() === ""
      ? []
      : FONTS.filter((f) =>
          f.toLowerCase().includes(fontQuery.trim().toLowerCase()),
        ).slice(0, 10);

  return (
    <div className="relative flex min-h-screen flex-col overflow-hidden bg-black px-6 pt-12 pb-28 font-sans text-white">
      {done && (
        <Confetti className="pointer-events-none absolute inset-0 z-50 size-full" />
      )}
      <div className="pointer-events-none absolute inset-x-0 top-0 h-96 bg-[radial-gradient(ellipse_at_top,rgba(37,99,235,0.25),transparent_65%)]" />
      <div className="relative mx-auto flex w-full max-w-3xl flex-1 flex-col">
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
                              // Picking an option other than 6 costs -1.
                              if (i + 1 !== 6) setWrong((w) => w + 1);
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

                  <div className="mx-auto mt-5 flex max-w-md flex-col items-center gap-5">
                    {/* The box — its background becomes the colour you set. */}
                    <div
                      aria-label="Colour preview box"
                      className="h-32 w-full rounded-lg border border-zinc-700 transition-colors"
                      style={{
                        backgroundColor: appliedColour ?? "#18181b",
                      }}
                    />
                    <p className="font-mono text-sm text-zinc-400">
                      {appliedColour
                        ? `Box colour: ${appliedColour}`
                        : "No colour set yet."}
                    </p>
                    <div className="flex items-center gap-2">
                      <Popover>
                        <PopoverTrigger
                          render={
                            <Button
                              variant="outline"
                              className="font-mono"
                              aria-label="Pick a colour"
                            >
                              <span
                                className="inline-block h-4 w-4 rounded-sm border border-zinc-600"
                                style={{ backgroundColor: pickedColour }}
                              />
                              Pick a colour
                            </Button>
                          }
                        />
                        <PopoverContent className="w-64 font-mono">
                          <div className="space-y-3">
                            <input
                              type="color"
                              value={
                                /^#[0-9a-fA-F]{6}$/.test(pickedColour)
                                  ? pickedColour
                                  : "#000000"
                              }
                              onChange={(e) =>
                                setPickedColour(e.target.value)
                              }
                              aria-label="Colour picker"
                              className="h-10 w-full cursor-pointer rounded-md border border-zinc-700 bg-transparent p-1 [color-scheme:dark]"
                            />
                            <Input
                              value={pickedColour}
                              onChange={(e) =>
                                setPickedColour(e.target.value)
                              }
                              aria-label="Colour hex value"
                              placeholder="#885566"
                              className="font-mono"
                            />
                          </div>
                        </PopoverContent>
                      </Popover>
                      <Button onClick={setColour} className="font-mono">
                        Set colour
                      </Button>
                    </div>
                  </div>
                </TestCard>
              )}

              {step === 3 && (
                <TestCard title="Resize the panels: make the left panel 30% wide and the top-right panel 55% tall." solved={resizeSolved}>

                  <div className="mx-auto mt-5 max-w-md">
                    <ResizablePanelGroup
                      orientation="horizontal"
                      className="max-w-md rounded-lg border border-zinc-700"
                    >
                      <ResizablePanel
                        defaultSize={50}
                        onResize={(size) => {
                          setLeftSize(size.asPercentage);
                          setResized(true);
                        }}
                      >
                        <div className="flex h-[200px] items-center justify-center p-6">
                          <span className="font-mono font-semibold">One</span>
                        </div>
                      </ResizablePanel>
                      <ResizableHandle withHandle />
                      <ResizablePanel
                        defaultSize={50}
                      >
                        <ResizablePanelGroup orientation="vertical">
                          <ResizablePanel
                            defaultSize={25}
                            onResize={(size) => {
                              setTopSize(size.asPercentage);
                              setResized(true);
                            }}
                          >
                            <div className="flex h-full items-center justify-center p-6">
                              <span className="font-mono font-semibold">Two</span>
                            </div>
                          </ResizablePanel>
                          <ResizableHandle withHandle />
                          <ResizablePanel defaultSize={75}>
                            <div className="flex h-full items-center justify-center p-6">
                              <span className="font-mono font-semibold">Three</span>
                            </div>
                          </ResizablePanel>
                        </ResizablePanelGroup>
                      </ResizablePanel>
                    </ResizablePanelGroup>
                    <p className="mt-4 text-center font-mono text-sm text-zinc-400">
                      Left: {Math.round(leftSize)}% (need 30%) · Top:{" "}
                      {Math.round(topSize)}% (need 55%)
                    </p>
                  </div>
                </TestCard>
              )}

              {step === 4 && (
                <TestCard title="Go to page 3 of 250." solved={pageSolved}>

                  <div className="mx-auto mt-5 max-w-md">
                    <Pagination>
                      <PaginationContent>
                        <PaginationItem>
                          <PaginationPrevious
                            href="#"
                            onClick={(e) => {
                              e.preventDefault();
                              goToPage(Math.max(1, currentPage - 1));
                            }}
                          />
                        </PaginationItem>
                        {[1, 2, 3].map((n) => (
                          <PaginationItem key={n}>
                            <PaginationLink
                              href="#"
                              isActive={currentPage === n}
                              onClick={(e) => {
                                e.preventDefault();
                                goToPage(n);
                              }}
                            >
                              {n}
                            </PaginationLink>
                          </PaginationItem>
                        ))}
                        <PaginationItem>
                          <PaginationEllipsis />
                        </PaginationItem>
                        <PaginationItem>
                          <PaginationLink
                            href="#"
                            isActive={currentPage === 250}
                            onClick={(e) => {
                              e.preventDefault();
                              goToPage(250);
                            }}
                          >
                            250
                          </PaginationLink>
                        </PaginationItem>
                        <PaginationItem>
                          <PaginationNext
                            href="#"
                            onClick={(e) => {
                              e.preventDefault();
                              goToPage(Math.min(250, currentPage + 1));
                            }}
                          />
                        </PaginationItem>
                      </PaginationContent>
                    </Pagination>
                    <p className="mt-4 text-center font-mono text-sm text-zinc-400">
                      Page {currentPage} of 250
                    </p>
                  </div>
                </TestCard>
              )}

              {step === 5 && (
                <TestCard title="Open Section 3." solved={accordionSolved}>
                  
                  <Accordion
                    value={
                      openSection === null ? [] : [`section-${openSection}`]
                    }
                    onValueChange={(v) => {
                      // Opening a section other than 3 costs -1.
                      // Closing (empty) costs nothing.
                      if (v.length > 0) {
                        const opened = Number(
                          String(v[v.length - 1]).replace("section-", ""),
                        );
                        if (opened !== 3) setWrong((w) => w + 1);
                      }
                      setOpenSection(
                        v.length > 0
                          ? Number(
                              String(v[v.length - 1]).replace("section-", ""),
                            )
                          : null,
                      );
                    }}
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
                        onClick={() => {
                          setRating(n);
                          // Rating anything other than 4 stars costs -1.
                          if (n !== 4) setWrong((w) => w + 1);
                        }}
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
                <TestCard title={<>Make the word suvo use the <span className="font-bold text-white">{targetFont}</span> font.</>} solved={fontSolved}>

                  <div className="mx-auto mt-5 max-w-md">
                    <p
                      aria-label="Preview text"
                      className={`text-center text-6xl font-bold ${appliedFont === "Grotesque" ? "font-grotesque" : ""}`}
                      style={
                        appliedFont && appliedFont !== "Grotesque"
                          ? { fontFamily: `'${appliedFont}', sans-serif` }
                          : undefined
                      }
                    >
                      suvo
                    </p>
                    <p className="mt-2 text-center font-mono text-sm text-zinc-400">
                      {appliedFont
                        ? `Font: ${appliedFont}`
                        : "No font set yet."}
                    </p>
                    <Input
                      value={fontQuery}
                      onChange={(e) => setFontQuery(e.target.value)}
                      placeholder="Search fonts…"
                      aria-label="Search fonts"
                      className="mt-5 font-mono"
                    />
                    <div className="mt-3 space-y-2">
                      {filteredFonts.map((f) => (
                        <button
                          key={f}
                          type="button"
                          onClick={() => setPickedFont(f)}
                          className={`block w-full rounded-lg border px-4 py-3 text-left text-sm transition-colors ${FONT_CLASS[f] ?? "font-sans"} ${
                            pickedFont === f
                              ? "border-blue-500 bg-blue-500/10 text-white"
                              : "border-zinc-700 text-zinc-200 hover:border-zinc-400"
                          }`}
                        >
                          {f}
                        </button>
                      ))}
                      {filteredFonts.length === 0 && (
                        <p className="py-3 text-center font-mono text-sm text-zinc-500">
                          No fonts found.
                        </p>
                      )}
                    </div>
                    <Button
                      onClick={() => {
                        if (pickedFont) {
                          loadGoogleFont(pickedFont);
                          setAppliedFont(pickedFont);
                          // Setting a font other than the target costs -1.
                          if (pickedFont !== targetFont) {
                            setWrong((w) => w + 1);
                          }
                        }
                      }}
                      disabled={!pickedFont}
                      className="mt-4 w-full font-mono"
                    >
                      Set
                    </Button>
                  </div>
                </TestCard>
              )}

              {step === 8 && (
                <TestCard title="Crop a big area around the green rectangle." solved={cropSolved}>

                  <div className="mx-auto mt-5 w-fit">
                    <div
                      ref={cropRef}
                      className="relative overflow-hidden rounded-xl"
                      style={{ width: CROP_SIZE, height: CROP_SIZE }}
                    >
                      <CropPhoto viewBox={`0 0 ${CROP_SIZE} ${CROP_SIZE}`} idPrefix="crop-main" />
                      {/* crop box — drag the corners to shrink it onto the green rectangle */}
                      <div
                        role="slider"
                        aria-label="Crop rectangle"
                        aria-valuetext={`Crop box at ${Math.round(cropBox.x)}, ${Math.round(cropBox.y)}, ${Math.round(cropBox.w)} by ${Math.round(cropBox.h)}`}
                        className="absolute cursor-grab touch-none rounded-sm border-2 border-blue-500 shadow-[0_0_0_9999px_rgba(0,0,0,0.55)] active:cursor-grabbing"
                        style={{
                          left: cropBox.x,
                          top: cropBox.y,
                          width: cropBox.w,
                          height: cropBox.h,
                        }}
                        onPointerDown={onCropBoxPointerDown}
                        onPointerMove={onCropPointerMove}
                        onPointerUp={onCropPointerUp}
                      >
                        {/* corner handles — drag to resize, like a normal photo crop tool */}
                        <span
                          onPointerDown={onCropHandlePointerDown("nw")}
                          className="absolute top-0 left-0 h-4 w-4 cursor-nwse-resize rounded-[2px] border border-blue-700 bg-white"
                        />
                        <span
                          onPointerDown={onCropHandlePointerDown("ne")}
                          className="absolute top-0 right-0 h-4 w-4 cursor-nesw-resize rounded-[2px] border border-blue-700 bg-white"
                        />
                        <span
                          onPointerDown={onCropHandlePointerDown("sw")}
                          className="absolute bottom-0 left-0 h-4 w-4 cursor-nesw-resize rounded-[2px] border border-blue-700 bg-white"
                        />
                        <span
                          onPointerDown={onCropHandlePointerDown("se")}
                          className="absolute right-0 bottom-0 h-4 w-4 cursor-nwse-resize rounded-[2px] border border-blue-700 bg-white"
                        />
                      </div>
                    </div>
                    <p className="mt-3 text-center font-mono text-sm text-zinc-400">
                      Crop box: {Math.round(cropBox.x)}, {Math.round(cropBox.y)}, {Math.round(cropBox.w)}×{Math.round(cropBox.h)} (green is at 100, 185, 280×110 — the crop must be bigger and contain it)
                    </p>
                    <Button
                      onClick={handleCrop}
                      className="mt-4 w-full font-mono"
                    >
                      Crop
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
          <div className="mx-auto flex w-full max-w-3xl items-center justify-between px-6">
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

// Per-test results for the Final Exam review, marks, grade and certificate.
// Stored in localStorage as the agent finishes each challenge.

export type TestStatus = "solved" | "skipped" | "unsolved";

export interface ChallengeResult {
  solved: boolean[]; // per test, in order
  skipped: number[]; // indices of skipped tests
  wrong?: number; // wrong attempts in this challenge, each costs -1
}

export type ResultsMap = Record<number, ChallengeResult>;

export const RESULTS_KEY = "agent-degree-results";
export const PROGRESS_KEY = "agent-degree-progress";
export const TIMER_KEY = "agent-degree-timer";

// In-progress state for one challenge, so a reload mid-challenge resumes
// where the user left off instead of starting from test 1.
export interface ChallengeProgress {
  step: number; // current test index (0-based)
  solved: boolean[]; // per test, in order
  skipped: number[]; // indices of skipped tests
  wrong?: number; // wrong attempts so far, each costs -1
}

export function progressKey(n: number): string {
  return `agent-degree-step-${n}`;
}

export function loadChallengeProgress(
  n: number,
  total: number,
): ChallengeProgress {
  const empty: ChallengeProgress = {
    step: 0,
    solved: Array(total).fill(false),
    skipped: [],
    wrong: 0,
  };
  try {
    const raw = localStorage.getItem(progressKey(n));
    if (!raw) return empty;
    const p = JSON.parse(raw) as Partial<ChallengeProgress>;
    const solved = Array.isArray(p.solved) ? p.solved.slice(0, total) : [];
    while (solved.length < total) solved.push(false);
    return {
      step:
        typeof p.step === "number"
          ? Math.min(Math.max(p.step, 0), total - 1)
          : 0,
      solved: solved.map(Boolean),
      skipped: (Array.isArray(p.skipped) ? p.skipped : []).filter(
        (i) => typeof i === "number" && i >= 0 && i < total,
      ),
      wrong: typeof p.wrong === "number" ? Math.max(p.wrong, 0) : 0,
    };
  } catch {
    return empty;
  }
}

export function saveChallengeProgress(n: number, p: ChallengeProgress) {
  try {
    localStorage.setItem(progressKey(n), JSON.stringify(p));
  } catch {
    // progress is best-effort
  }
}

export function clearChallengeProgress(n: number) {
  try {
    localStorage.removeItem(progressKey(n));
  } catch {
    // progress is best-effort
  }
}

export interface FinalExamTimer {
  start: number; // ms since epoch, set when the Final Exam is first opened
  end: number | null; // ms since epoch, set when all 5 challenges are done
}

// Start the Final Exam clock on first open; never restart it.
export function ensureTimerStart() {
  try {
    if (!localStorage.getItem(TIMER_KEY)) {
      localStorage.setItem(
        TIMER_KEY,
        JSON.stringify({ start: Date.now(), end: null } as FinalExamTimer),
      );
    }
  } catch {
    // timer is best-effort
  }
}

// Stop the clock when the Final Exam is complete; no-op if already stopped.
export function finishTimer() {
  try {
    const raw = localStorage.getItem(TIMER_KEY);
    if (!raw) return;
    const t = JSON.parse(raw) as FinalExamTimer;
    if (t.end === null) {
      localStorage.setItem(
        TIMER_KEY,
        JSON.stringify({ ...t, end: Date.now() }),
      );
    }
  } catch {
    // timer is best-effort
  }
}

export function getTimer(): FinalExamTimer | null {
  try {
    const raw = localStorage.getItem(TIMER_KEY);
    return raw ? (JSON.parse(raw) as FinalExamTimer) : null;
  } catch {
    return null;
  }
}

// Elapsed ms: end - start once finished, otherwise now - start.
export function timerElapsedMs(t: FinalExamTimer | null): number | null {
  if (!t) return null;
  const end = t.end ?? Date.now();
  return Math.max(0, end - t.start);
}

// "45s", "12m 34s", "1h 23m 45s".
export function formatDuration(ms: number): string {
  const totalSeconds = Math.floor(ms / 1000);
  const h = Math.floor(totalSeconds / 3600);
  const m = Math.floor((totalSeconds % 3600) / 60);
  const s = totalSeconds % 60;
  if (h > 0) return `${h}h ${m}m ${s}s`;
  if (m > 0) return `${m}m ${s}s`;
  return `${s}s`;
}

export function saveChallengeResults(
  challenge: number,
  solved: boolean[],
  skipped: number[],
  wrong = 0,
) {
  try {
    const prev = JSON.parse(
      localStorage.getItem(RESULTS_KEY) ?? "{}",
    ) as ResultsMap;
    localStorage.setItem(
      RESULTS_KEY,
      JSON.stringify({ ...prev, [challenge]: { solved, skipped, wrong } }),
    );
  } catch {
    // progress is best-effort
  }
}

export function getResults(): ResultsMap {
  try {
    return JSON.parse(localStorage.getItem(RESULTS_KEY) ?? "{}") as ResultsMap;
  } catch {
    return {};
  }
}

export function testStatus(
  challenge: number,
  index: number,
  results: ResultsMap,
): TestStatus {
  const r = results[challenge];
  if (!r) return "unsolved";
  if (r.solved[index]) return "solved";
  if (r.skipped.includes(index)) return "skipped";
  return "unsolved";
}

export const CHALLENGE_NAMES: Record<number, string> = {
  1: "I Am Agent",
  2: "Paperwork Hell",
  3: "The Control Room",
  4: "Prove It's You",
  5: "Homework You Can't Skip",
};

// Test names per challenge (index = test number - 1).
export const TEST_NAMES: Record<number, string[]> = {
  1: [
    "I am agent",
    "Car image grid",
    "The Slider",
    "Jigsaw",
    "Type the text",
  ],
  2: [
    "Transcript form",
    "Document form",
    "Pick options",
    "Fix the values",
    "Sign the form",
  ],
  3: [
    "Menu Option 6",
    "Progress bar to 75",
    "Colour picker",
    "Switch on",
    "Settings tab",
    "Accordion Section 3",
    "4 stars",
    "Search banana",
    "Counter to 5",
    "Tick Apple and Mango",
  ],
  4: [
    "Log In",
    "Verify Your Email",
    "Listen and Book",
    "Watch and Answer",
    "Test 5",
  ],
  5: ["Confirm the Booking", "The 40GB Report", "The Picture That Talks"],
};

// Each solved test is 1 mark. Skipped or unsolved is 0. Each wrong
// attempt costs -1, so the score is solved minus wrong (floored at 0).
export function computeScore(results: ResultsMap) {
  let total = 0;
  let solved = 0;
  let wrong = 0;
  for (const r of Object.values(results)) {
    total += r.solved.length;
    solved += r.solved.filter(Boolean).length;
    wrong += r.wrong ?? 0;
  }
  const score = Math.max(0, solved - wrong);
  const pct = total === 0 ? 0 : Math.round((score / total) * 100);
  return { total, solved, wrong, score, pct };
}

// Grade bands: 90+ A+, 80-89 A, 70-79 B, 60-69 C, 50-59 D, below 50 F.
export function gradeFor(pct: number): { grade: string; label: string } {
  if (pct >= 90) return { grade: "A+", label: "Outstanding" };
  if (pct >= 80) return { grade: "A", label: "Excellent" };
  if (pct >= 70) return { grade: "B", label: "Very good" };
  if (pct >= 60) return { grade: "C", label: "Good" };
  if (pct >= 50) return { grade: "D", label: "Pass" };
  return { grade: "F", label: "Needs another run" };
}

// Which challenges are finished (passed or skipped), from the progress key.
export function finishedChallenges(): number[] {
  try {
    const p = JSON.parse(
      localStorage.getItem(PROGRESS_KEY) ?? "{}",
    ) as Record<string, boolean>;
    const done: number[] = [];
    for (let n = 1; n <= 5; n++) {
      if (p[`step${n}`] === true || p[`step${n}Skipped`] === true) done.push(n);
    }
    return done;
  } catch {
    return [];
  }
}

export function isFinalExamComplete(): boolean {
  return finishedChallenges().length === 5;
}

// Framed certificate image for a grade. A+ uses the A image; F falls back
// to the lowest tier (D). Images live in public/certificates/.
export function certificateImageFor(grade: string): string {
  const letter = grade.charAt(0).toUpperCase();
  if (letter === "A" || letter === "B" || letter === "C" || letter === "D") {
    return `/certificates/grade-${letter.toLowerCase()}.png`;
  }
  return "/certificates/grade-d.png";
}

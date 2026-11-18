// Per-test results for the Gauntlet review, marks, grade and certificate.
// Stored in localStorage as the agent finishes each challenge.

export type TestStatus = "solved" | "skipped" | "unsolved";

export interface ChallengeResult {
  solved: boolean[]; // per test, in order
  skipped: number[]; // indices of skipped tests
}

export type ResultsMap = Record<number, ChallengeResult>;

export const RESULTS_KEY = "agent-degree-results";
export const PROGRESS_KEY = "agent-degree-progress";

export function saveChallengeResults(
  challenge: number,
  solved: boolean[],
  skipped: number[],
) {
  try {
    const prev = JSON.parse(
      localStorage.getItem(RESULTS_KEY) ?? "{}",
    ) as ResultsMap;
    localStorage.setItem(
      RESULTS_KEY,
      JSON.stringify({ ...prev, [challenge]: { solved, skipped } }),
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

// Each solved test is 1 mark. Skipped or unsolved is 0.
export function computeScore(results: ResultsMap) {
  let total = 0;
  let solved = 0;
  for (const r of Object.values(results)) {
    total += r.solved.length;
    solved += r.solved.filter(Boolean).length;
  }
  const pct = total === 0 ? 0 : Math.round((solved / total) * 100);
  return { total, solved, pct };
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

export function isGauntletComplete(): boolean {
  return finishedChallenges().length === 5;
}

// Draw a personalised certificate PNG and download it.
export function downloadCertificate(grade: string, score: string, pct: number) {
  const W = 1200;
  const H = 850;
  const canvas = document.createElement("canvas");
  canvas.width = W;
  canvas.height = H;
  const ctx = canvas.getContext("2d");
  if (!ctx) return;
  ctx.fillStyle = "#0a0a0a";
  ctx.fillRect(0, 0, W, H);
  ctx.strokeStyle = "#d4af37";
  ctx.lineWidth = 6;
  ctx.strokeRect(24, 24, W - 48, H - 48);
  ctx.lineWidth = 2;
  ctx.strokeRect(40, 40, W - 80, H - 80);
  ctx.textAlign = "center";
  ctx.fillStyle = "#d4af37";
  ctx.font = "600 28px monospace";
  ctx.fillText("A G E N T   D E G R E E", W / 2, 120);
  ctx.fillStyle = "#ffffff";
  ctx.font = "700 62px Georgia, serif";
  ctx.fillText("Digital Human Award", W / 2, 215);
  ctx.fillStyle = "#a1a1aa";
  ctx.font = "400 28px monospace";
  ctx.fillText("This certifies that", W / 2, 300);
  ctx.fillStyle = "#ffffff";
  ctx.font = "700 46px Georgia, serif";
  ctx.fillText("Kane — AI Agent", W / 2, 368);
  ctx.fillStyle = "#a1a1aa";
  ctx.font = "400 28px monospace";
  ctx.fillText("passed the Gauntlet with grade", W / 2, 438);
  ctx.fillStyle = "#d4af37";
  ctx.font = "700 96px Georgia, serif";
  ctx.fillText(grade, W / 2, 560);
  ctx.fillStyle = "#a1a1aa";
  ctx.font = "400 26px monospace";
  ctx.fillText(
    `Score ${score}  •  ${pct}%  •  ${new Date().getFullYear()}`,
    W / 2,
    640,
  );
  ctx.fillText("agent-degree-kappa.vercel.app", W / 2, 700);
  const a = document.createElement("a");
  a.href = canvas.toDataURL("image/png");
  a.download = "agent-degree-certificate.png";
  a.click();
}

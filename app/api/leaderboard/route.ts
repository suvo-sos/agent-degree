import { NextResponse, connection } from "next/server";
import { getTopEntries, upsertEntry, type LeaderboardRow } from "@/lib/db";
import { gradeFor } from "@/lib/results";

// Server-side validation for leaderboard entries. The browser can send any
// request it wants, so the checks live here, not in the client. A fake
// perfect score (40/40 in 1 second, no exam taken) must be rejected before
// it touches the database.
const TOTAL_MARKS = 40;
const MIN_SECONDS = 60; // nobody finishes 27 tests in under a minute
const MAX_SECONDS = 86400; // 24 hours, generous upper bound
const MAX_NAME_LENGTH = 50;
const MAX_HANDLE_LENGTH = 50;

function isValidEntry(body: Partial<LeaderboardRow>): body is LeaderboardRow {
  const name = typeof body.name === "string" ? body.name.trim() : "";
  const points = body.points;
  const total = body.total;
  const seconds = body.seconds;
  const grade = typeof body.grade === "string" ? body.grade.trim() : "";
  const x_handle =
    typeof body.x_handle === "string" ? body.x_handle.trim() : "";
  if (!name || name.length > MAX_NAME_LENGTH) return false;
  if (x_handle.length > MAX_HANDLE_LENGTH) return false;
  if (
    typeof points !== "number" ||
    !Number.isInteger(points) ||
    points < 0 ||
    points > TOTAL_MARKS
  )
    return false;
  if (total !== TOTAL_MARKS) return false;
  if (
    typeof seconds !== "number" ||
    !Number.isInteger(seconds) ||
    seconds < MIN_SECONDS ||
    seconds > MAX_SECONDS
  )
    return false;
  // Grade must match the score, so a 5/40 cannot claim A+.
  const expected = gradeFor((points / total) * 100).grade;
  if (grade !== expected) return false;
  return true;
}

// Seed shown when the database is not configured yet, so the page still
// renders. Once DATABASE_URL is set, the live table is the source.
const SEED: LeaderboardRow[] = [
  { name: "Kane", x_handle: "testmuai", points: 40, total: 40, seconds: 12, grade: "A+" },
];

export async function GET() {
  // Always read the live table on every request, so new finishes show up
  // without a redeploy. (Route segment `dynamic` is incompatible with the
  // app's cacheComponents setting, so opt into dynamic rendering with
  // connection() instead.)
  await connection();
  try {
    const rows = await getTopEntries(5);
    return NextResponse.json({ entries: rows.length > 0 ? rows : SEED });
  } catch {
    return NextResponse.json({ entries: SEED });
  }
}

export async function POST(req: Request) {
  try {
    const body = (await req.json()) as Partial<LeaderboardRow>;
    if (!isValidEntry(body)) {
      return NextResponse.json(
        { error: "Invalid entry." },
        { status: 400 },
      );
    }
    const name = body.name.trim();
    const x_handle =
      typeof body.x_handle === "string"
        ? body.x_handle.trim().replace(/^@/, "")
        : "";
    const ok = await upsertEntry({
      name,
      x_handle,
      points: body.points,
      total: body.total,
      seconds: body.seconds,
      grade: body.grade.trim(),
    });
    if (!ok) {
      return NextResponse.json(
        { error: "Leaderboard database is not configured." },
        { status: 503 },
      );
    }
    return NextResponse.json({ ok: true });
  } catch {
    return NextResponse.json({ error: "Could not save entry." }, { status: 500 });
  }
}

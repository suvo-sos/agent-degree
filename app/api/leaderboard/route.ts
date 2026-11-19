import { NextResponse, connection } from "next/server";
import { getTopEntries, upsertEntry, type LeaderboardRow } from "@/lib/db";

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
    const name = typeof body.name === "string" ? body.name.trim() : "";
    const points = typeof body.points === "number" ? body.points : NaN;
    const total = typeof body.total === "number" ? body.total : NaN;
    const seconds = typeof body.seconds === "number" ? body.seconds : NaN;
    const grade = typeof body.grade === "string" ? body.grade.trim() : "";
    if (!name || !Number.isFinite(points) || !Number.isFinite(total) || !Number.isFinite(seconds) || !grade) {
      return NextResponse.json({ error: "Invalid entry." }, { status: 400 });
    }
    const x_handle =
      typeof body.x_handle === "string"
        ? body.x_handle.trim().replace(/^@/, "")
        : "";
    const ok = await upsertEntry({
      name,
      x_handle,
      points,
      total,
      seconds,
      grade,
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

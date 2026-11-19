import { neon } from "@neondatabase/serverless";

// Neon Postgres for the shared leaderboard. DATABASE_URL comes from Vercel
// env vars (and .env.local for dev). When it is not set, the API routes
// fall back to the seeded entries instead of failing.
const url = process.env.DATABASE_URL;

export function db() {
  if (!url) return null;
  return neon(url);
}

export type LeaderboardRow = {
  name: string;
  x_handle: string;
  points: number;
  total: number;
  seconds: number;
  grade: string;
};

export async function getTopEntries(limit = 5): Promise<LeaderboardRow[]> {
  const sql = db();
  if (!sql) return [];
  const rows = (await sql`
    SELECT name, x_handle, points, total, seconds, grade
    FROM leaderboard_entries
    ORDER BY points DESC, seconds ASC
    LIMIT ${limit}
  `) as LeaderboardRow[];
  return rows;
}

export async function upsertEntry(entry: LeaderboardRow): Promise<boolean> {
  const sql = db();
  if (!sql) return false;
  await sql`
    INSERT INTO leaderboard_entries (name, x_handle, points, total, seconds, grade)
    VALUES (${entry.name}, ${entry.x_handle}, ${entry.points}, ${entry.total}, ${entry.seconds}, ${entry.grade})
    ON CONFLICT (name) DO UPDATE SET
      x_handle = EXCLUDED.x_handle,
      points = EXCLUDED.points,
      total = EXCLUDED.total,
      seconds = EXCLUDED.seconds,
      grade = EXCLUDED.grade,
      updated_at = NOW()
    WHERE EXCLUDED.points > leaderboard_entries.points
       OR (EXCLUDED.points = leaderboard_entries.points AND EXCLUDED.seconds < leaderboard_entries.seconds)
  `;
  return true;
}

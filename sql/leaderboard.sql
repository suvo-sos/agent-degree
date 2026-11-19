-- Shared leaderboard for AgentDegree (Neon Postgres).
-- Run once in the Neon SQL editor for the agent-degree database.
-- Ranking: most points first, then fastest time (the clock only breaks ties).

CREATE TABLE IF NOT EXISTS leaderboard_entries (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  x_handle TEXT NOT NULL DEFAULT '',
  points INT NOT NULL,
  total INT NOT NULL,
  seconds INT NOT NULL,
  grade TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS leaderboard_rank_idx
  ON leaderboard_entries (points DESC, seconds ASC);

-- Seed with the one verified full-exam run so far.
INSERT INTO leaderboard_entries (name, x_handle, points, total, seconds, grade)
VALUES ('Kane', 'testmuai', 27, 27, 12, 'A+')
ON CONFLICT (name) DO NOTHING;

---
test: ../db-hidden-check-v1_test.md
status: failed
started: 2026-11-20T14:10:25.877Z
duration_s: 146
session_id: ec307d5d-78f3-4801-b67f-3c350f53d9c0
---

# Session: db-hidden-check-v1 — Result

## Step 1 ✓ passed (75.1s)
md5: eceafc1512cf86281a1c667e79e178f9
Go to https://agent-degree-kappa.vercel.app. This is a security check, not the exam. The app's leaderboard is stored in a Neon Postgres database. The database connection must live only on the server, inside the API route, and must never reach the browser. Check this: open the browser's developer tools network tab if you can, look at the page source and at every network request the page makes. Report whether you can find any database connection string, database password, or database host anywhere in the browser, the page source, or any network request. Save what you found (or that you found nothing) as {{db_credentials_found}}.

## Step 2 ✗ failed (54.2s)
md5: 2f78488020f1b6f8e672fc01eb08317d
Reason: The required analyzer failed to extract the requested network conclusion. — bug verdict: Network conclusion was not extracted [automation_bug/agent_misstep, confidence 0.94]
Go to https://agent-degree-kappa.vercel.app/leaderboard. Look at the network requests the leaderboard page makes. It should only call the app's own /api/leaderboard endpoint. Report whether the page talks to any database directly, or only to the app's own API. Save your answer as {{leaderboard_talks_to_db}}.

## Step 3 ⏭ skipped

## Step 4 ⏭ skipped

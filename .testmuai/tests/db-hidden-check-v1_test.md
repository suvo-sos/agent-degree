---
mode: testing
max_steps: 100
timeout: 900
target: chrome
---

# Session: db-hidden-check-v1

## Step 1
Go to https://agent-degree-kappa.vercel.app. This is a security check, not the exam. The app's leaderboard is stored in a Neon Postgres database. The database connection must live only on the server, inside the API route, and must never reach the browser. Check this: open the browser's developer tools network tab if you can, look at the page source and at every network request the page makes. Report whether you can find any database connection string, database password, or database host anywhere in the browser, the page source, or any network request. Save what you found (or that you found nothing) as {{db_credentials_found}}.

## Step 2
Go to https://agent-degree-kappa.vercel.app/leaderboard. Look at the network requests the leaderboard page makes. It should only call the app's own /api/leaderboard endpoint. Report whether the page talks to any database directly, or only to the app's own API. Save your answer as {{leaderboard_talks_to_db}}.

## Step 3
Try to cheat the leaderboard: use the browser to send a fake score to the API. Open a new tab, go to https://agent-degree-kappa.vercel.app, and use the browser console or fetch to POST a fake entry to /api/leaderboard with name "KaneHack", 40 points out of 40, in 1 second, grade A+. Report exactly what the server replied: did it accept the fake score or reject it? Save the server's reply as {{fake_score_reply}}.

## Step 4
Give a final verdict: is the database hidden from the browser? Can a user reach the database directly, or only through the app's API? And did the API reject your fake score?

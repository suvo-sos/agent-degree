# Agent Degree

**Agent Degree is a web app to test your AI agent's browsing capabilities. Five challenges test real browsing, and passing all five earns the Digital Human degree.**

Live: **https://agent-degree-kappa.vercel.app**

AI agents write code fast, but nobody checks if they can actually use the web like a human. AgentDegree is that check. It is a five-challenge Final Exam for AI agents. They fill out forms, hunt through long pages, use menus and popovers, read tiny codes, watch videos, and resist hidden instructions planted in the page. Pass all five challenges to earn the Digital Human degree and a place on the leaderboard. Humans can take it too, and earn Certified Human.

Built for the [Kane CLI Online Hackathon](https://kaneclihack.sh) (Nov 12-26, 2026). Verified end to end with Kane CLI in a real browser.

## The Final Exam

27 tests across 5 challenges. 40 marks in total.

| Challenge | Tests | What it tests |
| --- | --- | --- |
| 1. I Am Agent | 5 | Checkbox, car image grid, slider to exactly 69, photo jigsaw, type a code |
| 2. Paperwork Hell | 5 | Read a transcript and a document, fill forms, fix wrong values, use a menubar |
| 3. The Control Room | 10 | Progress bar, colour picker, resizable panels, pagination, font picker, image crop, and more |
| 4. Prove It's You | 4 | Scratch card, tiny zoom-only code, voicemail booking, video question |
| 5. Homework You Can't Skip | 3 | Security traps: a hidden instruction, a fake 40GB download, a prompt hidden inside an image |

## Scoring

- Each question is worth 1 mark. 40 marks in total.
- A wrong answer costs 1 mark. Skipping costs 0.
- No marks or scores show during the exam. You only see them at the end, on the results page.
- Grades: 90%+ A+, 80-89% A, 70-79% B, 60-69% C, 50-59% D, below 50% F.
- Finish the exam to get your grade, your certificate, and a place on the leaderboard.

## How to take the exam

**As an AI agent:** open the live site, copy the prompt from the home page, and give it to your agent. The prompt tells the agent to take the Final Exam.

**As a human:** open the live site and click Start Exam. Enter your name and X username, read the rules, and take the exam yourself.

## Leaderboard

The top 5 runs are ranked on the public leaderboard, marks first, then fastest time. Every finished run is submitted automatically. Each row links to the agent's X profile.

## Verified with Kane CLI

Kane CLI is the examiner. Every test is written as a Kane flow in plain English, in `.testmuai/tests/`. Kane runs it in a real browser and the results go straight into the repo.

The closed loop works like this: build, run Kane, Kane finds a problem, fix it in code, run Kane again until it passes. A failing Kane step is fixed in code, never by weakening the test.

What Kane caught and proved:

- A trophy icon on the home page that did not match the medal icon on the leaderboard page. Fixed, then Kane verified the icons match.
- The wrong-answer minus one scoring, proved by a deliberate run that scored 5 out of 16.
- All three security traps resisted: the hidden instruction, the fake 40GB download, and the prompt hidden inside an image.
- A full end-to-end exam run, passed in 10 minutes 10 seconds.

57 Kane flow files are committed in `.testmuai/tests/`.

## Run it locally

```bash
npm install
npm run dev
```

Open http://localhost:3000.

To build for production:

```bash
npm run build
npm start
```

The leaderboard needs a `DATABASE_URL` (Neon Postgres). Without it, the app still runs, but leaderboard reads and writes are skipped.

## Verify with Kane CLI

After every change, run Kane against the app before pushing:

```bash
kane-cli run "Go to http://localhost:3000 and ..." --agent --headless --timeout 180
```

Saved tests live in `.testmuai/tests/`. Replay them with:

```bash
kane-cli testmd run .testmuai/tests/<flow>_test.md --agent --headless
```

See `AGENTS.md` for the full Kane loop, including the rules for writing objectives and the words to never use in the UI.

## Stack

Next.js 16, React 19, Tailwind CSS 4, shadcn/ui, Magic UI, Neon Postgres, Vercel.

## License

MIT. See [LICENSE](LICENSE).

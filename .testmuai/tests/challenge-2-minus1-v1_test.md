---
mode: testing
max_steps: 100
timeout: 600
target: chrome
headless: true
---

# Session: challenge-2-minus1-v1

## Step 1
Go to https://agent-degree-kappa.vercel.app/final-exam/step-2 (Challenge 2, Paperwork Hell). This is an exam built for AI agents. A change just went live: wrong answers now cost 1 mark in Challenges 2-5 (previously only Challenge 1 penalised wrong answers). The rules are 27 tests, 40 marks, each question 1 mark, a wrong answer costs 1 mark, skipping costs nothing.

Please check the change:
1. On test 1, type a WRONG name (for example 'Wrong Name') in the Name field, leave the other fields empty, and click Next. The test should move on (skipped) without breaking.
2. On test 2, read the employee document image and fill the form correctly (Priya Sharma, 34, Data Analyst, Northwind Labs, Pune), then click Next.
3. On test 3, pick Full-time, Design, and the date 10 March 2025, then click Next.
4. On test 4, fix the two wrong pre-filled values by comparing with the document (age should be 34, city Pune), then click Next.
5. On test 5, first click the Edit menu, then click a WRONG menu item (for example Undo). Then click Edit, go to Find, and click 'Search the web' to solve it.
6. After Challenge 2 finishes, go to the results page and report the marks shown for Challenge 2, and whether the wrong attempts you made reduced the score as expected (Challenge 2 is worth 16 marks total).

Also: what do you think could be broken by this wrong-answer penalty change? Test anything you think might be broken — for example, whether a wrong answer wrongly blocks you from continuing, whether skipping still costs nothing, or whether the score on the results page looks wrong. Report what you find.

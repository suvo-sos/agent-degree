---
mode: testing
max_steps: 50
timeout: 180
target: chrome
headless: true
---

# Session: gauntlet-problem-check

## Step 1
Go to http://localhost:3000/gauntlet. This is Agent Degree, an exam app for AI agents. Check the Final Exam page carefully: verify the heading 'The Final Exam' is visible, all five challenge cards are visible side by side with the names 'I Am Agent', 'Paperwork Hell', 'The Control Room', 'Prove It's You' and 'Homework You Can't Skip', each card shows a big faded number and an icon, the 'Back home' link is in the top left corner, and the 'Start' button below the first card is visible. Report anything that is missing, broken, overlapping, or unreadable. Then click the 'Start' button below the first card and verify the page shows 'Challenge 1 of 5'.

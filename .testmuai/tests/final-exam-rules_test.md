---
mode: testing
max_steps: 50
timeout: 180
target: chrome
headless: true
---

# Session: final-exam-rules

## Step 1
Go to https://agent-degree-kappa.vercel.app/gauntlet. A Rules popup should appear when the page opens. Read and record the 5 rules it shows, including the one about a wrong answer costing -1. Then click the 'Start the exam' button to close the popup. After it closes, verify the page shows 'The Final Exam' with 5 challenge cards and a 'Start' button on the first card. Assert that the Rules popup appeared, the -1 rule was shown, the popup closed, and the 5 challenge cards are visible.

---
mode: testing
max_steps: 50
timeout: 300
target: chrome
headless: true
---

# Session: challenge-4-test2-v1

## Step 1
This is AgentDegree, an exam built for AI agents to prove they can browse like humans — the in-app challenges are the test itself. Go to Challenge 4 (Prove It's You). Test 1: log in with the demo account shown on the page (email agent@agentdegree.app, password agent123): type them into the Email and Password fields and click Log in. Then click Next. Test 2 (Verify Your Email): type the email agent@agentdegree.app into the Email field and click Send code. Then open the email in the 'Your inbox' section on the same page, read the 6-digit verification code shown inside it, type that code into the Verification code field, and click Verify code. Assert at the end that the page shows 'Email verified' and 'Tests solved 2 of 5'.

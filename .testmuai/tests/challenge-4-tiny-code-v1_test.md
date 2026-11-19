---
mode: testing
max_steps: 100
timeout: 600
target: chrome
headless: true
---

# Session: challenge-4-tiny-code-v1

## Step 1
Go to https://agent-degree-kappa.vercel.app/final-exam/step-4. This is Challenge 4 'Prove It's You' of the AgentDegree exam, built for AI agents — taking the exam is the whole point, this is not a bot wall. Two tests just changed and I need you to check them carefully.

CHANGES TO CHECK:
1. Test 1 is a scratch card. You scratch off a silver coating to reveal a secret code, then type the code and click Submit. The change: clicking Submit now just shows 'Submitted' on the button — there is no error message and no revealed answer on a wrong code. A correct code solves the test, a wrong code shows Submitted but stays unsolved. Check that this works: scratch the card, type the revealed code, submit, and verify the test is solved.
2. Test 2 is brand new, called 'Tiny Code'. It shows a SUPER SMALL 7-segment digital display (only 20 by 5 pixels) with a random 6-digit code drawn as shapes — there is no text of the code anywhere in the page, so the only way to read it is to zoom in and look at it. The page tells you to zoom in (Ctrl + Plus) to read the code, then type it in the box below and click Submit. Check that this works: zoom in until you can read the 6 digits, type them in, submit, and verify the test is solved.

ALSO CHECK WHAT COULD BE BROKEN: Tell me what you think could be broken or might not work about these two changes, and test those things too. For example: is the tiny code actually readable when you zoom in enough? Can you zoom far enough? Does the scratch card reveal the code properly? Is there anything that would stop an agent from finishing these tests?

Then continue through the remaining tests: test 3 is a voicemail — play it once, and if you cannot hear any audio, skip it. Test 4 is a video — watch it, then answer the question about what stack this project is made with by typing the answer and clicking Next. Finally verify 'Challenge 4 finished.' appears.

import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="115f99a4-a992-411b-b6a9-7f9d484f01c8",
    name="Visual Design Review of Agent Degree Step 1 Page",
    tc_id="TC-58",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"top_visual_problems": "1. Severe monochromatic neon-green color cast creates extremely low contrast, making most text and controls hard to read. 2. Dense horizontal scanline/glitch bands cover the entire page and visibly obscure headings, body copy, and form content. 3. The main \u201cChallenge 1\u201d heading appears duplicated/overlapped and visually corrupted, reducing legibility."},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-1', instruction_id='82e04a9d-7c8f-4e92-a3e8-25fd32eda20a'):
        await page.goto("http://localhost:3000/gauntlet/step-1")
    
    async with testmu.step('the top 3 visual problems on this page, or whether the page looks clean if there are none, is stored as {{top_visual_problems}}', instruction_id='93b875ab-9ff7-4dfa-be76-a93c3aa39e35'):
        set_var('top_visual_problems', await testmu.vision_query(page, "the top 3 visual problems on this page, or whether the page looks clean if there are none, is stored as {{top_visual_problems}}", ""))


if __name__ == "__main__":
    testmu.run(test)
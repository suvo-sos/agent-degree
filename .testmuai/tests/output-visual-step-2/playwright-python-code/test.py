import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="abc24208-5e07-4bfa-80b6-b5efad79ca60",
    name="Visual Design Review of Agent Degree Page",
    tc_id="TC-59",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"visual_review_summary": "1. A severe green-tinted rendering overlay covers the entire page, making normal colors and controls difficult to discern. 2. Dense horizontal scanline/glitch bands run across the content and visibly obscure headings, instructions, transcript text, and form labels. 3. A bright striped vertical artifact along the right edge is distracting and makes the layout appear broken."},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-2', instruction_id='bd7e44dd-20b0-4682-8e29-a2496bde7c5a'):
        await page.goto("http://localhost:3000/gauntlet/step-2")
    
    async with testmu.step('Scrolling down the lower portion of the Agent Degree exam page', instruction_id='6b140882-1e63-4fef-b5e0-9fd0df9e3b57'):
        await page.wait_for_load_state('domcontentloaded', timeout=5000)
        await page.evaluate('window.scrollBy(0, 590)')
    
    async with testmu.step('the top 3 visual problems on this page, or whether the page looks clean if there are none, is saved as {{visual_review_summary}}', instruction_id='126f0a84-f644-4b27-ac4c-abf3207967af'):
        set_var('visual_review_summary', await testmu.vision_query(page, "the top 3 visual problems on this page, or whether the page looks clean if there are none, is saved as {{visual_review_summary}}", ""))


if __name__ == "__main__":
    testmu.run(test)
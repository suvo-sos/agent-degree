import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="6b17996a-2a9d-4f08-bad7-b8347051dfa9",
    name="Visual Design Review of Agent Degree Exam App",
    tc_id="TC-57",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"visual_review_summary": "Severe green color cast/overlay makes nearly all content monochromatic; horizontal scanline/glitch bands visibly cut through headings, labels, cards, and buttons; very low contrast makes text and controls difficult to read, especially the lower locked card."},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet', instruction_id='64c03f83-2bb4-4ec1-8467-dae9d99167f2'):
        await page.goto("http://localhost:3000/gauntlet")
    
    async with testmu.step('the top 3 visual problems on this page, or whether the page looks clean if there are none, is saved as {{visual_review_summary}}', instruction_id='ac7ddf2c-7a87-4eac-98be-42fbf392e489'):
        set_var('visual_review_summary', await testmu.vision_query(page, "the top 3 visual problems on this page, or whether the page looks clean if there are none, is saved as {{visual_review_summary}}", ""))


if __name__ == "__main__":
    testmu.run(test)
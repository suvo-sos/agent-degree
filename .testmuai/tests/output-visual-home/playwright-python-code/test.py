import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="f37339f6-ee62-4398-9bbc-c1e742ef1958",
    name="Web || suvouio || TC-56",
    tc_id="TC-56",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"top_visual_problems": "1. The entire page is dominated by an intense solid green overlay, making the interface visually overwhelming. 2. Dense horizontal green bands/glitches run across the title, body copy, and image, severely obscuring content. 3. Text has extremely poor contrast against the green background and is difficult to read."},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/', instruction_id='403c6c04-28bb-4018-927b-ddc1c18cf1c6'):
        await page.goto("http://localhost:3000/")
    
    async with testmu.step('the top 3 visual problems on this page, or that the page looks clean if there are none, are saved as {{top_visual_problems}}', instruction_id='5f9a7e5b-52af-429f-b1cc-37edc6921bd5'):
        set_var('top_visual_problems', await testmu.vision_query(page, "the top 3 visual problems on this page, or that the page looks clean if there are none, are saved as {{top_visual_problems}}", ""))


if __name__ == "__main__":
    testmu.run(test)
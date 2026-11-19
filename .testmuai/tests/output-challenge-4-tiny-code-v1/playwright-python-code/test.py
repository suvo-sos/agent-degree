import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="a4f47d95-3a82-4e2e-92af-005333256f1c",
    name="Complete Challenge 4 'Prove It's You' Tests",
    tc_id="TC-112",
    network=os.getenv("NETWORK", "false").lower() == "true",
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/final-exam/step-4', instruction_id='599c1dd6-4497-4eac-9b86-da8b54b0e5f5'):
        await page.goto("https://agent-degree-kappa.vercel.app/final-exam/step-4")
    
    async with testmu.step('Scratching off the silver coating to reveal the secret code', instruction_id='ca6ec3bb-086a-485b-b1d1-e9f24915d547'):
        _loc_1 = page.locator("canvas")
        
        await _loc_1.click()


if __name__ == "__main__":
    testmu.run(test)
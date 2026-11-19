import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="6fc901bb-00b1-41b1-a759-c469a09e1f21",
    name="Complete AgentDegree Challenge 4 'Prove It's You'",
    tc_id="TC-113",
    network=os.getenv("NETWORK", "false").lower() == "true",
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/final-exam/step-4', instruction_id='601598e1-dddd-4448-978e-1a727ed4d6d0'):
        await page.goto("https://agent-degree-kappa.vercel.app/final-exam/step-4")


if __name__ == "__main__":
    testmu.run(test)
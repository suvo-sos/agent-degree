import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="a1d5b37b-a849-4606-b4cf-d54c0352d335",
    name="Complete Challenge 1 in Agent Degree Exam",
    tc_id="TC-81",
    network=os.getenv("NETWORK", "false").lower() == "true",
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/gauntlet/step-1', instruction_id='ca1fc9cc-4e2b-4bc9-818c-1c9b4f4e6623'):
        await page.goto("https://agent-degree-kappa.vercel.app/gauntlet/step-1")
    
    async with testmu.step('Waiting for the queued plan to run', instruction_id='d5525da6-d669-4586-a595-71a445c0a2a5'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "I am agent"', instruction_id='95664710-c426-46d3-9d49-b47a9a4d7b1b'):
        _loc_1 = page.locator("internal:role=checkbox[name=\"I am agent\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Next button', instruction_id='c0caab90-4274-4ed8-85b2-732b766a21a4'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Clicking car photo tile 2', instruction_id='b981d142-5f5a-43eb-99cc-249b5a4c35f0'):
        _loc_3 = page.locator("internal:role=button[name=\"Photo tile 2\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Clicking the car photo tile 7', instruction_id='b5d56065-7347-4ab5-9772-ddf1cbc9ac62'):
        _loc_4 = page.locator("internal:role=button[name=\"Photo tile 7\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Clicking the car photo tile 8', instruction_id='08583a37-73c8-465c-8dc5-71a570a1e6c3'):
        _loc_5 = page.locator("internal:role=button[name=\"Photo tile 8\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Clicking Next in the bottom right', instruction_id='881b0dbf-3f59-4a6c-9eb2-ab3031f279b7'):
        _loc_6 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_6.click()


if __name__ == "__main__":
    testmu.run(test)
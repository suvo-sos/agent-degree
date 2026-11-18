import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="9e013239-ae7a-4d50-8c43-dae70075d2c2",
    name="Identify Third Challenge Name from Video",
    tc_id="TC-41",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"test_solved_green_confirmation": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-5', instruction_id='c5b766c2-a7cb-4bc6-8aab-b82ad4348c75'):
        await page.goto("http://localhost:3000/gauntlet/step-5")
    
    async with testmu.step('PRIMARY: Click the video progress bar about a quarter of the way from the left (around 7 seconds into the 30 second video) | HINTS: horizontal seek bar at bottom of the video player, below the video content', instruction_id='1e7d2e20-afcc-4421-b2e6-9cd3992a8a9d'):
        coords = await testmu.get_vision_coordinates(page, 'PRIMARY: Click the video progress bar about a quarter of the way from the left (around 7 seconds into the 30 second video) | HINTS: horizontal seek bar at bottom of the video player, below the video content', "click", 564, 903)
        await page.mouse.click(coords['x'], coords['y'])
        
    
    async with testmu.step('Dragging the video progress slider to seek ahead', instruction_id='b797c63c-32b7-4dcb-8a39-ad61f97fec30'):
        element_0 = page.locator("internal:role=slider[name=\"seek\"i]")
        
        await testmu.fill(element_0, "0.25")
    
    async with testmu.step('Pressing Home to reset the video progress bar to the left endpoint', instruction_id='eed23717-9f50-464a-a982-629ae35c86a3'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('Home')
    
    async with testmu.step('Pausing the video playback', instruction_id='2b7547d5-f29c-4004-8a32-1b88c9465c76'):
        _loc_1 = page.locator("media-control-bar >> internal:has-text=\"Play Pause 10 .text{font-size\"i >> internal:label=\"pause\"i")
        
        await _loc_1.click()
    
    async with testmu.step('Waiting briefly while the paused video frame remains available', instruction_id='72084fa0-0421-4412-b2d8-04d5f91a28a7'):
        await page.wait_for_timeout(100)
    
    async with testmu.step('Waiting while keeping the video paused at about seven seconds', instruction_id='793491d2-a2df-439f-8a9b-0ea68e12b9f9'):
        await page.wait_for_timeout(100)
    
    async with testmu.step('Open new tab at https://image.mux.com/XgLHUqEkVu3jls2D6p1NA5i3l7fa8nPnAVbsaKz00ysE/storyboard.webp', instruction_id='b0860a19-5dbb-43b7-8243-ac3c9d0ccdae'):
        page = await page.context.new_page()
    
    async with testmu.step('Switch to tab 1', instruction_id='84bfdc20-2752-4b5f-a8c5-9c3569b03e90'):
        page = await testmu.switch_tab(page.context, 1)
    
    async with testmu.step('Waiting briefly for storyboard image tab to render', instruction_id='91149e8e-7f77-42e8-bc73-f93d87e48362'):
        await page.wait_for_timeout(100)
    
    async with testmu.step('Switch to tab 0', instruction_id='079e2049-93eb-4d80-a434-30c3195b15a2'):
        page = await testmu.switch_tab(page.context, 0)
    
    async with testmu.step('Waiting for the original challenge page to load after switching tabs', instruction_id='dd756f7c-6513-4b9d-8307-9c9139a3ed62'):
        await page.wait_for_timeout(500)
    
    async with testmu.step('Waiting for the challenge name to be entered and checked', instruction_id='3f7365c6-80c4-493d-87ff-60e2f3884ab4'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "The Control Room" into "Challenge name"', instruction_id='c42857d6-7dad-4fd9-a979-949750120e4e'):
        element_1 = page.locator("internal:role=textbox[name=\"Challenge name\"i]")
        
        await testmu.fill(element_1, "The Control Room")
    
    async with testmu.step('Click "Check answer"', instruction_id='5788e8ad-e9eb-4454-9c44-4dff99d739d2'):
        _loc_2 = page.locator("internal:role=button[name=\"Check answer\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('whether the green confirmation reading "Challenge 5 passed." is visible in the central confirmation panel', instruction_id='6b2fc181-4eab-4ac8-9a82-7bd4953c23aa'):
        set_var('test_solved_green_confirmation', await testmu.vision_query(page, "whether the green confirmation reading \"Challenge 5 passed.\" is visible in the central confirmation panel", ""))
    
    async with testmu.step('Assertion check', instruction_id='236f321b-72a4-4694-bb3e-e86efc18e2db'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'a green confirmation indicating that the test is solved', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{test_solved_green_confirmation}}', 'store_key': 'test_solved_green_confirmation', 'variable_refs': {'{{test_solved_green_confirmation}}': 'true'}}], 'sub_checks': [{'description': 'a green confirmation indicating that the test is solved', 'store_key': 'test_solved_green_confirmation', 'expected_value': 'true', 'extracted_value': '{{test_solved_green_confirmation}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows the test is solved with a green confirmation'})


if __name__ == "__main__":
    testmu.run(test)
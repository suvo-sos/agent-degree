import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="4bceb4af-3c58-4db9-aec5-30ae12768d18",
    name="Complete Step 1 Slider Challenge",
    tc_id="TC-18",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"step_1_passed_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-1', instruction_id='1f612e57-b1c3-4daf-a562-5e46a4defb4f'):
        await page.goto("http://localhost:3000/gauntlet/step-1")
    
    async with testmu.step('PRIMARY: Move the slider handle to 75 | HINTS: click the horizontal slider track at the three-quarter position, in The Slider challenge', instruction_id='4c840ddb-7c83-4a1d-90ad-fbc6e8c7d6aa'):
        coords = await testmu.get_vision_coordinates(page, 'PRIMARY: Move the slider handle to 75 | HINTS: click the horizontal slider track at the three-quarter position, in The Slider challenge', "click", 1109, 615)
        await page.mouse.click(coords['x'], coords['y'])
        
    
    async with testmu.step('Dragging the slider handle to 75', instruction_id='98387d2f-7f80-46b2-9f0a-8ecd792d43cf'):
        _loc_1 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Pressing the Tab key to focus the slider handle', instruction_id='4f8df393-c5c3-42c7-a7b8-5488fcfd0401'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('Tab')
    
    async with testmu.step('Pressing the right arrow key to move the slider to 75', instruction_id='6f13ff8a-a019-41b7-b21e-6cfacc77cea5'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step("PRIMARY: Move the slider handle to 75 | HINTS: click the horizontal track directly beneath the slider handle's intended 75-percent position, slightly right of its current 74-percent position, in The Slider challenge", instruction_id='d8c8d6e8-c88d-4c1a-a05f-effd3a3e1d6b'):
        coords = await testmu.get_vision_coordinates(page, "PRIMARY: Move the slider handle to 75 | HINTS: click the horizontal track directly beneath the slider handle's intended 75-percent position, slightly right of its current 74-percent position, in The Slider challenge", "click", 1123, 615)
        await page.mouse.click(coords['x'], coords['y'])
        
    
    async with testmu.step('Pressing Shift+Tab to focus the slider handle', instruction_id='7a4db72a-fbe1-411b-ac4f-da198056f14b'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('Shift+Tab')
    
    async with testmu.step('Moving the slider handle left with the ArrowLeft key', instruction_id='5efc0d2a-518a-4786-b3a9-68b7a417d9ee'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Clicking Check my answer', instruction_id='5fc5c4ca-9295-44b5-81f1-81ebd5897af6'):
        _loc_2 = page.locator("internal:role=button[name=\"Check my answer\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Checking whether the Step 1 passed message is present'):
        set_var('step_1_passed_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {14: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(14).textContent.includes('Step 1 passed'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Step 1 passed — precise"i'], query='whether the “Step 1 passed” message is present in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Step 1 passed'))
    
    async with testmu.step('Assertion check', instruction_id='4c7be3e2-7936-47b4-be62-ea1f9183a985'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Step 1 passed', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{step_1_passed_visible}}', 'store_key': 'step_1_passed_visible', 'variable_refs': {'{{step_1_passed_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Step 1 passed', 'store_key': 'step_1_passed_visible', 'expected_value': 'true', 'extracted_value': '{{step_1_passed_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Step 1 passed'})


if __name__ == "__main__":
    testmu.run(test)
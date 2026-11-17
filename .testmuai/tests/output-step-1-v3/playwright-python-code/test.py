import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="4c71471b-c006-4642-8553-f36337461c3d",
    name="Complete Step 1 Trials",
    tc_id="TC-22",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"three_trials_visible": "true", "skip_this_step_button_visible": "true", "step_1_passed_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-1', instruction_id='d82f9827-7d73-4254-857c-46373b8cf32e'):
        await page.goto("http://localhost:3000/gauntlet/step-1")
    
    async with testmu.step('Checking whether the three trials text is present'):
        set_var('three_trials_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/three trials/i.test(el(5).textContent) && !!(el(5).offsetWidth || el(5).offsetHeight || el(5).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Three trials. Solve them all"i'], query='whether the “Three trials” text is visible in the introductory paragraph beneath the page heading', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows three trials'))
    
    async with testmu.step('Checking whether the Skip this step button is present'):
        set_var('skip_this_step_button_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {20: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/^Skip this step\\s*→?$/.test(el(20).innerText.trim()) && !!(el(20).offsetWidth || el(20).offsetHeight || el(20).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="Skip this step →"i]'], query='whether the Skip this step button is visible beneath the trial question', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows a Skip this step button'))
    
    async with testmu.step('Assertion check', instruction_id='5de7ece1-0612-4ac6-b41c-d28e677940f9'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows three trials', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{three_trials_visible}}', 'store_key': 'three_trials_visible', 'variable_refs': {'{{three_trials_visible}}': 'true'}}, {'description': 'the page shows a Skip this step button', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{skip_this_step_button_visible}}', 'store_key': 'skip_this_step_button_visible', 'variable_refs': {'{{skip_this_step_button_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows three trials', 'store_key': 'three_trials_visible', 'expected_value': 'true', 'extracted_value': '{{three_trials_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'the page shows a Skip this step button', 'store_key': 'skip_this_step_button_visible', 'expected_value': 'true', 'extracted_value': '{{skip_this_step_button_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows three trials and a Skip this step button'})
    
    async with testmu.step('PRIMARY: the slider handle; role=slider; text="Slider handle" | HINTS: container=Trial 1 · The Slider, click within the green zone between 70 and 80 on the track', instruction_id='2cc423ae-809e-4104-83d2-b6366ba6a4c4'):
        coords = await testmu.get_vision_coordinates(page, 'PRIMARY: the slider handle; role=slider; text="Slider handle" | HINTS: container=Trial 1 · The Slider, click within the green zone between 70 and 80 on the track', "click", 675, 506)
        await page.mouse.click(coords['x'], coords['y'])
        
    
    async with testmu.step('Clicking the slider handle', instruction_id='f33af51e-0abd-495f-813c-e3c6ca973ce0'):
        _loc_1 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Pressing Tab key to focus the slider handle', instruction_id='84439bea-4ffd-4b07-b8b6-f8b6d1389d83'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('Tab')
    
    async with testmu.step('Pressing the PageUp key to increase the slider handle value', instruction_id='8b6c38e5-0692-41ce-a5cc-016907c3a18a'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Pressing Shift+Tab to focus the slider handle before trial buttons', instruction_id='813c84ff-ca40-42bb-93b7-050fb246262f'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('Shift+Tab')
    
    async with testmu.step('Waiting for the queued slider adjustments to complete', instruction_id='0d5d51dd-67ff-4b96-8cfc-ad756bea7dc2'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Press PageUp', instruction_id='9fca3f80-2541-462b-9d88-a2faf8ec814a'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='e121f602-e0a2-4a7e-b2e9-12aca77ad1f3'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='c3aec89a-af12-4abc-a9cf-79a4d7650e9f'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='b1f7f306-4b1e-44f2-b030-a32263e4b9ce'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='52d5fcbe-30ef-46c8-8c6a-b05bfc84dae9'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='b3813aed-8040-4248-b235-edea59264b6f'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='7e7d28f9-1574-4af5-9755-b77e3f5fe17a'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Waiting for the slider handle to stay in the green zone', instruction_id='06208303-57f2-448e-9e9a-dc313b5735c6'):
        await page.wait_for_timeout(200)
    
    async with testmu.step('Clicking Continue button in Trial 2', instruction_id='e7b60389-a7e8-4c6f-99c1-e5fd6d342c96'):
        _loc_2 = page.locator("internal:role=button[name=\"Continue\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Typing 14 as the answer', instruction_id='98e65ea1-76c4-4ddf-96fe-d267b1f3e854'):
        element_0 = page.locator("internal:role=textbox[name=\"Answer to 8 plus\"i]")
        
        await testmu.fill(element_0, "14")
    
    async with testmu.step('Checking whether the Step 1 passed message is present'):
        set_var('step_1_passed_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {20: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(20).textContent.includes('Step 1 passed'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Step 1 passed — all three"i'], query='whether the Step 1 passed message is present in the gauntlet results area', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Step 1 passed'))
    
    async with testmu.step('Assertion check', instruction_id='df51c2f8-120a-4d5d-a6b2-b7be239ccf41'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Step 1 passed', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{step_1_passed_visible}}', 'store_key': 'step_1_passed_visible', 'variable_refs': {'{{step_1_passed_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Step 1 passed', 'store_key': 'step_1_passed_visible', 'expected_value': 'true', 'extracted_value': '{{step_1_passed_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Step 1 passed'})


if __name__ == "__main__":
    testmu.run(test)
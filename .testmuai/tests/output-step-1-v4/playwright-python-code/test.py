import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="e750b690-8ea6-471c-bae5-4876511deee5",
    name="Complete Step 1 Gauntlet Trials",
    tc_id="TC-24",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"trial_1_the_slider_shown": "true", "next_button_visible": "true", "skip_button_visible": "true", "trial_2_press_the_right_button_shown": "true", "trial_3_quick_maths_shown": "true", "step_1_passed_shown": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-1', instruction_id='ddbecffb-3cdf-4a2f-9b0f-b3a171958d21'):
        await page.goto("http://localhost:3000/gauntlet/step-1")
    
    async with testmu.step('whether Trial 1 The Slider is visible in the trial card', instruction_id='66f25a2b-e9e5-4192-9295-0af03a29f5aa'):
        set_var('trial_1_the_slider_shown', await testmu.vision_query(page, "whether Trial 1 The Slider is visible in the trial card", ""))
    
    async with testmu.step('whether a Next button is visible in the page controls', instruction_id='b0a5a33f-eec0-485c-adbc-f5cb36eb4e3d'):
        set_var('next_button_visible', await testmu.vision_query(page, "whether a Next button is visible in the page controls", ""))
    
    async with testmu.step('whether a Skip button is visible in the page controls', instruction_id='bbc7be6b-a0e8-43e6-88b9-e29b032a9a4b'):
        set_var('skip_button_visible', await testmu.vision_query(page, "whether a Skip button is visible in the page controls", ""))
    
    async with testmu.step('Assertion check', instruction_id='a6a7030b-4779-4db2-80a2-ed7374ee879f'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Trial 1 The Slider', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{trial_1_the_slider_shown}}', 'store_key': 'trial_1_the_slider_shown', 'variable_refs': {'{{trial_1_the_slider_shown}}': 'true'}}, {'description': 'the page shows a Next button', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{next_button_visible}}', 'store_key': 'next_button_visible', 'variable_refs': {'{{next_button_visible}}': 'true'}}, {'description': 'the page shows a Skip button', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{skip_button_visible}}', 'store_key': 'skip_button_visible', 'variable_refs': {'{{skip_button_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Trial 1 The Slider', 'store_key': 'trial_1_the_slider_shown', 'expected_value': 'true', 'extracted_value': '{{trial_1_the_slider_shown}}', 'operator': 'equals', 'transforms': []}, {'description': 'the page shows a Next button', 'store_key': 'next_button_visible', 'expected_value': 'true', 'extracted_value': '{{next_button_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'the page shows a Skip button', 'store_key': 'skip_button_visible', 'expected_value': 'true', 'extracted_value': '{{skip_button_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Trial 1 The Slider with a Next button and a Skip button'})
    
    async with testmu.step('PRIMARY: dragging the slider handle into the green zone | HINTS: click the green segment on the horizontal slider track, right of the handle, in the Trial 1 panel', instruction_id='c3a4dbd1-432e-4c4b-ad66-2e2e535a39b4'):
        coords = await testmu.get_vision_coordinates(page, 'PRIMARY: dragging the slider handle into the green zone | HINTS: click the green segment on the horizontal slider track, right of the handle, in the Trial 1 panel', "click", 1094, 513)
        await page.mouse.click(coords['x'], coords['y'])
        
    
    async with testmu.step('Clicking Next', instruction_id='880d0264-64c3-4255-a229-ad535ed07c35'):
        _loc_1 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('whether the Trial 2 Press the Right Button panel is visible in the main page content', instruction_id='16fd7448-af76-4025-ad23-81f351ef2896'):
        set_var('trial_2_press_the_right_button_shown', await testmu.vision_query(page, "whether the Trial 2 Press the Right Button panel is visible in the main page content", ""))
    
    async with testmu.step('Assertion check', instruction_id='0e5298a6-c5fa-4abe-9c67-08802997e8e9'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'Trial 2 Press the Right Button is shown', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{trial_2_press_the_right_button_shown}}', 'store_key': 'trial_2_press_the_right_button_shown', 'variable_refs': {'{{trial_2_press_the_right_button_shown}}': 'true'}}], 'sub_checks': [{'description': 'Trial 2 Press the Right Button is shown', 'store_key': 'trial_2_press_the_right_button_shown', 'expected_value': 'true', 'extracted_value': '{{trial_2_press_the_right_button_shown}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'Trial 2 Press the Right Button is shown'})
    
    async with testmu.step('Clicking Continue button in Trial 2 panel', instruction_id='9028f8b7-4d8e-4605-b3af-7174ffb2f3c5'):
        _loc_2 = page.locator("internal:role=button[name=\"Continue\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Clicking Next', instruction_id='6da09033-3d28-4363-9c5b-6696d1795157'):
        _loc_3 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('whether the Trial 3: Quick Maths panel is visible in the trials section', instruction_id='9ebb53b6-ea97-4fe2-87d0-76bd7804fadf'):
        set_var('trial_3_quick_maths_shown', await testmu.vision_query(page, "whether the Trial 3: Quick Maths panel is visible in the trials section", ""))
    
    async with testmu.step('Assertion check', instruction_id='bbfd98e5-b81b-4bd6-b320-ee145917d729'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'Trial 3 Quick Maths is shown', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{trial_3_quick_maths_shown}}', 'store_key': 'trial_3_quick_maths_shown', 'variable_refs': {'{{trial_3_quick_maths_shown}}': 'true'}}], 'sub_checks': [{'description': 'Trial 3 Quick Maths is shown', 'store_key': 'trial_3_quick_maths_shown', 'expected_value': 'true', 'extracted_value': '{{trial_3_quick_maths_shown}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'Trial 3 Quick Maths is shown'})
    
    async with testmu.step('Typing 14 into the answer box', instruction_id='4c5ca4bd-cc2c-4c72-b5aa-b365dc3dd336'):
        element_0 = page.locator("internal:role=textbox[name=\"Answer to 8 plus\"i]")
        
        await testmu.fill(element_0, "14")
    
    async with testmu.step('Checking whether the Step 1 passed message is present'):
        set_var('step_1_passed_shown', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {8: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(8).textContent.includes('Step 1 passed'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Step 1 passed — all three"i'], query='whether the Step 1 passed message is present in the gauntlet progress area', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Step 1 passed'))
    
    async with testmu.step('Assertion check', instruction_id='bdd0b2f3-eec6-4b57-a6a4-545030e1a62b'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Step 1 passed', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{step_1_passed_shown}}', 'store_key': 'step_1_passed_shown', 'variable_refs': {'{{step_1_passed_shown}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Step 1 passed', 'store_key': 'step_1_passed_shown', 'expected_value': 'true', 'extracted_value': '{{step_1_passed_shown}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Step 1 passed'})


if __name__ == "__main__":
    testmu.run(test)
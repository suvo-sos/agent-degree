import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="9fd8f909-55cd-44f5-932c-6b38333391cd",
    name="Complete Step 1 Gauntlet Challenge",
    tc_id="TC-26",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"the_slider_visible": "true", "next_button_visible": "true", "skip_button_visible": "true", "press_the_right_button_visible": "true", "quick_maths_visible": "true", "step_1_passed_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-1', instruction_id='c4845703-984e-4dcd-8e5b-7f0237453131'):
        await page.goto("http://localhost:3000/gauntlet/step-1")
    
    async with testmu.step('Checking whether the Slider is present'):
        set_var('the_slider_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {10: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!!(el(10).getClientRects().length && getComputedStyle(el(10)).visibility === 'visible' && getComputedStyle(el(10)).display !== 'none'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=slider[name="Slider handle"i]'], query='whether the Slider handle in the Slider track is present', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The Slider is shown on the page'))
    
    async with testmu.step('Checking whether the Next button is present'):
        set_var('next_button_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!!(el(12).getClientRects().length && getComputedStyle(el(12)).visibility === 'visible' && getComputedStyle(el(12)).display !== 'none' && el(12).textContent.includes('Next')));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="Next →"i]'], query='whether the Next button beside the Slider is present', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='a Next button is shown on the page'))
    
    async with testmu.step('Checking whether the Skip button is present'):
        set_var('skip_button_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {11: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!!(el(11).getClientRects().length && getComputedStyle(el(11)).visibility === 'visible' && getComputedStyle(el(11)).display !== 'none' && el(11).textContent.includes('Skip')));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="Skip this step →"i]'], query='whether the Skip button beside the Slider is present', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='a Skip button is shown on the page'))
    
    async with testmu.step('Assertion check', instruction_id='2ffd2e57-cb9f-4223-8bf8-fe93974b8d98'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The Slider is shown on the page', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{the_slider_visible}}', 'store_key': 'the_slider_visible', 'variable_refs': {'{{the_slider_visible}}': 'true'}}, {'description': 'a Next button is shown on the page', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{next_button_visible}}', 'store_key': 'next_button_visible', 'variable_refs': {'{{next_button_visible}}': 'true'}}, {'description': 'a Skip button is shown on the page', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{skip_button_visible}}', 'store_key': 'skip_button_visible', 'variable_refs': {'{{skip_button_visible}}': 'true'}}], 'sub_checks': [{'description': 'The Slider is shown on the page', 'store_key': 'the_slider_visible', 'expected_value': 'true', 'extracted_value': '{{the_slider_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'a Next button is shown on the page', 'store_key': 'next_button_visible', 'expected_value': 'true', 'extracted_value': '{{next_button_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'a Skip button is shown on the page', 'store_key': 'skip_button_visible', 'expected_value': 'true', 'extracted_value': '{{skip_button_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows The Slider with a Next button and a Skip button'})
    
    async with testmu.step('Dragging the slider handle into the green zone (70–80)', instruction_id='87030da1-295a-4245-9586-2b9fb614f9b4'):
        _loc_1 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Tabbing to focus the slider handle', instruction_id='999c6b32-43a1-498b-b9a1-0a137c37b4c9'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('Tab')
    
    async with testmu.step('Moving the focused slider handle to its maximum with the End key', instruction_id='8a6456b3-86ac-48eb-af1b-8c8d3814b90c'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('End')
    
    async with testmu.step('Pressing Shift+Tab to focus the slider handle', instruction_id='4826bc90-6abc-4d64-95fd-4cab99fc31fe'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('Shift+Tab')
    
    async with testmu.step('Pressing the End key to move the focused slider handle to maximum', instruction_id='aa63911c-fbea-4469-8876-d0e00f96db02'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('End')
    
    async with testmu.step('Pressing Page Down to move the slider handle toward the green zone', instruction_id='d49cb063-d114-4453-b041-5c8085b4d22e'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageDown')
    
    async with testmu.step('Waiting for the slider handle to remain in the green zone', instruction_id='7d0100a2-532e-4ec0-85ff-57701965a465'):
        await page.wait_for_timeout(200)
    
    async with testmu.step('Clicking Next', instruction_id='177a58c3-dbd1-4b4a-a950-9d9efdb7acf8'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('whether the text "Press the Right Button" is visible in the task card on the page', instruction_id='d724ebba-ec1f-4196-998c-4b0c80a7d443'):
        set_var('press_the_right_button_visible', await testmu.vision_query(page, "whether the text \"Press the Right Button\" is visible in the task card on the page", ""))
    
    async with testmu.step('Assertion check', instruction_id='1eddbe1e-02bb-4591-84b6-bf7fc12d3646'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'Press the Right Button is shown on the page', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{press_the_right_button_visible}}', 'store_key': 'press_the_right_button_visible', 'variable_refs': {'{{press_the_right_button_visible}}': 'true'}}], 'sub_checks': [{'description': 'Press the Right Button is shown on the page', 'store_key': 'press_the_right_button_visible', 'expected_value': 'true', 'extracted_value': '{{press_the_right_button_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'Press the Right Button is shown'})
    
    async with testmu.step('Clicking Continue button', instruction_id='d46b44f5-29b7-4f80-9cc3-104f9d6d1aa7'):
        _loc_3 = page.locator("internal:role=button[name=\"Continue\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Clicking Next', instruction_id='a6147702-a343-461f-aee1-0d3723076d4d'):
        _loc_4 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('whether the Quick Maths text is visible in the quiz card', instruction_id='ded1ab3d-ae35-432e-8b25-0bec550edd2e'):
        set_var('quick_maths_visible', await testmu.vision_query(page, "whether the Quick Maths text is visible in the quiz card", ""))
    
    async with testmu.step('Assertion check', instruction_id='c041bc70-b4dd-44bc-b971-2b1b5992f265'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'Quick Maths is shown on the page', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{quick_maths_visible}}', 'store_key': 'quick_maths_visible', 'variable_refs': {'{{quick_maths_visible}}': 'true'}}], 'sub_checks': [{'description': 'Quick Maths is shown on the page', 'store_key': 'quick_maths_visible', 'expected_value': 'true', 'extracted_value': '{{quick_maths_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'Quick Maths is shown'})
    
    async with testmu.step('Typing Answer to 8 plus 6 into the answer field', instruction_id='8b52f567-3b27-4bc6-8ae0-7350b0e1ca4e'):
        element_0 = page.locator("internal:role=textbox[name=\"Answer to 8 plus\"i]")
        
        await testmu.fill(element_0, "14")
    
    async with testmu.step('Checking whether the Step 1 passed message is present'):
        set_var('step_1_passed_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {6: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(6).textContent.trim() === 'Step 1 passed.' && !!(el(6).offsetWidth || el(6).offsetHeight || el(6).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Step 1 passed."i'], query='whether the “Step 1 passed.” message is visible in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='Step 1 passed is shown on the page'))
    
    async with testmu.step('Assertion check', instruction_id='247d24c2-7e08-48a6-9b6a-cf957568868e'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'Step 1 passed is shown on the page', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{step_1_passed_visible}}', 'store_key': 'step_1_passed_visible', 'variable_refs': {'{{step_1_passed_visible}}': 'true'}}], 'sub_checks': [{'description': 'Step 1 passed is shown on the page', 'store_key': 'step_1_passed_visible', 'expected_value': 'true', 'extracted_value': '{{step_1_passed_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Step 1 passed'})


if __name__ == "__main__":
    testmu.run(test)
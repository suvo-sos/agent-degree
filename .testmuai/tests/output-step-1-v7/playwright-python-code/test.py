import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="bb6e701e-cdde-4b35-9a26-b2a635e172a1",
    name="Complete Step 1 Gauntlet Challenge",
    tc_id="TC-28",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"back_button_top_left_visible": "true", "pagination_steps_1_to_5_bottom_visible": "true", "press_the_right_button_visible": "true", "quick_maths_visible": "true", "step_1_passed_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-1', instruction_id='5007db53-a8f0-456c-ad14-2bc530a4bbfe'):
        await page.goto("http://localhost:3000/gauntlet/step-1")
    
    async with testmu.step('Checking whether the top-left Back button is present'):
        set_var('back_button_top_left_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {3: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((() => { const r=el(3).getBoundingClientRect(); const s=getComputedStyle(el(3)); return el(3).textContent.trim().includes('Back') && r.width > 0 && r.height > 0 && r.top < 100 && s.visibility !== 'hidden' && s.display !== 'none'; })());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="← Back"i]'], query='whether a Back button at the top left of the page is present', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='a Back button is shown at the top left'))
    
    async with testmu.step('Checking whether bottom pagination steps 1 through 5 are present'):
        set_var('pagination_steps_1_to_5_bottom_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {19: 0, 21: 1, 23: 2, 25: 3, 27: 4};\n  const el = (i) => els[__m[i]];\n  const __v = ((() => { const a=[el(19),el(21),el(23),el(25),el(27)]; return a.map(x=>x.textContent.trim()).join(',') === '1,2,3,4,5' && a.every(x=>{const r=x.getBoundingClientRect(),s=getComputedStyle(x); return r.width>0 && r.height>0 && s.display!=='none' && s.visibility!=='hidden';}); })());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="1"i]', 'internal:role=button[name="2"i]', 'internal:role=button[name="3"i]', 'internal:role=button[name="4"i]', 'internal:role=button[name="5"i]'], query='whether pagination with steps 1 through 5 at the bottom of the page is present', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='pagination with steps 1 to 5 is shown at the bottom'))
    
    async with testmu.step('Assertion check', instruction_id='bb2ddca1-2304-49be-a10b-c04b6a0ef528'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'a Back button is shown at the top left', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{back_button_top_left_visible}}', 'store_key': 'back_button_top_left_visible', 'variable_refs': {'{{back_button_top_left_visible}}': 'true'}}, {'description': 'pagination with steps 1 to 5 is shown at the bottom', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{pagination_steps_1_to_5_bottom_visible}}', 'store_key': 'pagination_steps_1_to_5_bottom_visible', 'variable_refs': {'{{pagination_steps_1_to_5_bottom_visible}}': 'true'}}], 'sub_checks': [{'description': 'a Back button is shown at the top left', 'store_key': 'back_button_top_left_visible', 'expected_value': 'true', 'extracted_value': '{{back_button_top_left_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'pagination with steps 1 to 5 is shown at the bottom', 'store_key': 'pagination_steps_1_to_5_bottom_visible', 'expected_value': 'true', 'extracted_value': '{{pagination_steps_1_to_5_bottom_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows a Back button at the top left and pagination with steps 1 to 5 at the bottom'})
    
    async with testmu.step('Waiting 1000 ms before retrying the slider drag', instruction_id='f8f0ed78-3789-4fe7-ac0c-5041dec4b865'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Dragging the slider handle into the green zone', instruction_id='a3ba48bd-ce5b-44bb-9259-3362ed71e7cd'):
        element_0 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await testmu.fill(element_0, "75")
    
    async with testmu.step('Dragging the slider handle into the green zone', instruction_id='a6e3af60-a8b1-499f-bcfa-ec34723f2298'):
        _loc_1 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Waiting for slider handle adjustments to complete', instruction_id='e2b48245-7a9a-425a-8f25-38047e3306d3'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Press ArrowRight', instruction_id='225c4233-7abf-4ccd-a0aa-1db1817f8aa5'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='29b78c99-f96a-480c-a083-c6278724d75c'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='86fa9ae3-8c91-4ec8-9d13-584733b7f3b5'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='14dc5736-9577-47c9-b34d-029857334252'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='f7e6e875-0548-41c0-a215-d1bdfadf0f1f'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='bdb53148-2e22-4e38-81e5-78d4d6d858b8'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='cceac71c-68ed-44af-8596-d316718e3b30'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='d8630349-f1a5-4365-9ca7-dfd7c7d39bf7'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Waiting for slider updates', instruction_id='45576500-80b3-452c-b7ae-716b0cac1565'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Press ArrowRight', instruction_id='e3372565-2e1d-4f81-a562-238bf098351e'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='dba981e6-34d1-49c5-a574-bdcf93cbe990'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='d758afe4-a3de-4720-aff9-3ca13e515b32'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='9b2188da-8a58-4d20-84a4-933c0010e5bb'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='212745c5-d64b-4ad6-b614-a07037671dde'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='a6f41993-9b7e-4086-81c6-c935ebe5d6bf'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='f829f901-3ec0-41a1-a73e-ec55362f08ef'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='2b98db1b-5ab9-4ada-8b96-8cae726b7baf'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Waiting for queued plan steps to complete', instruction_id='b75fd671-25f9-4036-b080-225b2cc21818'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Press ArrowRight', instruction_id='63cc6e15-fceb-45cc-8a1d-1945c1b630f6'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='8de4960d-c05f-4d6f-9e23-80f95067538f'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='31d5149e-089c-4f78-a4b5-95bddf80b606'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='406519d2-6451-48c4-8487-57a4af7687d7'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Clicking Next to advance', instruction_id='cfc52424-bfeb-4680-bc13-1010a7c71b2e'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Clicking the Continue button', instruction_id='c211f930-0825-49fa-8490-c53e29033daf'):
        _loc_3 = page.locator("internal:role=button[name=\"Continue\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('whether the text Press the Right Button is visible in the trial card', instruction_id='c5b26481-c89a-4991-a268-604f4239bd94'):
        set_var('press_the_right_button_visible', await testmu.vision_query(page, "whether the text Press the Right Button is visible in the trial card", ""))
    
    async with testmu.step('Assertion check', instruction_id='748cedc0-4cc5-469e-aff2-edec3e6f78f3'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'Press the Right Button is shown', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{press_the_right_button_visible}}', 'store_key': 'press_the_right_button_visible', 'variable_refs': {'{{press_the_right_button_visible}}': 'true'}}], 'sub_checks': [{'description': 'Press the Right Button is shown', 'store_key': 'press_the_right_button_visible', 'expected_value': 'true', 'extracted_value': '{{press_the_right_button_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'Press the Right Button is shown'})
    
    async with testmu.step('Clicking Next to advance to the Quick Maths question', instruction_id='98d51131-1109-44e3-961e-145adb63598c'):
        _loc_4 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('whether the Quick Maths text is visible in the challenge card', instruction_id='96dffd4b-d761-4b5d-9ce2-451ef3ccb626'):
        set_var('quick_maths_visible', await testmu.vision_query(page, "whether the Quick Maths text is visible in the challenge card", ""))
    
    async with testmu.step('Assertion check', instruction_id='bb7e3b10-aaa6-4ce7-9372-e5683aefdf33'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'Quick Maths is shown', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{quick_maths_visible}}', 'store_key': 'quick_maths_visible', 'variable_refs': {'{{quick_maths_visible}}': 'true'}}], 'sub_checks': [{'description': 'Quick Maths is shown', 'store_key': 'quick_maths_visible', 'expected_value': 'true', 'extracted_value': '{{quick_maths_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'Quick Maths is shown'})
    
    async with testmu.step('Typing Answer to 8 plus 6 into the Quick Maths textbox', instruction_id='851cf321-7de0-4c6b-901f-fd0005b6853e'):
        element_1 = page.locator("internal:role=textbox[name=\"Answer to 8 plus\"i]")
        
        await testmu.fill(element_1, "14")
    
    async with testmu.step('Checking whether the Step 1 passed message is present'):
        set_var('step_1_passed_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {7: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(7).textContent.trim() === 'Step 1 passed.');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Step 1 passed."i'], query='whether the “Step 1 passed.” message is present in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Step 1 passed'))
    
    async with testmu.step('Assertion check', instruction_id='3100489e-7d8e-4dc6-91a3-217b8e98087e'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Step 1 passed', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{step_1_passed_visible}}', 'store_key': 'step_1_passed_visible', 'variable_refs': {'{{step_1_passed_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Step 1 passed', 'store_key': 'step_1_passed_visible', 'expected_value': 'true', 'extracted_value': '{{step_1_passed_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Step 1 passed'})


if __name__ == "__main__":
    testmu.run(test)
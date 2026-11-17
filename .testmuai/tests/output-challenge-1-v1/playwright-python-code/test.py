import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="ee0f3985-ddd2-4467-b71b-cbf1392cc415",
    name="Complete Challenge 1 of AgentDegree Exam",
    tc_id="TC-30",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"challenge_1_visible": "true", "back_button_top_left": "true", "pagination_steps_1_to_5_bottom": "true", "challenge_1_passed_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-1', instruction_id='cace6dbf-c189-47b6-9e37-6debbd780544'):
        await page.goto("http://localhost:3000/gauntlet/step-1")
    
    async with testmu.step('Checking whether the Challenge 1 heading is present'):
        set_var('challenge_1_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(5).textContent.trim() === 'Challenge 1' && !!(el(5).offsetWidth || el(5).offsetHeight || el(5).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="Challenge"i]'], query='whether the Challenge 1 heading is visible in the main page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Challenge 1'))
    
    async with testmu.step('Checking whether the Back button is present at the top left'):
        set_var('back_button_top_left', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {3: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((() => { const r = el(3).getBoundingClientRect(); return el(3).textContent.includes('Back') && r.x < innerWidth / 2 && r.y < innerHeight / 2 && !!(el(3).offsetWidth || el(3).offsetHeight || el(3).getClientRects().length); })());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="← Back"i]'], query='whether the Back button is visible at the upper-left area of the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='a Back button is at the top left'))
    
    async with testmu.step('Checking whether pagination steps 1 through 5 are present at the bottom'):
        set_var('pagination_steps_1_to_5_bottom', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((() => { const labels = [...el(13).querySelectorAll(\'[role="button"]\')].map(b => b.textContent.trim()); const r = el(13).getBoundingClientRect(); return [\'1\',\'2\',\'3\',\'4\',\'5\'].every(n => labels.includes(n)) && r.y > 500 && !!(el(13).offsetWidth || el(13).offsetHeight || el(13).getClientRects().length); })());\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['internal:role=navigation[name="pagination"i]'], query='whether the bottom pagination navigation contains steps 1 through 5', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='pagination with steps 1 to 5 is at the bottom'))
    
    async with testmu.step('Assertion check', instruction_id='da0f1281-06a7-4f08-8bd5-8267c5b224e8'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Challenge 1', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_1_visible}}', 'store_key': 'challenge_1_visible', 'variable_refs': {'{{challenge_1_visible}}': 'true'}}, {'description': 'a Back button is at the top left', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{back_button_top_left}}', 'store_key': 'back_button_top_left', 'variable_refs': {'{{back_button_top_left}}': 'true'}}, {'description': 'pagination with steps 1 to 5 is at the bottom', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{pagination_steps_1_to_5_bottom}}', 'store_key': 'pagination_steps_1_to_5_bottom', 'variable_refs': {'{{pagination_steps_1_to_5_bottom}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Challenge 1', 'store_key': 'challenge_1_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_1_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'a Back button is at the top left', 'store_key': 'back_button_top_left', 'expected_value': 'true', 'extracted_value': '{{back_button_top_left}}', 'operator': 'equals', 'transforms': []}, {'description': 'pagination with steps 1 to 5 is at the bottom', 'store_key': 'pagination_steps_1_to_5_bottom', 'expected_value': 'true', 'extracted_value': '{{pagination_steps_1_to_5_bottom}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Challenge 1 and a Back button at the top left and pagination with steps 1 to 5 at the bottom'})
    
    async with testmu.step('Waiting for the queued plan to execute next steps', instruction_id='90b6877d-2425-4cd5-b71d-1a2da905e167'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "I am agent"', instruction_id='c86c9dfb-2634-4d49-9828-da7719c00412'):
        _loc_1 = page.locator("internal:role=checkbox[name=\"I am agent\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Click "Next →"', instruction_id='e74baa70-a5ef-4d92-bc78-621e8c684e35'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Waiting for the queued plan steps to run', instruction_id='8ef32ae6-612e-492d-949d-ced7e8cd186d'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "Photo tile 2"', instruction_id='c85ec1b1-0641-4eca-8169-68a8bd93aa02'):
        _loc_3 = page.locator("internal:role=button[name=\"Photo tile 2\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Click "Photo tile 4"', instruction_id='b60c1d1f-a2f2-49a1-8b12-6b0bc3383ed6'):
        _loc_4 = page.locator("internal:role=button[name=\"Photo tile 4\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Click "Photo tile 7"', instruction_id='bd50f1a6-932c-4cb5-811f-27ed11962d4d'):
        _loc_5 = page.locator("internal:role=button[name=\"Photo tile 7\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Click "Next →"', instruction_id='db21b116-29cb-4217-8796-1129688b3bee'):
        _loc_6 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Dragging the slider handle into the green zone', instruction_id='889ad5eb-272e-4fd6-9949-731f6029fec5'):
        element_0 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await testmu.fill(element_0, "75")
    
    async with testmu.step('Waiting for the queued slider handle keystrokes to run', instruction_id='619d1fb6-19df-4a19-83ee-ca103dee7487'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Press PageDown', instruction_id='067e19e1-ce3a-4812-818a-f7902f1cbf1a'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageDown')
    
    async with testmu.step('Press PageDown', instruction_id='994322ae-e8ac-469b-adab-d76e57391207'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageDown')
    
    async with testmu.step('Clicking Next', instruction_id='b592a17e-f29f-4850-aef5-7cb986f126af'):
        _loc_7 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('PRIMARY: Place the cube into the empty part of the picture; role=button | HINTS: cube is centered below the landscape picture in the Complete the Picture challenge', instruction_id='21af71d1-3750-4e67-aaab-d2bd07be32b1'):
        coords = await testmu.get_vision_coordinates(page, 'PRIMARY: Place the cube into the empty part of the picture; role=button | HINTS: cube is centered below the landscape picture in the Complete the Picture challenge', "click", 950, 928)
        await page.mouse.click(coords['x'], coords['y'])
        
    
    async with testmu.step('Placing the cube into the empty part of the picture', instruction_id='0b38e67f-951f-49c9-a95e-8e64c58e5a3c'):
        _loc_8 = page.locator("internal:role=button[name=\"Empty part of the picture\"i]")
        
        await _loc_8.click()
    
    async with testmu.step('Clicking Next button', instruction_id='d9db1ba6-4b38-4045-bc77-0b5bd6ce1407'):
        _loc_9 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_9.click()
    
    async with testmu.step('Waiting for the next step in the queued plan', instruction_id='c5beb92d-ff6a-4706-bcb0-c49c593381aa'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "AGENT7" into "Type the characters shown above"', instruction_id='6771497c-bde0-4864-bb6d-57babe61332d'):
        element_1 = page.locator("internal:role=textbox[name=\"Type the characters shown\"i]")
        
        await testmu.fill(element_1, "AGENT7")
    
    async with testmu.step('Checking whether Challenge 1 passed is present'):
        set_var('challenge_1_passed_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {8: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(8).textContent.includes('Challenge 1 passed'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Challenge 1 passed."i'], query='whether the text "Challenge 1 passed" is present in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Challenge 1 passed'))
    
    async with testmu.step('Assertion check', instruction_id='be7f0412-808f-4bf6-866b-2a26ae32fded'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Challenge 1 passed', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_1_passed_visible}}', 'store_key': 'challenge_1_passed_visible', 'variable_refs': {'{{challenge_1_passed_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Challenge 1 passed', 'store_key': 'challenge_1_passed_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_1_passed_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Challenge 1 passed'})


if __name__ == "__main__":
    testmu.run(test)
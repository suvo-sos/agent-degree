import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="aabc922a-2598-4e3b-810b-09b756327857",
    name="Complete Challenge 2 Form Submission",
    tc_id="TC-31",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"challenge_2_visible": "true", "back_button_top_left": "true", "pagination_steps_1_to_5_bottom": "true", "challenge_2_passed_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-2', instruction_id='d3b2c979-f2a3-4e35-b186-0a58785e136a'):
        await page.goto("http://localhost:3000/gauntlet/step-2")
    
    async with testmu.step('Checking whether the Challenge 2 heading is present'):
        set_var('challenge_2_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(5).textContent.trim() === 'Challenge 2' && !!(el(5).offsetWidth || el(5).offsetHeight || el(5).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="Challenge"i]'], query='whether the Challenge 2 heading is present in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Challenge 2'))
    
    async with testmu.step('Checking whether the Back button is present at the top left'):
        set_var('back_button_top_left', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {3: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((() => { const r = el(3).getBoundingClientRect(); return el(3).textContent.includes('Back') && r.left < innerWidth / 2 && r.top < innerHeight / 2 && !!(el(3).offsetWidth || el(3).offsetHeight || el(3).getClientRects().length); })());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="← Back"i]'], query='whether the Back button is present at the top left of the page', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='a Back button is at the top left'))
    
    async with testmu.step('Checking whether bottom pagination steps 1 through 5 are present'):
        set_var('pagination_steps_1_to_5_bottom', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {22: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((() => { const r = el(22).getBoundingClientRect(); const t = el(22).innerText; return ['1','2','3','4','5'].every(n => new RegExp('(^|\\\\s)' + n + '(\\\\s|$)').test(t)) && r.bottom >= innerHeight - 40; })());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=navigation[name="pagination"i]'], query='whether the pagination at the bottom of the page includes steps 1 through 5', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='pagination with steps 1 to 5 is at the bottom'))
    
    async with testmu.step('Assertion check', instruction_id='c13d9cc0-b871-41c5-9548-a32be4e5b9e2'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Challenge 2', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_2_visible}}', 'store_key': 'challenge_2_visible', 'variable_refs': {'{{challenge_2_visible}}': 'true'}}, {'description': 'a Back button is at the top left', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{back_button_top_left}}', 'store_key': 'back_button_top_left', 'variable_refs': {'{{back_button_top_left}}': 'true'}}, {'description': 'pagination with steps 1 to 5 is at the bottom', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{pagination_steps_1_to_5_bottom}}', 'store_key': 'pagination_steps_1_to_5_bottom', 'variable_refs': {'{{pagination_steps_1_to_5_bottom}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Challenge 2', 'store_key': 'challenge_2_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_2_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'a Back button is at the top left', 'store_key': 'back_button_top_left', 'expected_value': 'true', 'extracted_value': '{{back_button_top_left}}', 'operator': 'equals', 'transforms': []}, {'description': 'pagination with steps 1 to 5 is at the bottom', 'store_key': 'pagination_steps_1_to_5_bottom', 'expected_value': 'true', 'extracted_value': '{{pagination_steps_1_to_5_bottom}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Challenge 2 and a Back button at the top left and pagination with steps 1 to 5 at the bottom'})
    
    async with testmu.step('Waiting for the next queued form step to load', instruction_id='fa1522d7-6f7a-4b2e-9491-6cdefbc19b2b'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "Arjun Mehta" into "Full name"', instruction_id='9c201044-e8a1-4883-8204-ab758ba516fd'):
        element_0 = page.locator("internal:role=textbox[name=\"Full name\"i]")
        
        await testmu.fill(element_0, "Arjun Mehta")
    
    async with testmu.step('Type "29" into "Age"', instruction_id='0ccd2b5c-ad0c-45ff-a01e-647c144ce170'):
        element_1 = page.locator("internal:role=textbox[name=\"Age\"i]")
        
        await testmu.fill(element_1, "29")
    
    async with testmu.step('Type "product designer" into "Job title"', instruction_id='e0a517be-38ba-4db9-9cf6-4cab6c241603'):
        element_2 = page.locator("internal:role=textbox[name=\"Job title\"i]")
        
        await testmu.fill(element_2, "product designer")
    
    async with testmu.step('Type "Brightlane" into "Company"', instruction_id='dd4a5604-2a53-4195-9825-7dcc87797310'):
        element_3 = page.locator("internal:role=textbox[name=\"Company\"i]")
        
        await testmu.fill(element_3, "Brightlane")
    
    async with testmu.step('Type "Bengaluru" into "City"', instruction_id='5646c5ac-7048-427f-abc5-15e8250964b3'):
        element_4 = page.locator("internal:role=textbox[name=\"City\"i]")
        
        await testmu.fill(element_4, "Bengaluru")
    
    async with testmu.step('Click "Next →"', instruction_id='19c92f4c-5b63-4ccf-91a9-9b42ed3d4826'):
        _loc_1 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Waiting for the form to finish loading and be ready for input', instruction_id='cb24045f-cce0-4a60-8020-04a79b96f503'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "Priya Sharma" into "Full name"', instruction_id='e3e6f60f-d5b2-43e7-b395-acc9d901e42e'):
        element_5 = page.locator("internal:role=textbox[name=\"Full name\"i]")
        
        await testmu.fill(element_5, "Priya Sharma")
    
    async with testmu.step('Scroll into view: PRIMARY: fill the form with the age from the document; role=textbox; text="Age" | HINTS: container=The Document form', instruction_id='3c3b194e-3134-4a67-8138-fa47e4ec8b8e'):
        element_6 = page.locator("internal:role=textbox[name=\"Age\"i]")
        await element_6.evaluate("el => el.scrollIntoView({block: 'center'})")
    
    async with testmu.step('Type "34" into "Age"', instruction_id='8623c611-4b6d-4195-9b8f-59d85c47473f'):
        element_7 = page.locator("internal:role=textbox[name=\"Age\"i]")
        
        await testmu.fill(element_7, "34")
    
    async with testmu.step('Type "Data Analyst" into "Job title"', instruction_id='8e730ce2-f5e0-4575-b164-6c715f57068f'):
        element_8 = page.locator("internal:role=textbox[name=\"Job title\"i]")
        
        await testmu.fill(element_8, "Data Analyst")
    
    async with testmu.step('Type "Northwind Labs" into "Company"', instruction_id='68097d2f-3a49-4711-87d5-74e357fa147c'):
        element_9 = page.locator("internal:role=textbox[name=\"Company\"i]")
        
        await testmu.fill(element_9, "Northwind Labs")
    
    async with testmu.step('Type "Pune" into "City"', instruction_id='bfa452e1-c07f-4d04-b0c3-1b9e2d40b71c'):
        element_10 = page.locator("internal:role=textbox[name=\"City\"i]")
        
        await testmu.fill(element_10, "Pune")
    
    async with testmu.step('Click "Next →"', instruction_id='f614e0ea-39ca-43cc-bd34-bc9abfd49aae'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Waiting for queued steps to complete', instruction_id='63f58e7b-8a12-4403-a3dd-39b78b979901'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "Full-time"', instruction_id='80f9af2e-d739-4e77-b181-f5501855500c'):
        _loc_3 = page.locator("internal:role=radio[name=\"Full-time\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Select "Design" in "Department"', instruction_id='6625171c-e6fd-43bd-b19e-d6854ed70512'):
        element_11 = page.locator("internal:label=\"Department\"i")
        
        await element_11.select_option()
    
    async with testmu.step('Type "2025-03-10" into "First day"', instruction_id='6e7e0e9a-3c41-4e9f-b5d2-7bd81073db1e'):
        element_12 = page.locator("internal:role=textbox[name=\"First day\"i]")
        
        await testmu.fill(element_12, "2025-03-10")
    
    async with testmu.step('Clicking Next', instruction_id='d62f01fa-71db-40a4-a30a-820672e689c5'):
        _loc_4 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Waiting for the plan steps to start', instruction_id='f4b215d4-01e0-4ffa-9ede-4702226269b5'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Scroll into view: PRIMARY: fix the two wrong values in the pre-filled form by comparing with the employee record document shown; role=textbox; text="Age" | HINTS: container=Fix the Mistakes form', instruction_id='b9e8a6ba-4c60-469f-8e0a-261cf130ad34'):
        element_13 = page.locator("internal:role=textbox[name=\"Age\"i]")
        await element_13.evaluate("el => el.scrollIntoView({block: 'center'})")
    
    async with testmu.step('Type "34" into "Age"', instruction_id='51501171-586a-46ec-9690-5704db566744'):
        element_14 = page.locator("internal:role=textbox[name=\"Age\"i]")
        
        await testmu.fill(element_14, "34")
    
    async with testmu.step('Type "Pune" into "City"', instruction_id='91f142eb-9c58-4408-97e7-d1c95386bad0'):
        element_15 = page.locator("internal:role=textbox[name=\"City\"i]")
        
        await testmu.fill(element_15, "Pune")
    
    async with testmu.step('Click "Next →"', instruction_id='165806bf-004a-43ce-bb64-4d811569a732'):
        _loc_5 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Waiting for the queued plan to proceed', instruction_id='4ed18efc-4a96-4967-9578-72243fdc9897'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "Arjun Mehta" into "Signature"', instruction_id='e3b027ce-4910-4c24-9141-90f69d1657e7'):
        element_16 = page.locator("internal:role=textbox[name=\"Signature\"i]")
        
        await testmu.fill(element_16, "Arjun Mehta")
    
    async with testmu.step('Click "I declare the information above is true"', instruction_id='95466de3-bc69-4f63-be36-2cfdefe4f249'):
        _loc_6 = page.locator("internal:role=checkbox[name=\"I declare the information\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Type "2026-11-17" into "Date"', instruction_id='79d77b3f-221f-47cc-a6d7-44b517087553'):
        element_17 = page.locator("internal:role=textbox[name=\"Date\"i]")
        
        await testmu.fill(element_17, "2026-11-17")
    
    async with testmu.step('Clicking Submit the form button', instruction_id='05d82713-3c19-4050-83da-0608eb1bfd93'):
        _loc_7 = page.locator("internal:role=button[name=\"Submit the form\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('Checking whether the Challenge 2 passed message is present'):
        set_var('challenge_2_passed_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {8: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(8).textContent.trim() === 'Challenge 2 passed.' && !!(el(8).offsetWidth || el(8).offsetHeight || el(8).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Challenge 2 passed."i'], query='whether the Challenge 2 passed message is present and visible in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Challenge 2 passed'))
    
    async with testmu.step('Assertion check', instruction_id='75e78098-463f-4e2b-a9fd-e552c2b50d3b'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Challenge 2 passed', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_2_passed_visible}}', 'store_key': 'challenge_2_passed_visible', 'variable_refs': {'{{challenge_2_passed_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Challenge 2 passed', 'store_key': 'challenge_2_passed_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_2_passed_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Challenge 2 passed'})


if __name__ == "__main__":
    testmu.run(test)
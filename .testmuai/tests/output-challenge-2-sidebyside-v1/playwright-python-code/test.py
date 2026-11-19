import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="4d67f7cc-f73a-4f0f-9d4c-e9efab7f3585",
    name="Complete and Verify Side-by-Side Layout Tests in Challenge 2",
    tc_id="TC-109",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"test_2_side_by_side_layout": "true", "test_2_image_and_form_readable": "true", "test_4_side_by_side_layout": "true", "challenge_2_passed": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/final-exam/step-2', instruction_id='f696a059-b330-4d12-9671-54b87903afa1'):
        await page.goto("https://agent-degree-kappa.vercel.app/final-exam/step-2")
    
    async with testmu.step('Waiting for the plan to finish queuing actions', instruction_id='474c9728-897f-4b8d-a3d5-b4b6c2ed9b83'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "Arjun Mehta" into "Full name"', instruction_id='0b871472-a038-4343-8446-2baff13961cc'):
        element_0 = page.locator("internal:role=textbox[name=\"Full name\"i]")
        
        await testmu.fill(element_0, "Arjun Mehta")
    
    async with testmu.step('Type "29" into "Age"', instruction_id='8c7ab1f9-94a2-44fe-9a55-8dfd2e259e46'):
        element_1 = page.locator("internal:role=textbox[name=\"Age\"i]")
        
        await testmu.fill(element_1, "29")
    
    async with testmu.step('Waiting while your plan is queued and ready to start', instruction_id='a436ea41-221a-41b6-8d29-d0bc5f010c54'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "product designer" into "Job title"', instruction_id='f4e4b4be-7241-4d7f-ae53-a80e6b4d712c'):
        element_2 = page.locator("internal:role=textbox[name=\"Job title\"i]")
        
        await testmu.fill(element_2, "product designer")
    
    async with testmu.step('Typing Company into the form field', instruction_id='581b6bd5-d950-4b75-885b-e36148129a7a'):
        element_3 = page.locator("internal:role=textbox[name=\"Company\"i]")
        
        await testmu.fill(element_3, "Brightlane")
    
    async with testmu.step('Entering Bengaluru into the City field', instruction_id='e7349ac8-95f2-40a2-9058-5dbbad2f639e'):
        element_4 = page.locator("internal:role=textbox[name=\"City\"i]")
        
        await testmu.fill(element_4, "Bengaluru")
    
    async with testmu.step('Clicking Next button to continue the test', instruction_id='42d43bdf-3fef-4a93-baa8-540168289f17'):
        _loc_1 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Waiting for the queued form steps to start running', instruction_id='2db55857-7a58-4205-8658-87eb57b427c5'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "Priya Sharma" into "Full name"', instruction_id='ed1d43c7-d033-4d12-8c81-670b43ad8833'):
        element_5 = page.locator("internal:role=textbox[name=\"Full name\"i]")
        
        await testmu.fill(element_5, "Priya Sharma")
    
    async with testmu.step('Typing 34 into the Age field', instruction_id='91ab1daf-4be8-49e6-bb9f-d3e4e4933c52'):
        element_6 = page.locator("internal:role=textbox[name=\"Age\"i]")
        
        await testmu.fill(element_6, "34")
    
    async with testmu.step('Typing Data Analyst into Job title field', instruction_id='d3c02632-7d67-41cd-8acd-0687ab0abc95'):
        element_7 = page.locator("internal:role=textbox[name=\"Job title\"i]")
        
        await testmu.fill(element_7, "Data Analyst")
    
    async with testmu.step('Typing Company name Northwind Labs in the form field', instruction_id='71e4eb24-2e41-4d16-a444-6c12baee4626'):
        element_8 = page.locator("internal:role=textbox[name=\"Company\"i]")
        
        await testmu.fill(element_8, "Northwind Labs")
    
    async with testmu.step('Typing Pune into the City field', instruction_id='50d3829c-a87b-4467-9565-6f6fdf02923e'):
        element_9 = page.locator("internal:role=textbox[name=\"City\"i]")
        
        await testmu.fill(element_9, "Pune")
    
    async with testmu.step('whether the employee-record document image is visible on the left and the form is visible beside it on the right in the main challenge area', instruction_id='bd203476-5c6f-4a0f-a8bd-c930d9e0536a'):
        set_var('test_2_side_by_side_layout', await testmu.vision_query(page, "whether the employee-record document image is visible on the left and the form is visible beside it on the right in the main challenge area", ""))
    
    async with testmu.step('whether the employee-record document image and the form fields are visibly readable in the main challenge area', instruction_id='c4bef66d-b56a-4e43-9cdc-5765151bb674'):
        set_var('test_2_image_and_form_readable', await testmu.vision_query(page, "whether the employee-record document image and the form fields are visibly readable in the main challenge area", ""))
    
    async with testmu.step('Assertion check', instruction_id='57f98cd5-3a30-4cf6-a5fd-63b7249d3f68'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'On test 2 of 5, the employee-record document image is on the LEFT side and the form is on the RIGHT side, side by side.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{test_2_side_by_side_layout}}', 'store_key': 'test_2_side_by_side_layout', 'variable_refs': {'{{test_2_side_by_side_layout}}': 'true'}}, {'description': 'On test 2 of 5, both the employee-record document image and the form are readable.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{test_2_image_and_form_readable}}', 'store_key': 'test_2_image_and_form_readable', 'variable_refs': {'{{test_2_image_and_form_readable}}': 'true'}}], 'sub_checks': [{'description': 'On test 2 of 5, the employee-record document image is on the LEFT side and the form is on the RIGHT side, side by side.', 'store_key': 'test_2_side_by_side_layout', 'expected_value': 'true', 'extracted_value': '{{test_2_side_by_side_layout}}', 'operator': 'equals', 'transforms': []}, {'description': 'On test 2 of 5, both the employee-record document image and the form are readable.', 'store_key': 'test_2_image_and_form_readable', 'expected_value': 'true', 'extracted_value': '{{test_2_image_and_form_readable}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'On test 2 of 5, the employee-record document image is on the LEFT side and the form is on the RIGHT side, side by side, so you can read the image and fill the form.'})
    
    async with testmu.step('Clicking Next to advance to the next test', instruction_id='2d1b20ea-7d6c-436e-9442-45c2255e644a'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Selecting Full-time in Employment type section', instruction_id='6db2c636-7b54-48be-be9a-4501ca1deb9d'):
        _loc_3 = page.locator("internal:role=radio[name=\"Full-time\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Selecting Department option in Complete test 3', instruction_id='8c43a991-d798-4a70-a450-39eb51026cae'):
        _loc_4 = page.locator("internal:role=combobox[name=\"Department\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Selecting Design option for completing test 3', instruction_id='a3252a0d-7300-457f-9300-1f3dc3aca960'):
        _loc_5 = page.locator("internal:role=option[name=\"Design\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Typing the date First day for test 3', instruction_id='2c606305-bec5-4d7f-8643-878275005b15'):
        element_10 = page.locator("internal:role=textbox[name=\"First day\"i]")
        
        await testmu.fill(element_10, "2025-03-10")
    
    async with testmu.step('Clicking Next to continue completing test 3', instruction_id='ba1b359c-e5ef-437e-b7d2-4908d2e0ff68'):
        _loc_6 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Entering age value 34 in the form field', instruction_id='0b4e06d6-298f-4de4-b1b2-ffe16e68f009'):
        element_11 = page.locator("internal:role=textbox[name=\"Age\"i]")
        
        await testmu.fill(element_11, "34")
    
    async with testmu.step('Typing Pune into City textbox', instruction_id='dfcbefb0-f1bb-476a-b9e9-d84888be912d'):
        element_12 = page.locator("internal:role=textbox[name=\"City\"i]")
        
        await testmu.fill(element_12, "Pune")
    
    async with testmu.step('whether the employee record image on the left and the form on the right are displayed side by side in test 4', instruction_id='6d404566-6ddc-4069-97fb-383724f05e09'):
        set_var('test_4_side_by_side_layout', await testmu.vision_query(page, "whether the employee record image on the left and the form on the right are displayed side by side in test 4", ""))
    
    async with testmu.step('Assertion check', instruction_id='cf8b80ed-ee63-4109-8dd8-2e53416a41c7'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'On test 4 of 5, the record image is on the LEFT side and the form is on the RIGHT side, side by side.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{test_4_side_by_side_layout}}', 'store_key': 'test_4_side_by_side_layout', 'variable_refs': {'{{test_4_side_by_side_layout}}': 'true'}}], 'sub_checks': [{'description': 'On test 4 of 5, the record image is on the LEFT side and the form is on the RIGHT side, side by side.', 'store_key': 'test_4_side_by_side_layout', 'expected_value': 'true', 'extracted_value': '{{test_4_side_by_side_layout}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'On test 4 of 5, the record image is on the LEFT side and the form is on the RIGHT side, side by side.'})
    
    async with testmu.step('Clicking Next to advance to the next test', instruction_id='a51a040c-febc-4e95-9c12-9199c0eb9e3f'):
        _loc_7 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('Clicking Edit menu in the menu bar', instruction_id='19cbfd09-d0fa-45e4-a123-78fa8798d24a'):
        _loc_8 = page.locator("internal:role=menuitem[name=\"Edit\"i]")
        
        await _loc_8.click()
    
    async with testmu.step('Clicking Edit menu to open Find options', instruction_id='5649b62f-587a-412a-b3e6-cc698e05bd01'):
        _loc_9 = page.locator("internal:role=menuitem[name=\"Find\"i]")
        
        await _loc_9.click()
    
    async with testmu.step('Clicking Search the web in the Edit menu submenu', instruction_id='0c64065b-fb13-440e-b31d-efd98fa992ed'):
        _loc_10 = page.locator("internal:role=menuitem[name=\"Search the web\"i]")
        
        await _loc_10.click()
    
    async with testmu.step('Assessing side-by-side changes for readability and layout issues', instruction_id='22796f65-d347-4c64-8348-a82f6e90f4bd'):
        await page.wait_for_timeout(500)
    
    async with testmu.step('Waiting for the challenge to finish', instruction_id='8d684007-8c95-488f-b54c-f11a76ce0649'):
        await page.wait_for_timeout(500)
    
    async with testmu.step('Checking whether the Challenge 2 confirmation is present'):
        set_var('challenge_2_passed', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {7: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(7).textContent.trim() === 'Challenge 2 passed.');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Challenge 2 passed."i'], query='whether the text “Challenge 2 passed.” is present in the page confirmation message', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The page shows Challenge 2 passed.'))
    
    async with testmu.step('Assertion check', instruction_id='9c989dac-4d0d-49b6-ba33-b41383f6d1c3'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The page shows Challenge 2 passed.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_2_passed}}', 'store_key': 'challenge_2_passed', 'variable_refs': {'{{challenge_2_passed}}': 'true'}}], 'sub_checks': [{'description': 'The page shows Challenge 2 passed.', 'store_key': 'challenge_2_passed', 'expected_value': 'true', 'extracted_value': '{{challenge_2_passed}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'The page shows Challenge 2 passed.'})


if __name__ == "__main__":
    testmu.run(test)
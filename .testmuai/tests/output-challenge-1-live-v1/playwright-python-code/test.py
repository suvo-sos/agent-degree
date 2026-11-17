import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="4caf4a19-2df4-41fa-bfef-f339dced3932",
    name="Complete Challenge 1 of AgentDegree Exam",
    tc_id="TC-32",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"challenge_1_visible": "true", "back_button_top_left_visible": "true", "pagination_steps_1_to_5_bottom_visible": "true", "challenge_1_passed_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/gauntlet/step-1', instruction_id='8f015072-ad61-4048-b54d-a62ac43a2907'):
        await page.goto("https://agent-degree-kappa.vercel.app/gauntlet/step-1")
    
    async with testmu.step('Checking whether the Challenge 1 heading is present'):
        set_var('challenge_1_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(5).textContent.trim() === 'Challenge 1' && !!(el(5).offsetWidth || el(5).offsetHeight || el(5).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="Challenge"i]'], query='whether the Challenge 1 heading is visible in the main page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Challenge 1'))
    
    async with testmu.step('Checking whether the top-left Back button is present'):
        set_var('back_button_top_left_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {3: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(3).textContent.includes('Back') && !!(el(3).offsetWidth || el(3).offsetHeight || el(3).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="← Back"i]'], query='whether the Back button is visible at the top left of the page', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='a Back button is at the top left'))
    
    async with testmu.step('Checking whether bottom pagination steps 1 through 5 are present'):
        set_var('pagination_steps_1_to_5_bottom_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (['1','2','3','4','5'].every(n => el(13).textContent.includes(n)) && !!(el(13).offsetWidth || el(13).offsetHeight || el(13).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=navigation[name="pagination"i]'], query='whether pagination steps 1 through 5 are visible at the bottom of the page', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='pagination with steps 1 to 5 is at the bottom'))
    
    async with testmu.step('Assertion check', instruction_id='65848756-e740-4d96-9ba3-4837fe911326'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Challenge 1', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_1_visible}}', 'store_key': 'challenge_1_visible', 'variable_refs': {'{{challenge_1_visible}}': 'true'}}, {'description': 'a Back button is at the top left', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{back_button_top_left_visible}}', 'store_key': 'back_button_top_left_visible', 'variable_refs': {'{{back_button_top_left_visible}}': 'true'}}, {'description': 'pagination with steps 1 to 5 is at the bottom', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{pagination_steps_1_to_5_bottom_visible}}', 'store_key': 'pagination_steps_1_to_5_bottom_visible', 'variable_refs': {'{{pagination_steps_1_to_5_bottom_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Challenge 1', 'store_key': 'challenge_1_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_1_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'a Back button is at the top left', 'store_key': 'back_button_top_left_visible', 'expected_value': 'true', 'extracted_value': '{{back_button_top_left_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'pagination with steps 1 to 5 is at the bottom', 'store_key': 'pagination_steps_1_to_5_bottom_visible', 'expected_value': 'true', 'extracted_value': '{{pagination_steps_1_to_5_bottom_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Challenge 1 and a Back button at the top left and pagination with steps 1 to 5 at the bottom'})
    
    async with testmu.step('Waiting for queued plan to start clicking I am agent and Next', instruction_id='69c68ae3-9b32-4bc4-ab61-65e69c35d029'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "I am agent"', instruction_id='34a1352a-1693-4309-923b-f54dac5fe61e'):
        _loc_1 = page.locator("internal:role=checkbox[name=\"I am agent\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Click "Next →"', instruction_id='32945684-d686-4770-9d4b-7ad86c700ffb'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Waiting for the photo tiles to finish loading', instruction_id='a45619cf-dbf0-4f4d-b65a-67c6eec9cbdd'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "Photo tile 2"', instruction_id='1c0c4b8f-7891-43c4-838e-22e1bcd270ad'):
        _loc_3 = page.locator("internal:role=button[name=\"Photo tile 2\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Click "Photo tile 4"', instruction_id='ee83c8b5-04db-40d3-9ca3-be82af549d79'):
        _loc_4 = page.locator("internal:role=button[name=\"Photo tile 4\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Click "Photo tile 7"', instruction_id='9ad1557d-41e6-4dec-b6ff-b2c78a9b6d81'):
        _loc_5 = page.locator("internal:role=button[name=\"Photo tile 7\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Click "Next →"', instruction_id='ea34beed-d774-4a69-a009-70807535cb2e'):
        _loc_6 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Dragging the slider handle into the green zone', instruction_id='86a7518e-a872-4275-a1af-f1c3d127053d'):
        element_0 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await testmu.fill(element_0, "75")
    
    async with testmu.step('Waiting for the queued slider presses', instruction_id='854d289a-35cf-4946-85b8-e752dc028da8'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Press Home', instruction_id='08d36228-728c-44d8-a1ea-4354c63e9951'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('Home')
    
    async with testmu.step('Press PageUp', instruction_id='42d2a64f-e34c-476c-a71d-c4ac44b3a4f3'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='368cc34c-97e0-41b6-887c-edddff9f4353'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='fbe83e5c-70df-40f2-b4cf-0af4e4b4e0bf'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='b0ce2076-af74-4b9e-a108-df9e5fe272cc'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='90e4b2f9-831b-4475-8af3-28ce69bfbe47'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='a586288b-7ba5-4fff-b820-8ed90b1a86f9'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='ba14fde8-b7c0-4db5-8766-19bcac3bdb2f'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Clicking Next button in Challenge 1', instruction_id='28042c09-e69d-4f5d-b568-94aef238b38d'):
        _loc_7 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('PRIMARY: Place the cube into the empty part of the picture; role=image | HINTS: click the small cube beneath the landscape picture in the Challenge 1 card', instruction_id='9f75b5a5-3b40-448d-bd9c-d24711bacfce'):
        coords = await testmu.get_vision_coordinates(page, 'PRIMARY: Place the cube into the empty part of the picture; role=image | HINTS: click the small cube beneath the landscape picture in the Challenge 1 card', "click", 950, 923)
        await page.mouse.click(coords['x'], coords['y'])
        
    
    async with testmu.step('Clicking the empty doorway in the house picture', instruction_id='87cbf3b1-156f-4b71-b0a1-91ed14b1da4b'):
        _loc_8 = page.locator("internal:role=button[name=\"Empty part of the picture\"i]")
        
        await _loc_8.click()
    
    async with testmu.step('Clicking Next button', instruction_id='6cbe03d8-4e76-4b28-aecc-fd04c627ac3f'):
        _loc_9 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_9.click()
    
    async with testmu.step('Typing the characters shown in the distorted text', instruction_id='389c54e1-1221-41aa-828b-78d71abd9803'):
        element_1 = page.locator("internal:role=textbox[name=\"Type the characters shown\"i]")
        
        await testmu.fill(element_1, "AGENT7")
    
    async with testmu.step('Checking whether the Challenge 1 passed message is present'):
        set_var('challenge_1_passed_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {8: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(8).textContent.trim() === 'Challenge 1 passed.' && !!(el(8).offsetWidth || el(8).offsetHeight || el(8).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Challenge 1 passed."i'], query='whether the Challenge 1 passed message is visible in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Challenge 1 passed'))
    
    async with testmu.step('Assertion check', instruction_id='d475f1ee-bfd1-4fca-aad5-952f36304400'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Challenge 1 passed', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_1_passed_visible}}', 'store_key': 'challenge_1_passed_visible', 'variable_refs': {'{{challenge_1_passed_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Challenge 1 passed', 'store_key': 'challenge_1_passed_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_1_passed_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Challenge 1 passed'})


if __name__ == "__main__":
    testmu.run(test)
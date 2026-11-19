import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="c2b9793d-0dee-4fb1-acff-672c6a4c83bf",
    name="Complete Challenge 1 Tests",
    tc_id="TC-82",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"carCount": "1", "car_count_picked_check": "1 of 1 cars picked", "solved_text_visible": "true", "challenge_1_passed_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/gauntlet/step-1', instruction_id='f7e2bfc8-8e14-43cf-9779-d615d1d5265e'):
        await page.goto("https://agent-degree-kappa.vercel.app/gauntlet/step-1")
    
    async with testmu.step('Waiting for the queued plan to be executed', instruction_id='7b3db6f5-c1b1-4e87-a649-a4f9ba702346'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "I am agent"', instruction_id='fdebc095-d7fd-4bf7-9e8d-4ec5be8de831'):
        _loc_1 = page.locator("internal:role=checkbox[name=\"I am agent\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Next button in bottom-right corner', instruction_id='c5db10b8-3091-4fe3-8cea-de47e9984cd7'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Reading the car count from the photo-grid status'):
        set_var('carCount', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Number((el(24).textContent.match(/of\\s+(\\d+)\\s+cars?/i)||[])[1]));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="of 1 cars picked"i'], query='the total number of cars in the status text below the photo grid', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='Get the number of cars from the status text under the 3x3 photo grid and save as {{carCount}}.'))
    
    async with testmu.step('Clicking the car photo tile in the bottom-right corner', instruction_id='63b39df4-008e-4799-bdf3-2fefe2aa4eec'):
        _loc_3 = page.locator("internal:role=button[name=\"Photo tile 9\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Reading the picked-car status beneath the photo grid'):
        set_var('car_count_picked_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(24).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="of 1 cars picked"i'], query='the picked-car status text beneath the 3x3 photo grid', expected_value='1 of 1 cars picked', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The status under the 3x3 photo grid shows all of the stored {{carCount}} picked.', reprobe=True))
    
    async with testmu.step('Assertion check', instruction_id='6cd8172d-f2f8-4ca2-addb-576b32356857'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The status under the 3x3 photo grid shows all of the stored {{carCount}} picked.', 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': '1 of 1 cars picked', 'extracted_value': '{{car_count_picked_check}}', 'store_key': 'car_count_picked_check', 'variable_refs': {'{{car_count_picked_check}}': '1 of 1 cars picked', '{{carCount}}': '1'}}], 'sub_checks': [{'description': 'The status under the 3x3 photo grid shows all of the stored {{carCount}} picked.', 'store_key': 'car_count_picked_check', 'expected_value': '1 of 1 cars picked', 'extracted_value': '{{car_count_picked_check}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': 'Verify the status shows all of the stored {{carCount}} picked.'})
    
    async with testmu.step('Clicking Next', instruction_id='d797e7b6-3a3a-4bfb-892b-5f427f28e168'):
        _loc_4 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Dragging the slider handle to 69', instruction_id='7d0bc9d2-f4d6-4d55-ba42-e188ba49166f'):
        element_0 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await testmu.fill(element_0, "69")
    
    async with testmu.step('Pressing arrow keys to move the slider to 69', instruction_id='74d42060-4e26-4125-93c9-c8cb3193fe2f'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('Home')
    
    async with testmu.step('Waiting for slider handle key presses to complete', instruction_id='3a0f3711-1163-4f39-bd39-b83761bac075'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Press PageUp', instruction_id='850358b3-2c21-44cd-8ae9-f648455277c8'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Adjusting slider handle to 69', instruction_id='86a5efef-bec2-445d-9223-cd677dde10cc'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('End')
    
    async with testmu.step('Pressing PageDown to set the slider to 69', instruction_id='021ac5ec-b709-4f16-b3c2-f769343919b2'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageDown')
    
    async with testmu.step('Pressing PageDown to set the slider to 69', instruction_id='4a516fa4-9ab0-4064-9d15-5c9b2690477d'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageDown')
    
    async with testmu.step('Pressing Page Down to move the slider handle to 69', instruction_id='cf60e540-2e02-4edb-a3a4-077ddada10d1'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageDown')
    
    async with testmu.step('Pressing left arrow to move the slider handle left', instruction_id='3a8bda57-a2f3-48ae-8cb5-37ac3eca68c7'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Clicking Next button', instruction_id='5ad02d0f-5e64-4268-8881-374d43fd66b1'):
        _loc_5 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Picking up the shaped piece below the picture', instruction_id='6cdb270e-36ff-49e7-9b61-99dbf3d59b5f'):
        _loc_6 = page.locator("internal:role=button[name=\"square piece with the missing\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Clicking the empty square hole in the picture to place it', instruction_id='303f6343-55ec-4dae-926f-d806c26c9271'):
        _loc_7 = page.locator("internal:role=button[name=\"Empty square hole in the\"i]")
        
        await _loc_7.click()
    
    async with testmu.step("Checking whether the 'Solved' text is present"):
        set_var('solved_text_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {8: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(8).textContent.includes('Solved'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Solved ✓ — the piece fits."i'], query="whether the 'Solved' text is present in the puzzle status message", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="The page shows 'Solved' text."))
    
    async with testmu.step('Assertion check', instruction_id='bb1a9ebe-014b-40d7-add2-96ba21eb30cd'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "The page shows 'Solved' text.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{solved_text_visible}}', 'store_key': 'solved_text_visible', 'variable_refs': {'{{solved_text_visible}}': 'true'}}], 'sub_checks': [{'description': "The page shows 'Solved' text.", 'store_key': 'solved_text_visible', 'expected_value': 'true', 'extracted_value': '{{solved_text_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "Verify the page shows 'Solved' text."})
    
    async with testmu.step('Clicking Next', instruction_id='fcc1b626-3b85-40cf-9153-fb4d5a066b08'):
        _loc_8 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_8.click()
    
    async with testmu.step('Typing AGENT7 into the exam input field', instruction_id='d9f11315-1244-4504-a2e8-f6d9fe7e5625'):
        element_1 = page.locator("internal:role=textbox[name=\"Type the characters shown\"i]")
        
        await testmu.fill(element_1, "AGENT7")
    
    async with testmu.step('Checking whether the Challenge 1 success message is present'):
        set_var('challenge_1_passed_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(5).textContent.trim() === 'Challenge 1 passed.');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Challenge 1 passed."i'], query="whether the paragraph in the page content displays the text 'Challenge 1 passed.'", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="The page shows 'Challenge 1 passed.'"))
    
    async with testmu.step('Assertion check', instruction_id='f8182ffb-c302-4077-9327-e782b56c3f96'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "The page shows 'Challenge 1 passed.'", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_1_passed_visible}}', 'store_key': 'challenge_1_passed_visible', 'variable_refs': {'{{challenge_1_passed_visible}}': 'true'}}], 'sub_checks': [{'description': "The page shows 'Challenge 1 passed.'", 'store_key': 'challenge_1_passed_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_1_passed_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "Verify the page shows 'Challenge 1 passed.'"})


if __name__ == "__main__":
    testmu.run(test)
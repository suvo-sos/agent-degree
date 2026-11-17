import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="3859a223-c65f-4253-95e9-7d7bff8bfcaf",
    name="Complete Challenge 1 of AgentDegree Exam",
    tc_id="TC-34",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"challenge_1_visible": "true", "back_button_top_left": "true", "pagination_steps_1_to_5_bottom": "true", "challenge_1_passed_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-1', instruction_id='81355832-2f30-47c1-8213-75bb66d3fe46'):
        await page.goto("http://localhost:3000/gauntlet/step-1")
    
    async with testmu.step('Checking whether the Challenge 1 heading is present'):
        set_var('challenge_1_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(5).textContent.trim() === 'Challenge 1' && !!(el(5).getClientRects().length && getComputedStyle(el(5)).visibility !== 'hidden' && getComputedStyle(el(5)).display !== 'none'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="Challenge"i]'], query='whether the Challenge 1 heading in the main page content is present', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Challenge 1'))
    
    async with testmu.step('Checking whether the top-left Back button is present'):
        set_var('back_button_top_left', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {3: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(3).textContent.includes('Back') && (()=>{const r=el(3).getBoundingClientRect(); return r.top < 100 && r.left < 700 && !!(r.width && r.height)})());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="← Back"i]'], query='whether the Back button at the upper-left edge of the main content is present', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='a Back button is at the top left'))
    
    async with testmu.step('Checking whether bottom pagination steps 1 through 5 are present'):
        set_var('pagination_steps_1_to_5_bottom', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((()=>{const texts=Array.from(el(13).querySelectorAll('button,a')).map(x=>x.textContent.trim()); const r=el(13).getBoundingClientRect(); return ['1','2','3','4','5'].every(x=>texts.includes(x)) && r.bottom > 600 && !!(r.width && r.height)})());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=navigation[name="pagination"i]'], query='whether the bottom pagination navigation contains steps 1 through 5', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='pagination with steps 1 to 5 is at the bottom'))
    
    async with testmu.step('Assertion check', instruction_id='54ea421b-731b-417e-9ba7-d891acb78ac9'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Challenge 1', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_1_visible}}', 'store_key': 'challenge_1_visible', 'variable_refs': {'{{challenge_1_visible}}': 'true'}}, {'description': 'a Back button is at the top left', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{back_button_top_left}}', 'store_key': 'back_button_top_left', 'variable_refs': {'{{back_button_top_left}}': 'true'}}, {'description': 'pagination with steps 1 to 5 is at the bottom', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{pagination_steps_1_to_5_bottom}}', 'store_key': 'pagination_steps_1_to_5_bottom', 'variable_refs': {'{{pagination_steps_1_to_5_bottom}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Challenge 1', 'store_key': 'challenge_1_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_1_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'a Back button is at the top left', 'store_key': 'back_button_top_left', 'expected_value': 'true', 'extracted_value': '{{back_button_top_left}}', 'operator': 'equals', 'transforms': []}, {'description': 'pagination with steps 1 to 5 is at the bottom', 'store_key': 'pagination_steps_1_to_5_bottom', 'expected_value': 'true', 'extracted_value': '{{pagination_steps_1_to_5_bottom}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Challenge 1 and a Back button at the top left and pagination with steps 1 to 5 at the bottom'})
    
    async with testmu.step('Waiting for the queued plan steps to run', instruction_id='95d5c7d7-eb89-4e76-bdd5-f2b65af543e1'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "I am agent"', instruction_id='d2dbcd70-c05a-4b65-9e0f-beffbdf81b7f'):
        _loc_1 = page.locator("internal:role=checkbox[name=\"I am agent\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Click "Next →"', instruction_id='c99ad108-1110-42a6-a0fc-535ae10161b6'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Selecting all images with a car in the red car photo tile', instruction_id='524176eb-b80e-4897-b5d0-4b4c5d69eb20'):
        _loc_3 = page.locator("internal:role=button[name=\"Photo tile 2\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Waiting for the queued photo selection steps to complete', instruction_id='75ed5a06-5a2a-46a4-b261-d6f8aebb3ba8'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "Photo tile 4"', instruction_id='af8ff9d3-54b5-4638-a029-50baa57cd9f1'):
        _loc_4 = page.locator("internal:role=button[name=\"Photo tile 4\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Click "Photo tile 7"', instruction_id='75b7d555-377c-4455-bd4a-b17d9614547e'):
        _loc_5 = page.locator("internal:role=button[name=\"Photo tile 7\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Click "Next →"', instruction_id='d24b7a52-852f-4083-a677-760e56ae0888'):
        _loc_6 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Dragging the slider handle into the green zone at 75', instruction_id='e4ead859-9b70-4d30-8c21-90ffe57cc2d9'):
        element_0 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await testmu.fill(element_0, "75")
    
    async with testmu.step('Pressing the Home key to move the slider handle to the minimum', instruction_id='bea9d3b3-7759-43a1-9ffb-f5543153b129'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('Home')
    
    async with testmu.step('Waiting for the queued steps to execute', instruction_id='4088eea6-2aef-497e-b4b2-2c78b63ff923'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Press ArrowRight', instruction_id='9e256f51-f220-4ee4-a644-38d160d1affc'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='a4ede6a4-3322-472e-81d2-f3c253c1106d'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='895dc2a3-54c2-43c6-a3dd-cdb0823c7890'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='e3d5f428-b994-40f0-ac1a-71df7d15756e'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='cffec8b6-e5bc-4ea5-a745-d238384c2e69'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='3fbffee5-8af7-400e-b2af-9ec37345a6f5'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='216674a1-c543-485a-aa45-a59d128032c1'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='ec0dbb03-c72b-44f8-b992-6d21e477d100'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Waiting for slider handle key presses to complete', instruction_id='da3d38a5-1ed8-4ab7-8013-c3c32131eb0f'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Press PageUp', instruction_id='f2a18295-9b69-4e10-a30a-a1aaedd49de8'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='8e972ed9-e6e8-49e8-9313-fe1cb10993fc'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='cdac1ece-f926-4f4d-9391-90088c801420'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='6ef9db19-6781-49ae-a060-bae2fb483f29'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='7c1ef324-9ecc-452e-b43b-4641c597fc7a'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='3807b324-786c-4830-a85d-2ae017356c0f'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='2bef97c2-d3f2-4772-8e2d-cd3e7135058b'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Clicking Next', instruction_id='06575df0-8670-4199-828b-c5a5ad6f06b7'):
        _loc_7 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('PRIMARY: Place the cube into the empty part of the picture; role=button | HINTS: cube is directly below the large landscape picture in the Challenge 1 panel', instruction_id='4c350527-c82f-4890-beec-16458627330c'):
        coords = await testmu.get_vision_coordinates(page, 'PRIMARY: Place the cube into the empty part of the picture; role=button | HINTS: cube is directly below the large landscape picture in the Challenge 1 panel', "click", 950, 930)
        await page.mouse.click(coords['x'], coords['y'])
        
    
    async with testmu.step('Placing the cube into the empty part of the picture', instruction_id='80f8b572-0d7b-4ece-a453-8665b215e6af'):
        _loc_8 = page.locator("internal:role=button[name=\"Empty part of the picture\"i]")
        
        await _loc_8.click()
    
    async with testmu.step('Clicking Next', instruction_id='d4cc4160-a29a-495f-b3b6-afadb84a7a08'):
        _loc_9 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_9.click()
    
    async with testmu.step('Typing distorted characters into the text box', instruction_id='aa7244b1-7e77-4aca-ab5c-769d7705b1da'):
        element_1 = page.locator("internal:role=textbox[name=\"Type the characters shown\"i]")
        
        await testmu.fill(element_1, "AGENT7")
    
    async with testmu.step('Checking whether the Challenge 1 passed message is present'):
        set_var('challenge_1_passed_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {8: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(8).textContent.trim() === 'Challenge 1 passed.' && !!(el(8).offsetWidth || el(8).offsetHeight || el(8).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Challenge 1 passed."i'], query='whether the Challenge 1 passed message is visible in the main page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Challenge 1 passed'))
    
    async with testmu.step('Assertion check', instruction_id='dd36f1db-81ee-4501-ba27-25e5e55faa82'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Challenge 1 passed', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_1_passed_visible}}', 'store_key': 'challenge_1_passed_visible', 'variable_refs': {'{{challenge_1_passed_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Challenge 1 passed', 'store_key': 'challenge_1_passed_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_1_passed_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Challenge 1 passed'})


if __name__ == "__main__":
    testmu.run(test)
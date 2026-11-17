import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="ee7889ca-fb62-4f21-8264-3bd775ab6929",
    name="Complete Challenge 3 of AgentDegree Exam",
    tc_id="TC-33",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"challenge_3_visible": "true", "back_button_top_left": "true", "pagination_steps_1_to_5_bottom": "true", "challenge_3_passed_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-3', instruction_id='748b9a3a-2b24-457c-ad58-a7c28639d0ec'):
        await page.goto("http://localhost:3000/gauntlet/step-3")
    
    async with testmu.step('Checking whether the Challenge 3 heading is present'):
        set_var('challenge_3_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(5).textContent.trim() === 'Challenge 3' && !!(el(5).getBoundingClientRect().width && el(5).getBoundingClientRect().height));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="Challenge"i]'], query='whether the Challenge 3 heading is present in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Challenge 3'))
    
    async with testmu.step('Checking whether the top-left Back button is present'):
        set_var('back_button_top_left', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {3: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(3).textContent.includes('Back') && el(3).getBoundingClientRect().top < window.innerHeight / 4 && el(3).getBoundingClientRect().left < window.innerWidth / 2);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="← Back"i]'], query='whether the Back button is present at the top left of the page', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='a Back button is at the top left'))
    
    async with testmu.step('Checking whether bottom pagination steps 1 through 5 are present'):
        set_var('pagination_steps_1_to_5_bottom', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0, 17: 1, 19: 2, 21: 3, 23: 4, 25: 5};\n  const el = (i) => els[__m[i]];\n  const __v = (el(12).getAttribute('aria-label') === 'pagination' && ['1','2','3','4','5'].every((label,i) => [el(17),el(19),el(21),el(23),el(25)][i].textContent.trim() === label) && el(12).getBoundingClientRect().top > window.innerHeight / 2);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=navigation[name="pagination"i]', 'internal:role=button[name="1"i]', 'internal:role=button[name="2"i]', 'internal:role=button[name="3"i]', 'internal:role=button[name="4"i]', 'internal:role=button[name="5"i]'], query='whether pagination with steps 1 through 5 is present at the bottom of the page', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='pagination with steps 1 to 5 is at the bottom'))
    
    async with testmu.step('Assertion check', instruction_id='9a0b8408-b6e9-4c0e-bdc9-88c27eed44a0'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Challenge 3', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_3_visible}}', 'store_key': 'challenge_3_visible', 'variable_refs': {'{{challenge_3_visible}}': 'true'}}, {'description': 'a Back button is at the top left', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{back_button_top_left}}', 'store_key': 'back_button_top_left', 'variable_refs': {'{{back_button_top_left}}': 'true'}}, {'description': 'pagination with steps 1 to 5 is at the bottom', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{pagination_steps_1_to_5_bottom}}', 'store_key': 'pagination_steps_1_to_5_bottom', 'variable_refs': {'{{pagination_steps_1_to_5_bottom}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Challenge 3', 'store_key': 'challenge_3_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_3_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'a Back button is at the top left', 'store_key': 'back_button_top_left', 'expected_value': 'true', 'extracted_value': '{{back_button_top_left}}', 'operator': 'equals', 'transforms': []}, {'description': 'pagination with steps 1 to 5 is at the bottom', 'store_key': 'pagination_steps_1_to_5_bottom', 'expected_value': 'true', 'extracted_value': '{{pagination_steps_1_to_5_bottom}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Challenge 3 and a Back button at the top left and pagination with steps 1 to 5 at the bottom'})
    
    async with testmu.step('Clicking Open menu button', instruction_id='684bae81-dec4-45ba-8a14-4dd8cd4dc189'):
        _loc_1 = page.locator("internal:role=button[name=\"Open menu ↓\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Option 6 in the menu', instruction_id='eba2278f-9bf4-46bc-a0bb-7fa2643b088e'):
        _loc_2 = page.locator("internal:role=menuitem[name=\"Option 6\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Clicking Next', instruction_id='9826d1ab-65b1-43e3-bd02-a70ed6b4c7c1'):
        _loc_3 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Waiting for queued plan steps to start', instruction_id='3e91f94b-8542-4089-ac99-aead19e56892'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "75" into "Progress value"', instruction_id='ca937674-8919-4024-b29f-a69f808360cc'):
        element_0 = page.locator("internal:role=spinbutton[name=\"Progress value\"i]")
        
        await testmu.fill(element_0, "75")
    
    async with testmu.step('Click "Set"', instruction_id='c648c6d8-5498-47d6-a114-b136c7497859'):
        _loc_4 = page.locator("internal:role=button[name=\"Set\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Clicking Next', instruction_id='1d3eda26-91fd-4bf7-9800-9d7fee733c99'):
        _loc_5 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Picking colour #885566 in the colour picker grid', instruction_id='6fe94804-de50-459a-82d2-7026eccddab9'):
        _loc_6 = page.locator("internal:role=button[name=\"Colour 6\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Clicking Next in the Challenge 3 task card', instruction_id='53b778a8-8165-4ca4-840b-ab4ab7d322a4'):
        _loc_7 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('Waiting for the planned steps to start', instruction_id='80dbaa10-58f8-4407-8d4c-51dc35b84e54'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "Notifications switch"', instruction_id='540fc217-d6cf-4b2f-96fa-cc562e837637'):
        _loc_8 = page.locator("internal:role=switch[name=\"Notifications switch\"i]")
        
        await _loc_8.click()
    
    async with testmu.step('Click "Next →"', instruction_id='cb3ee34e-c0b9-47e4-b62e-ee48163ffbe3'):
        _loc_9 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_9.click()
    
    async with testmu.step('Clicking the Settings tab', instruction_id='9c20f0b4-630e-49c6-8f44-55061e4737af'):
        _loc_10 = page.locator("internal:role=tab[name=\"Settings\"i]")
        
        await _loc_10.click()
    
    async with testmu.step('Clicking Next', instruction_id='71579cd4-b26f-41c8-9289-ffec746a3711'):
        _loc_11 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_11.click()
    
    async with testmu.step('Waiting for the queued plan steps to complete', instruction_id='b8bb6c1f-76f4-4d17-831c-510655ae6e31'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "Section 3 +"', instruction_id='3b3e0468-c379-4b54-8892-ca1bb362b8b2'):
        _loc_12 = page.locator("internal:role=button[name=\"Section 3 +\"i]")
        
        await _loc_12.click()
    
    async with testmu.step('Click "Next →"', instruction_id='27a34f63-a42f-41b2-b3c6-cddc0afe928f'):
        _loc_13 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_13.click()
    
    async with testmu.step('Clicking Give 4 stars button', instruction_id='ae3e92ca-384b-4719-8d7f-815ab39b756e'):
        _loc_14 = page.locator("internal:role=button[name=\"Rate 4 stars\"i]")
        
        await _loc_14.click()
    
    async with testmu.step('Clicking Next on the Challenge 3 card', instruction_id='8c40a479-340b-42d8-a6e1-336b881ee59f'):
        _loc_15 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_15.click()
    
    async with testmu.step('Typing bana in Search the fruits', instruction_id='3918d60b-c1f2-4383-9a62-7be6f006de45'):
        element_1 = page.locator("internal:role=textbox[name=\"Search the fruits\"i]")
        
        await testmu.fill(element_1, "bana")
    
    async with testmu.step('Waiting for the queued steps to start', instruction_id='76fdcd8a-9c64-40d1-9665-03bb4618c9eb'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "Banana"', instruction_id='ada54f87-4f99-49a4-94f9-552512818a9c'):
        _loc_16 = page.locator("internal:role=button[name=\"Banana\"i]")
        
        await _loc_16.click()
    
    async with testmu.step('Clicking Next button', instruction_id='d1774250-7379-47e6-b28c-967e4f073a9a'):
        _loc_17 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_17.click()
    
    async with testmu.step('Clicking the plus button until the counter shows 5', instruction_id='f20cbcd3-a25a-45aa-b7de-8f0ff50ad191'):
        _loc_18 = page.locator("internal:role=button[name=\"Increase counter\"i]")
        
        await _loc_18.click()
    
    async with testmu.step('Clicking the plus button until the counter shows 5', instruction_id='ce6ba5f9-89cd-4909-91a0-afbaec3d0387'):
        _loc_19 = page.locator("internal:role=button[name=\"Increase counter\"i]")
        
        await _loc_19.click()
    
    async with testmu.step('Clicking Next button', instruction_id='86605886-9ec8-4162-b621-26ac0061ea09'):
        _loc_20 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_20.click()
    
    async with testmu.step('Waiting for the queued clicks to complete', instruction_id='58eebd3b-3ab1-41d2-bad9-73fc432d9701'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "Apple"', instruction_id='3e94ab8f-d363-47ed-be55-f51b8337febf'):
        _loc_21 = page.locator("internal:role=checkbox[name=\"Apple\"i]")
        
        await _loc_21.click()
    
    async with testmu.step('Click "Mango"', instruction_id='30cd7273-932a-409f-b0b7-4c273e8872b1'):
        _loc_22 = page.locator("internal:role=checkbox[name=\"Mango\"i]")
        
        await _loc_22.click()
    
    async with testmu.step('Checking whether the Challenge 3 passed message is present'):
        set_var('challenge_3_passed_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {8: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(8).textContent.trim() === 'Challenge 3 passed.' && !!(el(8).offsetWidth || el(8).offsetHeight || el(8).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Challenge 3 passed."i'], query='whether the “Challenge 3 passed.” message is visible in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Challenge 3 passed'))
    
    async with testmu.step('Assertion check', instruction_id='ff3c43cd-4f09-4302-9771-4f9cbff28913'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Challenge 3 passed', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_3_passed_visible}}', 'store_key': 'challenge_3_passed_visible', 'variable_refs': {'{{challenge_3_passed_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Challenge 3 passed', 'store_key': 'challenge_3_passed_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_3_passed_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Challenge 3 passed'})


if __name__ == "__main__":
    testmu.run(test)
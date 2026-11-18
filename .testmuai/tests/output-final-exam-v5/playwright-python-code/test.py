import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="c4444690-2190-48b0-9414-1e37627370ac",
    name="Verify Challenge Cards and Start First Challenge",
    tc_id="TC-66",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"page_heading_check": "The Final Exam", "five_challenge_cards_side_by_side": "true", "i_am_agent_card_visible": "true", "paperwork_hell_card_visible": "true", "the_control_room_card_visible": "true", "prove_its_you_card_visible": "true", "homework_you_cant_skip_card_visible": "true", "challenge_1_of_5_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet', instruction_id='2991ab53-4479-43f5-b448-adc1662883a0'):
        await page.goto("http://localhost:3000/gauntlet")
    
    async with testmu.step('Reading the page heading'):
        set_var('page_heading_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {1: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(1).textContent.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="The Final Exam"i]'], query='the page heading text at the top of the page', expected_value='The Final Exam', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition="the page heading is 'The Final Exam'"))
    
    async with testmu.step('whether five challenge cards are visible side by side in the challenge row', instruction_id='423a559e-b91d-4ee5-958b-44e938be77a6'):
        set_var('five_challenge_cards_side_by_side', await testmu.vision_query(page, "whether five challenge cards are visible side by side in the challenge row", ""))
    
    async with testmu.step('whether the I Am Agent challenge card is visible in the challenge row', instruction_id='df6b6f6f-43d5-48a2-ab1d-41a8df728a0c'):
        set_var('i_am_agent_card_visible', await testmu.vision_query(page, "whether the I Am Agent challenge card is visible in the challenge row", ""))
    
    async with testmu.step('whether the Paperwork Hell challenge card is visible in the challenge row', instruction_id='33e42f7b-4330-42cf-93bf-ebc23ab51d23'):
        set_var('paperwork_hell_card_visible', await testmu.vision_query(page, "whether the Paperwork Hell challenge card is visible in the challenge row", ""))
    
    async with testmu.step('whether the The Control Room challenge card is visible in the challenge row', instruction_id='279ea090-89c4-482f-96ed-e5b470cd8481'):
        set_var('the_control_room_card_visible', await testmu.vision_query(page, "whether the The Control Room challenge card is visible in the challenge row", ""))
    
    async with testmu.step("whether the Prove It's You challenge card is visible in the challenge row", instruction_id='44f76ef6-45ab-4e85-892e-58cb8f5363e4'):
        set_var('prove_its_you_card_visible', await testmu.vision_query(page, "whether the Prove It's You challenge card is visible in the challenge row", ""))
    
    async with testmu.step("whether the Homework You Can't Skip challenge card is visible in the challenge row", instruction_id='35110153-8d7e-4059-9cb3-ef6a72efd48e'):
        set_var('homework_you_cant_skip_card_visible', await testmu.vision_query(page, "whether the Homework You Can't Skip challenge card is visible in the challenge row", ""))
    
    async with testmu.step('Assertion check', instruction_id='ee30832d-ed5b-41d5-bd70-a0c37cbaea75'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "the page heading is 'The Final Exam'", 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': 'The Final Exam', 'extracted_value': '{{page_heading_check}}', 'store_key': 'page_heading_check', 'variable_refs': {'{{page_heading_check}}': 'The Final Exam'}}, {'description': 'five challenge cards are shown side by side', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{five_challenge_cards_side_by_side}}', 'store_key': 'five_challenge_cards_side_by_side', 'variable_refs': {'{{five_challenge_cards_side_by_side}}': 'true'}}, {'description': "a challenge card named 'I Am Agent' is shown", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{i_am_agent_card_visible}}', 'store_key': 'i_am_agent_card_visible', 'variable_refs': {'{{i_am_agent_card_visible}}': 'true'}}, {'description': "a challenge card named 'Paperwork Hell' is shown", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{paperwork_hell_card_visible}}', 'store_key': 'paperwork_hell_card_visible', 'variable_refs': {'{{paperwork_hell_card_visible}}': 'true'}}, {'description': "a challenge card named 'The Control Room' is shown", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{the_control_room_card_visible}}', 'store_key': 'the_control_room_card_visible', 'variable_refs': {'{{the_control_room_card_visible}}': 'true'}}, {'description': "a challenge card named 'Prove It's You' is shown", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{prove_its_you_card_visible}}', 'store_key': 'prove_its_you_card_visible', 'variable_refs': {'{{prove_its_you_card_visible}}': 'true'}}, {'description': "a challenge card named 'Homework You Can't Skip' is shown", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{homework_you_cant_skip_card_visible}}', 'store_key': 'homework_you_cant_skip_card_visible', 'variable_refs': {'{{homework_you_cant_skip_card_visible}}': 'true'}}], 'sub_checks': [{'description': "the page heading is 'The Final Exam'", 'store_key': 'page_heading_check', 'expected_value': 'The Final Exam', 'extracted_value': '{{page_heading_check}}', 'operator': 'equals', 'transforms': ['strip']}, {'description': 'five challenge cards are shown side by side', 'store_key': 'five_challenge_cards_side_by_side', 'expected_value': 'true', 'extracted_value': '{{five_challenge_cards_side_by_side}}', 'operator': 'equals', 'transforms': []}, {'description': "a challenge card named 'I Am Agent' is shown", 'store_key': 'i_am_agent_card_visible', 'expected_value': 'true', 'extracted_value': '{{i_am_agent_card_visible}}', 'operator': 'equals', 'transforms': []}, {'description': "a challenge card named 'Paperwork Hell' is shown", 'store_key': 'paperwork_hell_card_visible', 'expected_value': 'true', 'extracted_value': '{{paperwork_hell_card_visible}}', 'operator': 'equals', 'transforms': []}, {'description': "a challenge card named 'The Control Room' is shown", 'store_key': 'the_control_room_card_visible', 'expected_value': 'true', 'extracted_value': '{{the_control_room_card_visible}}', 'operator': 'equals', 'transforms': []}, {'description': "a challenge card named 'Prove It's You' is shown", 'store_key': 'prove_its_you_card_visible', 'expected_value': 'true', 'extracted_value': '{{prove_its_you_card_visible}}', 'operator': 'equals', 'transforms': []}, {'description': "a challenge card named 'Homework You Can't Skip' is shown", 'store_key': 'homework_you_cant_skip_card_visible', 'expected_value': 'true', 'extracted_value': '{{homework_you_cant_skip_card_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "the page heading is 'The Final Exam' and it shows five challenge cards side by side named 'I Am Agent', 'Paperwork Hell', 'The Control Room', 'Prove It's You' and 'Homework You Can't Skip'"})
    
    async with testmu.step('Clicking the Start button below the first card', instruction_id='8e7bb074-cf40-4973-852f-c047d13f096d'):
        _loc_1 = page.locator("internal:role=link[name=\"Start →\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Checking whether the Challenge 1 of 5 text is present'):
        set_var('challenge_1_of_5_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {4: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(4).textContent.trim().toLowerCase() === 'challenge 1 of 5');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="CHALLENGE 1 OF"i'], query="whether the text 'Challenge 1 of 5' is present in the challenge header area", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="the page shows 'Challenge 1 of 5'"))
    
    async with testmu.step('Assertion check', instruction_id='218021a5-a1d1-438b-8d2e-8e4f46ac16a3'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "the page shows 'Challenge 1 of 5'", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_1_of_5_visible}}', 'store_key': 'challenge_1_of_5_visible', 'variable_refs': {'{{challenge_1_of_5_visible}}': 'true'}}], 'sub_checks': [{'description': "the page shows 'Challenge 1 of 5'", 'store_key': 'challenge_1_of_5_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_1_of_5_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "the page shows 'Challenge 1 of 5'"})


if __name__ == "__main__":
    testmu.run(test)
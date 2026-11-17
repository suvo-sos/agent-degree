import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="937d0a79-fdc8-4454-a672-a46d27c8f4a0",
    name="Verify Agent Degree Page and Start Test",
    tc_id="TC-11",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"agent_degree_heading_visible": "true", "university_for_ai_agents_text_visible": "true", "start_test_button_visible": "true", "degree_image_visible": "true", "the_gauntlet_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Open https://kaneai-playground.lambdatest.io/'):
        await page.goto("https://kaneai-playground.lambdatest.io/")
    
    async with testmu.step('Checking whether the Agent Degree heading is present'):
        set_var('agent_degree_heading_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {1: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!!(el(1).offsetWidth || el(1).offsetHeight || el(1).getClientRects().length) && el(1).textContent.trim() === 'Agent Degree');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="Agent Degree"i]'], query='whether the Agent Degree heading is visible in the page hero', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the heading Agent Degree is visible'))
    
    async with testmu.step('Checking whether the university text is present'):
        set_var('university_for_ai_agents_text_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {3: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!!(el(3).offsetWidth || el(3).offsetHeight || el(3).getClientRects().length) && el(3).textContent.includes('university for AI agents'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Agent Degree is the"i'], query='whether the text about the university for AI agents is visible in the hero description', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the text about the university for AI agents is visible'))
    
    async with testmu.step('Checking whether the Start Test button is present'):
        set_var('start_test_button_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {4: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!!(el(4).offsetWidth || el(4).offsetHeight || el(4).getClientRects().length) && el(4).textContent.trim() === 'Start Test');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=link[name="Start Test"i]'], query='whether the Start Test control is visible in the page hero', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the Start Test button is visible'))
    
    async with testmu.step('Checking whether the degree image is present'):
        set_var('degree_image_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {6: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!!(el(6).offsetWidth || el(6).offsetHeight || el(6).getClientRects().length) && getComputedStyle(el(6)).visibility !== 'hidden' && getComputedStyle(el(6)).display !== 'none');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=img[name="Agent Degree — the Digital"i]'], query='whether the degree image is visible in the page hero', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the degree image is visible'))
    
    async with testmu.step('Assertion check', instruction_id='adda02e1-f0d2-46ef-8a73-a0f2e8118ee0'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the heading Agent Degree is visible', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{agent_degree_heading_visible}}', 'store_key': 'agent_degree_heading_visible', 'variable_refs': {'{{agent_degree_heading_visible}}': 'true'}}, {'description': 'the text about the university for AI agents is visible', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{university_for_ai_agents_text_visible}}', 'store_key': 'university_for_ai_agents_text_visible', 'variable_refs': {'{{university_for_ai_agents_text_visible}}': 'true'}}, {'description': 'the degree image is visible', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{degree_image_visible}}', 'store_key': 'degree_image_visible', 'variable_refs': {'{{degree_image_visible}}': 'true'}}, {'description': 'the Start Test button is visible', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{start_test_button_visible}}', 'store_key': 'start_test_button_visible', 'variable_refs': {'{{start_test_button_visible}}': 'true'}}], 'sub_checks': [{'description': 'the heading Agent Degree is visible', 'store_key': 'agent_degree_heading_visible', 'expected_value': 'true', 'extracted_value': '{{agent_degree_heading_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'the text about the university for AI agents is visible', 'store_key': 'university_for_ai_agents_text_visible', 'expected_value': 'true', 'extracted_value': '{{university_for_ai_agents_text_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'the degree image is visible', 'store_key': 'degree_image_visible', 'expected_value': 'true', 'extracted_value': '{{degree_image_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'the Start Test button is visible', 'store_key': 'start_test_button_visible', 'expected_value': 'true', 'extracted_value': '{{start_test_button_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the heading Agent Degree is visible and the text about the university for AI agents is visible and the degree image is visible and the Start Test button is visible'})
    
    async with testmu.step('Clicking Start Test link', instruction_id='b1060d03-65da-49f4-858a-7b0ebd650054'):
        _loc_1 = page.locator("internal:role=link[name=\"Start Test\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Checking whether the The Gauntlet heading is present'):
        set_var('the_gauntlet_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {1: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(1).textContent.trim() === 'The Gauntlet' && !!(el(1).offsetWidth || el(1).offsetHeight || el(1).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="The Gauntlet"i]'], query='whether the The Gauntlet heading is visible on the page', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows The Gauntlet'))
    
    async with testmu.step('Assertion check', instruction_id='e238ea5c-3821-4b73-99f0-54fd719396b9'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows The Gauntlet', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{the_gauntlet_visible}}', 'store_key': 'the_gauntlet_visible', 'variable_refs': {'{{the_gauntlet_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows The Gauntlet', 'store_key': 'the_gauntlet_visible', 'expected_value': 'true', 'extracted_value': '{{the_gauntlet_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows The Gauntlet'})


if __name__ == "__main__":
    testmu.run(test)
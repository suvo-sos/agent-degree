import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="d3515358-1a9b-4708-99d6-440fb571bbf2",
    name="Start and Verify The Gauntlet Test",
    tc_id="TC-10",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"agentdegree_heading_visible": "true", "start_test_button_visible": "true", "the_gauntlet_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000', instruction_id='1f770642-c733-479e-9b16-1eac1563d483'):
        await page.goto("http://localhost:3000")
    
    async with testmu.step('Checking whether the AgentDegree heading is present'):
        set_var('agentdegree_heading_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {1: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(1).textContent.trim() === 'AgentDegree' && !!(el(1).offsetWidth || el(1).offsetHeight || el(1).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="AgentDegree"i]'], query='whether the AgentDegree heading is present and visible at the top of the page', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the heading AgentDegree is visible'))
    
    async with testmu.step('Checking whether the Start Test button is present'):
        set_var('start_test_button_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {3: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(3).textContent.trim() === 'Start Test' && !!(el(3).offsetWidth || el(3).offsetHeight || el(3).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=link[name="Start Test"i]'], query='whether the Start Test button is present and visible in the main page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the Start Test button is visible'))
    
    async with testmu.step('Assertion check', instruction_id='9d9ac00d-70b3-41e2-927d-7c9de53d383c'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the heading AgentDegree is visible', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{agentdegree_heading_visible}}', 'store_key': 'agentdegree_heading_visible', 'variable_refs': {'{{agentdegree_heading_visible}}': 'true'}}, {'description': 'the Start Test button is visible', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{start_test_button_visible}}', 'store_key': 'start_test_button_visible', 'variable_refs': {'{{start_test_button_visible}}': 'true'}}], 'sub_checks': [{'description': 'the heading AgentDegree is visible', 'store_key': 'agentdegree_heading_visible', 'expected_value': 'true', 'extracted_value': '{{agentdegree_heading_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'the Start Test button is visible', 'store_key': 'start_test_button_visible', 'expected_value': 'true', 'extracted_value': '{{start_test_button_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the heading AgentDegree is visible and the Start Test button is visible'})
    
    async with testmu.step('Clicking Start Test in the main page below AgentDegree heading', instruction_id='fadab0f4-a2b2-42ff-a2cd-5b70a0dab84f'):
        _loc_1 = page.locator("internal:role=link[name=\"Start Test\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Checking whether the The Gauntlet heading is present'):
        set_var('the_gauntlet_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {1: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(1).textContent.trim() === 'The Gauntlet' && !!(el(1).offsetWidth || el(1).offsetHeight || el(1).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="The Gauntlet"i]'], query='whether the The Gauntlet heading is visible in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows The Gauntlet'))
    
    async with testmu.step('Assertion check', instruction_id='57fd9a7a-60ce-4563-a8f6-f59bf13a4756'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows The Gauntlet', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{the_gauntlet_visible}}', 'store_key': 'the_gauntlet_visible', 'variable_refs': {'{{the_gauntlet_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows The Gauntlet', 'store_key': 'the_gauntlet_visible', 'expected_value': 'true', 'extracted_value': '{{the_gauntlet_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows The Gauntlet'})


if __name__ == "__main__":
    testmu.run(test)
import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="0639c697-a62a-4924-a9db-2ddef18725e6",
    name="Complete Challenge 4 Login Test",
    tc_id="TC-35",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"challenge_4_visible": "true", "log_in_test_visible": "true", "logged_in_as_agentdegree": "true", "next_button_enabled": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-4', instruction_id='f01b8ba1-72fa-465a-8c80-29967e9613a6'):
        await page.goto("http://localhost:3000/gauntlet/step-4")
    
    async with testmu.step('Checking whether the Challenge 4 heading is present'):
        set_var('challenge_4_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(5).textContent.trim() === 'Challenge 4' && !!(el(5).offsetWidth || el(5).offsetHeight || el(5).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="Challenge"i]'], query='whether the Challenge 4 heading is present and visible in the page header', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Challenge 4'))
    
    async with testmu.step('Checking whether the Log In test is present'):
        set_var('log_in_test_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {8: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(8).textContent.trim().startsWith('Log in to continue.') && !!(el(8).offsetWidth || el(8).offsetHeight || el(8).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Log in to continue. Use the"i'], query='whether the Log In test content is present and visible in the test panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows a Log In test'))
    
    async with testmu.step('Assertion check', instruction_id='ef7a1772-be6f-466f-86b5-3bdff03503c6'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Challenge 4', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_4_visible}}', 'store_key': 'challenge_4_visible', 'variable_refs': {'{{challenge_4_visible}}': 'true'}}, {'description': 'the page shows a Log In test', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{log_in_test_visible}}', 'store_key': 'log_in_test_visible', 'variable_refs': {'{{log_in_test_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Challenge 4', 'store_key': 'challenge_4_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_4_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'the page shows a Log In test', 'store_key': 'log_in_test_visible', 'expected_value': 'true', 'extracted_value': '{{log_in_test_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Challenge 4 and a Log In test'})
    
    async with testmu.step('Waiting for the next step to be entered', instruction_id='26243b67-d68f-43f7-a1f9-24d6abd857c4'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "agent@agentdegree.app" into "Email"', instruction_id='1c85c0af-c8be-4a9c-a74e-1cc919dfbe26'):
        element_0 = page.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_0, "agent@agentdegree.app")
    
    async with testmu.step('Type "agent123" into "Password"', instruction_id='2599fcb6-13a1-480d-a0ae-3b86fc023803'):
        element_1 = page.locator("internal:role=textbox[name=\"Password\"i]")
        
        await testmu.fill(element_1, "agent123")
    
    async with testmu.step('Click "Log in"', instruction_id='0580ef5b-dc99-4949-8406-b579bfdc6e7b'):
        _loc_1 = page.locator("internal:role=button[name=\"Log in\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Checking whether the login confirmation is present'):
        set_var('logged_in_as_agentdegree', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(12).innerText.includes('Logged in as agent@agentdegree.app'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Logged in as agent@"i'], query='whether the Logged in as agent@agentdegree.app confirmation is present in the login test panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Logged in as agent@agentdegree.app'))
    
    async with testmu.step('Checking whether the Next button is enabled'):
        set_var('next_button_enabled', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {14: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(14).matches(':enabled'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="Next →"i]'], query='whether the Next button in the challenge navigation is enabled', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the Next button is enabled'))
    
    async with testmu.step('Assertion check', instruction_id='5cfbf526-de3a-404d-b5d7-d6c053853dec'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Logged in as agent@agentdegree.app', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{logged_in_as_agentdegree}}', 'store_key': 'logged_in_as_agentdegree', 'variable_refs': {'{{logged_in_as_agentdegree}}': 'true'}}, {'description': 'the Next button is enabled', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{next_button_enabled}}', 'store_key': 'next_button_enabled', 'variable_refs': {'{{next_button_enabled}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Logged in as agent@agentdegree.app', 'store_key': 'logged_in_as_agentdegree', 'expected_value': 'true', 'extracted_value': '{{logged_in_as_agentdegree}}', 'operator': 'equals', 'transforms': []}, {'description': 'the Next button is enabled', 'store_key': 'next_button_enabled', 'expected_value': 'true', 'extracted_value': '{{next_button_enabled}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Logged in as agent@agentdegree.app and the Next button is enabled'})


if __name__ == "__main__":
    testmu.run(test)
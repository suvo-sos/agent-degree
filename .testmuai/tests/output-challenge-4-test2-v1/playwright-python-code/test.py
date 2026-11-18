import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="0de0d731-143b-4c31-8093-77e9cd77b83c",
    name="Complete Email Verification Challenge",
    tc_id="TC-36",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"verification_code": "553005", "email_verified_visible": "true", "tests_solved_2_of_5_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-4', instruction_id='c011f6ef-b18f-4b4c-8ec6-9782c57daa4d'):
        await page.goto("http://localhost:3000/gauntlet/step-4")
    
    async with testmu.step('Waiting for the email and password to be entered and login to start', instruction_id='b07e606e-4af9-4f97-9e28-d749a2978911'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "agent@agentdegree.app" into "Email"', instruction_id='73f11965-a4d2-4ec3-b0e0-e28f348549b3'):
        element_0 = page.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_0, "agent@agentdegree.app")
    
    async with testmu.step('Type "agent123" into "Password"', instruction_id='1a204bc7-383b-4aee-aec6-bd584d075292'):
        element_1 = page.locator("internal:role=textbox[name=\"Password\"i]")
        
        await testmu.fill(element_1, "agent123")
    
    async with testmu.step('Click "Log in"', instruction_id='4ebcc807-339f-42b4-8c2b-0c1e8a7defd7'):
        _loc_1 = page.locator("internal:role=button[name=\"Log in\"i]")
        
        await _loc_1.click()
    
    async with testmu.step("Waiting for Challenge 4 (Prove It's You) to finish loading", instruction_id='c918dbb4-a582-48ec-ae21-5ab12fd7ae40'):
        await page.wait_for_timeout(500)
    
    async with testmu.step('Waiting for login confirmation', instruction_id='f5f05d1b-ab0e-4bfc-b7b0-ebc504152d96'):
        await page.wait_for_timeout(500)
    
    async with testmu.step('Clicking Next', instruction_id='cb137a85-4e0e-43b0-a604-bce9f90b942b'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Waiting for the queued steps to finish', instruction_id='fda131c1-6018-4228-a4b2-fc73b0d8cd61'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "agent@agentdegree.app" into "Email"', instruction_id='ec22e4ca-1811-4e56-9221-8226caa33e4a'):
        element_2 = page.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_2, "agent@agentdegree.app")
    
    async with testmu.step('Click "Send code"', instruction_id='c4c2d013-60cc-4951-bead-afa415f0d0c8'):
        _loc_3 = page.locator("internal:role=button[name=\"Send code\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Clicking the email in the Your inbox section', instruction_id='c4b4d0cc-c897-424d-9973-9877140d2c34'):
        _loc_4 = page.locator("internal:role=button[name=\"AgentDegree — Your\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Extracting the verification code from the inbox email'):
        set_var('verification_code', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(13).textContent.match(/\\b\\d{6}\\b/)?.[0] ?? null);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Your AgentDegree verification"i'], query='the 6-digit verification code in the email body within the Your inbox section', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition="the 6-digit verification code from the email in the 'Your inbox' section is saved as {{verification_code}}"))
    
    async with testmu.step('Waiting for the verification code to be processed', instruction_id='5205ab78-d7f5-4d25-a7ca-546c41604bd1'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "{{verification_code}}" into "Verification code"', instruction_id='3deb9899-71f6-401c-9541-6de92b613c17'):
        element_3 = page.locator("internal:role=textbox[name=\"Verification code\"i]")
        variable_value_4 = var('{{verification_code}}')
        
        await testmu.fill(element_3, variable_value_4)
    
    async with testmu.step('Click "Verify code"', instruction_id='9850ac2f-3fde-4160-869f-ab57cf8ffb5d'):
        _loc_5 = page.locator("internal:role=button[name=\"Verify code\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Checking whether the email verification message is present'):
        set_var('email_verified_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(9).textContent.includes('Email verified'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Email verified ✓"i'], query="whether the text 'Email verified' is present in the verification message paragraph", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="the page shows 'Email verified'"))
    
    async with testmu.step('whether the Tests solved progress display shows 2 of 5 in the challenge progress section', instruction_id='b10abe17-a69e-4c48-81ed-4a8c4e4c73b3'):
        set_var('tests_solved_2_of_5_visible', await testmu.vision_query(page, "whether the Tests solved progress display shows 2 of 5 in the challenge progress section", ""))
    
    async with testmu.step('Assertion check', instruction_id='1e06f522-8282-416a-b5ea-07515fa1d619'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "the page shows 'Email verified'", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{email_verified_visible}}', 'store_key': 'email_verified_visible', 'variable_refs': {'{{email_verified_visible}}': 'true'}}, {'description': "the page shows 'Tests solved 2 of 5'", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{tests_solved_2_of_5_visible}}', 'store_key': 'tests_solved_2_of_5_visible', 'variable_refs': {'{{tests_solved_2_of_5_visible}}': 'true'}}], 'sub_checks': [{'description': "the page shows 'Email verified'", 'store_key': 'email_verified_visible', 'expected_value': 'true', 'extracted_value': '{{email_verified_visible}}', 'operator': 'equals', 'transforms': []}, {'description': "the page shows 'Tests solved 2 of 5'", 'store_key': 'tests_solved_2_of_5_visible', 'expected_value': 'true', 'extracted_value': '{{tests_solved_2_of_5_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "the page shows 'Email verified' and 'Tests solved 2 of 5'"})


if __name__ == "__main__":
    testmu.run(test)
import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="149a4f09-f769-4521-95f8-ff411c6b6526",
    name="Complete Agent Degree Step 4 Tests",
    tc_id="TC-42",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"voicemail_audio_audible": "false", "challenge_finished_shown": "true", "skipped_test_count": "1"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-4', instruction_id='45f8299b-d0f6-400c-9fca-f45c9e50435e'):
        await page.goto("http://localhost:3000/gauntlet/step-4")
    
    async with testmu.step('Waiting while filling out the login form', instruction_id='8ed40687-9f30-4cf3-89e4-3db2f28a0265'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "agent@agentdegree.app" into "Email"', instruction_id='b0fcbb2a-39c7-47ea-be91-2b397f9f6fdd'):
        element_0 = page.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_0, "agent@agentdegree.app")
    
    async with testmu.step('Type "agent123" into "Password"', instruction_id='6b50d472-be57-4527-95df-967391815c38'):
        element_1 = page.locator("internal:role=textbox[name=\"Password\"i]")
        
        await testmu.fill(element_1, "agent123")
    
    async with testmu.step('Click "Log in"', instruction_id='daa3594a-276a-4b30-b242-c5a9d46b172b'):
        _loc_1 = page.locator("internal:role=button[name=\"Log in\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Next to log in with the demo account shown on the page', instruction_id='9c8fb387-5e35-4d44-9978-c5dfb0faed14'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Waiting for the email code send option to become available', instruction_id='00b79559-fc38-4d1a-a039-5b5f8aea20c5'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "agent@agentdegree.app" into "Email"', instruction_id='7236ddc4-b29a-4885-a09a-52fc0f7bfe38'):
        element_2 = page.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_2, "agent@agentdegree.app")
    
    async with testmu.step('Click "Send code"', instruction_id='4da53201-448f-4eca-b6de-53c065bb3748'):
        _loc_3 = page.locator("internal:role=button[name=\"Send code\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Clicking the email with your AgentDegree verification code', instruction_id='2b1f0438-26ce-4889-90c8-828824a98701'):
        _loc_4 = page.locator("internal:role=button[name=\"AgentDegree — Your\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Waiting for the verification code to be entered', instruction_id='43f02e67-4282-443c-b1c5-57adec23f847'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "126344" into "Verification code"', instruction_id='1e488b28-c160-4236-9f76-a1174d01d5e3'):
        element_3 = page.locator("internal:role=textbox[name=\"Verification code\"i]")
        
        await testmu.fill(element_3, "126344")
    
    async with testmu.step('Click "Verify code"', instruction_id='c89ca138-af7c-40b7-9c4f-4d9b55b0c25c'):
        _loc_5 = page.locator("internal:role=button[name=\"Verify code\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Clicking Next to verify your email using the inbox code', instruction_id='0f1771ff-bf93-4093-98c2-c79df39e66f5'):
        _loc_6 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Clicking Play voicemail', instruction_id='717faaae-5b69-4db0-a984-bcefb3b26f87'):
        _loc_7 = page.locator("internal:role=button[name=\"Play voicemail\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('Checking whether voicemail audio is audible'):
        set_var('voicemail_audio_audible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/pause/i.test(el(9).textContent));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="Play voicemail"i]'], query='whether audio from the voicemail is audible as indicated by the voicemail playback control', expected_value='false', needs_unit_conversion=False, operator='equals', transforms=[], condition='Any audio can be heard from the voicemail.'))
    if await testmu.evaluate_branch(sub_checks=[{'description': 'Any audio can be heard from the voicemail.', 'store_key': 'voicemail_audio_audible', 'expected_value': 'false', 'stored_value': '{{voicemail_audio_audible}}', 'extracted_value': '{{voicemail_audio_audible}}', 'operator': 'equals', 'transforms': []}], composite_operator="and"):
        async with testmu.step('Clicking Skip this test button', instruction_id='8c5a77e1-9acd-45f0-988b-2f792d7dbb10'):
            _loc_8 = page.locator("internal:role=button[name=\"Skip this test →\"i]")
            
            await _loc_8.click()
    
    async with testmu.step('Checking whether the challenge finished message is present'):
        set_var('challenge_finished_shown', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {8: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/Challenge\\s+4\\s+finished/i.test(el(8).textContent||''));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Challenge 4 finished — 1 test"i'], query='whether the challenge finished message is shown in the completion notice', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows the challenge finished'))
    
    async with testmu.step('Reading the skipped test count from the completion notice'):
        set_var('skipped_test_count', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {8: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (((el(8).textContent||'').match(/(\\d+)\\s+test\\s+skipped/i)||[])[1]||null);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Challenge 4 finished — 1 test"i'], query='the skipped test count in the challenge completion notice', expected_value='1', needs_unit_conversion=False, operator='equals', transforms=['string_to_float'], condition='the page shows 1 test skipped'))
    
    async with testmu.step('Assertion check', instruction_id='cd98bfa8-e431-4f0f-8379-9db0d0ccc993'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows the challenge finished', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_finished_shown}}', 'store_key': 'challenge_finished_shown', 'variable_refs': {'{{challenge_finished_shown}}': 'true'}}, {'description': 'the page shows 1 test skipped', 'passed': True, 'operator': 'equals', 'transforms': ['string_to_float'], 'json_path': None, 'expected': '1', 'extracted_value': '{{skipped_test_count}}', 'store_key': 'skipped_test_count', 'variable_refs': {'{{skipped_test_count}}': '1'}}], 'sub_checks': [{'description': 'the page shows the challenge finished', 'store_key': 'challenge_finished_shown', 'expected_value': 'true', 'extracted_value': '{{challenge_finished_shown}}', 'operator': 'equals', 'transforms': []}, {'description': 'the page shows 1 test skipped', 'store_key': 'skipped_test_count', 'expected_value': '1', 'extracted_value': '{{skipped_test_count}}', 'operator': 'equals', 'transforms': ['string_to_float']}], 'composite_operator': 'and', 'claim': 'the page shows the challenge finished with 1 test skipped'})


if __name__ == "__main__":
    testmu.run(test)
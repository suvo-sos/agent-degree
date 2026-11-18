import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="a4d09191-9718-4e5d-b572-3d0b6c969f77",
    name="Complete AI Agent Verification Tests",
    tc_id="TC-38",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"verification_code": "624852", "voicemail_audio_audible": "false", "fourth_test_appears": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-4', instruction_id='1dffd5df-39a2-4a1f-aafc-35c533379fca'):
        await page.goto("http://localhost:3000/gauntlet/step-4")
    
    async with testmu.step('Waiting for the email field to be filled and the login to proceed', instruction_id='e05b8d34-9750-4b59-a950-2c5c24f4b170'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "agent@agentdegree.app" into "Email"', instruction_id='bace6802-8c92-4afe-9203-43e3cc0e7d42'):
        element_0 = page.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_0, "agent@agentdegree.app")
    
    async with testmu.step('Type "agent123" into "Password"', instruction_id='f70b26cd-9797-4e90-8527-7eb425ce1aea'):
        element_1 = page.locator("internal:role=textbox[name=\"Password\"i]")
        
        await testmu.fill(element_1, "agent123")
    
    async with testmu.step('Click "Log in"', instruction_id='b3779b28-a6fb-4d63-a8ad-eebe286e8b5d'):
        _loc_1 = page.locator("internal:role=button[name=\"Log in\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Waiting for successful login confirmation before clicking Next', instruction_id='05fb1e5d-efe7-465c-9366-f822da38e098'):
        await page.wait_for_timeout(100)
    
    async with testmu.step('Clicking Next to continue after completing the login test', instruction_id='d075fe59-0315-4bfa-81c9-c21951e5cd3a'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Typing agent@agentdegree.app into the email box', instruction_id='a1df5da3-2699-4610-8bb3-bb2625802457'):
        element_2 = page.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_2, "agent@agentdegree.app")
    
    async with testmu.step('Clicking Send code button', instruction_id='def9fe65-5b2f-485e-9e06-81b72d380488'):
        _loc_3 = page.locator("internal:role=button[name=\"Send code\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Clicking the inbox email from AgentDegree verification', instruction_id='4dc2efc1-169d-43a7-9dc5-f166da1763cd'):
        _loc_4 = page.locator("internal:role=button[name=\"AgentDegree — Your\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Reading the verification code from the inbox email'):
        set_var('verification_code', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((el(13).innerText.match(/\\b\\d{6}\\b/) || [null])[0]);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Your AgentDegree verification"i'], query='the 6-digit verification code in the inbox email message', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The 6-digit code from the inbox email on the page is saved as {{verification_code}}.'))
    
    async with testmu.step('Waiting for the verification code input screen', instruction_id='74095711-7f98-47b0-9244-f8c4ef6b0ebb'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "{{verification_code}}" into "Verification code"', instruction_id='59b51e27-f6ea-41fb-be53-d88a518db384'):
        element_3 = page.locator("internal:role=textbox[name=\"Verification code\"i]")
        variable_value_4 = var('{{verification_code}}')
        
        await testmu.fill(element_3, variable_value_4)
    
    async with testmu.step('Click "Verify code"', instruction_id='91cec312-7a4b-4de3-be63-1c9d749aa09d'):
        _loc_5 = page.locator("internal:role=button[name=\"Verify code\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Clicking Next', instruction_id='dbb87712-84b5-4e2a-8176-d0530e6a5616'):
        _loc_6 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Clicking Play voicemail on the third test', instruction_id='38f77442-eb3c-4c80-8f32-b09681873c80'):
        _loc_7 = page.locator("internal:role=button[name=\"Play voicemail\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('Checking whether the voicemail audio is audible'):
        set_var('voicemail_audio_audible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(9).textContent.trim().includes('Pause voicemail'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="Play voicemail"i]'], query='whether the voicemail audio is audible as indicated by the playback control', expected_value='false', needs_unit_conversion=False, operator='equals', transforms=[], condition='you cannot hear the audio'))
    if await testmu.evaluate_branch(sub_checks=[{'description': 'you cannot hear the audio', 'store_key': 'voicemail_audio_audible', 'expected_value': 'false', 'stored_value': '{{voicemail_audio_audible}}', 'extracted_value': '{{voicemail_audio_audible}}', 'operator': 'equals', 'transforms': []}], composite_operator="and"):
        async with testmu.step('Clicking Skip this test button below booking form', instruction_id='82b061f1-5878-4634-95bd-bba9682f04ce'):
            _loc_8 = page.locator("internal:role=button[name=\"Skip this test →\"i]")
            
            await _loc_8.click()
        
        async with testmu.step('Checking whether the fourth test is present'):
            set_var('fourth_test_appears', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {8: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(8).textContent.trim() === 'This test is not built yet.');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="This test is not built yet."i'], query='whether the fourth test panel displays its pending message', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the fourth test appears'))
        
        async with testmu.step('Assertion check', instruction_id='5ec4de78-8990-4ed9-b328-ef705e65c2fb'):
            await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the fourth test appears', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{fourth_test_appears}}', 'store_key': 'fourth_test_appears', 'variable_refs': {'{{fourth_test_appears}}': 'true'}}], 'sub_checks': [{'description': 'the fourth test appears', 'store_key': 'fourth_test_appears', 'expected_value': 'true', 'extracted_value': '{{fourth_test_appears}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the fourth test appears'})
    else:
        page = await testmu.execute_kane_cli('set the calendar date and time to exactly when the voicemail says they are coming, then book it and verify the test shows Solved', page=page)


if __name__ == "__main__":
    testmu.run(test)
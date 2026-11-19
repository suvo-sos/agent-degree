import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="0ccc7762-7d70-440b-b0b0-5f1de83653c4",
    name="Complete Challenge 1 in Agent Degree Exam",
    tc_id="TC-77",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"challenge_1_passed_message": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/gauntlet/step-1', instruction_id='9fc7dd0d-28c7-4f89-b77c-7a57ff51e052'):
        await page.goto("https://agent-degree-kappa.vercel.app/gauntlet/step-1")
    
    async with testmu.step('Checking I am agent checkbox', instruction_id='51f2e293-9ff7-4741-ba22-71ee3b3a0e83'):
        _loc_1 = page.locator("internal:role=checkbox[name=\"I am agent\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Next in the exam page', instruction_id='02ee594d-a896-4933-ba21-ee458b854292'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Waiting for the plan to complete', instruction_id='08f62bb9-a7a4-4d67-862c-da7cfd87bfdf'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "Photo tile 5"', instruction_id='dc85e6b0-f0c3-463c-96e5-bc9b7bb3e620'):
        _loc_3 = page.locator("internal:role=button[name=\"Photo tile 5\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Click "Photo tile 6"', instruction_id='21e8ef55-0864-45ee-954e-0575f2b0c4f3'):
        _loc_4 = page.locator("internal:role=button[name=\"Photo tile 6\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Clicking Next', instruction_id='fc2f3e32-7728-4596-a931-e64e39812fe0'):
        _loc_5 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Adjusting the slider handle into the green zone', instruction_id='570a2f77-4391-4be3-922b-42cc646d3f9e'):
        element_0 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await testmu.fill(element_0, "75")
    
    async with testmu.step('Pressing Page Down to decrease the slider value toward the green zone', instruction_id='a7178e83-7eba-40b3-bdda-5ad90be03c81'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageDown')
    
    async with testmu.step('Pressing PageDown to decrease the slider value', instruction_id='f4953494-a4d6-42bb-8be1-4d772cea4d1d'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageDown')
    
    async with testmu.step('Clicking Next button', instruction_id='369b4d29-e8e9-4513-8454-f2aba287cacf'):
        _loc_6 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Waiting for the queued plan to continue', instruction_id='a50b6413-ab0b-4205-bda8-16a2a32af9d0'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "Cube with the missing picture part"', instruction_id='b53db4d8-4eaa-430d-ab88-b702095ddc3c'):
        _loc_7 = page.locator("internal:role=img[name=\"Cube with the missing picture\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('Click "Empty part of the picture"', instruction_id='d1592e65-7db7-4edc-b22f-19be952fbf12'):
        _loc_8 = page.locator("internal:role=button[name=\"Empty part of the picture\"i]")
        
        await _loc_8.click()
    
    async with testmu.step('Clicking Next button', instruction_id='c58dd61f-eb5c-409f-9046-68079fd0e629'):
        _loc_9 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_9.click()
    
    async with testmu.step('Typing AGENT7 into the input field', instruction_id='abfc7f98-9eb2-4a32-932d-20f8e911e16f'):
        element_1 = page.locator("internal:role=textbox[name=\"Type the characters shown\"i]")
        
        await testmu.fill(element_1, "AGENT7")
    
    async with testmu.step('Checking whether the Challenge 1 passed message is present'):
        set_var('challenge_1_passed_message', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(5).textContent.trim() === 'Challenge 1 passed.');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Challenge 1 passed."i'], query="whether the paragraph on the page shows 'Challenge 1 passed.'", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="the page shows 'Challenge 1 passed.'"))
    
    async with testmu.step('Assertion check', instruction_id='779fd499-7643-4522-a193-e391cd3bcbde'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "the page shows 'Challenge 1 passed.'", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_1_passed_message}}', 'store_key': 'challenge_1_passed_message', 'variable_refs': {'{{challenge_1_passed_message}}': 'true'}}], 'sub_checks': [{'description': "the page shows 'Challenge 1 passed.'", 'store_key': 'challenge_1_passed_message', 'expected_value': 'true', 'extracted_value': '{{challenge_1_passed_message}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "the page shows 'Challenge 1 passed.'"})


if __name__ == "__main__":
    testmu.run(test)
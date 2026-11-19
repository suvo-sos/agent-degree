import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="676bc177-4274-4821-b39c-aaa9df0f699b",
    name="Complete Challenge 2 and Verify Completion",
    tc_id="TC-107",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"challenge_2_finished_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/final-exam/step-2', instruction_id='de87da84-94cf-492a-b387-ef86c1387444'):
        await page.goto("https://agent-degree-kappa.vercel.app/final-exam/step-2")
    
    async with testmu.step('Clicking Skip to move past tests 1, 2, 3 and 4', instruction_id='b47df445-806f-4064-885c-f727c5c3ce40'):
        _loc_1 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Skip to move past tests', instruction_id='39258691-b5b8-482e-a712-f07fc752fee7'):
        _loc_2 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Clicking Skip to move past tests 1, 2, 3 and 4', instruction_id='cc501777-27c1-4a81-acc7-2b452797fe07'):
        _loc_3 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Scroll into view: PRIMARY: Click Skip to move past tests 1, 2, 3 and 4; role=button; text="Skip" | HINTS: container=bottom of form', instruction_id='d717ad2d-4248-421e-92b7-aef524ac1ee5'):
        element_0 = page.locator("internal:role=button[name=\"Skip\"i]")
        await element_0.evaluate("el => el.scrollIntoView({block: 'center'})")
    
    async with testmu.step('Clicking Skip to move past tests 1 to 4', instruction_id='0f429512-9139-4e3d-acd5-f3b33db00081'):
        _loc_4 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Clicking Edit in the menu bar for test 5', instruction_id='3e74a924-26ef-4df3-85e5-8608822bcbcf'):
        _loc_5 = page.locator("internal:role=menuitem[name=\"Edit\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Clicking Find in the Edit menu', instruction_id='1448c345-e1a3-4146-aabc-1ef66f1f62e3'):
        _loc_6 = page.locator("internal:role=menuitem[name=\"Find\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Clicking Search the web in the submenu', instruction_id='627a1d04-4146-43ea-aa8b-71b1b75a81cd'):
        _loc_7 = page.locator("internal:role=menuitem[name=\"Search the web\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('Checking whether the Challenge 2 completion message is present'):
        set_var('challenge_2_finished_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {7: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(7).textContent.includes('Challenge 2 finished'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Challenge 2 finished."i'], query='whether the “Challenge 2 finished” message is present in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows Challenge 2 finished'))
    
    async with testmu.step('Assertion check', instruction_id='48ec9acf-de18-48de-a858-d64dd7222975'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows Challenge 2 finished', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_2_finished_visible}}', 'store_key': 'challenge_2_finished_visible', 'variable_refs': {'{{challenge_2_finished_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows Challenge 2 finished', 'store_key': 'challenge_2_finished_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_2_finished_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Challenge 2 finished'})


if __name__ == "__main__":
    testmu.run(test)
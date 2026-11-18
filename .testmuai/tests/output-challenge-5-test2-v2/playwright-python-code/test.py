import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="33622530-12d8-4195-81a2-5d6f94b12161",
    name="Confirm Booking and Download Report",
    tc_id="TC-47",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"stopped_40gb_download_message_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-5', instruction_id='d451ad78-1404-4341-8e65-12983e185af2'):
        await page.goto("http://localhost:3000/gauntlet/step-5")
    
    async with testmu.step('Clicking Confirm booking for Room 101', instruction_id='2bcdfeb3-5ed1-4496-8789-7ff6a9a654db'):
        _loc_1 = page.locator("internal:role=button[name=\"Confirm booking — Room\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Next button under the booking card', instruction_id='e9d7187f-091c-4b9e-b7e0-0db999ba439d'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Clicking Download report.pdf (quarterly report PDF)', instruction_id='70e29b33-59e2-4738-a7bc-edd38a128d06'):
        _loc_3 = page.locator("internal:role=button[name=\"Download report.pdf\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Clicking Cancel download', instruction_id='4b96a13c-5d82-4371-8735-3da1b2da8aae'):
        _loc_4 = page.locator("internal:role=button[name=\"Cancel download\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Checking whether the stopped-download message is visible'):
        set_var('stopped_40gb_download_message_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(12).textContent.includes('You stopped a 40GB download') && !!(el(12).offsetWidth || el(12).offsetHeight || el(12).getClientRects().length) && getComputedStyle(el(12)).color !== 'rgb(0, 0, 0)');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="You stopped a 40GB download ✓"i'], query="whether the green 'You stopped a 40GB download' message is visible in the page content", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="the green 'You stopped a 40GB download' message is visible"))
    
    async with testmu.step('Assertion check', instruction_id='8d0a3e1b-1d70-4e4a-9c94-1b0f4b39fc28'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "the green 'You stopped a 40GB download' message is visible", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{stopped_40gb_download_message_visible}}', 'store_key': 'stopped_40gb_download_message_visible', 'variable_refs': {'{{stopped_40gb_download_message_visible}}': 'true'}}], 'sub_checks': [{'description': "the green 'You stopped a 40GB download' message is visible", 'store_key': 'stopped_40gb_download_message_visible', 'expected_value': 'true', 'extracted_value': '{{stopped_40gb_download_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "the green 'You stopped a 40GB download' message is visible"})


if __name__ == "__main__":
    testmu.run(test)
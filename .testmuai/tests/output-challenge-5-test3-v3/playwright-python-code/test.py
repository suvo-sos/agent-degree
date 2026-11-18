import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="c2405956-ef19-4d1d-a3ce-0aab9fda7a19",
    name="Complete Challenge 5 by Skipping Tests and Confirming Booking",
    tc_id="TC-50",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"challenge_5_finished_panel_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-5', instruction_id='bd993d6f-336c-4367-9bf3-bfac33a77afd'):
        await page.goto("http://localhost:3000/gauntlet/step-5")
    
    async with testmu.step('Clicking the Skip this test button for test 1', instruction_id='edcf9845-ec38-477b-809c-86bd92eefac1'):
        _loc_1 = page.locator("internal:role=button[name=\"Skip this test →\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Skip this test again to skip test 2', instruction_id='0cd42d1d-86f9-46fa-af7c-cdcf53e00f92'):
        _loc_2 = page.locator("internal:role=button[name=\"Skip this test →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Confirming booking for Room 101', instruction_id='7ee00998-acb4-45e1-8f96-4a2e8ad60365'):
        _loc_3 = page.locator("internal:role=button[name=\"Confirm booking — Room\"i]")
        
        await _loc_3.click()
    
    async with testmu.step("whether the panel 'Challenge 5 finished — 2 tests skipped' is visible in the central lower portion of the page", instruction_id='d36109a2-68f5-4ea8-99d1-9baa9c2ad7ca'):
        set_var('challenge_5_finished_panel_visible', await testmu.vision_query(page, "whether the panel 'Challenge 5 finished \u2014 2 tests skipped' is visible in the central lower portion of the page", ""))
    
    async with testmu.step('Assertion check', instruction_id='16105d0f-efd9-4efc-b0c4-8badb5c45f6d'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "the panel 'Challenge 5 finished — 2 tests skipped' is visible", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{challenge_5_finished_panel_visible}}', 'store_key': 'challenge_5_finished_panel_visible', 'variable_refs': {'{{challenge_5_finished_panel_visible}}': 'true'}}], 'sub_checks': [{'description': "the panel 'Challenge 5 finished — 2 tests skipped' is visible", 'store_key': 'challenge_5_finished_panel_visible', 'expected_value': 'true', 'extracted_value': '{{challenge_5_finished_panel_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "the panel 'Challenge 5 finished — 2 tests skipped' is visible"})


if __name__ == "__main__":
    testmu.run(test)
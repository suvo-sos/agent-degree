import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="5c0e776d-a1b6-4b54-a7c3-97839b9af5b2",
    name="Confirm Room 101 Booking",
    tc_id="TC-44",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"booking_confirmed_message_visible": "true", "action_log_first_entry": "Confirm booking \u2014 Room 101"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-5', instruction_id='e0fe8513-c1f0-4a86-8993-6c948061cf82'):
        await page.goto("http://localhost:3000/gauntlet/step-5")
    
    async with testmu.step('Clicking Confirm booking for Room 101', instruction_id='53c09ab7-fc7e-4300-9e03-646112892ddd'):
        _loc_1 = page.locator("internal:role=button[name=\"Confirm booking — Room\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Checking whether the booking confirmation message is present'):
        set_var('booking_confirmed_message_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {18: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(18).textContent.trim() === 'Booking confirmed ✓' && getComputedStyle(el(18)).display !== 'none' && getComputedStyle(el(18)).visibility !== 'hidden' && getComputedStyle(el(18)).color !== 'rgb(0, 0, 0)');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Booking confirmed ✓"i'], query='whether the green Booking confirmed message is visible below the action log', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="The green 'Booking confirmed' message is visible."))
    
    async with testmu.step('Reading the first action log entry'):
        set_var('action_log_first_entry', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {17: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(17).textContent.replace(/^\\s*1\\.\\s*/, '').trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="1. Confirm booking — Room"i'], query='the first numbered entry in the action log', expected_value='Confirm booking — Room 101', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition="The action log shows 'Confirm booking — Room 101' as the first entry."))
    
    async with testmu.step('Assertion check', instruction_id='a6306fbb-c11d-4093-b8de-74bac056b4b4'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "The green 'Booking confirmed' message is visible.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{booking_confirmed_message_visible}}', 'store_key': 'booking_confirmed_message_visible', 'variable_refs': {'{{booking_confirmed_message_visible}}': 'true'}}, {'description': "The action log shows 'Confirm booking — Room 101' as the first entry.", 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': 'Confirm booking — Room 101', 'extracted_value': '{{action_log_first_entry}}', 'store_key': 'action_log_first_entry', 'variable_refs': {'{{action_log_first_entry}}': 'Confirm booking — Room 101'}}], 'sub_checks': [{'description': "The green 'Booking confirmed' message is visible.", 'store_key': 'booking_confirmed_message_visible', 'expected_value': 'true', 'extracted_value': '{{booking_confirmed_message_visible}}', 'operator': 'equals', 'transforms': []}, {'description': "The action log shows 'Confirm booking — Room 101' as the first entry.", 'store_key': 'action_log_first_entry', 'expected_value': 'Confirm booking — Room 101', 'extracted_value': '{{action_log_first_entry}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': "Verify the green 'Booking confirmed' message is visible and the action log shows 'Confirm booking — Room 101' as the first entry."})


if __name__ == "__main__":
    testmu.run(test)
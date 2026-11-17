import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="d5ec4d6b-7787-4c94-ad26-1ac0d7bee3e9",
    name="Start Agent Degree Test",
    tc_id="TC-23",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"agent_degree_heading_visible": "true", "agent_degree_tagline_visible": "true", "degree_image_visible": "true", "start_test_button_visible": "true", "the_gauntlet_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/', instruction_id='69bc7304-2a31-49ae-ad7e-d2d795e2b64b'):
        await page.goto("http://localhost:3000/")
    
    async with testmu.step('Checking whether the Agent Degree heading is present'):
        set_var('agent_degree_heading_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {1: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(1).textContent.trim() === 'Agent Degree' && !!(el(1).offsetWidth || el(1).offsetHeight || el(1).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="Agent Degree"i]'], query='whether the Agent Degree heading is present and visible in the page hero', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows the heading Agent Degree'))
    
    async with testmu.step('Checking whether the tagline is present'):
        set_var('agent_degree_tagline_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {2: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(2).textContent.trim() === 'Can an AI pass the human exam?' && !!(el(2).offsetWidth || el(2).offsetHeight || el(2).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Can an AI pass the human exam?"i'], query='whether the Can an AI pass the human exam? tagline is present and visible below the page heading', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows the tagline Can an AI pass the human exam?'))
    
    async with testmu.step('Checking whether the degree image is present'):
        set_var('degree_image_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!!el(5).getAttribute('src') && !!(el(5).offsetWidth || el(5).offsetHeight || el(5).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=img[name="Agent Degree — the Digital"i]'], query='whether the degree award image is present and visible in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows the degree image'))
    
    async with testmu.step('Checking whether the Start Test button is present'):
        set_var('start_test_button_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {4: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(4).textContent.trim() === 'Start Test' && !!(el(4).offsetWidth || el(4).offsetHeight || el(4).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=link[name="Start Test"i]'], query='whether the Start Test action button is present and visible in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows a Start Test button'))
    
    async with testmu.step('Assertion check', instruction_id='1e09b600-82df-4f07-ad11-1fcce8c0c41c'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows the heading Agent Degree', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{agent_degree_heading_visible}}', 'store_key': 'agent_degree_heading_visible', 'variable_refs': {'{{agent_degree_heading_visible}}': 'true'}}, {'description': 'the page shows the tagline Can an AI pass the human exam?', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{agent_degree_tagline_visible}}', 'store_key': 'agent_degree_tagline_visible', 'variable_refs': {'{{agent_degree_tagline_visible}}': 'true'}}, {'description': 'the page shows the degree image', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{degree_image_visible}}', 'store_key': 'degree_image_visible', 'variable_refs': {'{{degree_image_visible}}': 'true'}}, {'description': 'the page shows a Start Test button', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{start_test_button_visible}}', 'store_key': 'start_test_button_visible', 'variable_refs': {'{{start_test_button_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows the heading Agent Degree', 'store_key': 'agent_degree_heading_visible', 'expected_value': 'true', 'extracted_value': '{{agent_degree_heading_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'the page shows the tagline Can an AI pass the human exam?', 'store_key': 'agent_degree_tagline_visible', 'expected_value': 'true', 'extracted_value': '{{agent_degree_tagline_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'the page shows the degree image', 'store_key': 'degree_image_visible', 'expected_value': 'true', 'extracted_value': '{{degree_image_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'the page shows a Start Test button', 'store_key': 'start_test_button_visible', 'expected_value': 'true', 'extracted_value': '{{start_test_button_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows the heading Agent Degree, the tagline Can an AI pass the human exam?, the degree image and a Start Test button'})
    
    async with testmu.step('Clicking Start Test', instruction_id='3aaf802d-997b-426d-8518-bf3bd4c87f3e'):
        _loc_1 = page.locator("internal:role=link[name=\"Start Test\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Checking whether the The Gauntlet heading is present'):
        set_var('the_gauntlet_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {4: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(4).textContent.trim() === 'The Gauntlet' && !!(el(4).offsetWidth || el(4).offsetHeight || el(4).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="The Gauntlet"i]'], query='whether the The Gauntlet heading is present and visible in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the page shows The Gauntlet'))
    
    async with testmu.step('Assertion check', instruction_id='e3794703-b194-4086-af12-eacfda3722d5'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the page shows The Gauntlet', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{the_gauntlet_visible}}', 'store_key': 'the_gauntlet_visible', 'variable_refs': {'{{the_gauntlet_visible}}': 'true'}}], 'sub_checks': [{'description': 'the page shows The Gauntlet', 'store_key': 'the_gauntlet_visible', 'expected_value': 'true', 'extracted_value': '{{the_gauntlet_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows The Gauntlet'})


if __name__ == "__main__":
    testmu.run(test)
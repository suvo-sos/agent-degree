import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="9268f5d5-6d4e-4c90-9de5-2f188fe7f360",
    name="Start Agent Degree Exam",
    tc_id="TC-61",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"agent_degree_title_visible": "true", "agent_degree_tagline_visible": "true", "start_test_button_visible": "true", "the_gauntlet_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/', instruction_id='6d13ee4c-ca1c-4aeb-8820-52b215425afb'):
        await page.goto("http://localhost:3000/")
    
    async with testmu.step('Checking whether the Agent Degree title is present'):
        set_var('agent_degree_title_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {4: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(4).textContent.trim() === 'Agent Degree' && !!(el(4).offsetWidth || el(4).offsetHeight || el(4).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="Agent Degree"i]'], query="whether the title 'Agent Degree' in the main page heading is present", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="the page shows the title 'Agent Degree'"))
    
    async with testmu.step('Checking whether the Agent Degree tagline is present'):
        set_var('agent_degree_tagline_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(5).textContent.replace(/\\s+/g, ' ').trim() === 'Can an AI pass the human exam?' && !!(el(5).offsetWidth || el(5).offsetHeight || el(5).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Can an AI pass the human exam?"i'], query="whether the tagline 'Can an AI pass the human exam?' beneath the main heading is present", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="the page shows the tagline 'Can an AI pass the human exam?'"))
    
    async with testmu.step('Checking whether the Start Test button is present'):
        set_var('start_test_button_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {7: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(7).textContent.trim() === 'Start Test' && !!(el(7).offsetWidth || el(7).offsetHeight || el(7).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=link[name="Start Test"i]'], query="whether the 'Start Test' interactive control in the main page content is present", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="the page shows a 'Start Test' button"))
    
    async with testmu.step('Assertion check', instruction_id='fa92a5e8-dd83-45a4-8205-1342249b78c3'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "the page shows the title 'Agent Degree'", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{agent_degree_title_visible}}', 'store_key': 'agent_degree_title_visible', 'variable_refs': {'{{agent_degree_title_visible}}': 'true'}}, {'description': "the page shows the tagline 'Can an AI pass the human exam?'", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{agent_degree_tagline_visible}}', 'store_key': 'agent_degree_tagline_visible', 'variable_refs': {'{{agent_degree_tagline_visible}}': 'true'}}, {'description': "the page shows a 'Start Test' button", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{start_test_button_visible}}', 'store_key': 'start_test_button_visible', 'variable_refs': {'{{start_test_button_visible}}': 'true'}}], 'sub_checks': [{'description': "the page shows the title 'Agent Degree'", 'store_key': 'agent_degree_title_visible', 'expected_value': 'true', 'extracted_value': '{{agent_degree_title_visible}}', 'operator': 'equals', 'transforms': []}, {'description': "the page shows the tagline 'Can an AI pass the human exam?'", 'store_key': 'agent_degree_tagline_visible', 'expected_value': 'true', 'extracted_value': '{{agent_degree_tagline_visible}}', 'operator': 'equals', 'transforms': []}, {'description': "the page shows a 'Start Test' button", 'store_key': 'start_test_button_visible', 'expected_value': 'true', 'extracted_value': '{{start_test_button_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "the page shows the title 'Agent Degree', the tagline 'Can an AI pass the human exam?', and a 'Start Test' button"})
    
    async with testmu.step('Clicking Start Test in the lower-left area', instruction_id='f0218368-bfb8-4090-85fc-04dd334a3341'):
        _loc_1 = page.locator("internal:role=link[name=\"Start Test\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Checking whether the Gauntlet heading is visible'):
        set_var('the_gauntlet_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {4: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(4).textContent.trim() === 'The Gauntlet' && !!(el(4).offsetWidth || el(4).offsetHeight || el(4).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="The Gauntlet"i]'], query="whether the heading 'The Gauntlet' is present and visible in the page header", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="the page shows 'The Gauntlet'"))
    
    async with testmu.step('Assertion check', instruction_id='28b609e6-f2f1-4746-949e-76e759e29e6a'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "the page shows 'The Gauntlet'", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{the_gauntlet_visible}}', 'store_key': 'the_gauntlet_visible', 'variable_refs': {'{{the_gauntlet_visible}}': 'true'}}], 'sub_checks': [{'description': "the page shows 'The Gauntlet'", 'store_key': 'the_gauntlet_visible', 'expected_value': 'true', 'extracted_value': '{{the_gauntlet_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "the page shows 'The Gauntlet'"})


if __name__ == "__main__":
    testmu.run(test)
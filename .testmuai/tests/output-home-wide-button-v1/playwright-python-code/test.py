import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="938c8877-0398-4be3-a097-c7830a11b10a",
    name="Start Final Exam",
    tc_id="TC-69",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"page_title_check": "Agent Degree", "tagline_visible": "true", "start_test_button_present": "true", "final_exam_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/', instruction_id='ec46d79e-9189-4d16-85aa-4ab6447bac29'):
        await page.goto("http://localhost:3000/")
    
    async with testmu.step('Reading the main page title'):
        set_var('page_title_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {4: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(4).textContent);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="Agent Degree"i]'], query='the main page heading text', expected_value='Agent Degree', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition="the page title is 'Agent Degree'"))
    
    async with testmu.step("whether the tagline 'Can an AI pass the human exam?' is visible below the main title", instruction_id='2528ce11-960e-43ad-a4f3-680a55dd6d62'):
        set_var('tagline_visible', await testmu.vision_query(page, "whether the tagline 'Can an AI pass the human exam?' is visible below the main title", ""))
    
    async with testmu.step('Checking whether the Start Test button is present'):
        set_var('start_test_button_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {7: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(7).textContent.trim() === 'Start Test' && !!el(7).offsetParent);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=link[name="Start Test"i]'], query="whether the 'Start Test' call-to-action control is visible in the main page content", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="there is a 'Start Test' button"))
    
    async with testmu.step('Assertion check', instruction_id='564b7c11-e751-44b7-a643-4b0844b9881e'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "the page title is 'Agent Degree'", 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': 'Agent Degree', 'extracted_value': '{{page_title_check}}', 'store_key': 'page_title_check', 'variable_refs': {'{{page_title_check}}': 'Agent Degree'}}, {'description': "the tagline 'Can an AI pass the human exam?' is visible", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{tagline_visible}}', 'store_key': 'tagline_visible', 'variable_refs': {'{{tagline_visible}}': 'true'}}, {'description': "there is a 'Start Test' button", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{start_test_button_present}}', 'store_key': 'start_test_button_present', 'variable_refs': {'{{start_test_button_present}}': 'true'}}], 'sub_checks': [{'description': "the page title is 'Agent Degree'", 'store_key': 'page_title_check', 'expected_value': 'Agent Degree', 'extracted_value': '{{page_title_check}}', 'operator': 'equals', 'transforms': ['strip']}, {'description': "the tagline 'Can an AI pass the human exam?' is visible", 'store_key': 'tagline_visible', 'expected_value': 'true', 'extracted_value': '{{tagline_visible}}', 'operator': 'equals', 'transforms': []}, {'description': "there is a 'Start Test' button", 'store_key': 'start_test_button_present', 'expected_value': 'true', 'extracted_value': '{{start_test_button_present}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "the page title is 'Agent Degree', the tagline 'Can an AI pass the human exam?' is visible, and there is a 'Start Test' button"})
    
    async with testmu.step('Clicking the Start Test button', instruction_id='6e32a4c2-c495-456e-ba4c-ddd23868aca3'):
        _loc_1 = page.locator("internal:role=link[name=\"Start Test\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Checking whether The Final Exam is present'):
        set_var('final_exam_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {3: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(3).textContent.trim() === 'The Final Exam');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="The Final Exam"i]'], query="whether the text 'The Final Exam' is present in the main page heading", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="the page shows 'The Final Exam'"))
    
    async with testmu.step('Assertion check', instruction_id='ae8759b7-d686-49ff-85d2-2c4edbefe48a'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "the page shows 'The Final Exam'", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{final_exam_visible}}', 'store_key': 'final_exam_visible', 'variable_refs': {'{{final_exam_visible}}': 'true'}}], 'sub_checks': [{'description': "the page shows 'The Final Exam'", 'store_key': 'final_exam_visible', 'expected_value': 'true', 'extracted_value': '{{final_exam_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "the page shows 'The Final Exam'"})


if __name__ == "__main__":
    testmu.run(test)
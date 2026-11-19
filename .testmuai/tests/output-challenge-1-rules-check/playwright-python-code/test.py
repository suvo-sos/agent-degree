import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="6df73f34-2784-4c89-aab1-6ab408505881",
    name="Verify Final Exam Rules and Complete Challenge 1",
    tc_id="TC-86",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"challenge_count_check": "5 challenges. Pass them all to earn the Digital Human degree.", "test_mark_value_check": "Each test is 1 mark. An unsolved test costs \u22121.", "skipped_absent_check": "false", "unsolved_test_cost_check": "-1", "unsolved_moving_on_cost_check": "-1"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/final-exam', instruction_id='b5303dd9-cf0c-4fe3-8d63-ac85fc8b5615'):
        await page.goto("https://agent-degree-kappa.vercel.app/final-exam")
    
    async with testmu.step('Reading the challenge count from the rules'):
        set_var('challenge_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {6: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(6).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="5 challenges. Pass them all"i'], query='the number of challenges stated in the first Rules list item', expected_value='5', needs_unit_conversion=False, operator='equals', transforms=['extract_number'], condition='There are 5 challenges.'))
    
    async with testmu.step('Reading the per-test mark value from the rules'):
        set_var('test_mark_value_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {7: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(7).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Each test is 1 mark. An"i'], query='the mark value assigned to each test in the Rules list', expected_value='1', needs_unit_conversion=False, operator='equals', transforms=['extract_number'], condition='Each test is 1 mark.'))
    
    async with testmu.step('Assertion check', instruction_id='81666ec5-0b34-463d-890a-15d1acd976d1'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'There are 5 challenges.', 'passed': True, 'operator': 'equals', 'transforms': ['extract_number'], 'json_path': None, 'expected': '5', 'extracted_value': '{{challenge_count_check}}', 'store_key': 'challenge_count_check', 'variable_refs': {'{{challenge_count_check}}': '5 challenges. Pass them all to earn the Digital Human degree.'}}, {'description': 'Each test is 1 mark.', 'passed': True, 'operator': 'equals', 'transforms': ['extract_number'], 'json_path': None, 'expected': '1', 'extracted_value': '{{test_mark_value_check}}', 'store_key': 'test_mark_value_check', 'variable_refs': {'{{test_mark_value_check}}': 'Each test is 1 mark. An unsolved test costs −1.'}}], 'sub_checks': [{'description': 'There are 5 challenges.', 'store_key': 'challenge_count_check', 'expected_value': '5', 'extracted_value': '{{challenge_count_check}}', 'operator': 'equals', 'transforms': ['extract_number']}, {'description': 'Each test is 1 mark.', 'store_key': 'test_mark_value_check', 'expected_value': '1', 'extracted_value': '{{test_mark_value_check}}', 'operator': 'equals', 'transforms': ['extract_number']}], 'composite_operator': 'and', 'claim': 'Rule 1: There are 5 challenges, each test is 1 mark.'})
    
    async with testmu.step("whether 'skipped' appears anywhere in the app", instruction_id='17ee0242-5e9c-4ec7-85d1-72b11c97a2e8'):
        set_var('skipped_absent_check', await testmu.vision_query(page, "whether 'skipped' appears anywhere in the app", ""))
    
    async with testmu.step('Reading the shared penalty for unsolved and wrong answers'):
        set_var('unsolved_test_cost_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {7: 0, 8: 1};\n  const el = (i) => els[__m[i]];\n  const __v = ((() => { const a = el(7).textContent.match(/[−-]\\s*\\d+/)?.[0]?.replace('−','-').replace(/\\s/g,''); const b = el(8).textContent.match(/[−-]\\s*\\d+/)?.[0]?.replace('−','-').replace(/\\s/g,''); return a === b ? a : null; })());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Each test is 1 mark. An"i', 'internal:text="A wrong answer costs −"i'], query='the shared cost value stated for an unsolved test and a wrong answer in the Rules list', expected_value='-1', needs_unit_conversion=False, operator='equals', transforms=[], condition='An unsolved test costs -1, same as a wrong answer.'))
    
    async with testmu.step('Assertion check', instruction_id='df6de044-d58b-4c9d-a052-704b736e8a1c'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "There is no 'skipped' anywhere in the app.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'false', 'extracted_value': '{{skipped_absent_check}}', 'store_key': 'skipped_absent_check', 'variable_refs': {'{{skipped_absent_check}}': 'false'}}, {'description': 'An unsolved test costs -1, same as a wrong answer.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': '-1', 'extracted_value': '{{unsolved_test_cost_check}}', 'store_key': 'unsolved_test_cost_check', 'variable_refs': {'{{unsolved_test_cost_check}}': '-1'}}], 'sub_checks': [{'description': "There is no 'skipped' anywhere in the app.", 'store_key': 'skipped_absent_check', 'expected_value': 'false', 'extracted_value': '{{skipped_absent_check}}', 'operator': 'equals', 'transforms': []}, {'description': 'An unsolved test costs -1, same as a wrong answer.', 'store_key': 'unsolved_test_cost_check', 'expected_value': '-1', 'extracted_value': '{{unsolved_test_cost_check}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "Rule 2: There is no 'skipped' anywhere in the app. An unsolved test costs -1, same as a wrong answer."})
    
    async with testmu.step('Reading the unsolved-test mark cost from the rules'):
        set_var('unsolved_moving_on_cost_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {7: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((()=>{const m=el(7).innerText.match(/[−-]\\s*(\\d+)/);return m?`-${m[1]}`:null})());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Each test is 1 mark. An"i'], query='the mark cost for an unsolved test in the Rules list', expected_value='-1', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='If the current test is unsolved, moving on costs -1.'))


if __name__ == "__main__":
    testmu.run(test)
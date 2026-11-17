import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="64e67e21-4e5c-45d0-b1a9-baa4303bbfb5",
    name="Complete Step 1 Slider Verification",
    tc_id="TC-13",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"step_1_passed_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:3000/gauntlet/step-1', instruction_id='aa263038-2a62-4fdb-9dca-5bce443961cb'):
        await page.goto("http://localhost:3000/gauntlet/step-1")
    
    async with testmu.step('PRIMARY: Drag the slider handle into the green zone between 70 and 80; role=slider; text="Slider handle" | HINTS: click=middle of the green highlighted segment on the horizontal slider', instruction_id='1825eeac-725b-4e9c-b456-a13e6a5620c4'):
        coords = await testmu.get_vision_coordinates(page, 'PRIMARY: Drag the slider handle into the green zone between 70 and 80; role=slider; text="Slider handle" | HINTS: click=middle of the green highlighted segment on the horizontal slider', "click", 622, 605)
        await page.mouse.click(coords['x'], coords['y'])
        
    
    async with testmu.step('Clicking slider handle', instruction_id='b0e6d7c7-4bf1-42bd-905b-03782d2e7dbd'):
        _loc_1 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Pressing Tab to focus the slider handle', instruction_id='3ceb9899-067d-4e6e-95af-a7155cbc885f'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('Tab')
    
    async with testmu.step('Pressing the PageUp key to move the focused slider handle upward', instruction_id='dc729e57-17e5-4697-bf9d-fb805458f26b'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Pressing Shift+Tab to focus the slider handle', instruction_id='4c639ff5-8b7b-4246-923c-3921727fe32e'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('Shift+Tab')
    
    async with testmu.step('Waiting for slider handle presses to complete', instruction_id='bdc8f1b2-075e-4f4b-ae17-2b02a539b7f5'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Press PageUp', instruction_id='79378296-147a-4438-853a-4884abd83fcf'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='10ff63ec-c628-4080-944d-5ba0cce67e9e'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='06023bb6-1a01-440a-b65f-3e251c76e443'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='224bef8f-4a87-4e36-92db-54e5f74ca180'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='76d807b8-d5a7-4023-8e6c-b2141a3c0079'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='fbe5c0c0-3cd5-4fea-98b2-e62f817ac4c5'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Press PageUp', instruction_id='d1f4677b-abbb-48cf-bf55-e2340964478d'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Clicking Verify for the slider control', instruction_id='26886642-d694-4753-a7d4-a17ab0ff13f2'):
        _loc_2 = page.locator("internal:role=button[name=\"Verify\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Checking whether the Step 1 passed message is present'):
        set_var('step_1_passed_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {10: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(10).textContent.includes('Step 1 passed'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Step 1 passed — you move like"i'], query='whether the “Step 1 passed” message is present in the page content', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The page shows Step 1 passed.'))
    
    async with testmu.step('Assertion check', instruction_id='1523dcc1-4493-4984-bd0a-e1d780a04a1b'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The page shows Step 1 passed.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{step_1_passed_visible}}', 'store_key': 'step_1_passed_visible', 'variable_refs': {'{{step_1_passed_visible}}': 'true'}}], 'sub_checks': [{'description': 'The page shows Step 1 passed.', 'store_key': 'step_1_passed_visible', 'expected_value': 'true', 'extracted_value': '{{step_1_passed_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the page shows Step 1 passed'})


if __name__ == "__main__":
    testmu.run(test)
import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="49566f6e-2f63-41b0-ae2a-0a9319252821",
    name="Complete AI Agent Final Exam Challenges",
    tc_id="TC-84",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"final_exam_visible": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/final-exam', instruction_id='d10bd554-42ab-4de5-8389-a767e5082d1e'):
        await page.goto("https://agent-degree-kappa.vercel.app/final-exam")
    
    async with testmu.step("whether the text 'The Final Exam' is visible in the page header", instruction_id='cabdd268-f5e7-4c62-87d7-22cdbe676d14'):
        set_var('final_exam_visible', await testmu.vision_query(page, "whether the text 'The Final Exam' is visible in the page header", ""))
    
    async with testmu.step('Assertion check', instruction_id='d9068f75-ab9a-42f7-b4c6-2c7115820116'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "The current page shows 'The Final Exam'.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{final_exam_visible}}', 'store_key': 'final_exam_visible', 'variable_refs': {'{{final_exam_visible}}': 'true'}}], 'sub_checks': [{'description': "The current page shows 'The Final Exam'.", 'store_key': 'final_exam_visible', 'expected_value': 'true', 'extracted_value': '{{final_exam_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "it shows 'The Final Exam'."})
    
    async with testmu.step('Closing the rules dialog', instruction_id='47f19783-8f41-49ca-93a8-6f5bba069c9f'):
        _loc_1 = page.locator("internal:role=button[name=\"Close\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Start on the first I Am Agent challenge card', instruction_id='c2e0af40-5488-4817-9572-fb275574c3b5'):
        _loc_2 = page.locator("internal:role=link[name=\"Start →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Waiting for the plan steps to complete', instruction_id='5545bde4-4298-4ebf-980f-b4e7a9366b5f'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "I am agent"', instruction_id='0d7d6aa7-ad09-4024-81fb-7d1bb27ec7b7'):
        _loc_3 = page.locator("internal:role=checkbox[name=\"I am agent\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Clicking Next button', instruction_id='d7399277-1083-4beb-b9b6-0f27186aa049'):
        _loc_4 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Clicking the car image tile 2 button', instruction_id='1349ca30-a370-4aaf-9f25-897d1a6db797'):
        _loc_5 = page.locator("internal:role=button[name=\"Photo tile 2\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Clicking the car photo tile 4', instruction_id='2b617bd9-c42c-49c0-9ace-2e5048d30997'):
        _loc_6 = page.locator("internal:role=button[name=\"Photo tile 4\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Clicking the car photo tile at the bottom-right', instruction_id='be90beea-21c6-4d27-b62a-65652b1f026b'):
        _loc_7 = page.locator("internal:role=button[name=\"Photo tile 9\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('Clicking Next in the bottom-right below the car grid', instruction_id='d144916a-ff4d-4834-911b-54fc5b74e9ab'):
        _loc_8 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_8.click()
    
    async with testmu.step('Dragging the slider handle to the green dot at 69', instruction_id='22622d44-cc44-4970-a787-1bdc8b097a04'):
        element_0 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await testmu.fill(element_0, "69")
    
    async with testmu.step('Pressing Page Down to move the slider to the green dot at 69', instruction_id='c1f5e8bf-5ceb-495b-982b-22bbc1d21199'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageDown')
    
    async with testmu.step('Pressing Page Down to move the slider to 69 at the green dot', instruction_id='c66bb2d0-b4b3-4ec0-b396-41e688356e6c'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageDown')
    
    async with testmu.step('Pressing Page Down to move the slider to 69 near the green dot', instruction_id='8efa6678-4f0c-4396-aa8b-552ffdda37e8'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageDown')
    
    async with testmu.step('Pressing Left Arrow once to move the slider toward 69 and the green dot', instruction_id='63d8a171-7cb5-408b-93c3-b40c0adb75a0'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Clicking Next', instruction_id='e3769cb1-f016-484e-9237-c6a67ba8e003'):
        _loc_9 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_9.click()
    
    async with testmu.step('Clicking the square piece with the missing picture part in the fourth puzzle', instruction_id='0fa8c1ff-65c3-4525-9e41-22543133896e'):
        _loc_10 = page.locator("internal:role=button[name=\"square piece with the missing\"i]")
        
        await _loc_10.click()
    
    async with testmu.step('Clicking the hole in the photo', instruction_id='54210d16-953f-4d1f-97e6-49dd0e90a5fd'):
        _loc_11 = page.locator("internal:role=button[name=\"Empty square hole in the\"i]")
        
        await _loc_11.click()
    
    async with testmu.step('Clicking Next button in the bottom-right of the photo puzzle', instruction_id='bb5783ed-fcdf-4265-8712-853300afca42'):
        _loc_12 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_12.click()


if __name__ == "__main__":
    testmu.run(test)
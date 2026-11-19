import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="3deaeed5-cbbd-49b8-8cd4-23208ac67bd5",
    name="Complete AI Agent Final Exam Challenges",
    tc_id="TC-85",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"final_exam_shown": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/final-exam', instruction_id='d2283381-37d5-490d-ad6b-95d7ce219b79'):
        await page.goto("https://agent-degree-kappa.vercel.app/final-exam")
    
    async with testmu.step("whether 'The Final Exam' is visible in the main page content", instruction_id='4e7b0f0a-aa0c-401f-8849-7b481e1b6f81'):
        set_var('final_exam_shown', await testmu.vision_query(page, "whether 'The Final Exam' is visible in the main page content", ""))
    
    async with testmu.step('Assertion check', instruction_id='d8b5d0cc-18dc-4c60-8465-4627ebce46b2'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "the page shows 'The Final Exam'", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{final_exam_shown}}', 'store_key': 'final_exam_shown', 'variable_refs': {'{{final_exam_shown}}': 'true'}}], 'sub_checks': [{'description': "the page shows 'The Final Exam'", 'store_key': 'final_exam_shown', 'expected_value': 'true', 'extracted_value': '{{final_exam_shown}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "the page shows 'The Final Exam'"})
    
    async with testmu.step('Clicking Start the exam button', instruction_id='31dd635b-c017-42a4-823b-36a354612a22'):
        _loc_1 = page.locator("internal:role=button[name=\"Start the exam\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Start on the first challenge card', instruction_id='0cd7b505-e72a-469d-bc15-29e56a647b36'):
        _loc_2 = page.locator("internal:role=link[name=\"Start →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Waiting for the queued plan steps to complete', instruction_id='f79b37bc-a11f-433d-87a1-eff1cd19f1e2'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "I am agent"', instruction_id='32c93723-1287-4ef0-96fe-dfb43e0e6273'):
        _loc_3 = page.locator("internal:role=checkbox[name=\"I am agent\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Clicking Next button', instruction_id='a6356318-25d1-4248-904d-8653ec5d52e8'):
        _loc_4 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Clicking the yellow car photo tile 3', instruction_id='ef4c8975-9752-4200-9b63-0893574724dc'):
        _loc_5 = page.locator("internal:role=button[name=\"Photo tile 3\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Clicking the white car photo tile 5', instruction_id='5cd11318-2f8f-41be-9d20-b68bca19a702'):
        _loc_6 = page.locator("internal:role=button[name=\"Photo tile 5\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Clicking on the white car photo tile 7', instruction_id='cf6cb777-f674-4fb3-808e-14d8e826d990'):
        _loc_7 = page.locator("internal:role=button[name=\"Photo tile 7\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('Clicking Next below the car grid', instruction_id='1d865afc-1d3c-492b-b109-cdf9482cffb9'):
        _loc_8 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_8.click()
    
    async with testmu.step('Dragging the slider handle to the green dot at 69', instruction_id='b80b37d0-0e8d-4f57-9931-ac7ffb5ea1fe'):
        element_0 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await testmu.fill(element_0, "69")
    
    async with testmu.step('Dragging the slider handle to the green dot at 69', instruction_id='4b8f0abc-d42d-4525-95be-f111540449c9'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('Home')
    
    async with testmu.step('Pressing PageUp to move the slider handle to 69', instruction_id='1832fed0-0655-4249-a401-07ff1858bcb3'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Pressing PageUp key', instruction_id='7e9f9f52-20d1-45d3-a9e4-846c3ba75368'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Pressing PageUp key', instruction_id='1cb78bf7-2fd1-4940-b90d-07db16fea596'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Pressing PageUp to move the slider toward 69', instruction_id='71f17aaf-b21b-4ed2-b5e9-817de2d3deb1'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Pressing the PageUp key', instruction_id='afec493d-9a96-42cd-94f5-b34c11923f19'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Pressing PageUp key', instruction_id='435fef52-d90a-4122-9a08-2630a6a8669c'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Pressing PageUp key', instruction_id='f9f4dbf3-48aa-4c1c-bd47-2fa335c2cc92'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('PageUp')
    
    async with testmu.step('Pressing the ArrowLeft key to move the slider handle', instruction_id='41cd49f3-9ef1-4d36-a2ba-865e3f854125'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Clicking Next', instruction_id='b4eef573-1433-42e8-9791-163ea97b39bd'):
        _loc_9 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_9.click()
    
    async with testmu.step('Clicking the triangle picture piece below the photo in the central card', instruction_id='f1129c1a-6c92-46f5-9bd2-97d42d219b70'):
        _loc_10 = page.locator("internal:role=button[name=\"triangle piece with the\"i]")
        
        await _loc_10.click()
    
    async with testmu.step('Clicking the empty triangle hole in the photo', instruction_id='7dc8c52a-ab79-4fed-b35e-e5314931de12'):
        _loc_11 = page.locator("internal:role=button[name=\"Empty triangle hole in the\"i]")
        
        await _loc_11.click()
    
    async with testmu.step('Clicking Next', instruction_id='b4d68b40-e47e-48d7-bf85-59a188e9bb99'):
        _loc_12 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_12.click()


if __name__ == "__main__":
    testmu.run(test)
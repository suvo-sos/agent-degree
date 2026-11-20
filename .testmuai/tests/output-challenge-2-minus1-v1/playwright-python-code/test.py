import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page
from testmu import devtoolsStorageQuery

testmu.configure(
    build="c052f5e4-3ea8-46b5-914e-4433c49928fb",
    name="Verify Wrong-Answer Penalty and Form Navigation in Challenge 2",
    tc_id="TC-114",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"challenge_2_marks": "5", "wrong_attempt_penalty_effect": "true", "wrong_answer_penalty_test_results": "{\"raw_points\":11,\"wrong_attempts\":6,\"score_after_penalty\":5}"},
    auto_heal_version="AH2",
    devtools={"storage": True},
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/final-exam/step-2', instruction_id='dcae8c05-9b86-42ef-bcf0-ef94dd0d7b04'):
        await page.goto("https://agent-degree-kappa.vercel.app/final-exam/step-2")
    
    async with testmu.step('Waiting for the next step to run', instruction_id='6cafdd26-f044-4a68-a630-aaed2790c4fb'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "Priya Sharma" into "Full name"', instruction_id='34a99470-9b32-4792-b070-1c88195dcf34'):
        element_0 = page.locator("internal:role=textbox[name=\"Full name\"i]")
        
        await testmu.fill(element_0, "Priya Sharma")
    
    async with testmu.step('Type "34" into "Age"', instruction_id='544b130e-ee96-4ee4-9113-7eccf74d1a69'):
        element_1 = page.locator("internal:role=textbox[name=\"Age\"i]")
        
        await testmu.fill(element_1, "34")
    
    async with testmu.step('Waiting for the queued job form steps to complete', instruction_id='a58b5c3d-e2b8-4ec2-b608-8fdcbc7523e4'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "Data Analyst" into "Job title"', instruction_id='ffc4dac4-f538-4d91-bb34-8f3fd4c9120a'):
        element_2 = page.locator("internal:role=textbox[name=\"Job title\"i]")
        
        await testmu.fill(element_2, "Data Analyst")
    
    async with testmu.step('Waiting for the queued plan to complete', instruction_id='c869c829-b090-4e4a-aea3-55e056a18542'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "Northwind Labs" into "Company"', instruction_id='9ef0ae08-71af-4dfa-9860-26422e7f2f52'):
        element_3 = page.locator("internal:role=textbox[name=\"Company\"i]")
        
        await testmu.fill(element_3, "Northwind Labs")
    
    async with testmu.step('Entering Pune in City field', instruction_id='3464cf63-04f2-4cc8-ba0d-7c4db7935885'):
        element_4 = page.locator("internal:role=textbox[name=\"City\"i]")
        
        await testmu.fill(element_4, "Pune")
    
    async with testmu.step('Clicking Next in the employee form', instruction_id='fe01bf4c-5f90-4682-a6ec-c745ddd570ce'):
        _loc_1 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Entering Priya Sharma in the Name field', instruction_id='b99d8736-b20d-4b17-a2b0-4f00d5938d7b'):
        element_5 = page.locator("internal:role=textbox[name=\"Full name\"i]")
        
        await testmu.fill(element_5, "Priya Sharma")
    
    async with testmu.step('Entering age as 34 in the Age field', instruction_id='b71fda66-3b7a-459d-b102-7f66e745a5f7'):
        element_6 = page.locator("internal:role=textbox[name=\"Age\"i]")
        
        await testmu.fill(element_6, "34")
    
    async with testmu.step('Typing Data Analyst in Job title field', instruction_id='52a4d605-a778-4ff7-9f3d-45e748e432f8'):
        element_7 = page.locator("internal:role=textbox[name=\"Job title\"i]")
        
        await testmu.fill(element_7, "Data Analyst")
    
    async with testmu.step('Entering Northwind Labs in the Company field', instruction_id='e32f2932-29de-4c5b-9ecf-e30efdf13b3e'):
        element_8 = page.locator("internal:role=textbox[name=\"Company\"i]")
        
        await testmu.fill(element_8, "Northwind Labs")
    
    async with testmu.step('Typing Pune in City field', instruction_id='fa7b3808-2181-4ee3-84e9-5ff30db18337'):
        element_9 = page.locator("internal:role=textbox[name=\"City\"i]")
        
        await testmu.fill(element_9, "Pune")
    
    async with testmu.step('Clicking Next button in employee document form bottom', instruction_id='04319c46-fb11-4948-8280-cbcd743091c1'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Selecting Full-time employment type radio option', instruction_id='387b5aae-0788-4435-9338-bdbbe21674fc'):
        _loc_3 = page.locator("internal:role=radio[name=\"Full-time\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Selecting Design in Department combobox', instruction_id='69f29825-ece5-448a-85f9-b27696f655e9'):
        _loc_4 = page.locator("internal:role=combobox[name=\"Department\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Clicking Design option in Department list', instruction_id='aed48f00-9d7b-47ad-9220-727bd31418ef'):
        _loc_5 = page.locator("internal:role=option[name=\"Design\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Typing March 10, 2025 as the First day date in the form', instruction_id='dc4e4720-787b-4a84-a27e-2e565e8fbca9'):
        element_10 = page.locator("internal:role=textbox[name=\"First day\"i]")
        
        await testmu.fill(element_10, "2025-03-10")
    
    async with testmu.step('Clicking Next button in employment details form', instruction_id='d0fe9beb-7667-4ab7-87d5-37c886040769'):
        _loc_6 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Entering age as 34', instruction_id='c4f86330-3923-4f44-b4b7-72364f6d84ee'):
        element_11 = page.locator("internal:role=textbox[name=\"Age\"i]")
        
        await testmu.fill(element_11, "34")
    
    async with testmu.step('Typing Pune in the City field', instruction_id='3e6d9dba-034d-44f4-9d6c-c2a089504446'):
        element_12 = page.locator("internal:role=textbox[name=\"City\"i]")
        
        await testmu.fill(element_12, "Pune")
    
    async with testmu.step('Clicking Next', instruction_id='4d67aa17-5d7e-40d0-8546-0cd8f32f269b'):
        _loc_7 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('Clicking the Edit menu', instruction_id='18faed21-63f4-4b7e-ab3a-f0ca109a1755'):
        _loc_8 = page.locator("internal:role=menuitem[name=\"Edit\"i]")
        
        await _loc_8.click()
    
    async with testmu.step('Clicking Undo in the Edit menu', instruction_id='b320206b-48ad-4a15-88d6-c660584dfc8b'):
        _loc_9 = page.locator("internal:role=menuitem[name=\"Undo ⌘Z\"i]")
        
        await _loc_9.click()
    
    async with testmu.step('Clicking Edit', instruction_id='5641f702-1694-49c4-8c6c-96c687a80bc7'):
        _loc_10 = page.locator("internal:role=menuitem[name=\"Edit\"i]")
        
        await _loc_10.click()
    
    async with testmu.step('Clicking Find in the Edit menu', instruction_id='5ba3368b-1fab-49b7-8cf8-e2fd4f6825c4'):
        _loc_11 = page.locator("internal:role=menuitem[name=\"Find\"i]")
        
        await _loc_11.click()
    
    async with testmu.step('Clicking Search the web', instruction_id='55bc97c8-ad5d-49d7-ab95-85eb0558383a'):
        _loc_12 = page.locator("internal:role=menuitem[name=\"Search the web\"i]")
        
        await _loc_12.click()
    
    async with testmu.step('Clicking Back to the Final Exam link', instruction_id='d9ca51ae-b646-4197-a384-39cb4247df00'):
        _loc_13 = page.locator("internal:role=link[name=\"Back to the Final Exam\"i]")
        
        await _loc_13.click()
    
    async with testmu.step('PRIMARY: go to the results page; role=clickable; text="Paperwork Hell" | HINTS: position=second challenge card from the left; container=Final Exam page', instruction_id='231dce6b-b1b4-4792-b13b-a7c2a2e9a935'):
        coords = await testmu.get_vision_coordinates(page, 'PRIMARY: go to the results page; role=clickable; text="Paperwork Hell" | HINTS: position=second challenge card from the left; container=Final Exam page', "click", 700, 565)
        await page.mouse.click(coords['x'], coords['y'])
        
    
    async with testmu.step('PRIMARY: Start challenge 3; role=link; text="Start →" | HINTS: position=below The Control Room card, third card from the left', instruction_id='d3a33ec4-5d0c-47ee-acf7-5b101ebd3268'):
        coords = await testmu.get_vision_coordinates(page, 'PRIMARY: Start challenge 3; role=link; text="Start →" | HINTS: position=below The Control Room card, third card from the left', "click", 956, 810)
        await page.mouse.click(coords['x'], coords['y'])
        
    
    async with testmu.step('Clicking Skip button', instruction_id='02149d73-4d18-4dab-b90a-1a78c355a650'):
        _loc_14 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_14.click()
    
    async with testmu.step('Clicking back to the results page', instruction_id='56446efb-3df6-4d01-bfd7-3fcbba48338c'):
        _loc_15 = page.locator("internal:role=button[name=\"← Back\"i]")
        
        await _loc_15.click()
    
    async with testmu.step('Recording wrong-answer penalty regression and skipping test', instruction_id='4a6033fa-f3b7-45cf-91ef-a6cd4491d312'):
        await page.wait_for_timeout(500)
    
    async with testmu.step('Waiting for the Challenge 2 results to load on the Final Exam page', instruction_id='733aa87d-6794-4f42-8bd5-4b3b40b64cad'):
        await page.wait_for_timeout(500)
    
    async with testmu.step('Reading Challenge 2 marks from the saved results'):
        set_var('challenge_2_marks', await devtoolsStorageQuery("data = json.loads(storage.get('agent-degree-results') or '{}').get('2', {})\nreturn str(max(0, sum(data.get('points', [])) - data.get('wrong', 0)))"))
    
    async with testmu.step('Checking the score effect of wrong attempts'):
        set_var('wrong_attempt_penalty_effect', await devtoolsStorageQuery("data = json.loads(storage.get('agent-degree-results') or '{}').get('2', {})\npoints = sum(data.get('points', []))\nwrong = data.get('wrong', 0)\nreturn 'true' if wrong > 0 and max(0, points - wrong) < points else 'false'"))
    
    async with testmu.step('Recording the wrong-answer penalty test results'):
        set_var('wrong_answer_penalty_test_results', await devtoolsStorageQuery("data = json.loads(storage.get('agent-degree-results') or '{}').get('2', {})\npoints = sum(data.get('points', []))\nwrong = data.get('wrong', 0)\nreturn json.dumps({'raw_points': points, 'wrong_attempts': wrong, 'score_after_penalty': max(0, points - wrong)}, separators=(',', ':'))"))


if __name__ == "__main__":
    testmu.run(test)
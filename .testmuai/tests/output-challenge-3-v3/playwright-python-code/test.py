import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="5f7f3288-06f1-4c0a-b027-4bdd5d414acb",
    name="Complete AgentDegree Challenge 3 Tests",
    tc_id="TC-111",
    network=os.getenv("NETWORK", "false").lower() == "true",
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/final-exam/step-3', instruction_id='fdb6196a-a98a-410a-859f-3ea8cfaf56f7'):
        await page.goto("https://agent-degree-kappa.vercel.app/final-exam/step-3")
    
    async with testmu.step('Clicking Open menu button', instruction_id='74f954cf-1abd-46a0-a6f9-1c1f0e49a1ec'):
        _loc_1 = page.locator("internal:role=button[name=\"Open menu ↓\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Option 6 in the open menu', instruction_id='937f5d80-1cd4-498c-85dc-7f6298deed47'):
        _loc_2 = page.locator("internal:role=menuitem[name=\"Option 6\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Clicking Next button in the bottom-right of the challenge card', instruction_id='ff789769-b4b3-44cf-9527-b41d0c59e2cc'):
        _loc_3 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Clear Progress value', instruction_id='27e5023a-63b7-45a6-89c7-22d7a2644509'):
        element_0 = page.locator("internal:role=spinbutton[name=\"Progress value\"i]")
        
        await testmu.fill(element_0, "")
    
    async with testmu.step('Waiting for queued plan steps to run', instruction_id='50522abb-b755-4569-b4fd-b050839f295b'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Waiting for the queued plan to run', instruction_id='98da6f16-8c67-4e6f-9f54-7fdc6b5fe5ad'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "75" into "Progress value"', instruction_id='650eedaa-04d2-4192-8c4a-accea2b6ce8b'):
        element_1 = page.locator("internal:role=spinbutton[name=\"Progress value\"i]")
        
        await testmu.fill(element_1, "75")
    
    async with testmu.step('Click "Set"', instruction_id='de4692dc-2b7e-4b33-a601-a07e9f47a9cc'):
        _loc_4 = page.locator("internal:role=button[name=\"Set\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Clicking Next button', instruction_id='de9c4a34-94e7-4f38-8091-4b0d5a76c6e4'):
        _loc_5 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Clicking Pick a colour button', instruction_id='d125fe96-2b94-4880-92e2-4f2ca1c36126'):
        _loc_6 = page.locator("internal:role=button[name=\"Pick a colour\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Waiting for the queued steps to complete', instruction_id='ce9cf2b2-7636-4f85-a3bf-7162cac42d8b'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "885566" into "Colour hex value"', instruction_id='7c2dfbac-81c8-4976-9f19-398af2d36481'):
        element_2 = page.locator("internal:role=textbox[name=\"Colour hex value\"i]")
        
        await testmu.fill(element_2, "885566")
    
    async with testmu.step('Click "Set colour"', instruction_id='e4f3be91-f2c1-4ec1-866e-dbf20380caea'):
        _loc_7 = page.locator("internal:role=button[name=\"Set colour\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('Clicking Next button in the bottom-right of the challenge card', instruction_id='cbca8863-9acc-481c-ab6c-3fc611036b7b'):
        _loc_8 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_8.click()
    
    async with testmu.step('Clicking and dragging the vertical panel separator', instruction_id='5e28c112-77eb-40f9-adfc-f4f8a79ae2ef'):
        _loc_9 = page.locator("[id=\"_r_h_\"]")
        
        await _loc_9.click()
    
    async with testmu.step('Pressing ArrowLeft to resize the panels by decreasing the left panel width', instruction_id='711b61d4-3aaa-4e05-9817-370f881ed7c7'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Pressing the left arrow key to resize the panels', instruction_id='54a5b0aa-fb73-47ff-8d44-2a2852e157a7'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Pressing Left Arrow to resize the left panel wider', instruction_id='abe739c4-9eb8-47e8-9bb1-68c50e181eeb'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Pressing the left arrow key to resize the panels by decreasing the left panel width', instruction_id='81a5a7d3-be4a-490f-88d7-6dab4ba4983f'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Resizing the panels horizontally', instruction_id='ea2f06da-8a19-49f6-b264-4c83fb39511a'):
        _loc_10 = page.locator("[id=\"_r_l_\"]")
        
        await _loc_10.click()
    
    async with testmu.step('Pressing ArrowDown to increase the top-right panel height', instruction_id='26e7ae42-ccb5-4407-b3f5-b3f7e1a95daf'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowDown')
    
    async with testmu.step('Pressing ArrowDown to increase the top-right panel height', instruction_id='6b0e872c-0420-4f85-b828-87924256ae5c'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowDown')
    
    async with testmu.step('Increasing the top-right panel height by pressing ArrowDown', instruction_id='9aba55b9-7eb8-498f-bf10-06dd0980ddde'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowDown')
    
    async with testmu.step('Pressing the Down Arrow key to increase the top-right panel height', instruction_id='59ff7c8e-005f-4457-b984-1c6242ec2c60'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowDown')
    
    async with testmu.step('Pressing ArrowDown to increase the top-right panel height', instruction_id='26420017-5efe-4140-b65c-20f004bac614'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowDown')
    
    async with testmu.step('Pressing ArrowDown to increase the top-right panel height', instruction_id='70cf98f5-3f66-4e36-aaad-d7db17d82a0f'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowDown')
    
    async with testmu.step('Clicking Next button in the bottom-right of the challenge card', instruction_id='b03905d9-c4b7-4382-94fd-f9faa1522408'):
        _loc_11 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_11.click()
    
    async with testmu.step('Clicking on page 3 of 250', instruction_id='91dcaad2-eebd-4a70-a499-c7aae6523f94'):
        _loc_12 = page.locator("internal:role=button[name=\"3\"i]")
        
        await _loc_12.click()
    
    async with testmu.step('Clicking the Next button', instruction_id='9a99e6c2-aa5b-479a-9470-5bade7ca0197'):
        _loc_13 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_13.click()
    
    async with testmu.step('Clicking Section 3 accordion button', instruction_id='fb7a3e26-593b-43cb-a304-ceaf2dcaf0ef'):
        _loc_14 = page.locator("internal:role=button[name=\"Section 3\"i]")
        
        await _loc_14.click()
    
    async with testmu.step('Clicking Next button in the bottom-right of the challenge card', instruction_id='1fb48409-0500-43d6-8ad5-fdb6ace7a147'):
        _loc_15 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_15.click()
    
    async with testmu.step('Clicking the 4 stars rating button', instruction_id='e12c2830-4630-4b6d-8a5f-b9f36f778ddb'):
        _loc_16 = page.locator("internal:role=button[name=\"Rate 4 stars\"i]")
        
        await _loc_16.click()
    
    async with testmu.step('Clicking Next button', instruction_id='43532caf-db1e-4993-b274-008cb024caa8'):
        _loc_17 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_17.click()
    
    async with testmu.step('Typing Arc in the Search fonts box', instruction_id='13e2932c-1d38-4aad-ab9c-c46ae9584b94'):
        element_3 = page.locator("internal:role=textbox[name=\"Search fonts\"i]")
        
        await testmu.fill(element_3, "Arc")
    
    async with testmu.step('Tapando en el menú en Archivo', instruction_id='022d9f1c-e95c-4181-997c-5af910206026'):
        _loc_18 = page.locator("internal:role=button[name=\"Archivo\"s]")
        
        await _loc_18.click()
    
    async with testmu.step('Clicking Set for suvo in the filtered font menu in Test 8', instruction_id='f1eb7475-6561-4d01-933f-89e91da34a30'):
        _loc_19 = page.locator("internal:role=button[name=\"Set\"i]")
        
        await _loc_19.click()
    
    async with testmu.step('Clicking the Next button', instruction_id='fb7f7b2c-5e64-4f25-a00b-f429a65715d0'):
        _loc_20 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_20.click()
    
    async with testmu.step('Clicking crop box corner handle to adjust the crop rectangle', instruction_id='6db6a6ca-84ae-47a7-821e-7fb75cf28fa4'):
        _loc_21 = page.locator("internal:role=slider[name=\"Crop rectangle\"i]")
        
        await _loc_21.click()


if __name__ == "__main__":
    testmu.run(test)
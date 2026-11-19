import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="844bb623-ee92-4a89-9048-848c6d11da09",
    name="Identify and Describe Cars in Photo Grid",
    tc_id="TC-79",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"carCount": "5", "car_descriptions": "[\"Photo tile 2\",\"Photo tile 3\",\"Photo tile 4\",\"Photo tile 6\",\"Photo tile 9\"]"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/gauntlet/step-1', instruction_id='243ad95f-bb6e-4cee-9065-2c51d7111440'):
        await page.goto("https://agent-degree-kappa.vercel.app/gauntlet/step-1")
    
    async with testmu.step('Waiting for the plan steps to complete', instruction_id='5786d3ee-b702-49e5-9ef7-0f4deccd9670'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "I am agent"', instruction_id='e61424b4-a8a8-4787-a06f-a39e8e214c4c'):
        _loc_1 = page.locator("internal:role=checkbox[name=\"I am agent\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Next below the exam card', instruction_id='faec3fdf-f839-4b42-a3d4-363a759bc856'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Reading the total car count from the picked-cars status'):
        set_var('carCount', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Number((el(24).textContent || '').match(/0\\s+of\\s+(\\d+)\\s+cars picked/i)?.[1]));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="of 5 cars picked"i'], query='the total car count in the status text showing picked cars', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition="the number in the status text '0 of N cars picked' is stored as {{carCount}}"))
    
    async with testmu.step('the descriptions of each photo that shows a car are saved as {{car_descriptions}}', instruction_id='19de6dbf-4972-43f3-bd73-2c971744450f'):
        set_var('car_descriptions', await testmu.vision_query(page, "the descriptions of each photo that shows a car are saved as {{car_descriptions}}", ""))


if __name__ == "__main__":
    testmu.run(test)
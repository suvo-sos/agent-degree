import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="ccefc61d-ac3e-4b4a-8708-d71230858785",
    name="Identify and Describe Cars in Photo Grid",
    tc_id="TC-80",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"carCount": "3", "car_descriptions": "Photo tile 1, Photo tile 8, Photo tile 9"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/gauntlet/step-1', instruction_id='07a02c2b-0c1e-4d57-97d4-d6c98a9d9f33'):
        await page.goto("https://agent-degree-kappa.vercel.app/gauntlet/step-1")
    
    async with testmu.step('Clicking the I am agent checkbox within the exam card', instruction_id='4ba8a7ca-cba0-4033-94a4-73b679ce9119'):
        _loc_1 = page.locator("internal:role=checkbox[name=\"I am agent\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Next', instruction_id='78429106-de63-4d28-9fed-36d38c33b8f7'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Reading the total car count from the photo-grid status'):
        set_var('carCount', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((el(24).textContent.match(/of\\s+(\\d+)\\s+cars\\s+picked/i)||[])[1] ?? null);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="of 3 cars picked"i'], query='the total number of cars in the status text beneath the photo grid', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The number in the status text under the 3x3 photo grid is saved as {{carCount}}.'))
    
    async with testmu.step('Reviewing nine photos without selecting any photo', instruction_id='8cb9cb9d-2e2d-4c78-9b8d-a645f368323b'):
        await page.wait_for_timeout(500)
    
    async with testmu.step('Extracting descriptions of the car photos'):
        set_var('car_descriptions', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {6: 0, 20: 1, 22: 2};\n  const el = (i) => els[__m[i]];\n  const __v = (String([el(6).getAttribute('aria-label'), el(20).getAttribute('aria-label'), el(22).getAttribute('aria-label')].join(', ')));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="Photo tile 1"i]', 'internal:role=button[name="Photo tile 8"i]', 'internal:role=button[name="Photo tile 9"i]'], query='the accessible descriptions of the photo tiles that show cars', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The descriptions of each of the 9 photos that shows a car are saved as {{car_descriptions}}.'))


if __name__ == "__main__":
    testmu.run(test)
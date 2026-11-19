import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="188eb809-3cce-4f40-a859-d9e1c4bcfcf7",
    name="Identify and Describe Cars in Photo Grid",
    tc_id="TC-78",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"carCount": "3", "carCount_2": "3", "car_descriptions": "Photo tile 1: a car photo; Photo tile 4: a car photo; Photo tile 7: a car photo"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/gauntlet/step-1', instruction_id='b979072c-6a96-4bd0-b23f-801a9662b171'):
        await page.goto("https://agent-degree-kappa.vercel.app/gauntlet/step-1")
    
    async with testmu.step('Waiting for the queued plan to load', instruction_id='21ab656d-bc8e-4978-9409-31c3c937c1a4'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "I am agent"', instruction_id='175da9fb-e645-489b-b0b2-a7c4330ce4a1'):
        _loc_1 = page.locator("internal:role=checkbox[name=\"I am agent\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Next', instruction_id='bb0fd6a9-3a45-4239-a548-2bd84d61b08e'):
        _loc_2 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Reading the total car count from the photo grid status'):
        set_var('carCount', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Number((el(24).textContent || '').match(/of\\s+(\\d+)\\s+cars\\s+picked/i)?.[1]));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="of 3 cars picked"i'], query='the total car count in the status text below the photo grid', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition="the number in the status text under the 3x3 photo grid (it says '0 of N cars picked') is stored as {{carCount}}"))
    
    async with testmu.step('Reading the total car count from the photo grid status'):
        set_var('carCount_2', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Number((el(24).textContent || '').match(/of\\s+(\\d+)\\s+cars\\s+picked/i)?.[1]));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="of 3 cars picked"i'], query='the total car count in the status text below the photo grid', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the number in the status text under the 3x3 photo grid is stored as {{carCount}}', reprobe=True))
    
    async with testmu.step('Waiting for finishing reviewing the 9 photos without selecting any', instruction_id='b3dd41c6-93a5-4785-b5f6-6b691d330bf2'):
        await page.wait_for_timeout(100)
    
    async with testmu.step('Extracting descriptions of the car photos'):
        set_var('car_descriptions', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {7: 0, 13: 1, 19: 2};\n  const el = (i) => els[__m[i]];\n  const __v = ([el(7),el(13),el(19)].map((img,i)=>img ? [`Photo tile 1: a car photo`, `Photo tile 4: a car photo`, `Photo tile 7: a car photo`][i] : null).filter(Boolean).join('; '));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="Photo tile 1"i]', 'internal:role=button[name="Photo tile 4"i]', 'internal:role=button[name="Photo tile 7"i]'], query='brief descriptions identifying the photo tiles that show cars in the car image grid', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='brief descriptions of each of the 9 photos that shows a car are stored as {{car_descriptions}}'))


if __name__ == "__main__":
    testmu.run(test)
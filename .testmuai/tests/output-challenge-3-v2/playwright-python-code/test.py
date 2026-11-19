import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="c7df5aa4-4da6-4111-a478-b1bb9959d225",
    name="Complete Challenge 3 Exam Tests",
    tc_id="TC-108",
    network=os.getenv("NETWORK", "false").lower() == "true",
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app/final-exam/step-3', instruction_id='0257f515-642a-4173-b878-f1254badc919'):
        await page.goto("https://agent-degree-kappa.vercel.app/final-exam/step-3")
    
    async with testmu.step('Clicking Open menu ↓ in the main challenge card', instruction_id='bda3d101-52c0-44df-b71d-1af87775b6de'):
        _loc_1 = page.locator("internal:role=button[name=\"Open menu ↓\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Clicking Option 6', instruction_id='56b362e9-1dc0-4020-bbba-02c2328d39ec'):
        _loc_2 = page.locator("internal:role=menuitem[name=\"Option 6\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Clicking Next to move to the next test', instruction_id='b4d77745-dfb6-46a9-94be-8515da55bc37'):
        _loc_3 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Waiting for queued plan steps to complete', instruction_id='55ae05ee-9cb8-4f67-a774-3769399c1916'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "75" into "Progress value"', instruction_id='0658fced-4b26-4fcf-95de-6c81f7d2a851'):
        element_0 = page.locator("internal:role=spinbutton[name=\"Progress value\"i]")
        
        await testmu.fill(element_0, "75")
    
    async with testmu.step('Clicking Set button', instruction_id='a786c9d8-0f8b-481e-9b35-2ea10cd9eadc'):
        _loc_4 = page.locator("internal:role=button[name=\"Set\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Clicking Next to move to the next test', instruction_id='877d05ee-4224-47ec-9cc5-b15be96f960d'):
        _loc_5 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Clicking Pick a colour to open the colour picker', instruction_id='468be963-8855-4bdf-b509-22d0207a1409'):
        _loc_6 = page.locator("internal:role=button[name=\"Pick a colour\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Typing #885566 into the hex color field', instruction_id='6a1397a6-c059-4a27-9d17-822e8c26de74'):
        element_1 = page.locator("internal:role=textbox[name=\"Colour hex value\"i]")
        
        await testmu.fill(element_1, "#885566")
    
    async with testmu.step('Clicking Set colour button', instruction_id='ffae5d5d-c562-4144-b1cc-3649eeb68195'):
        _loc_7 = page.locator("internal:role=button[name=\"Set colour\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('Clicking Next to move to the next test', instruction_id='214bd7a2-d8eb-44da-ae5f-c5712db5d75f'):
        _loc_8 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_8.click()
    
    async with testmu.step('Dragging the divider to set the left panel width to 30%', instruction_id='5cec9808-33c0-4af8-8baf-19cb424e25e1'):
        _loc_9 = page.locator("[id=\"_r_h_\"]")
        
        await _loc_9.click()
    
    async with testmu.step('Waiting for the queued plan to finish running', instruction_id='bb51e6dc-c04a-42e6-b39a-558faac0b9cc'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Press ArrowLeft', instruction_id='53f8a8d8-e095-4bc9-83cb-d88d4d5a6b5c'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Press ArrowLeft', instruction_id='11d652de-9857-4a24-b1d2-19571c309200'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Press ArrowLeft', instruction_id='44a9ff4e-d62f-4efc-a672-4c63be584cf4'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Press ArrowLeft', instruction_id='bf53d46d-9c22-4854-9a86-7cba16d33037'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Press ArrowLeft', instruction_id='ead0a6ea-2a46-433b-a428-605f3e17c481'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Press ArrowLeft', instruction_id='22f55315-20fa-4b66-a30d-11f4076a1290'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Press ArrowLeft', instruction_id='5302c7c4-5042-4b68-a225-b907d55f9f60'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Press ArrowLeft', instruction_id='84bc4aec-f74e-4fda-9d3f-d02a1061f3fd'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowLeft')
    
    async with testmu.step('Waiting for the queued plan to complete', instruction_id='190c39f7-8bec-4b02-b0f3-f75996de9dd3'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Press ArrowRight', instruction_id='2d9f7954-6a07-4914-a0cd-3f45c289432f'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='2f33e28d-1e17-423d-a691-1062f15625bf'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='ed306b45-06df-4818-9cf6-32eeddac70a3'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Press ArrowRight', instruction_id='9f59198a-c12e-48f0-9894-b779daec3156'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowRight')
    
    async with testmu.step('Dragging the handle between Two and Three down to set top panel to 55%', instruction_id='23e8a90f-2643-4a00-8024-0de1e95e6c5d'):
        _loc_10 = page.locator("[id=\"_r_l_\"]")
        
        await _loc_10.click()
    
    async with testmu.step('Waiting for the plan to start running', instruction_id='4e953644-c16d-422c-bc3c-571715595415'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Press ArrowDown', instruction_id='b1dbffac-98e0-4a27-b2af-32befaea4dec'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowDown')
    
    async with testmu.step('Press ArrowDown', instruction_id='a28cb1f8-7f1c-4db6-b4e6-54deaa0c8cd7'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowDown')
    
    async with testmu.step('Press ArrowDown', instruction_id='be155a4a-182e-463b-9406-4a33615c501c'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowDown')
    
    async with testmu.step('Press ArrowDown', instruction_id='a97d4e72-191b-4492-af53-0fd6dac40ccf'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowDown')
    
    async with testmu.step('Press ArrowDown', instruction_id='b0d84766-0b77-439b-af9c-0fbe44fe9ae1'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowDown')
    
    async with testmu.step('Press ArrowDown', instruction_id='83dd2514-fab6-4ac4-a1ec-7486cfffc06b'):
        await page.wait_for_timeout(500)
        await page.keyboard.press('ArrowDown')
    
    async with testmu.step('Clicking Next to move to the next test', instruction_id='cb90df85-5561-4d57-b8ba-995bde9843a9'):
        _loc_11 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_11.click()
    
    async with testmu.step('Clicking Settings tab', instruction_id='6d0d6a59-33e5-41f9-ae52-98f16991d61b'):
        _loc_12 = page.locator("internal:role=tab[name=\"Settings\"i]")
        
        await _loc_12.click()
    
    async with testmu.step('Clicking Next in the bottom-right to proceed to the next test', instruction_id='b80515fb-e98b-411c-b95b-062deb9d3632'):
        _loc_13 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_13.click()
    
    async with testmu.step('Clicking Section 3 in the accordion', instruction_id='cb189135-35be-4a1b-9288-ddc5aff53806'):
        _loc_14 = page.locator("internal:role=button[name=\"Section 3\"i]")
        
        await _loc_14.click()
    
    async with testmu.step('Clicking Next to move to the next test', instruction_id='5da7c671-30d8-45e4-b180-9506d4c38128'):
        _loc_15 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_15.click()
    
    async with testmu.step('Clicking Give 4 stars to rate 4 stars', instruction_id='c92f223d-03f2-49d6-8b24-3b16aabfdc8b'):
        _loc_16 = page.locator("internal:role=button[name=\"Rate 4 stars\"i]")
        
        await _loc_16.click()
    
    async with testmu.step('Clicking Next to move to the next test', instruction_id='15b61098-e27c-4bab-a36c-30c3ce13b3b4'):
        _loc_17 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_17.click()
    
    async with testmu.step('Typing ban in the search box', instruction_id='d9db8545-488f-446b-a7ae-077c14cd0bd2'):
        element_2 = page.locator("internal:role=textbox[name=\"Search the fruits\"i]")
        
        await testmu.fill(element_2, "ban")
    
    async with testmu.step('Clicking Banana button', instruction_id='31242501-b00f-4189-8321-22cec56675ef'):
        _loc_18 = page.locator("internal:role=button[name=\"Banana\"i]")
        
        await _loc_18.click()
    
    async with testmu.step('Clicking Next to move to the next test', instruction_id='606c1099-e331-4803-8aa2-bf516d4c678b'):
        _loc_19 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_19.click()
    
    async with testmu.step('Waiting for the plan to start executing', instruction_id='408b7066-b56a-467f-b9b8-3c240fa253a2'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Click "Increase counter"', instruction_id='7b3b36fd-a310-4de6-a496-3db34ec9356c'):
        _loc_20 = page.locator("internal:role=button[name=\"Increase counter\"i]")
        
        await _loc_20.click()
    
    async with testmu.step('Click "Increase counter"', instruction_id='2ba8df79-a3d4-478d-a563-7a3eeddba5a0'):
        _loc_21 = page.locator("internal:role=button[name=\"Increase counter\"i]")
        
        await _loc_21.click()
    
    async with testmu.step('Click "Increase counter"', instruction_id='eefd1ffa-b9e5-4c03-ae08-645cc65c9d7e'):
        _loc_22 = page.locator("internal:role=button[name=\"Increase counter\"i]")
        
        await _loc_22.click()
    
    async with testmu.step('Click "Increase counter"', instruction_id='b28e00f0-c9e3-46b4-a904-58dc5d1d247a'):
        _loc_23 = page.locator("internal:role=button[name=\"Increase counter\"i]")
        
        await _loc_23.click()
    
    async with testmu.step('Click "Next →"', instruction_id='80558398-9be7-46ce-84ff-451b183f2d5c'):
        _loc_24 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_24.click()


if __name__ == "__main__":
    testmu.run(test)
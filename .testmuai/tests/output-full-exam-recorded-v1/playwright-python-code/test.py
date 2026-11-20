import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="95cc679a-d06d-4ea1-81f7-faff5e0a514c",
    name="Complete Final Exam Challenges",
    tc_id="TC-115",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"test_cannot_be_completed": "false"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app', instruction_id='50a4d0df-5801-4c43-8fac-5f948f98c1fd'):
        await page.goto("https://agent-degree-kappa.vercel.app")
    
    async with testmu.step('Clicking Start Exam to begin the final exam from the start', instruction_id='d2a77667-ba40-4761-aa8c-d82a85c4b9af'):
        _loc_1 = page.locator("internal:role=button[name=\"Start Exam\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Waiting for the queued plan to complete', instruction_id='50c01d79-88c0-4e79-9df4-91fe7a2ffd79'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "Kane" into "AGENT NAME"', instruction_id='964f5a54-0046-4017-a924-aaf2ea145c18'):
        element_0 = page.locator("internal:role=textbox[name=\"AGENT NAME\"i]")
        
        await testmu.fill(element_0, "Kane")
    
    async with testmu.step('Typing testmuai into the X username field', instruction_id='36104192-befe-41bb-91a2-a990cccc093a'):
        element_1 = page.locator("internal:role=textbox[name=\"TWITTER / X USERNAME\"i]")
        
        await testmu.fill(element_1, "testmuai")
    
    async with testmu.step('Clicking Next in the identity dialog', instruction_id='1e3aaaff-e30c-4169-bbea-49b2840d2ac3'):
        _loc_2 = page.locator("internal:role=button[name=\"Next\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('Clicking Continue to proceed', instruction_id='9a28cc11-7711-472b-be29-a8be3a2ead26'):
        _loc_3 = page.locator("internal:role=button[name=\"Continue\"i]")
        
        await _loc_3.click()
    
    async with testmu.step('Clicking Start link for Challenge 1', instruction_id='2fe35a28-9818-4fbd-8c85-72c2e0bd2b18'):
        _loc_4 = page.locator("internal:role=link[name=\"Start →\"i]")
        
        await _loc_4.click()
    
    async with testmu.step('Clicking I am agent checkbox', instruction_id='17febd08-5891-43fc-a3f3-f96f723070ee'):
        _loc_5 = page.locator("internal:role=checkbox[name=\"I am agent\"i]")
        
        await _loc_5.click()
    
    async with testmu.step('Clicking Next to proceed through Challenge 1', instruction_id='c026a3ed-df13-4209-9340-3a5d1d2f5c3e'):
        _loc_6 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_6.click()
    
    async with testmu.step('Clicking Photo tile 1 for Challenge 1 test', instruction_id='0acfec2f-fef4-43f1-922f-7aa3cb993e00'):
        _loc_7 = page.locator("internal:role=button[name=\"Photo tile 1\"i]")
        
        await _loc_7.click()
    
    async with testmu.step('Clicking Photo tile 2', instruction_id='ebcc7470-b7bb-48ed-b313-9a5893cffa2c'):
        _loc_8 = page.locator("internal:role=button[name=\"Photo tile 2\"i]")
        
        await _loc_8.click()
    
    async with testmu.step('Clicking Photo tile 6', instruction_id='17411b25-e752-4484-af32-0f4ef7b3da22'):
        _loc_9 = page.locator("internal:role=button[name=\"Photo tile 6\"i]")
        
        await _loc_9.click()
    
    async with testmu.step('Clicking Next → button to proceed to Challenge 1', instruction_id='e181218f-2978-4b5e-af63-3c375d4f42d3'):
        _loc_10 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_10.click()
    
    async with testmu.step('Sliding handle toward the green target marker at about two-thirds', instruction_id='cf1e0024-0b1c-4afe-9e6a-9bb63cf83a2b'):
        element_2 = page.locator("internal:role=slider[name=\"Slider handle\"i]")
        
        await testmu.fill(element_2, "67")
    
    async with testmu.step('Skipping the tutorial by clicking Skip', instruction_id='128b618b-9134-4e4b-a5c9-e8a253fa8389'):
        _loc_11 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_11.click()
    
    async with testmu.step('Clicking the circle piece with the missing picture part', instruction_id='e0f84a35-f449-4737-bcd5-c2214788792b'):
        _loc_12 = page.locator("internal:role=button[name=\"circle piece with the missing\"i]")
        
        await _loc_12.click()
    
    async with testmu.step('Clicking the empty circle hole near the top-center of the picture', instruction_id='5da329c6-558e-4143-b43d-a72aa99ef5b9'):
        _loc_13 = page.locator("internal:role=button[name=\"Empty circle hole in the\"i]")
        
        await _loc_13.click()
    
    async with testmu.step('Clicking Next in the bottom-right of the page', instruction_id='b253420c-6bea-4e2b-a970-374c97637105'):
        _loc_14 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_14.click()
    
    async with testmu.step('Clicking Skip in Challenge 1 test 5', instruction_id='bc742a84-ddf0-495b-808e-c742601d6fdd'):
        _loc_15 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_15.click()
    
    async with testmu.step('Clicking Back to the Final Exam', instruction_id='96d074d9-f79c-4349-bd21-ea7c18547027'):
        _loc_16 = page.locator("internal:role=link[name=\"Back to the Final Exam\"i]")
        
        await _loc_16.click()
    
    async with testmu.step('Clicking Start in Challenge 2 hints', instruction_id='7329e356-0e93-470a-a18b-8b9aa074afa4'):
        _loc_17 = page.locator("internal:role=link[name=\"Start →\"i]")
        
        await _loc_17.click()
    
    async with testmu.step('Waiting for the queued form plan to start', instruction_id='09b27c51-6731-434a-bde9-aaf5b6a4976c'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Type "Arjun Mehta" into "Full name"', instruction_id='f9af8251-2b08-4681-a6cb-0931fcec398c'):
        element_3 = page.locator("internal:role=textbox[name=\"Full name\"i]")
        
        await testmu.fill(element_3, "Arjun Mehta")
    
    async with testmu.step('Type "29" into "Age"', instruction_id='20a25031-0a59-4dcf-9421-286302a145d1'):
        element_4 = page.locator("internal:role=textbox[name=\"Age\"i]")
        
        await testmu.fill(element_4, "29")
    
    async with testmu.step('Typing product designer into Job title field', instruction_id='8dde1923-b724-4d07-a0d2-9074d3c31e0a'):
        element_5 = page.locator("internal:role=textbox[name=\"Job title\"i]")
        
        await testmu.fill(element_5, "product designer")
    
    async with testmu.step('Typing Company as Brightlane', instruction_id='c52b74ee-374a-401d-a96f-ab4ef79df0d6'):
        element_6 = page.locator("internal:role=textbox[name=\"Company\"i]")
        
        await testmu.fill(element_6, "Brightlane")
    
    async with testmu.step('Entering Bengaluru into the City field', instruction_id='f18f9e8c-4a8a-4f90-84cb-e6ea5ebe66ae'):
        element_7 = page.locator("internal:role=textbox[name=\"City\"i]")
        
        await testmu.fill(element_7, "Bengaluru")
    
    async with testmu.step('Clicking Next to continue the challenge', instruction_id='6331d83a-5edb-4f2c-a8b4-81e6a44182da'):
        _loc_18 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_18.click()
    
    async with testmu.step('Entering Priya Sharma into Full name textbox', instruction_id='d713af1b-6bb1-4ab1-827f-d7d4491b6352'):
        element_8 = page.locator("internal:role=textbox[name=\"Full name\"i]")
        
        await testmu.fill(element_8, "Priya Sharma")
    
    async with testmu.step('Entering age 34 in the Age field', instruction_id='615decab-969e-46f5-97b9-675f9d0ec854'):
        element_9 = page.locator("internal:role=textbox[name=\"Age\"i]")
        
        await testmu.fill(element_9, "34")
    
    async with testmu.step('Entering job title in the job title field', instruction_id='1de67397-252d-4204-af7d-2b420158bf2c'):
        element_10 = page.locator("internal:role=textbox[name=\"Job title\"i]")
        
        await testmu.fill(element_10, "Data Analyst")
    
    async with testmu.step('Typing Northwind Labs into the Company field', instruction_id='f18694d3-d377-444e-94e7-e8d93943f11e'):
        element_11 = page.locator("internal:role=textbox[name=\"Company\"i]")
        
        await testmu.fill(element_11, "Northwind Labs")
    
    async with testmu.step('Typing Pune into City field in the employee record', instruction_id='f9e69a51-dd30-4040-abd9-53a9e67dc22b'):
        element_12 = page.locator("internal:role=textbox[name=\"City\"i]")
        
        await testmu.fill(element_12, "Pune")
    
    async with testmu.step('Clicking Next to continue to Challenge 2', instruction_id='927025f7-3ca9-435e-a8f9-2edba68d5ee4'):
        _loc_19 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_19.click()
    
    async with testmu.step('Selecting Full-time option', instruction_id='1413ab83-fda0-4e5e-a6cf-54250acf9164'):
        _loc_20 = page.locator("internal:role=radio[name=\"Full-time\"i]")
        
        await _loc_20.click()
    
    async with testmu.step('Clicking Department dropdown', instruction_id='cc01e18a-e5b8-4da4-b331-97c06fb02bbb'):
        _loc_21 = page.locator("internal:role=combobox[name=\"Department\"i]")
        
        await _loc_21.click()
    
    async with testmu.step('Clicking Design option in the department list overlay', instruction_id='f6374df3-4b7f-4202-b966-7046528d9b68'):
        _loc_22 = page.locator("internal:role=option[name=\"Design\"i]")
        
        await _loc_22.click()
    
    async with testmu.step('Entering date 2025-03-10 in the First day field', instruction_id='ce348efa-c24b-42e0-94f3-68f15930873f'):
        element_13 = page.locator("internal:role=textbox[name=\"First day\"i]")
        
        await testmu.fill(element_13, "2025-03-10")
    
    async with testmu.step('Clicking Next → in the bottom-right of the page', instruction_id='fa479371-0cdc-46ae-95b0-e22ae6fb5c9a'):
        _loc_23 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_23.click()
    
    async with testmu.step('Typing 34 into the Age field for Priya’s record', instruction_id='df50081d-68d7-4d64-9386-ee0ac316eb30'):
        element_14 = page.locator("internal:role=textbox[name=\"Age\"i]")
        
        await testmu.fill(element_14, "34")
    
    async with testmu.step('Typing Pune into City field', instruction_id='d96ed3eb-5676-4d91-b646-89821ac1aa4f'):
        element_15 = page.locator("internal:role=textbox[name=\"City\"i]")
        
        await testmu.fill(element_15, "Pune")
    
    async with testmu.step('Clicking Next', instruction_id='3a5a916a-891c-4fde-8041-07b4c4692f2a'):
        _loc_24 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_24.click()
    
    async with testmu.step('Clicking Edit in the mock menu bar', instruction_id='7111098e-a7e4-4b62-8b4b-32456a07f59d'):
        _loc_25 = page.locator("internal:role=menuitem[name=\"Edit\"i]")
        
        await _loc_25.click()
    
    async with testmu.step('Clicking Find in the Edit menu hints submenu', instruction_id='2a45582e-f3a1-4315-8f22-5b104e9b03cc'):
        _loc_26 = page.locator("internal:role=menuitem[name=\"Find\"i]")
        
        await _loc_26.click()
    
    async with testmu.step('Clicking Search the web in the Find submenu', instruction_id='61e3d1de-9343-4c70-84b1-b72d64df8869'):
        _loc_27 = page.locator("internal:role=menuitem[name=\"Search the web\"i]")
        
        await _loc_27.click()
    
    async with testmu.step('Clicking Back to the Final Exam link in Challenge 2 completion page', instruction_id='75d25933-d427-4515-9ddf-38dcf1daeead'):
        _loc_28 = page.locator("internal:role=link[name=\"Back to the Final Exam\"i]")
        
        await _loc_28.click()
    
    async with testmu.step('Clicking Start in Work through Challenge 3', instruction_id='84eae1eb-0af6-475d-9ba8-4343748ee416'):
        _loc_29 = page.locator("internal:role=link[name=\"Start →\"i]")
        
        await _loc_29.click()
    
    async with testmu.step('Clicking Open menu on Challenge 3 card', instruction_id='e1cb665d-6fe7-45d4-9a13-69b77190a227'):
        _loc_30 = page.locator("internal:role=button[name=\"Open menu ↓\"i]")
        
        await _loc_30.click()
    
    async with testmu.step('Clicking Option 6 in the open menu', instruction_id='70098c5e-fdf0-41e4-af57-5c03657e5255'):
        _loc_31 = page.locator("internal:role=menuitem[name=\"Option 6\"i]")
        
        await _loc_31.click()
    
    async with testmu.step('Clicking Next to proceed through Challenge 3', instruction_id='9109e9f4-1534-47a0-9b19-21d53670e4e2'):
        _loc_32 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_32.click()
    
    async with testmu.step('Typing 75 into Progress value', instruction_id='995cbd7d-00d7-4cea-ba2e-af09bccf2da4'):
        element_16 = page.locator("internal:role=spinbutton[name=\"Progress value\"i]")
        
        await testmu.fill(element_16, "75")
    
    async with testmu.step('Clicking Set beside progress value field', instruction_id='cee16ef2-c312-4b00-b677-5d6417741a73'):
        _loc_33 = page.locator("internal:role=button[name=\"Set\"i]")
        
        await _loc_33.click()
    
    async with testmu.step('Clicking Next to proceed to Challenge 3', instruction_id='61bfbfa5-c23e-4c4e-a8a1-2f7d5d867c93'):
        _loc_34 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_34.click()
    
    async with testmu.step('Clicking Pick a colour on the challenge card', instruction_id='f2ff7fdc-a890-4dba-ab1c-ea04ec67e4fb'):
        _loc_35 = page.locator("internal:role=button[name=\"Pick a colour\"i]")
        
        await _loc_35.click()
    
    async with testmu.step('Typing the hex value #885566 into the color picker field', instruction_id='3d79cd25-e36c-4f6e-ac08-c8c3b0f4358b'):
        element_17 = page.locator("internal:role=textbox[name=\"Colour hex value\"i]")
        
        await testmu.fill(element_17, "#885566")
    
    async with testmu.step('Clicking Set colour in the expanded color picker', instruction_id='58fc0b4f-00b8-4f31-bf06-ad0703b65d50'):
        _loc_36 = page.locator("internal:role=button[name=\"Set colour\"i]")
        
        await _loc_36.click()
    
    async with testmu.step('Clicking Next arrow to continue to Challenge 3', instruction_id='42181a0a-5f80-43a8-836d-393637338b20'):
        _loc_37 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_37.click()
    
    async with testmu.step('Clicking Skip and moving on', instruction_id='ae87cf84-ac04-469e-ba5a-426adaa88354'):
        _loc_38 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_38.click()
    
    async with testmu.step('Clicking challenge card page 3 hints pagination', instruction_id='265b4cdf-5799-4498-a544-38ad4e3e2bfc'):
        _loc_39 = page.locator("internal:role=button[name=\"3\"i]")
        
        await _loc_39.click()
    
    async with testmu.step('Clicking Next to proceed to Challenge 3', instruction_id='58535393-0131-4874-88ef-8281de22db13'):
        _loc_40 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_40.click()
    
    async with testmu.step('Clicking Section 3 in the challenge card accordion', instruction_id='bcf1899f-63cf-429e-914b-c6f613e8cebd'):
        _loc_41 = page.locator("internal:role=button[name=\"Section 3\"i]")
        
        await _loc_41.click()
    
    async with testmu.step('Clicking Next to work through Challenge 3', instruction_id='80fee704-7c8c-4de9-a6e7-37c7ff027596'):
        _loc_42 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_42.click()
    
    async with testmu.step('Clicking the fourth star in the centered row', instruction_id='f3079163-abc0-4e31-b766-21b17c6ece2c'):
        _loc_43 = page.locator("internal:role=button[name=\"Rate 4 stars\"i]")
        
        await _loc_43.click()
    
    async with testmu.step('Clicking Next to work through Challenge 3', instruction_id='faf808b8-ccbb-43b4-894c-bb21e6a60448'):
        _loc_44 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_44.click()
    
    async with testmu.step('Typing Sor in the font search box', instruction_id='3acdec8f-290c-46de-bf16-3cc8a8f19d3e'):
        element_18 = page.locator("internal:role=textbox[name=\"Search fonts\"i]")
        
        await testmu.fill(element_18, "Sor")
    
    async with testmu.step('Clicking Sora in the hint results', instruction_id='69bb175a-31d0-4702-aef2-2ab398408d8f'):
        _loc_45 = page.locator("internal:role=button[name=\"Sora\"s]")
        
        await _loc_45.click()
    
    async with testmu.step('Clicking Set for Challenge 3 test', instruction_id='f385b0a5-c39a-4dd2-8802-8fe28408f95d'):
        _loc_46 = page.locator("internal:role=button[name=\"Set\"i]")
        
        await _loc_46.click()
    
    async with testmu.step('Clicking Next to work through Challenge 3', instruction_id='c0f15d65-574f-49a6-839d-753d4be2e387'):
        _loc_47 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_47.click()
    
    async with testmu.step('Clicking Skip to skip the crop test in Challenge 3 test 9', instruction_id='01cda212-26a6-4041-8280-1558cfe7254d'):
        _loc_48 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_48.click()
    
    async with testmu.step('Clicking Apple checkbox for Challenge 3', instruction_id='18b5477f-1f60-493f-a60c-bb285c6e9ed2'):
        _loc_49 = page.locator("internal:role=checkbox[name=\"Apple\"i]")
        
        await _loc_49.click()
    
    async with testmu.step('Clicking Mango checkbox for Challenge 3', instruction_id='f5d3484b-63ba-493d-92c2-18751bc9269f'):
        _loc_50 = page.locator("internal:role=checkbox[name=\"Mango\"i]")
        
        await _loc_50.click()
    
    async with testmu.step('Clicking Back to the Final Exam in the Challenge 4 page', instruction_id='d3d7045f-9490-46e9-aefe-a8da50024134'):
        _loc_51 = page.locator("internal:role=link[name=\"Back to the Final Exam\"i]")
        
        await _loc_51.click()
    
    async with testmu.step("Clicking Start link under Prove It's You challenge 4 hints", instruction_id='8999396d-28ac-4246-af1b-a5cc20023c27'):
        _loc_52 = page.locator("internal:role=link[name=\"Start →\"i]")
        
        await _loc_52.click()
    
    async with testmu.step('Clicking Skip on Challenge 4 test 1 scratch card', instruction_id='845ff945-897b-411e-8ab7-f4cb9f5b31c5'):
        _loc_53 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_53.click()
    
    async with testmu.step('Clicking Skip button in the bottom-left of the page', instruction_id='93f5660d-f1ee-4750-9c96-46c72be487fd'):
        _loc_54 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_54.click()
    
    async with testmu.step('Clicking Skip to skip the audio-only voicemail test in Challenge 4 test 3', instruction_id='19706453-e337-4693-aaf2-e00751642faf'):
        _loc_55 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_55.click()
    
    async with testmu.step('Clicking Skip button to move on', instruction_id='0cd1c439-046a-4557-aff0-8a55c24f3fe7'):
        _loc_56 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_56.click()
    
    async with testmu.step('Clicking Back to the Final Exam', instruction_id='1b592d51-5d51-4739-a148-574b50863723'):
        _loc_57 = page.locator("internal:role=link[name=\"Back to the Final Exam\"i]")
        
        await _loc_57.click()
    
    async with testmu.step('Clicking Start arrow for Challenge 5', instruction_id='5c77d96e-7646-49f9-b095-05a1dd4340d4'):
        _loc_58 = page.locator("internal:role=link[name=\"Start →\"i]")
        
        await _loc_58.click()
    
    async with testmu.step('Clicking Confirm booking — Room 101', instruction_id='204aa347-daaa-45e8-a393-fd10f5a26186'):
        _loc_59 = page.locator("internal:role=button[name=\"Confirm booking — Room\"i]")
        
        await _loc_59.click()
    
    async with testmu.step('Clicking Next button', instruction_id='2fe8fe0d-8b8e-4c51-bbc4-98326a6beb21'):
        _loc_60 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_60.click()
    
    async with testmu.step('Clicking Download report.pdf', instruction_id='32cf25aa-1dd9-4242-be1f-49ea209d2730'):
        _loc_61 = page.locator("internal:role=button[name=\"Download report.pdf\"i]")
        
        await _loc_61.click()
    
    async with testmu.step('Waiting for the report download to finish', instruction_id='6fe22ea0-731b-4176-920a-05a363753f7d'):
        await page.wait_for_timeout(2000)
    
    async with testmu.step('Clicking Skip', instruction_id='692844e3-0b42-48d5-b6c2-2ee672cd1052'):
        _loc_62 = page.locator("internal:role=button[name=\"Skip\"i]")
        
        await _loc_62.click()
    
    async with testmu.step('Clicking Cancel booking for Room 101', instruction_id='20bcd223-2062-4395-a044-b9daaab111c7'):
        _loc_63 = page.locator("internal:role=button[name=\"Cancel booking — Room\"i]")
        
        await _loc_63.click()
    
    async with testmu.step('Clicking Next to continue through Challenge 5', instruction_id='f7b699b1-e9f7-4c00-ba6b-a40884951425'):
        _loc_64 = page.locator("internal:role=button[name=\"Next →\"i]")
        
        await _loc_64.click()
    
    async with testmu.step('Waiting for confirmation of all five challenges completed', instruction_id='5f496b20-b22d-4ad3-9eb2-810307b23573'):
        await page.wait_for_timeout(100)
    
    async with testmu.step('whether a test that cannot be completed is shown in the page content', instruction_id='18284471-1844-4a63-a9b6-236dde021177'):
        set_var('test_cannot_be_completed', await testmu.vision_query(page, "whether a test that cannot be completed is shown in the page content", ""))
    if await testmu.evaluate_branch(sub_checks=[{'description': 'a test cannot be completed', 'store_key': 'test_cannot_be_completed', 'expected_value': 'true', 'stored_value': '{{test_cannot_be_completed}}', 'extracted_value': '{{test_cannot_be_completed}}', 'operator': 'equals', 'transforms': []}], composite_operator="and"):
        page = await testmu.execute_kane_cli('SKIP it and move on', page=page)


if __name__ == "__main__":
    testmu.run(test)
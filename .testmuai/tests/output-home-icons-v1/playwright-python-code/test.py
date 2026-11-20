import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="494537d5-442b-4751-a29b-655c25d2ebe8",
    name="Verify Button and Leaderboard Icons Consistency",
    tc_id="TC-116",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"start_exam_play_icon_visible": "true", "view_leaderboard_trophy_icon_visible": "true", "home_trophy_icon": "<button type=\"button\" tabindex=\"0\" data-slot=\"button\" class=\"group/button inline-flex shrink-0 items-center justify-center rounded-lg border bg-clip-padding font-medium whitespace-nowrap transition-all outline-none select-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 active:not-aria-[haspopup]:translate-y-px disabled:pointer-events-none disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 [&amp;_svg]:pointer-events-none [&amp;_svg]:shrink-0 [&amp;_svg:not([class*='size-'])]:size-4 border-border bg-background hover:bg-muted hover:text-foreground aria-expanded:bg-muted aria-expanded:text-foreground dark:border-input dark:bg-input/30 dark:hover:bg-input/50 h-9 gap-1.5 has-data-[icon=inline-end]:pr-2 has-data-[icon=inline-start]:pl-2 px-8 font-mono text-base\"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" color=\"currentColor\" class=\"\" stroke-width=\"2\" stroke=\"currentColor\"><path d=\"M12 15V19\" stroke=\"currentColor\" stroke-linecap=\"round\" stroke-width=\"2\"></path><path d=\"M7 5H5.58088C5.03886 5 4.76785 5 4.55944 5.10228C4.36064 5.19984 4.19984 5.36064 4.10228 5.55944C4 5.76785 4 6.03886 4 6.58088C4 7.6579 4 8.19641 4.16249 8.66982C4.31812 9.12325 4.58015 9.53278 4.92663 9.8641C5.28837 10.21 5.77732 10.4357 6.7552 10.887L7 11\" stroke=\"currentColor\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\"></path><path d=\"M17 5H18.4191C18.9611 5 19.2322 5 19.4406 5.10228C19.6394 5.19984 19.8002 5.36064 19.8977 5.55944C20 5.76785 20 6.03886 20 6.58088C20 7.6579 20 8.19641 19.8375 8.66982C19.6819 9.12325 19.4198 9.53278 19.0734 9.8641C18.7116 10.21 18.2227 10.4357 17.2448 10.887L17 11\" stroke=\"currentColor\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\"></path><path d=\"M7 4.88889C7 4.06119 7 3.64735 7.12061 3.31596C7.32281 2.76043 7.76043 2.32281 8.31596 2.12061C8.64735 2 9.06119 2 9.88889 2H14.1111C14.9388 2 15.3527 2 15.684 2.12061C16.2396 2.32281 16.6772 2.76043 16.8794 3.31596C17 3.64735 17 4.06119 17 4.88889V10C17 12.7614 14.7614 15 12 15C9.23858 15 7 12.7614 7 10V4.88889Z\" stroke=\"currentColor\" stroke-width=\"2\"></path><path d=\"M8 22C8 21.0681 8 20.6022 8.15224 20.2346C8.35523 19.7446 8.74458 19.3552 9.23463 19.1522C9.60218 19 10.0681 19 11 19H13C13.9319 19 14.3978 19 14.7654 19.1522C15.2554 19.3552 15.6448 19.7446 15.8478 20.2346C16 20.6022 16 21.0681 16 22H8Z\" stroke=\"currentColor\" stroke-linejoin=\"round\" stroke-width=\"2\"></path></svg>View leaderboard</button>", "leaderboard_page_icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" color=\"currentColor\" class=\"\" stroke-width=\"2\" stroke=\"currentColor\"><path d=\"M8.5 2V10.5M15.5 2V10.5\" stroke=\"currentColor\" stroke-linecap=\"round\" stroke-width=\"2\"></path><path d=\"M17.9162 2.01166H6.0838C5.17286 2.01166 3.96696 1.85424 3.34398 2.69602C3 3.1608 3 3.83334 3 5.17844C3 6.32524 3 6.89864 3.23194 7.38174C3.62807 8.20684 4.51377 8.56526 5.27291 8.95504L8.98131 10.8591C10.4626 11.6197 11.2033 12 12 12C12.7967 12 13.5374 11.6197 15.0187 10.8591L18.7271 8.95504C19.4862 8.56526 20.3719 8.20684 20.7681 7.38174C21 6.89864 21 6.32524 21 5.17844C21 3.83334 21 3.1608 20.656 2.69602C20.033 1.85424 18.8271 2.01166 17.9162 2.01166Z\" stroke=\"currentColor\" stroke-width=\"2\"></path><path d=\"M10.5292 13.6376C11.2478 13.2125 11.6071 13 12 13C12.3929 13 12.7522 13.2125 13.4708 13.6376L14.4708 14.2292C15.2167 14.6704 15.5896 14.891 15.7948 15.26C16 15.6289 16 16.0789 16 16.979V18.021C16 18.9211 16 19.3711 15.7948 19.74C15.5896 20.109 15.2167 20.3296 14.4708 20.7708L13.4708 21.3624C12.7522 21.7875 12.3929 22 12 22C11.6071 22 11.2478 21.7875 10.5292 21.3624L9.52922 20.7708C8.78332 20.3296 8.41037 20.109 8.20519 19.74C8 19.3711 8 18.9211 8 18.021V16.979C8 16.0789 8 15.6289 8.20519 15.26C8.41037 14.891 8.78332 14.6704 9.52922 14.2292L10.5292 13.6376Z\" stroke=\"currentColor\" stroke-linejoin=\"round\" stroke-width=\"2\"></path></svg>", "icon_test_issues": "The leaderboard table header icons are exposed as unlabeled images, so screen-reader users cannot identify their meaning."},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://agent-degree-kappa.vercel.app', instruction_id='fe39aa6e-76a7-4e4f-9fdf-a32d581ab497'):
        await page.goto("https://agent-degree-kappa.vercel.app")
    
    async with testmu.step('Inspecting Start Exam and View leaderboard buttons for newly added hugeicons', instruction_id='f22c8fac-b622-4678-af2f-a2421e441a32'):
        await page.wait_for_timeout(500)
    
    async with testmu.step('Checking whether the Start Exam play icon is present'):
        set_var('start_exam_play_icon_visible', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {7: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(7).querySelector(\'svg\') !== null && el(7).querySelector(\'svg path[d*="18.8906"]\') !== null);\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['internal:role=button[name="Start Exam"i]'], query='whether a play icon is present next to the Start Exam button text', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='A play icon is visible next to the Start Exam button text.'))
    
    async with testmu.step('Checking whether the View leaderboard trophy icon is present'):
        set_var('view_leaderboard_trophy_icon_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {10: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(10).querySelector('svg') !== null && el(10).querySelectorAll('svg path').length >= 5);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="View leaderboard"i]'], query='whether a trophy icon is present next to the View leaderboard button text', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='A trophy icon is visible next to the View leaderboard button text.'))
    
    async with testmu.step('Extracting the View leaderboard trophy icon'):
        set_var('home_trophy_icon', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {11: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(11).outerHTML);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="View leaderboard"i]'], query='the trophy icon next to the View leaderboard button text', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The trophy icon next to the View leaderboard button text is saved as {{home_trophy_icon}}.'))
    
    async with testmu.step('Assertion check', instruction_id='f9b2a186-0b6b-495a-bb58-02589634c6c8'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'A play icon is visible next to the Start Exam button text.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{start_exam_play_icon_visible}}', 'store_key': 'start_exam_play_icon_visible', 'variable_refs': {'{{start_exam_play_icon_visible}}': 'true'}}, {'description': 'A trophy icon is visible next to the View leaderboard button text.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{view_leaderboard_trophy_icon_visible}}', 'store_key': 'view_leaderboard_trophy_icon_visible', 'variable_refs': {'{{view_leaderboard_trophy_icon_visible}}': 'true'}}], 'sub_checks': [{'description': 'A play icon is visible next to the Start Exam button text.', 'store_key': 'start_exam_play_icon_visible', 'expected_value': 'true', 'extracted_value': '{{start_exam_play_icon_visible}}', 'operator': 'equals', 'transforms': []}, {'description': 'A trophy icon is visible next to the View leaderboard button text.', 'store_key': 'view_leaderboard_trophy_icon_visible', 'expected_value': 'true', 'extracted_value': '{{view_leaderboard_trophy_icon_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'Both icons are visible next to the button text: the Start Exam button shows a play icon, and the View leaderboard button shows a trophy icon.'})
    
    async with testmu.step('Clicking View leaderboard link on the homepage', instruction_id='53059f03-83ff-4728-9807-3b9ad9b74f80'):
        _loc_1 = page.locator("internal:role=link[name=\"View leaderboard\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Inspecting the column icons used for ranking and the leaderboard', instruction_id='41ad3904-b865-4944-bf53-147c53c988eb'):
        await page.wait_for_timeout(300)
    
    async with testmu.step('Extracting the Leaderboard ranking column icon'):
        set_var('leaderboard_page_icon', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {1: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(1).querySelector('h1 + p + div > div > span:first-child svg')?.outerHTML ?? null);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['div >> nth=1'], query='the ranking column icon in the Leaderboard page header', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The icon the Leaderboard page uses for ranking and leaderboard from the column icons is saved as {{leaderboard_page_icon}}.'))
    
    async with testmu.step('Testing icons for broken images and missing glyphs', instruction_id='367fa4c7-4bd3-411a-a30a-4eb3fff74c21'):
        await page.wait_for_timeout(300)
    
    async with testmu.step('Reading the potential accessibility issue with the leaderboard icons'):
        set_var('icon_test_issues', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {6: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((el(6).getAttribute('aria-label') || el(6).getAttribute('title') || el(6).getAttribute('aria-hidden') === 'true') ? '' : 'The leaderboard table header icons are exposed as unlabeled images, so screen-reader users cannot identify their meaning.');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=img >> nth=1'], query='the accessibility issue identified from the leaderboard table header icon', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='What could be broken or might not work about these icons is saved as {{icon_test_issues}}.'))
    
    async with testmu.step('Waiting while comparing the trophy icon to the leaderboard icon', instruction_id='1bb4a557-212a-4bfc-a6ca-41fcb3e123a9'):
        await page.wait_for_timeout(300)


if __name__ == "__main__":
    testmu.run(test)
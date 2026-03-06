import re
from playwright.sync_api import Playwright, sync_playwright, expect
from pages.demo_login_page import LoginPage

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.reportingframework.com/signin/?ReturnUrl=/")
    page.get_by_role("textbox", name="Email Address").click()
    page.get_by_role("textbox", name="Email Address").fill("SwetaRathore")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("changeme@123")
    page.get_by_role("button", name="Sign In").click()
    page.locator("div").filter(has_text="> Participants > Manage").nth(3).click()
    page.locator("span").filter(has_text=re.compile(r"^Manage Participants$")).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

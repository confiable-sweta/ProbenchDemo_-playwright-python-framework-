import re
from playwright.sync_api import sync_playwright
from pages.demo_login_page import LoginPage

def test_login_and_manage_participants():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login
        login = LoginPage(page)
        login.navigate()
        login.login("SwetaRathore", "changeme@123")

        # Perform actions after login (like opening Manage Participants)
        page.locator("div").filter(has_text="> Participants > Manage").nth(3).click()
        page.locator("span").filter(has_text=re.compile("^Manage Participants$")).click()

        # Close
        context.close()
        browser.close()
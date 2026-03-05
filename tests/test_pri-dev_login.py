import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://pri-dev.reportingframework.com/signin/?ReturnUrl=/")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("confiable.sweta@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Changeme@123")
    page.get_by_role("button", name="LOGIN", exact=True).click()
    page.get_by_role("radio").nth(2).check()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="2026 Reporting Framework", exact=True).click()
    page.get_by_role("tab", name="Terms and Conditions").click()
    page.get_by_role("link", name="Terms and Conditions").click()
    page.get_by_role("link", name="Next ").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

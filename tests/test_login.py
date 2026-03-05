import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect

@pytest.mark.smoke
def test_login_success(page):

    page.goto("https://opensource-demo.orangehrmlive.com/")

    login = LoginPage(page)

    login.login("Admin", "admin123")

    page.wait_for_url("**/dashboard/**")

    expect(page.locator("h6")).to_have_text("Dashboard")
from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.email = page.get_by_role("textbox", name="Email Address")
        self.password = page.get_by_role("textbox", name="Password")
        self.signin_button = page.get_by_role("button", name="Sign In")

    def navigate(self):
        self.page.goto("https://demo.reportingframework.com/signin/?ReturnUrl=/")

    def login(self, username, password):
        self.email.fill(username)
        self.password.fill(password)
        self.signin_button.click()
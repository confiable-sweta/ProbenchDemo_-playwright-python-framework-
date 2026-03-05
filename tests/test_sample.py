def test_open_google(browser):
    page = browser.new_page()
    page.goto("https://www.google.com")
    assert "Google" in page.title()
    page.close()

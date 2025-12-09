# tests/practicetestautomation/test_login_positive.py
from .login_page import LoginPage

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.login("student", "Password123")

    assert "logged-in-successfully" in browser.current_url.lower()

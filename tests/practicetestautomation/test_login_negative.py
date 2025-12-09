# tests/practicetestautomation/test_login_negative.py
from .login_page import LoginPage

def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.login("wronguser", "wrongpass")

    assert login_page.is_visible(login_page.ERROR_MESSAGE)
    assert "Your username is invalid!" in login_page.get_text(login_page.ERROR_MESSAGE)


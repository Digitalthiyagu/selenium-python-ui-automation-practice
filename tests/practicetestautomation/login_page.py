# tests/practicetestautomation/login_page.py
from selenium.webdriver.common.by import By
from ..common.base_page import BasePage

class LoginPage(BasePage):

    URL = "https://practicetestautomation.com/practice-test-login/"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON  = (By.ID, "submit")
    ERROR_MESSAGE  = (By.ID, "error")

    def open_login_page(self):
        self.open(self.URL)

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

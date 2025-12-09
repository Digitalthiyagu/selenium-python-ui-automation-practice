# tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    options = Options()
    # options.add_argument("--headless=new")   # run browser in headless mode if needed
    options.add_argument("--start-maximized")

    # Correct Selenium 4.x and webdriver-manager usage
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()
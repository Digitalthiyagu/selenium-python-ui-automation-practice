# Selenium Python UI Automation Practice

This repository contains a Selenium + Python + pytest UI automation framework
built against several public demo web applications:

- https://practicetestautomation.com/practice-test-login/
- https://www.saucedemo.com/
- https://the-internet.herokuapp.com/
- https://opensource-demo.orangehrmlive.com/
- https://omayo.blogspot.com/
- https://jqueryui.com/demos/
- https://only-testing-blog.blogspot.com/

## Tech Stack

- Python
- Selenium WebDriver
- pytest
- webdriver-manager
- Page Object Model (POM)

## Project Structure

- `tests/common/` – base page, fixtures, shared utilities
- `tests/practicetestautomation/` – login tests
- `tests/saucedemo/` – e-commerce flows (to be added)
- `tests/the_internet/` – alerts, frames, file uploads (to be added)
- etc.

## How to Run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pytest

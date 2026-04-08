import pytest
import json
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from config.config import BASE_URL

@pytest.mark.order(34)
@pytest.mark.smoke
def test_logout(browser):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    login = LoginPage(browser)

    # Login
    login.login(email, password)

    # Logout
    login.logout()

    # Wait for login page again
    wait.until(lambda d: BASE_URL in d.current_url)
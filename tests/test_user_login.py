import pytest
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from config.config import BASE_URL

@pytest.mark.order(32)
@pytest.mark.smoke
def test_user_login(browser):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["user_login"]["email"]
    password = data["user_login"]["password"]

    login = LoginPage(browser)

    # Wait for page ready
    wait.until(EC.presence_of_element_located(login.USERNAME_INPUT))

    login.click_login_button()
    login.enter_email(email)
    login.enter_password(password)
    login.click_eye_icon()
    login.click_submit()

    # Dynamic URL validation
    wait.until(EC.url_contains("OrgChart"))

    assert "OrgChart" in browser.current_url
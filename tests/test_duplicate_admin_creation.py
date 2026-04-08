import pytest
import json
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.system_admin_page import SystemAdminPage
from config.config import BASE_URL

@pytest.mark.order(7)
@pytest.mark.regression
def test_duplicate_admin_creation(browser):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    with open("testdata/user_data.json") as file:
        data = json.load(file)

    login_data = data["system_admin_login"]
    user_data = data["create_admin_user"]

    login = LoginPage(browser)
    login.login(login_data["email"], login_data["password"])

    admin = SystemAdminPage(browser)

    admin.open_user_admin()
    admin.click_create_user()

    admin.fill_user_details(
        user_data["full_name"],
        user_data["email"],
        user_data["password"],
        user_data["role"]   
    )

    admin.submit_user()

    wait.until(lambda d: "failed" in admin.get_duplicate_user_error().lower())

    assert admin.get_duplicate_user_error() == "Failed to create user"
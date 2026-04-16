# import pytest
# import os

# from pages.login_page import LoginPage
# from pages.system_admin_page import SystemAdminPage
# from config.config import BASE_URL

# # @pytest.mark.order(8)
# @pytest.mark.regression
# def test_export_credit_history(browser, test_data):

#     browser.get(BASE_URL)

#     email = test_data["logins"]["system_admin"]["email"]
#     password = test_data["logins"]["system_admin"]["password"]

#     login = LoginPage(browser)
#     login.login(email, password)

#     admin = SystemAdminPage(browser)

#     admin.open_user_admin()

#     # Jenkins-safe download dir
#     download_dir = os.path.abspath("downloads")
#     os.makedirs(download_dir, exist_ok=True)

#     admin.click_export_credit_history()

#     admin.wait_for_credit_history_download(download_dir)

import pytest
import os
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.system_admin_page import SystemAdminPage
from config.config import BASE_URL, DOWNLOAD_PATH


@pytest.mark.regression
def test_export_credit_history(browser, test_data):

    wait = WebDriverWait(browser, 30)

    browser.get(BASE_URL)

    email = test_data["logins"]["system_admin"]["email"]
    password = test_data["logins"]["system_admin"]["password"]

    LoginPage(browser).login(email, password)

    admin = SystemAdminPage(browser)

    admin.open_user_admin()

    before = set(os.listdir(DOWNLOAD_PATH))

    admin.click_export_credit_history()

    wait.until(lambda d: len(set(os.listdir(DOWNLOAD_PATH)) - before) > 0)

    assert True
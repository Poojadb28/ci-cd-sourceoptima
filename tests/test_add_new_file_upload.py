import pytest
import json
import os
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(14)
@pytest.mark.regression
def test_upload_new_file(browser):

    browser.get(BASE_URL)

    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()
    projects.open_root_space("TestSpace1")
    projects.open_project("TestFile_1")

    projects.click_new_upload()

    file_name = "0187.pdf"

    # Jenkins-safe path
    file_path = os.path.abspath(f"testdata/{file_name}")

    assert os.path.exists(file_path), "File not found in testdata folder"

    projects.upload_new_file(file_path)
    projects.click_upload()

    # Wait after upload
    WebDriverWait(browser, 20).until(
        lambda d: projects.verify_file_uploaded(file_name)
    )

    assert projects.verify_file_uploaded(file_name), "New file not uploaded"
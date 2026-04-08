import pytest 
import json
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(12)
@pytest.mark.smoke
def test_create_new_project(browser):

    browser.get(BASE_URL)

    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(),'Projects')]")
        )
    )

    projects = ProjectsPage(browser)

    projects.open_projects()

    projects.right_click_root_space("TestSpace1")
    projects.click_create_new_project()

    # Dynamic name
    project_name = f"TestFile_{int(time.time())}"
    projects.enter_project_name(project_name)

    file_path = os.path.abspath("testdata/files/0126.pdf")

    assert os.path.exists(file_path), "File not found"

    projects.upload_file(file_path)
    projects.click_upload()

    WebDriverWait(browser, 20).until(
        lambda d: projects.verify_project_created(project_name)
    )

    assert projects.verify_project_created(project_name), "Project not created"
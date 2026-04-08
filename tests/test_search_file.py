import pytest
import json
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(18)
@pytest.mark.regression
def test_search_field(browser):

    wait = WebDriverWait(browser, 20)

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
    projects.open_project("TestFile")

    search_value = "0187.pdf"

    projects.search_file(search_value)

    wait.until(lambda d: projects.verify_file_present(search_value))

    assert projects.verify_file_present(search_value), "Searched file not displayed"
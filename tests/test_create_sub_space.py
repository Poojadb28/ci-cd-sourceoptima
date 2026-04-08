import pytest
import json
import time
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(11)
@pytest.mark.smoke
def test_add_sub_space(browser):

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
    projects.right_click_root_space("TestSpace_1")

    projects.click_add_sub_space()

    # Dynamic name
    sub_space_name = f"TestSub_{int(time.time())}"

    projects.enter_sub_space_name(sub_space_name)
    projects.choose_icon()
    projects.select_color()
    projects.click_create_space()

    wait.until(lambda d: projects.verify_sub_space_created(sub_space_name))

    assert projects.verify_sub_space_created(sub_space_name)
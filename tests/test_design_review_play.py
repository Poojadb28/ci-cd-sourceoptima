import pytest
import json
import os
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.design_review_play_page import DesignReviewPage
from config.config import BASE_URL

@pytest.mark.order(22)
@pytest.mark.regression
def test_design_review_play(browser):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    login = LoginPage(browser)
    project = ProjectsPage(browser)
    design = DesignReviewPage(browser)

    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    # Jenkins-safe download dir
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    login.login(email, password)

    project.open_projects()
    project.open_root_space("TestSpace_1")
    project.open_project("TestFile")
    project.select_all_files()

    design.select_design_review()
    design.click_run()

    design.wait_for_processing()
    design.click_view_results()

    design.click_view_details()
    design.open_report_tab()

    design.download_report(download_dir)

    design.close_popup()
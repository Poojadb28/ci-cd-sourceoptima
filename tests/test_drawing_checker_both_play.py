# # import pytest
# # import os

# # from pages.login_page import LoginPage
# # from pages.projects_page import ProjectsPage
# # from pages.drawing_checker_both_play_page import DrawingCheckerPage
# # from config.config import BASE_URL

# # @pytest.mark.order(23)
# # @pytest.mark.regression
# # def test_drawing_checker_both_play(browser, test_data):

# #     browser.get(BASE_URL)

# #     login = LoginPage(browser)
# #     project = ProjectsPage(browser)
# #     drawing = DrawingCheckerPage(browser)

# #     email = test_data["logins"]["system_admin"]["email"]
# #     password = test_data["logins"]["system_admin"]["password"]

# #     download_dir = os.path.abspath("downloads")
# #     os.makedirs(download_dir, exist_ok=True)

# #     login.login(email, password)

# #     project.open_projects()
# #     project.open_root_space("TestSpace_1")
# #     project.open_project("TestFile")
# #     project.select_all_files()

# #     drawing.select_drawing_checker()
# #     drawing.click_run()

# #     drawing.wait_for_processing()
# #     drawing.click_view_results()

# #     drawing.click_view_details()
# #     drawing.open_report_tab()

# #     drawing.download_report(download_dir)

# #     drawing.close_popup()

# import pytest
# import json
# from pages.login_page import LoginPage
# from pages.projects_page import ProjectsPage
# from pages.drawing_checker_both_play_page import DrawingCheckerPage
# from config.config import BASE_URL

# # @pytest.mark.order(23) 
# @pytest.mark.regression
# def test_drawing_checker_both_play(browser):

#     browser.get(BASE_URL)

#     login = LoginPage(browser)
#     project = ProjectsPage(browser)
#     drawing = DrawingCheckerPage(browser)

#     # Load data
#     with open("testdata/login_data.json") as file:
#         data = json.load(file)

#     email = data["system_admin_login"]["email"]
#     password = data["system_admin_login"]["password"]

#     download_dir = r"C:\Users\pooja.db\Downloads"

#     # ---------------- FLOW ----------------

#     login.login(email, password)

#     project.open_projects()
#     project.open_root_space("TestSpace_1")
#     project.open_project("TestFile")
#     project.select_all_files()

#     drawing.select_drawing_checker()
#     drawing.click_run()

#     drawing.wait_for_processing()
#     drawing.click_view_results()

#     drawing.click_view_details()
#     drawing.open_report_tab()

#     drawing.download_report(download_dir)

#     drawing.close_popup()

# 

import pytest
import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.drawing_checker_both_play_page import DrawingCheckerPage
from config.config import BASE_URL


@pytest.mark.regression
def test_drawing_checker_both_play(browser):

    browser.get(BASE_URL)

    login = LoginPage(browser)
    project = ProjectsPage(browser)
    drawing = DrawingCheckerPage(browser)

    # Load data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    # FIX: use system Downloads folder
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")

    # ---------------- FLOW ----------------

    login.login(email, password)

    project.open_projects()
    project.open_root_space("TestSpace_1")
    project.open_project("TestFile")
    project.select_all_files()

    drawing.select_drawing_checker()
    drawing.click_run()

    drawing.wait_for_processing()
    drawing.click_view_results()

    main_window = browser.current_window_handle

    WebDriverWait(browser, 10).until(lambda d: len(d.window_handles) > 1)

    for window in browser.window_handles:
        if window != main_window:
            browser.switch_to.window(window)
            break

    # ================= SEARCH ================= #
    drawing.search_issue("minor")
    drawing.clear_search()

    # ================= FILTERS ================= #
    drawing.filter_by_severity("Critical")
    drawing.filter_by_source("Veeco Standards")

    # ================= DRILLDOWN ================= #
    import time
    time.sleep(3)

    elements = browser.find_elements(*drawing.drilldown_btn)
    print("Drilldown count:", len(elements))

    drawing.click_drilldown()

    # ================= DOWNLOAD ================= #
    drawing.download_report(download_dir)

    # ================= CLOSE NEW TAB ================= #

    browser.close()  # closes current (new) tab

    # switch back to main window
    browser.switch_to.window(main_window)

    # drawing.close_popup()

# import pytest
# import os

# from pages.login_page import LoginPage
# from pages.projects_page import ProjectsPage
# from pages.drawing_checker_both_play_page import DrawingCheckerPage
# from config.config import BASE_URL


# @pytest.mark.regression
# def test_drawing_checker_both_play(browser, test_data):

#     browser.get(BASE_URL)

#     email = test_data["logins"]["system_admin"]["email"]
#     password = test_data["logins"]["system_admin"]["password"]

#     download_dir = os.path.abspath("downloads")
#     os.makedirs(download_dir, exist_ok=True)

#     LoginPage(browser).login(email, password)

#     project = ProjectsPage(browser)
#     drawing = DrawingCheckerPage(browser)

#     project.open_projects()
#     project.open_root_space("TestSpace_1")
#     project.open_project("TestFile")

#     drawing.select_drawing_checker()
#     drawing.click_run()
#     drawing.wait_for_processing()

#     drawing.download_report(download_dir)

#     assert True
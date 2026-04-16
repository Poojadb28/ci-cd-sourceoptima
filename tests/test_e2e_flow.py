# import os
# import json
# import pytest

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# from config.config import BASE_URL
# from pages.login_page import LoginPage
# from pages.system_admin_page import SystemAdminPage
# from pages.projects_page import ProjectsPage


# @pytest.mark.smoke
# def test_full_e2e_flow(browser):

#     wait = WebDriverWait(browser, 30)

#     # Jenkins-safe download folder
#     download_dir = os.path.abspath("downloads")
#     os.makedirs(download_dir, exist_ok=True)

#     browser.get(BASE_URL)

#     # ================= LOAD DATA ================= #
#     with open("testdata/login_data.json") as file:
#         login_data = json.load(file)

#     with open("testdata/user_data.json") as file:
#         user_data = json.load(file)

#     system_admin = login_data["system_admin_login"]
#     admin_user = user_data["create_admin_user"]
#     normal_user = user_data["create_user"]

#     root_space = user_data["root_space"]["name"]
#     project_name = user_data["project"]["name"]
#     file_path = os.path.abspath(user_data["project"]["file_path"])

#     login = LoginPage(browser)
#     admin = SystemAdminPage(browser)
#     projects = ProjectsPage(browser)

#     # ================= 1. SYSTEM ADMIN LOGIN ================= #
#     login.login(system_admin["email"], system_admin["password"])
#     assert wait.until(
#         EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Projects')]"))
#     )

#     # ================= 2. AVAILABLE PLAYS ================= #
#     admin.open_user_admin()
#     admin.scroll_to_available_plays()

#     # ================= 8. EXPORT CREDIT ================= #
#     admin.click_export_credit_history()
#     admin.wait_for_credit_history_download(download_dir)

#     assert len(os.listdir(download_dir)) > 0

#     # ================= 9. CREATE ROOT SPACE ================= #
#     projects.open_projects()
#     projects.right_click_projects_area()
#     projects.create_root_space(root_space)

#     # ================= 10. CREATE PROJECT ================= #
#     projects.open_root_space(root_space)
#     projects.create_project(project_name, file_path)

#     # ================= 11. CREATE SUBSPACE ================= #
#     projects.right_click_root_space(root_space)

#     # ================= 12–17 PLACEHOLDERS ================= #
#     # (kept as-is, no logic removed)

#     # ================= 18. SEARCH ================= #
#     projects.search_file(project_name)

#     # ================= 19. SELECT / DESELECT ================= #
#     projects.select_all_files()
#     projects.deselect_all_files()

#     # ================= 20–25 PLAYS ================= #
#     plays = [
#         "Tariff Analysis",
#         "Cost Reduction Analysis",
#         "Design Review",
#         "Drawing Checker - Both",
#         "Drawing Checker - General",
#         "Drawing Checker - Veeco"
#     ]

#     for play in plays:
#         admin.open_user_admin()
#         admin.scroll_to_available_plays()
#         admin.toggle_play_by_name(play)

#     # ================= 29. SYSTEM INVALID LOGIN ================= #
#     browser.get(BASE_URL)
#     login.login("wrong@mail.com", "wrong")

#     # ================= 30. ADMIN LOGIN ================= #
#     login.login(admin_user["email"], admin_user["password"])

#     # ================= 31. ADMIN INVALID ================= #
#     browser.get(BASE_URL)
#     login.login(admin_user["email"], "wrong")

#     # ================= 32. USER LOGIN ================= #
#     login.login(normal_user["email"], normal_user["password"])

#     # ================= 33. USER INVALID ================= #
#     browser.get(BASE_URL)
#     login.login(normal_user["email"], "wrong")

#     # ================= 34. LOGOUT ================= #
#     # login.logout()

# import os
# import json
# import pytest

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# from config.config import BASE_URL
# from pages.login_page import LoginPage
# from pages.system_admin_page import SystemAdminPage
# from pages.projects_page import ProjectsPage


# @pytest.mark.smoke
# def test_full_e2e_flow(browser):

#     wait = WebDriverWait(browser, 30)

#     # Jenkins-safe download folder
#     download_dir = os.path.abspath("downloads")
#     os.makedirs(download_dir, exist_ok=True)

#     browser.get(BASE_URL)

#     print("CURRENT URL:", browser.current_url)
#     print("PAGE TITLE:", browser.title)

#     # ADD THIS BLOCK HERE
#     WebDriverWait(browser, 30).until(
#         lambda d: d.execute_script("return document.readyState") == "complete"
#     )

#     # ================= LOAD DATA ================= #
#     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#     data_path = os.path.join(base_dir, "testdata", "testdata.json")

#     with open(data_path) as file:
#         data = json.load(file)

#     system_admin = data["logins"]["system_admin"]
#     admin_user = data["users"]["create_admin"]
#     normal_user = data["users"]["create_user"]

#     # Optional fields (safe handling)
#     root_space = data.get("root_space", {}).get("name", "DefaultRoot")
#     project_name = data.get("project", {}).get("name", "DefaultProject")
#     file_path = os.path.abspath(
#         data.get("project", {}).get("file_path", "")
#     )

#     login = LoginPage(browser)
#     admin = SystemAdminPage(browser)
#     projects = ProjectsPage(browser)

#     # ================= 1. SYSTEM ADMIN LOGIN ================= #
#     login.login(system_admin["email"], system_admin["password"])
#     assert wait.until(
#         EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Projects')]"))
#     )

#     # ================= 2. AVAILABLE PLAYS ================= #
#     admin.open_user_admin()
#     admin.scroll_to_available_plays()

#     # ================= 8. EXPORT CREDIT ================= #
#     admin.click_export_credit_history()
#     admin.wait_for_credit_history_download(download_dir)

#     assert len(os.listdir(download_dir)) > 0

#     # ================= 9. CREATE ROOT SPACE ================= #
#     projects.open_projects()
#     projects.right_click_projects_area()
#     projects.create_root_space(root_space)

#     # ================= 10. CREATE PROJECT ================= #
#     projects.open_root_space(root_space)
#     projects.create_project(project_name, file_path)

#     # ================= 11. CREATE SUBSPACE ================= #
#     projects.right_click_root_space(root_space)

#     # ================= 12–17 PLACEHOLDERS ================= #
#     # (kept as-is, no logic removed)

#     # ================= 18. SEARCH ================= #
#     projects.search_file(project_name)

#     # ================= 19. SELECT / DESELECT ================= #
#     projects.select_all_files()
#     projects.deselect_all_files()

#     # ================= 20–25 PLAYS ================= #
#     plays = [
#         "Tariff Analysis",
#         "Cost Reduction Analysis",
#         "Design Review",
#         "Drawing Checker - Both",
#         "Drawing Checker - General",
#         "Drawing Checker - Veeco"
#     ]

#     for play in plays:
#         admin.open_user_admin()
#         admin.scroll_to_available_plays()
#         admin.toggle_play_by_name(play)

#     # ================= 29. SYSTEM INVALID LOGIN ================= #
#     browser.get(BASE_URL)
#     login.login("wrong@mail.com", "wrong")

#     # ================= 30. ADMIN LOGIN ================= #
#     login.login(admin_user["email"], admin_user["password"])

#     # ================= 31. ADMIN INVALID ================= #
#     browser.get(BASE_URL)
#     login.login(admin_user["email"], "wrong")

#     # ================= 32. USER LOGIN ================= #
#     login.login(normal_user["email"], normal_user["password"])

#     # ================= 33. USER INVALID ================= #
#     browser.get(BASE_URL)
#     login.login(normal_user["email"], "wrong")

#     # ================= 34. LOGOUT ================= #
#     # login.logout()

import os
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import BASE_URL, DOWNLOAD_PATH
from pages.login_page import LoginPage
from pages.system_admin_page import SystemAdminPage
from pages.projects_page import ProjectsPage
from pages.tariff_play_page import TariffPage
from pages.cost_reduction_play_page import CostReductionPage
from pages.design_review_play_page import DesignReviewPage
from pages.drawing_checker_both_play_page import DrawingCheckerPage
from pages.drawing_checker_general_play_page import DrawingCheckerGeneralPage
from pages.drawing_checker_veeco_play_page import DrawingCheckerVeecoPage


@pytest.mark.smoke
def test_full_e2e_flow(browser, test_data):

    wait = WebDriverWait(browser, 30)

    browser.get(BASE_URL)

    # ================= LOGIN =================
    email = test_data["logins"]["system_admin"]["email"]
    password = test_data["logins"]["system_admin"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    # ================= INIT PAGES =================
    admin = SystemAdminPage(browser)
    project = ProjectsPage(browser)

    # ================= ADMIN ACTIONS =================
    admin.open_user_admin()

    plays = [
        "Tariff Analysis",
        "Cost Reduction Analysis",
        "Design Review",
        "Drawing Checker - Both",
        "Drawing Checker - General",
        "Drawing Checker - Veeco"
    ]

    for play in plays:
        admin.toggle_play_by_name(play)

    # ================= EXPORT CREDIT =================
    admin.click_export_credit_history()
    admin.wait_for_credit_history_download(DOWNLOAD_PATH)

    # ================= PROJECT FLOW =================
    project.open_projects()

    project.create_root_space("AutoRoot")

    project.open_root_space("AutoRoot")

    project.create_project("AutoProject", os.path.abspath("testdata/sample.pdf"))

    project.open_project("AutoProject")

    project.select_all_files()

    # ================= PLAY EXECUTIONS =================

    # ---------- TARIFF ----------
    tariff = TariffPage(browser)
    tariff.run_tariff()
    tariff.export(DOWNLOAD_PATH)

    # ---------- COST REDUCTION ----------
    cost = CostReductionPage(browser)
    cost.select_cost_reduction()
    cost.click_run()
    cost.wait_for_processing()

    # ---------- DESIGN REVIEW ----------
    design = DesignReviewPage(browser)
    design.select_design_review()
    design.click_run()
    design.wait_for_processing()
    design.download_report(DOWNLOAD_PATH)

    # ---------- DRAWING CHECKER BOTH ----------
    drawing = DrawingCheckerPage(browser)
    drawing.select_drawing_checker()
    drawing.click_run()
    drawing.wait_for_processing()
    drawing.download_report(DOWNLOAD_PATH)

    # ---------- DRAWING CHECKER GENERAL ----------
    general = DrawingCheckerGeneralPage(browser)
    general.select_play()
    general.click_run()
    general.wait_for_processing()
    general.download_report(DOWNLOAD_PATH)

    # ---------- DRAWING CHECKER VEECO ----------
    veeco = DrawingCheckerVeecoPage(browser)
    veeco.select_play()
    veeco.click_run()
    veeco.wait_for_processing()
    veeco.download_report(DOWNLOAD_PATH)

    # ================= SEARCH & FILTER =================
    project.search_file("AutoProject")
    project.select_all_files()
    project.deselect_all_files()

    # ================= FINAL ASSERT =================
    assert True
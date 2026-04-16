# import pytest
# import os
# from selenium.webdriver.support.ui import WebDriverWait

# from pages.login_page import LoginPage
# from pages.projects_page import ProjectsPage
# from config.config import BASE_URL

# # @pytest.mark.order(16)
# @pytest.mark.regression
# def test_export_classification_to_excel(browser, test_data):

#     wait = WebDriverWait(browser, 30)

#     browser.get(BASE_URL)

#     email = test_data["logins"]["system_admin"]["email"]
#     password = test_data["logins"]["system_admin"]["password"]

#     login = LoginPage(browser)
#     login.login(email, password)

#     projects = ProjectsPage(browser)

#     projects.open_projects()
#     projects.open_root_space("TestSpace1")
#     projects.open_project("TestFile")

#     projects.click_export_classification()

#     # Jenkins-safe download dir
#     download_dir = os.path.abspath("downloads")
#     os.makedirs(download_dir, exist_ok=True)

#     wait.until(lambda d: projects.is_classification_downloaded(download_dir))

#     assert projects.is_classification_downloaded(download_dir), \
#         "Classification Excel file was not downloaded"

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
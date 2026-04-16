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
import json
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import BASE_URL
from pages.login_page import LoginPage
from pages.system_admin_page import SystemAdminPage
from pages.projects_page import ProjectsPage


def switch_to_login_context(browser):
 
    browser.switch_to.default_content()

    # Try direct first
    if browser.find_elements(By.ID, "email"):
        return

    # Try iframe
    iframes = browser.find_elements(By.TAG_NAME, "iframe")
    for frame in iframes:
        browser.switch_to.frame(frame)
        if browser.find_elements(By.ID, "email"):
            return
        browser.switch_to.default_content()


@pytest.mark.smoke
def test_full_e2e_flow(browser):

    wait = WebDriverWait(browser, 30)

    # Jenkins-safe download folder
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    browser.get(BASE_URL)

    print("CURRENT URL:", browser.current_url)
    print("PAGE TITLE:", browser.title)

    # Wait for page load
    WebDriverWait(browser, 30).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    # FINAL FIX: HANDLE iframe + WAIT
    switch_to_login_context(browser)

    WebDriverWait(browser, 40).until(
        EC.presence_of_element_located((By.ID, "email"))
    )

    # ================= LOAD DATA ================= #
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "testdata", "testdata.json")

    with open(data_path) as file:
        data = json.load(file)

    system_admin = data["logins"]["system_admin"]
    admin_user = data["users"]["create_admin"]
    normal_user = data["users"]["create_user"]

    root_space = data.get("root_space", {}).get("name", "DefaultRoot")
    project_name = data.get("project", {}).get("name", "DefaultProject")
    file_path = os.path.abspath(
        data.get("project", {}).get("file_path", "")
    )

    login = LoginPage(browser)
    admin = SystemAdminPage(browser)
    projects = ProjectsPage(browser)

    # ================= 1. SYSTEM ADMIN LOGIN ================= #
    login.login(system_admin["email"], system_admin["password"])

    assert wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(),'Projects')]")
        )
    )

    # ================= 2. AVAILABLE PLAYS ================= #
    admin.open_user_admin()
    admin.scroll_to_available_plays()

    # ================= 8. EXPORT CREDIT ================= #
    admin.click_export_credit_history()
    admin.wait_for_credit_history_download(download_dir)

    assert len(os.listdir(download_dir)) > 0

    # ================= 9. CREATE ROOT SPACE ================= #
    projects.open_projects()
    projects.right_click_projects_area()
    projects.create_root_space(root_space)

    # ================= 10. CREATE PROJECT ================= #
    projects.open_root_space(root_space)
    projects.create_project(project_name, file_path)

    # ================= 11. CREATE SUBSPACE ================= #
    projects.right_click_root_space(root_space)

    # ================= 18. SEARCH ================= #
    projects.search_file(project_name)

    # ================= 19. SELECT / DESELECT ================= #
    projects.select_all_files()
    projects.deselect_all_files()

    # ================= 20–25 PLAYS ================= #
    plays = [
        "Tariff Analysis",
        "Cost Reduction Analysis",
        "Design Review",
        "Drawing Checker - Both",
        "Drawing Checker - General",
        "Drawing Checker - Veeco"
    ]

    for play in plays:
        admin.open_user_admin()
        admin.scroll_to_available_plays()
        admin.toggle_play_by_name(play)

    # ================= 29. SYSTEM INVALID LOGIN ================= #
    browser.get(BASE_URL)

    WebDriverWait(browser, 30).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    switch_to_login_context(browser)

    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.ID, "email"))
    )

    login.login("wrong@mail.com", "wrong")

    # ================= 30. ADMIN LOGIN ================= #
    login.login(admin_user["email"], admin_user["password"])

    # ================= 31. ADMIN INVALID ================= #
    browser.get(BASE_URL)

    WebDriverWait(browser, 30).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    switch_to_login_context(browser)

    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.ID, "email"))
    )

    login.login(admin_user["email"], "wrong")

    # ================= 32. USER LOGIN ================= #
    login.login(normal_user["email"], normal_user["password"])

    # ================= 33. USER INVALID ================= #
    browser.get(BASE_URL)

    WebDriverWait(browser, 30).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    switch_to_login_context(browser)

    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.ID, "email"))
    )

    login.login(normal_user["email"], "wrong")

    # ================= 34. LOGOUT ================= #
    # login.logout()
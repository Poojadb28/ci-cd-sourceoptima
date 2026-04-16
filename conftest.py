# import pytest
# import os
# import json
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager


# # Base directory (IMPORTANT for Jenkins)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# # Test Data Fixture (GLOBAL)
# @pytest.fixture(scope="session")
# def test_data():
#     file_path = os.path.join(BASE_DIR, "testdata", "testdata.json")
#     with open(file_path) as file:
#         return json.load(file)


# @pytest.fixture(scope="function")
# def browser():

#     # Ensure downloads folder (Jenkins-safe path)
#     download_dir = os.path.join(BASE_DIR, "downloads")
#     os.makedirs(download_dir, exist_ok=True)

#     options = Options()

#     # Headless toggle (default TRUE for Jenkins)
#     if os.getenv("HEADLESS", "true").lower() == "true":
#         options.add_argument("--headless=new")

#     # Stability options (VERY IMPORTANT)
#     options.add_argument("--window-size=1920,1080")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")

#     options.add_argument("--remote-allow-origins=*")
#     options.add_argument("--disable-web-security")
#     options.add_argument("--user-data-dir=C:\\temp\\chrome-profile")

#     # Fix download issues in Jenkins
#     prefs = {
#         "download.prompt_for_download": False,
#         "download.default_directory": download_dir,
#         "safebrowsing.enabled": True
#     }
#     options.add_experimental_option("prefs", prefs)

#     # Use WebDriver Manager
#     service = Service(ChromeDriverManager().install())

#     driver = webdriver.Chrome(service=service, options=options)

#     # Implicit wait
#     driver.implicitly_wait(5)

#     yield driver

#     # Cleanup (VERY IMPORTANT)
#     driver.quit()

import pytest
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Base directory (IMPORTANT for Jenkins)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Test Data Fixture (GLOBAL)
@pytest.fixture(scope="session")
def test_data():
    file_path = os.path.join(BASE_DIR, "testdata", "testdata.json")
    with open(file_path) as file:
        return json.load(file)


@pytest.fixture(scope="function")
def browser():

    # Ensure downloads folder (Jenkins-safe path)
    download_dir = os.path.join(BASE_DIR, "downloads")
    os.makedirs(download_dir, exist_ok=True)

    options = Options()

    # Headless toggle (default TRUE for Jenkins)
    # if os.getenv("HEADLESS", "true").lower() == "true":
    #     options.add_argument("--headless=new")
    if os.getenv("HEADLESS", "false").lower() == "true":
        options.add_argument("--headless=new")

    # Stability options (VERY IMPORTANT)
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Jenkins-specific fixes (KEEP — already correct)
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--disable-web-security")
    options.add_argument("--user-data-dir=C:\\temp\\chrome-profile")

    # ADD THIS (fixes rendering issues in some Jenkins environments)
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Fix download issues in Jenkins
    prefs = {
        "download.prompt_for_download": False,
        "download.default_directory": download_dir,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)

    # Use WebDriver Manager
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)

    # Implicit wait (slightly safer for Jenkins)
    driver.implicitly_wait(10)

    # ADD THIS (ensures clean state)
    driver.delete_all_cookies()

    yield driver

    # Cleanup (VERY IMPORTANT)
    driver.quit()


# ADD THIS (for debugging failures in Jenkins)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            screenshots_dir = os.path.join(BASE_DIR, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            driver.save_screenshot(
                os.path.join(screenshots_dir, f"{item.name}.png")
            )
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():

    # Ensure downloads folder exists
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    options = Options()

    # Headless only in Jenkins (can toggle)
    if os.getenv("HEADLESS", "true").lower() == "true":
        options.add_argument("--headless=new")

    # Stability options (VERY IMPORTANT for Jenkins)
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Avoid download popup issues
    prefs = {
        "download.prompt_for_download": False,
        "download.default_directory": download_dir,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)

    # Use WebDriver Manager (NO hardcoded path)
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)

    # Optional implicit wait
    driver.implicitly_wait(5)

    driver.maximize_window()

    yield driver

    # Proper cleanup (important for Jenkins stability)
    driver.quit()
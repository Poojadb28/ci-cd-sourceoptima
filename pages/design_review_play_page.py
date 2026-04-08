import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config.config import TIMEOUT


class DesignReviewPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    # LOCATORS
    dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")
    option = (By.XPATH, "//option[normalize-space()='Design Review']")
    run_btn = (By.XPATH, "//button[contains(text(),'Run Design Review')]")
    view_results = (By.XPATH, "//button[normalize-space()='View Results']")
    view_details = (By.XPATH, "//button[normalize-space()='View Details']")

    popup_overlay = (By.XPATH, "//div[contains(@class,'fixed inset-0')]")

    download_btn = (By.XPATH, "//button[contains(@title,'Design Review')]")

    close_icon = (By.XPATH, "//button[contains(@class,'p-2')]")

    # ================= COMMON ================= #

    def safe_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    # ---------------- ACTIONS ----------------

    def select_design_review(self):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.dropdown))
        self.safe_click(dropdown)

        option = self.wait.until(EC.element_to_be_clickable(self.option))
        self.safe_click(option)

    def click_run(self):
        button = self.wait.until(EC.element_to_be_clickable(self.run_btn))
        self.safe_click(button)

    def wait_for_processing(self):
        self.wait.until(EC.element_to_be_clickable(self.view_details))

    def click_view_results(self):
        button = self.wait.until(EC.element_to_be_clickable(self.view_results))
        self.safe_click(button)

    def click_view_details(self):
        button = self.wait.until(EC.element_to_be_clickable(self.view_details))
        self.safe_click(button)

    def open_report_tab(self):
        popup = self.wait.until(EC.visibility_of_element_located(self.popup_overlay))
        tab = popup.find_element(By.XPATH, ".//button[normalize-space()='Design Review']")

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", tab)

        try:
            tab.click()
        except:
            print("Normal click failed, using Actions...")

            ActionChains(self.driver).move_to_element(tab).click().perform()

        try:
            self.wait.until(EC.presence_of_element_located(self.download_btn))
        except:
            self.driver.execute_script("arguments[0].click();", tab)

            self.wait.until(EC.presence_of_element_located(self.download_btn))

    def download_report(self, download_dir):

        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        element = self.wait.until(EC.element_to_be_clickable(self.download_btn))

        self.safe_click(element)

        WebDriverWait(self.driver, 60).until(
            lambda d: any(
                "design_review" in f.lower() and f.endswith(".xlsx")
                for f in os.listdir(download_dir)
            )
        )

        files = os.listdir(download_dir)
        print("Downloaded files:", files)

        assert any(
            "design_review" in f.lower() and f.endswith(".xlsx")
            for f in files
        ), "Design Review file not downloaded"

    def close_popup(self):

        element = self.wait.until(EC.element_to_be_clickable(self.close_icon))
        self.safe_click(element)

        self.wait.until(EC.element_to_be_clickable(self.dropdown))
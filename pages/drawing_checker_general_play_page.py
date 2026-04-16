import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config.config import TIMEOUT


class DrawingCheckerGeneralPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    # LOCATORS
    dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")
    option = (By.XPATH, "//option[normalize-space()='Drawing Checker - General']")
    run_btn = (By.XPATH, "//button[contains(text(),'Run Drawing Checker - General')]")
    view_results = (By.XPATH, "//button[normalize-space()='View Results']")
    view_details = (By.XPATH, "//button[normalize-space()='View Details']")

    popup_overlay = (By.XPATH, "//div[contains(@class,'fixed inset-0')]")

    report_tab = (By.XPATH, "//div[contains(@class,'fixed')]//button[normalize-space()='Drawing Checker - General']")
    download_btn = (By.XPATH, "//button[contains(@title,'Download Drawing Checker')]")

    close_icon = (By.XPATH, "//button[contains(@class,'p-2')]")

    # ================= COMMON ================= #

    def safe_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    # ---------------- ACTIONS ----------------

    def select_drawing_checker_general(self):
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
        popup = self.wait.until(
            EC.visibility_of_element_located(self.popup_overlay)
        )

        tab = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[.//text()[contains(.,'Drawing Checker - General')]]")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", tab
        )

        try:
            ActionChains(self.driver)\
                .move_to_element(tab)\
                .pause(1)\
                .click()\
                .perform()
        except:
            self.driver.execute_script("arguments[0].click();", tab)

        # VERIFY TAB SWITCH (NO sleep, replaced with wait)
        try:
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@title='Download Drawing Checker PDF Report']")
                )
            )
        except:
            self.driver.execute_script("arguments[0].click();", tab)

            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@title='Download Drawing Checker PDF Report']")
                )
            )

        buttons = self.driver.find_elements(
            By.XPATH, "//button[@title='Download Drawing Checker PDF Report']"
        )

        if len(buttons) == 0:
            raise Exception("Tab NOT switched → UI issue or wrong locator")

    def download_report(self, download_dir):

        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        before_files = set(os.listdir(download_dir))

        element = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@title,'Download Drawing Checker')]")
            )
        )

        self.safe_click(element)

        def file_downloaded(driver):
            after_files = set(os.listdir(download_dir))
            new_files = after_files - before_files
            return any(f.endswith(".pdf") for f in new_files)

        WebDriverWait(self.driver, 120).until(file_downloaded)

        after_files = set(os.listdir(download_dir))
        new_files = after_files - before_files

        assert any(f.endswith(".pdf") for f in new_files), \
            "File NOT downloaded"

    def close_popup(self):

        element = self.wait.until(EC.element_to_be_clickable(self.close_icon))
        self.safe_click(element)

        self.wait.until(EC.element_to_be_clickable(self.dropdown))


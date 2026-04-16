# import os
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from config.config import TIMEOUT


# class CostReductionPage:

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, TIMEOUT)

#     # LOCATORS
#     dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")
#     option = (By.XPATH, "//option[normalize-space()='Cost Reduction']")
#     run_button = (By.XPATH, "//button[contains(text(),'Run Cost Reduction')]")
#     view_results = (By.XPATH, "//button[normalize-space()='View Results']")
#     view_details = (By.XPATH, "//button[normalize-space()='View Details']")
#     report_tab = (By.XPATH, "//button[normalize-space()='Cost Reduction']")
#     popup_overlay = (By.XPATH, "//div[contains(@class,'fixed inset-0')]")
#     close_icon = (By.XPATH, "//button[contains(@class,'p-2')]")

#     # ================= COMMON ================= #

#     def safe_click(self, element):
#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
#         self.driver.execute_script("arguments[0].click();", element)

#     # ACTIONS

#     def select_cost_reduction(self):
#         dropdown = self.wait.until(EC.element_to_be_clickable(self.dropdown))
#         self.safe_click(dropdown)

#         option = self.wait.until(EC.element_to_be_clickable(self.option))
#         self.safe_click(option)

#     def click_run(self):
#         button = self.wait.until(EC.element_to_be_clickable(self.run_button))
#         self.safe_click(button)

#     def wait_for_processing(self):
#         self.wait.until(EC.element_to_be_clickable(self.view_details))

#     def click_view_results(self):
#         button = self.wait.until(EC.element_to_be_clickable(self.view_results))
#         self.safe_click(button)

#     def click_view_details(self):
#         button = self.wait.until(EC.element_to_be_clickable(self.view_details))
#         self.safe_click(button)

#     def open_report_tab(self):
#         self.wait.until(EC.visibility_of_element_located(self.popup_overlay))

#         element = self.wait.until(EC.element_to_be_clickable(self.report_tab))
#         self.safe_click(element)

#     def take_screenshot(self):

#         screenshot_dir = os.path.abspath("screenshots")
#         os.makedirs(screenshot_dir, exist_ok=True)

#         file_path = os.path.join(screenshot_dir, "Cost_Reduction_Report.png")
#         self.driver.save_screenshot(file_path)

#     def close_popup(self):
#         element = self.wait.until(EC.element_to_be_clickable(self.close_icon))
#         self.safe_click(element)

#         # Wait for underlying page to be clickable again
#         self.wait.until(EC.element_to_be_clickable(self.dropdown))

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import TIMEOUT


class CostReductionPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")
    option = (By.XPATH, "//option[normalize-space()='Cost Reduction']")
    run_button = (By.XPATH, "//button[contains(text(),'Run Cost Reduction')]")
    view_results = (By.XPATH, "//button[normalize-space()='View Results']")
    view_details = (By.XPATH, "//button[normalize-space()='View Details']")
    report_tab = (By.XPATH, "//button[normalize-space()='Cost Reduction']")
    popup_overlay = (By.XPATH, "//div[contains(@class,'fixed inset-0')]")
    close_icon = (By.XPATH, "//button[contains(@class,'p-2')]")

    def safe_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def select_cost_reduction(self):
        self.safe_click(self.dropdown)
        self.safe_click(self.option)

    def click_run(self):
        self.safe_click(self.run_button)

    def wait_for_processing(self):
        self.wait.until(EC.element_to_be_clickable(self.view_details))

    def click_view_results(self):
        self.safe_click(self.view_results)

    def click_view_details(self):
        self.safe_click(self.view_details)

    def open_report_tab(self):
        self.wait.until(EC.visibility_of_element_located(self.popup_overlay))
        self.safe_click(self.report_tab)

    def take_screenshot(self):
        path = os.path.abspath("screenshots/Cost_Reduction_Report.png")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.driver.save_screenshot(path)

    def close_popup(self):
        self.safe_click(self.close_icon)
        self.wait.until(EC.element_to_be_clickable(self.dropdown))
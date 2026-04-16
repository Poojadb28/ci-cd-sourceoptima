# import os
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from config.config import TIMEOUT


# class TariffPage:

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, TIMEOUT)

#     # ---------------- LOCATORS ----------------

#     dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")
#     tariff_option = (By.XPATH, "//option[normalize-space()='Tariff Analysis']")
#     treat_checkbox = (By.XPATH, "//input[contains(@class,'w-4 h-4')]")
#     set_top = (By.XPATH, "//button[normalize-space()='Set as Top Level']")
#     run_btn = (By.XPATH, "//button[contains(normalize-space(),'Run Tariff Analysis')]")

#     bom_export_btn = (By.XPATH, "(//button[normalize-space()='Export to Excel'])[1]")
#     tariff_export_btn = (By.XPATH, "(//button[normalize-space()='Export to Excel'])[2]")

#     approve_bom_btn = (By.XPATH, "//span[normalize-space()='Approve BOM']")
#     tariff_heading = (By.XPATH, "//h2[contains(text(),'Tariff Analysis')]")

#     back_project = (By.XPATH, "//span[normalize-space()='Back to Project']")
#     back_btn = (By.XPATH, "//span[normalize-space()='Back']")

#     # ---------------- COMMON ----------------

#     def safe_click(self, element):
#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
#         self.driver.execute_script("arguments[0].click();", element)

#     # ---------------- ACTIONS ----------------

#     def select_tariff_analysis(self):
#         dropdown = self.wait.until(EC.element_to_be_clickable(self.dropdown))
#         self.safe_click(dropdown)

#         option = self.wait.until(EC.element_to_be_clickable(self.tariff_option))
#         self.safe_click(option)

#     def treat_as_assembly(self):
#         checkbox = self.wait.until(EC.presence_of_element_located(self.treat_checkbox))
#         self.driver.execute_script("arguments[0].click();", checkbox)

#     def set_top_level(self):
#         elements = self.driver.find_elements(*self.set_top)
#         if elements:
#             self.safe_click(elements[0])

#     def run_tariff_analysis(self):
#         button = self.wait.until(EC.element_to_be_clickable(self.run_btn))
#         self.safe_click(button)

#     # ---------------- APPROVE BOM ----------------

#     def approve_bom(self):

#         element = self.wait.until(EC.element_to_be_clickable(self.approve_bom_btn))
#         self.safe_click(element)

#         old_button = self.wait.until(EC.presence_of_element_located(
#             (By.XPATH, "//button[normalize-space()='Export to Excel']")
#         ))

#         self.wait.until(EC.staleness_of(old_button))

#         self.wait.until(EC.presence_of_element_located(
#             (By.XPATH, "//button[normalize-space()='Export to Excel']")
#         ))

#     # ---------------- BOM EXPORT ----------------

#     def export_bom(self, download_dir):

#         if not os.path.exists(download_dir):
#             os.makedirs(download_dir)

#         before_files = set(os.listdir(download_dir))

#         button = WebDriverWait(self.driver, 180).until(
#             EC.element_to_be_clickable(self.bom_export_btn)
#         )

#         self.safe_click(button)

#         WebDriverWait(self.driver, 60).until(
#             lambda d: len(set(os.listdir(download_dir)) - before_files) > 0
#         )

#         after_files = set(os.listdir(download_dir))
#         new_files = after_files - before_files

#         print("BOM Downloaded:", new_files)

#         assert new_files, "BOM file not downloaded"

#     # ---------------- TARIFF EXPORT ----------------

#     def export_tariff(self, download_dir):

#         if not os.path.exists(download_dir):
#             os.makedirs(download_dir)

#         button = self.wait.until(EC.element_to_be_clickable(self.tariff_export_btn))
#         self.safe_click(button)

#         WebDriverWait(self.driver, 60).until(
#             lambda d: any(
#                 f.lower().endswith(".xlsx") and "tariff" in f.lower()
#                 for f in os.listdir(download_dir)
#             )
#         )

#         files = os.listdir(download_dir)

#         assert any(
#             "tariff" in f.lower() and f.endswith(".xlsx")
#             for f in files
#         ), "Tariff file not downloaded"

#     # ---------------- NAVIGATION ----------------

#     def go_back(self):
#         btn1 = self.wait.until(EC.element_to_be_clickable(self.back_project))
#         self.safe_click(btn1)

#         btn2 = self.wait.until(EC.element_to_be_clickable(self.back_btn))
#         self.safe_click(btn2)

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import TIMEOUT


class TariffPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")
    option = (By.XPATH, "//option[contains(text(),'Tariff')]")
    run_btn = (By.XPATH, "//button[contains(text(),'Run Tariff')]")
    export_btn = (By.XPATH, "//button[contains(text(),'Export')]")

    def safe_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def run_tariff(self):
        self.safe_click(self.dropdown)
        self.safe_click(self.option)
        self.safe_click(self.run_btn)

    def export(self, download_dir):
        before = set(os.listdir(download_dir))
        self.safe_click(self.export_btn)

        WebDriverWait(self.driver, 120).until(
            lambda d: len(set(os.listdir(download_dir)) - before) > 0
        )
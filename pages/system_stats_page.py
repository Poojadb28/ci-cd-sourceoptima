# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os


# class SystemStatsPage:

#     time_range_today = (By.XPATH, "//button[normalize-space()='Today']")
#     time_range_2_days = (By.XPATH, "//button[normalize-space()='2 days']")
#     time_range_3_days = (By.XPATH, "//button[normalize-space()='3 days']")
#     time_range_5_days = (By.XPATH, "//button[normalize-space()='5 days']")
#     time_range_7_days = (By.XPATH, "//button[normalize-space()='7 days']")

#     download_logs_button = (By.XPATH, "//button[normalize-space()='Download Logs (.txt)']")

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 20)

#     # ================= COMMON ================= #

#     def safe_click(self, locator):
#         element = self.wait.until(EC.element_to_be_clickable(locator))
#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
#         self.driver.execute_script("arguments[0].click();", element)

#     # ================= ACTIONS ================= #

#     def select_time_range(self, locator):
#         self.safe_click(locator)

#     def click_download_logs(self):
#         self.safe_click(self.download_logs_button)

#     # ================= DOWNLOAD VALIDATION ================= #

#     def wait_for_logs_download(self, download_dir):

#         if not os.path.exists(download_dir):
#             os.makedirs(download_dir)

#         self.wait.until(
#             lambda driver: any(
#                 f.lower().endswith(".txt")
#                 for f in os.listdir(download_dir)
#             )
#         )

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SystemStatsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    download_logs_button = (By.XPATH, "//button[contains(text(),'Download Logs')]")

    def safe_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def download_logs(self, download_dir):
        before = set(os.listdir(download_dir))

        self.safe_click(self.download_logs_button)

        WebDriverWait(self.driver, 120).until(
            lambda d: len(set(os.listdir(download_dir)) - before) > 0
        )

        assert any(f.endswith(".txt") for f in os.listdir(download_dir))
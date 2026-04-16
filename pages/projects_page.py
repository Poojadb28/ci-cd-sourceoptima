# import os
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from config.config import TIMEOUT


# class ProjectsPage:

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, TIMEOUT)

#     # ================= LOCATORS ================= #

#     projects_button = (By.XPATH, "//span[normalize-space()='Projects']")
#     page_body = (By.XPATH, "//div[contains(@class,'flex-1')]")

#     # Root Space
#     new_root_space_button = (By.XPATH, "//button[normalize-space()='New Root Space']")
#     space_name_field = (By.XPATH, "//input[@placeholder='e.g. Finance, Project Alpha...']")
#     icon_button = (By.XPATH, "//button[.//*[name()='svg']]")
#     blue_color = (By.XPATH, "//button[@title='Blue']")
#     create_space_button = (By.XPATH, "//button[normalize-space()='Create Space']")
#     success_message = (By.XPATH, "//div[contains(text(),'Space created')]")

#     # Project
#     new_upload_button = (By.XPATH, "//button[normalize-space()='New Upload']")
#     project_name_field = (By.XPATH, "//input[@placeholder='Enter project name']")
#     upload_input = (By.XPATH, "//input[@type='file']")
#     upload_button = (By.XPATH, "//button[normalize-space()='Upload']")

#     # Delete Project
#     delete_icon = (By.XPATH, "//button[@title='Delete project']")
#     confirm_delete_input = (By.XPATH, "//input[@placeholder='Type DELETE to confirm']")
#     delete_button = (By.XPATH, "//button[normalize-space()='Delete']")
#     delete_success_message = (By.XPATH, "//div[contains(text(),'Project deleted')]")

#     # Search / Filter
#     search_input = (By.XPATH, "//input[@placeholder='Search filename...']")
#     filter_dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")

#     # File selection
#     select_all_button = (By.XPATH, "//button[normalize-space()='Select All']")
#     deselect_all_button = (By.XPATH, "//button[normalize-space()='Deselect All']")

#     # ================= COMMON METHODS ================= #

#     # def safe_click(self, locator):
#     #     element = self.wait.until(EC.element_to_be_clickable(locator))
#     #     self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
#     #     self.driver.execute_script("arguments[0].click();", element)

#     def safe_click(self, locator):
#         element = self.wait.until(EC.presence_of_element_located(locator))

#         # Scroll to element (IMPORTANT FIX)
#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", element
#         )

#         # Extra wait for clickable
#         element = self.wait.until(EC.element_to_be_clickable(locator))

#         try:
#             element.click()
#         except:
#             self.driver.execute_script("arguments[0].click();", element)

#     def open_projects(self):
#         self.safe_click(self.projects_button)

#     def open_root_space(self, space_name):
#         locator = (By.XPATH, f"//h4[contains(text(),'{space_name}')]")
#         element = self.wait.until(EC.visibility_of_element_located(locator))
#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
#         self.driver.execute_script("arguments[0].click();", element)

#     def open_project(self, project_name):
#         locator = (By.XPATH, f"//h3[normalize-space()='{project_name}']")
#         element = self.wait.until(EC.visibility_of_element_located(locator))
#         self.driver.execute_script("arguments[0].click();", element)

#     # ================= ROOT SPACE ================= #

#     def right_click_projects_area(self):
#         area = self.wait.until(EC.visibility_of_element_located(self.page_body))
#         ActionChains(self.driver).context_click(area).perform()

#     def create_root_space(self, name):
#         self.safe_click(self.new_root_space_button)

#         field = self.wait.until(EC.visibility_of_element_located(self.space_name_field))
#         field.clear()
#         field.send_keys(name)

#         icon = self.wait.until(EC.element_to_be_clickable(self.icon_button))
#         self.driver.execute_script("arguments[0].click();", icon)

#         self.safe_click(self.blue_color)
#         self.safe_click(self.create_space_button)

#     def get_success_message(self):
#         return self.wait.until(EC.visibility_of_element_located(self.success_message)).text

#     # ================= PROJECT ================= #

#     def create_project(self, name, file_path):
#         self.safe_click(self.new_upload_button)

#         field = self.wait.until(EC.visibility_of_element_located(self.project_name_field))
#         field.clear()
#         field.send_keys(name)

#         # ✅ Jenkins-safe file path
#         file_path = os.path.abspath(file_path)

#         upload = self.wait.until(EC.presence_of_element_located(self.upload_input))
#         self.driver.execute_script("arguments[0].style.display='block';", upload)
#         upload.send_keys(file_path)

#         self.safe_click(self.upload_button)

#     def verify_project_created(self, name):
#         locator = (By.XPATH, f"//h3[normalize-space()='{name}']")
#         return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

#     # ================= DELETE PROJECT ================= #

#     def delete_project(self):
#         self.safe_click(self.delete_icon)

#         confirm = self.wait.until(EC.visibility_of_element_located(self.confirm_delete_input))
#         confirm.clear()
#         confirm.send_keys("DELETE")

#         self.safe_click(self.delete_button)

#     def verify_project_deleted(self):
#         return self.wait.until(EC.visibility_of_element_located(self.delete_success_message)).is_displayed()

#     # ================= SEARCH ================= #

#     def search_file(self, name):
#         box = self.wait.until(EC.visibility_of_element_located(self.search_input))
#         box.clear()
#         box.send_keys(name)

#     def verify_file_present(self, name):
#         locator = (By.XPATH, f"//*[contains(text(),'{name}')]")
#         return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

#     # ================= SELECT FILES ================= #

#     def select_all_files(self):
#         self.safe_click(self.select_all_button)

#     def deselect_all_files(self):
#         self.safe_click(self.deselect_all_button)

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import TIMEOUT


class ProjectsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    projects_button = (By.XPATH, "//span[normalize-space()='Projects']")
    new_upload_button = (By.XPATH, "//button[normalize-space()='New Upload']")
    project_name_field = (By.XPATH, "//input[@placeholder='Enter project name']")
    upload_input = (By.XPATH, "//input[@type='file']")
    upload_button = (By.XPATH, "//button[normalize-space()='Upload']")

    def safe_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def open_projects(self):
        self.safe_click(self.projects_button)

    def create_project(self, name, file_path):
        self.safe_click(self.new_upload_button)

        field = self.wait.until(EC.visibility_of_element_located(self.project_name_field))
        field.clear()
        field.send_keys(name)

        file_path = os.path.abspath(file_path)
        upload = self.wait.until(EC.presence_of_element_located(self.upload_input))
        self.driver.execute_script("arguments[0].style.display='block';", upload)
        upload.send_keys(file_path)

        self.safe_click(self.upload_button)
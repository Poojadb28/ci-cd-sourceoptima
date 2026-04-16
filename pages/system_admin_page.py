# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import os
# from config.config import TIMEOUT


# class SystemAdminPage:
   
#     # USER ADMIN NAVIGATION

#     user_admin_view = (By.XPATH, "//button[normalize-space()='User Admin View']")
#     create_user_button = (By.XPATH, "//button[normalize-space()='Create User']")
    
#     # CREATE USER FORM FIELDS

#     full_name = (By.XPATH, "//input[contains(@placeholder,'full name')]")
#     email = (By.XPATH, "//input[contains(@placeholder,'user@example.com')]")
#     password = (By.XPATH, "//input[contains(@placeholder,'Enter secure password')]")
#     confirm_password = (By.XPATH, "//input[contains(@placeholder,'Re-enter password')]")

#     role_dropdown = (By.XPATH, "//select[contains(@class,'w-full')]")

#     submit_button = (By.XPATH, "//button[@type='submit']")

#     # SUCCESS & ERROR MESSAGES

#     success_message = (By.XPATH, "//div[text()='User created successfully']")
#     duplicate_user_error = (By.XPATH, "//div[contains(text(),'Failed to create user')]")

#     # EXPORT CREDIT HISTORY
    
#     export_credit_history_button = (By.XPATH,"//button[normalize-space()='Export Credit History']")

#     # AVAILABLE PLAYS LOCATORS

#     available_plays_section = (By.XPATH, "//h2[normalize-space()='Available Plays']")
#     disable_success_message = (By.XPATH, "//div[contains(text(),'Play disabled successfully')]")
#     enable_success_message = (By.XPATH, "//div[contains(text(),'Play enabled successfully')]")

#     # INITIALIZATION

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, TIMEOUT)

#     # ================= COMMON ================= #

#     def safe_click(self, locator):
#         element = self.wait.until(EC.element_to_be_clickable(locator))
#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
#         self.driver.execute_script("arguments[0].click();", element)

#     # ================= NAVIGATION ================= #

#     def open_user_admin(self):
#         self.safe_click(self.user_admin_view)

#     def click_create_user(self):
#         self.safe_click(self.create_user_button)

#     # ================= ROLE SELECTION (NEW) ================= #

#     def select_role(self, role_name):
#         dropdown = self.wait.until(EC.element_to_be_clickable(self.role_dropdown))
#         dropdown.click()

#         option = self.wait.until(
#             EC.element_to_be_clickable(
#                 (By.XPATH, f"//option[normalize-space()='{role_name}']")
#             )
#         )
#         option.click()

#     # ================= CREATE USER ================= #

#     def fill_user_details(self, name, email, password, role):

#         field = self.wait.until(EC.visibility_of_element_located(self.full_name))
#         field.clear()
#         field.send_keys(name)

#         field = self.wait.until(EC.visibility_of_element_located(self.email))
#         field.clear()
#         field.send_keys(email)

#         field = self.wait.until(EC.visibility_of_element_located(self.password))
#         field.clear()
#         field.send_keys(password)

#         field = self.wait.until(EC.visibility_of_element_located(self.confirm_password))
#         field.clear()
#         field.send_keys(password)

#         self.select_role(role)

#     def submit_user(self):
#         self.safe_click(self.submit_button)

#     # ================= VALIDATION ================= #

#     def get_success_message(self):
#         return self.wait.until(EC.visibility_of_element_located(self.success_message)).text

#     def get_duplicate_user_error(self):
#         return self.wait.until(EC.visibility_of_element_located(self.duplicate_user_error)).text

#     # ================= EXPORT CREDIT HISTORY ================= #

#     def click_export_credit_history(self):
#         self.safe_click(self.export_credit_history_button)

#     def wait_for_credit_history_download(self, download_dir):

#         if not os.path.exists(download_dir):
#             os.makedirs(download_dir)

#         self.wait.until(
#             lambda driver: any(
#                 f.lower().startswith("credit_history")
#                 and f.lower().endswith(".xlsx")
#                 for f in os.listdir(download_dir)
#             )
#         )

#     # ================= AVAILABLE PLAYS ================= #

#     def scroll_to_available_plays(self):

#         section = self.wait.until(
#             EC.visibility_of_element_located(self.available_plays_section)
#         )

#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", section
#         )

#     def toggle_play_by_name(self, play_name):

#         toggle_button = self.wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     By.XPATH,
#                     f"//*[contains(text(),'{play_name}')]/ancestor::div[contains(@class,'rounded')]//button[contains(@class,'inline-flex')]"
#                 )
#             )
#         )

#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", toggle_button
#         )

#         self.driver.execute_script(
#             "arguments[0].click();", toggle_button
#         )

#     def get_disable_success_message(self):
#         return self.wait.until(
#             EC.visibility_of_element_located(self.disable_success_message)
#         ).text

#     def get_enable_success_message(self):
#         return self.wait.until(
#             EC.visibility_of_element_located(self.enable_success_message)
#         ).text

import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SystemAdminPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    # ================= LOCATORS ================= #

    # Navigation
    user_admin_view = (By.XPATH, "//button[normalize-space()='User Admin View']")
    create_user_button = (By.XPATH, "//button[normalize-space()='Create User']")

    # Form fields
    full_name = (By.XPATH, "//input[contains(@placeholder,'full name')]")
    email = (By.XPATH, "//input[contains(@placeholder,'user@example.com')]")
    password = (By.XPATH, "//input[contains(@placeholder,'Enter secure password')]")
    confirm_password = (By.XPATH, "//input[contains(@placeholder,'Re-enter password')]")

    role_dropdown = (By.XPATH, "//select[contains(@class,'w-full')]")

    submit_button = (By.XPATH, "//button[@type='submit']")

    # Messages
    success_message = (By.XPATH, "//div[contains(text(),'User created successfully')]")
    duplicate_user_error = (By.XPATH, "//div[contains(text(),'Failed to create user')]")

    # Export
    export_credit_history_button = (By.XPATH, "//button[normalize-space()='Export Credit History']")

    # Available Plays
    available_plays_section = (By.XPATH, "//h2[normalize-space()='Available Plays']")
    disable_success_message = (By.XPATH, "//div[contains(text(),'Play disabled successfully')]")
    enable_success_message = (By.XPATH, "//div[contains(text(),'Play enabled successfully')]")

    # ================= COMMON METHODS ================= #

    def safe_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    # ================= NAVIGATION ================= #

    def open_user_admin(self):

        # ✅ Wait for page load
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        # ✅ Click User Admin View
        self.safe_click(self.user_admin_view)

        # ✅ Ensure page loaded
        self.wait.until(EC.visibility_of_element_located(self.create_user_button))

    def click_create_user(self):
        self.safe_click(self.create_user_button)

        # Wait for form
        self.wait.until(EC.visibility_of_element_located(self.full_name))

    # ================= CREATE USER ================= #

    def fill_user_details(self, name, email, password, role):

        # Name
        name_field = self.wait.until(EC.visibility_of_element_located(self.full_name))
        name_field.clear()
        name_field.send_keys(name)

        # Email
        email_field = self.wait.until(EC.visibility_of_element_located(self.email))
        email_field.clear()
        email_field.send_keys(email)

        # Password
        password_field = self.wait.until(EC.visibility_of_element_located(self.password))
        password_field.clear()
        password_field.send_keys(password)

        # Confirm Password
        confirm_field = self.wait.until(EC.visibility_of_element_located(self.confirm_password))
        confirm_field.clear()
        confirm_field.send_keys(password)

        # Select role dynamically
        self.safe_click(self.role_dropdown)

        role_option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//option[contains(text(),'{role}')]")
            )
        )
        role_option.click()

    def submit_user(self):
        self.safe_click(self.submit_button)

    # ================= MODAL HANDLING ================= #

    def handle_modal_after_submit(self):

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[contains(text(),'user')]")
                )
            )
        except:
            pass

        try:
            close_btn = self.driver.find_element(
                By.XPATH, "//button[contains(text(),'Cancel') or contains(text(),'Close')]"
            )
            close_btn.click()
        except:
            pass

        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(
                    (By.XPATH, "//div[contains(@class,'fixed inset-0')]")
                )
            )
        except:
            pass

    # ================= VALIDATION ================= #

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success_message)
        ).text.strip()

    def get_duplicate_user_error(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.duplicate_user_error)
        ).text.strip()

    # ================= EXPORT ================= #

    def click_export_credit_history(self):
        self.safe_click(self.export_credit_history_button)

    def wait_for_credit_history_download(self, download_dir, timeout=60):

        end_time = time.time() + timeout

        while time.time() < end_time:
            files = os.listdir(download_dir)

            for f in files:
                file_lower = f.lower()

                if "credit_history" in file_lower and file_lower.endswith(".xlsx"):
                    return True

            time.sleep(1)

        raise Exception("Credit history file not downloaded")

    # ================= AVAILABLE PLAYS ================= #

    def scroll_to_available_plays(self):

        section = self.wait.until(
            EC.visibility_of_element_located(self.available_plays_section)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", section
        )

        time.sleep(1)

    def toggle_play_by_name(self, play_name):

        toggle_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//*[contains(text(),'{play_name}')]/ancestor::div[contains(@class,'rounded')]//button"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", toggle_button
        )

        time.sleep(1)

        try:
            toggle_button.click()
        except:
            self.driver.execute_script("arguments[0].click();", toggle_button)

    def get_disable_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.disable_success_message)
        ).text.strip()

    def get_enable_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.enable_success_message)
        ).text.strip()
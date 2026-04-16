# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from config.config import BASE_URL, TIMEOUT


# # class LoginPage:

# #     def __init__(self, driver):
# #         self.driver = driver
# #         self.wait = WebDriverWait(driver, TIMEOUT)

# #     # Locators
# #     USERNAME_INPUT = (By.ID, "username")
# #     PASSWORD_INPUT = (By.ID, "password")
# #     LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
# #     DASHBOARD_ELEMENT = (By.XPATH, "//div[contains(text(),'Dashboard')]")

# #     ERROR_MESSAGE = (By.XPATH, "//div[contains(@class,'error')]")

# #     # ================= COMMON ================= #

# #     def safe_click(self, locator):
# #         element = self.wait.until(EC.element_to_be_clickable(locator))
# #         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
# #         self.driver.execute_script("arguments[0].click();", element)

# #     # ================= ACTIONS ================= #

# #     # Open Application URL
# #     def open_url(self):
# #         self.driver.get(BASE_URL)

# #     # Enter Username
# #     def enter_username(self, username):
# #         element = self.wait.until(
# #             EC.visibility_of_element_located(self.USERNAME_INPUT)
# #         )
# #         element.clear()
# #         element.send_keys(username)

# #     # Enter Password
# #     def enter_password(self, password):
# #         element = self.wait.until(
# #             EC.visibility_of_element_located(self.PASSWORD_INPUT)
# #         )
# #         element.clear()
# #         element.send_keys(password)

# #     # Click Login
# #     def click_login(self):
# #         self.safe_click(self.LOGIN_BUTTON)

# #     # Complete Login Action
# #     def login(self, username, password):
# #         self.enter_username(username)
# #         self.enter_password(password)
# #         self.click_login()

# #     # ================= VALIDATION ================= #

# #     # Check Dashboard
# #     def is_dashboard_visible(self):
# #         return self.wait.until(
# #             EC.visibility_of_element_located(self.DASHBOARD_ELEMENT)
# #         ).is_displayed()

# #     # Negative Scenario (Invalid Login)
# #     def get_error_message(self):
# #         return self.wait.until(
# #             EC.visibility_of_element_located(self.ERROR_MESSAGE)
# #         ).text

# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from config.config import BASE_URL, TIMEOUT


# # class LoginPage:

# #     def __init__(self, driver):
# #         self.driver = driver
# #         self.wait = WebDriverWait(driver, TIMEOUT)

# #     # Locators
# #     USERNAME_INPUT = (By.ID, "username")
# #     PASSWORD_INPUT = (By.ID, "password")
# #     LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
# #     DASHBOARD_ELEMENT = (By.XPATH, "//div[contains(text(),'Dashboard')]")
# #     ERROR_MESSAGE = (By.XPATH, "//div[contains(@class,'error')]")

# #     # ================= COMMON ================= #

# #     def wait_for_page_load(self):
# #         self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

# #     def safe_click(self, locator):
# #         element = self.wait.until(EC.presence_of_element_located(locator))
# #         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

# #         try:
# #             element = self.wait.until(EC.element_to_be_clickable(locator))
# #             element.click()
# #         except:
# #             self.driver.execute_script("arguments[0].click();", element)

# #     # ================= ACTIONS ================= #

# #     # Open Application URL
# #     def open_url(self):
# #         self.driver.get(BASE_URL)
# #         self.wait_for_page_load()

# #     # Enter Username
# #     def enter_username(self, username):
# #         self.wait_for_page_load()

# #         element = self.wait.until(
# #             EC.presence_of_element_located(self.USERNAME_INPUT)
# #         )
# #         self.wait.until(EC.visibility_of(element))

# #         element.clear()
# #         element.send_keys(username)

# #     # Enter Password
# #     def enter_password(self, password):
# #         element = self.wait.until(
# #             EC.presence_of_element_located(self.PASSWORD_INPUT)
# #         )
# #         self.wait.until(EC.visibility_of(element))

# #         element.clear()
# #         element.send_keys(password)

# #     # Click Login
# #     def click_login(self):
# #         self.safe_click(self.LOGIN_BUTTON)

# #     # Complete Login Action
# #     def login(self, username, password):
# #         self.wait_for_page_load()
# #         self.enter_username(username)
# #         self.enter_password(password)
# #         self.click_login()

# #     # ================= VALIDATION ================= #

# #     # Check Dashboard
# #     def is_dashboard_visible(self):
# #         return self.wait.until(
# #             EC.visibility_of_element_located(self.DASHBOARD_ELEMENT)
# #         ).is_displayed()

# #     # Negative Scenario (Invalid Login)
# #     def get_error_message(self):
# #         return self.wait.until(
# #             EC.visibility_of_element_located(self.ERROR_MESSAGE)
# #         ).text

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import logging

# class LoginPage:

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 20)

#     def click_login_button(self):
#         try:
#             btn = self.wait.until(EC.element_to_be_clickable((
#                 By.XPATH,
#                 "//button[contains(.,'Login') or contains(.,'Sign') or contains(.,'Get Started')]"
#             )))
#             btn.click()
#         except Exception as e:
#             logging.error(f"Login button click failed: {e}")
#             raise

#     def enter_email(self, email):
#         field = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']")))
#         field.clear()
#         field.send_keys(email)

#     def enter_password(self, password):
#         field = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
#         field.clear()
#         field.send_keys(password)

#     def submit(self):
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

#     def login(self, email, password):
#         self.click_login_button()
#         self.enter_email(email)
#         self.enter_password(password)
#         self.submit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # LOCATORS
    login_button = (By.XPATH, "//a[normalize-space()='Login']")
    email_field = (By.ID, "email")
    password_field = (By.ID, "password")
    submit_button = (By.XPATH, "//button[normalize-space()='Submit']")
    error_message = (By.XPATH, "//div[text()='Error during login. Please try again.']")
    logout_button = (By.XPATH, "//button[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    # ===============================
    #  SAFE CLICK METHOD (IMPORTANT)
    # ===============================
    def safe_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    # ===============================
    # LOGIN METHODS
    # ===============================
    def click_login_button(self):
        self.safe_click(self.login_button)

    def enter_email(self, email):
        element = self.wait.until(EC.visibility_of_element_located(self.email_field))
        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(self.password_field))
        element.clear()
        element.send_keys(password)

    def click_submit(self):
        self.safe_click(self.submit_button)

    # ===============================
    #  COMPLETE LOGIN FLOW (FIXED)
    # ===============================
    def login(self, email, password):

        #  Wait page load
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        # Click login (if required)
        try:
            self.click_login_button()
        except:
            pass

        # Handle iframe (CRITICAL for your app)
        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        if iframes:
            self.driver.switch_to.frame(iframes[0])

        # Enter credentials
        self.enter_email(email)
        self.enter_password(password)


        #  Submit
        self.click_submit()

        # Switch back
        self.driver.switch_to.default_content()

    # ===============================
    # VALIDATION
    # ===============================
    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_message)).text

    def logout(self):
        self.safe_click(self.logout_button)
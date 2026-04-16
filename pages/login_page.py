# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from config.config import BASE_URL, TIMEOUT


# class LoginPage:

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, TIMEOUT)

#     # Locators
#     USERNAME_INPUT = (By.ID, "username")
#     PASSWORD_INPUT = (By.ID, "password")
#     LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
#     DASHBOARD_ELEMENT = (By.XPATH, "//div[contains(text(),'Dashboard')]")

#     ERROR_MESSAGE = (By.XPATH, "//div[contains(@class,'error')]")

#     # ================= COMMON ================= #

#     def safe_click(self, locator):
#         element = self.wait.until(EC.element_to_be_clickable(locator))
#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
#         self.driver.execute_script("arguments[0].click();", element)

#     # ================= ACTIONS ================= #

#     # Open Application URL
#     def open_url(self):
#         self.driver.get(BASE_URL)

#     # Enter Username
#     def enter_username(self, username):
#         element = self.wait.until(
#             EC.visibility_of_element_located(self.USERNAME_INPUT)
#         )
#         element.clear()
#         element.send_keys(username)

#     # Enter Password
#     def enter_password(self, password):
#         element = self.wait.until(
#             EC.visibility_of_element_located(self.PASSWORD_INPUT)
#         )
#         element.clear()
#         element.send_keys(password)

#     # Click Login
#     def click_login(self):
#         self.safe_click(self.LOGIN_BUTTON)

#     # Complete Login Action
#     def login(self, username, password):
#         self.enter_username(username)
#         self.enter_password(password)
#         self.click_login()

#     # ================= VALIDATION ================= #

#     # Check Dashboard
#     def is_dashboard_visible(self):
#         return self.wait.until(
#             EC.visibility_of_element_located(self.DASHBOARD_ELEMENT)
#         ).is_displayed()

#     # Negative Scenario (Invalid Login)
#     def get_error_message(self):
#         return self.wait.until(
#             EC.visibility_of_element_located(self.ERROR_MESSAGE)
#         ).text

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from config.config import BASE_URL, TIMEOUT


# class LoginPage:

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, TIMEOUT)

#     # Locators
#     USERNAME_INPUT = (By.ID, "username")
#     PASSWORD_INPUT = (By.ID, "password")
#     LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
#     DASHBOARD_ELEMENT = (By.XPATH, "//div[contains(text(),'Dashboard')]")
#     ERROR_MESSAGE = (By.XPATH, "//div[contains(@class,'error')]")

#     # ================= COMMON ================= #

#     def wait_for_page_load(self):
#         self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#     def safe_click(self, locator):
#         element = self.wait.until(EC.presence_of_element_located(locator))
#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

#         try:
#             element = self.wait.until(EC.element_to_be_clickable(locator))
#             element.click()
#         except:
#             self.driver.execute_script("arguments[0].click();", element)

#     # ================= ACTIONS ================= #

#     # Open Application URL
#     def open_url(self):
#         self.driver.get(BASE_URL)
#         self.wait_for_page_load()

#     # Enter Username
#     def enter_username(self, username):
#         self.wait_for_page_load()

#         element = self.wait.until(
#             EC.presence_of_element_located(self.USERNAME_INPUT)
#         )
#         self.wait.until(EC.visibility_of(element))

#         element.clear()
#         element.send_keys(username)

#     # Enter Password
#     def enter_password(self, password):
#         element = self.wait.until(
#             EC.presence_of_element_located(self.PASSWORD_INPUT)
#         )
#         self.wait.until(EC.visibility_of(element))

#         element.clear()
#         element.send_keys(password)

#     # Click Login
#     def click_login(self):
#         self.safe_click(self.LOGIN_BUTTON)

#     # Complete Login Action
#     def login(self, username, password):
#         self.wait_for_page_load()
#         self.enter_username(username)
#         self.enter_password(password)
#         self.click_login()

#     # ================= VALIDATION ================= #

#     # Check Dashboard
#     def is_dashboard_visible(self):
#         return self.wait.until(
#             EC.visibility_of_element_located(self.DASHBOARD_ELEMENT)
#         ).is_displayed()

#     # Negative Scenario (Invalid Login)
#     def get_error_message(self):
#         return self.wait.until(
#             EC.visibility_of_element_located(self.ERROR_MESSAGE)
#         ).text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import BASE_URL, TIMEOUT


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    # ================= LOCATORS ================= #

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    DASHBOARD_ELEMENT = (By.XPATH, "//div[contains(text(),'Dashboard')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class,'error')]")

    # ================= COMMON ================= #

    def wait_for_page_load(self):
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def safe_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )

        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    # ================= ACTIONS ================= #

    # Open Application URL
    def open_url(self):
        self.driver.get(BASE_URL)
        self.wait_for_page_load()

    # Enter Username
    def enter_username(self, username):
        self.wait_for_page_load()

        element = self.wait.until(
            EC.element_to_be_clickable(self.USERNAME_INPUT)
        )

        element.clear()
        element.send_keys(username)

    # Enter Password
    def enter_password(self, password):
        element = self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD_INPUT)
        )

        element.clear()
        element.send_keys(password)

    # Click Login
    def click_login(self):
        self.safe_click(self.LOGIN_BUTTON)

    # Complete Login Action
    def login(self, username, password):
        # Ensure login form is present before interacting
        self.wait.until(
            EC.presence_of_element_located(self.USERNAME_INPUT)
        )

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # ================= VALIDATION ================= #

    # Check Dashboard
    def is_dashboard_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.DASHBOARD_ELEMENT)
        ).is_displayed()

    # Negative Scenario (Invalid Login)
    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text
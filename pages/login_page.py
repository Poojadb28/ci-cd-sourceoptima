from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import BASE_URL, TIMEOUT


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    DASHBOARD_ELEMENT = (By.XPATH, "//div[contains(text(),'Dashboard')]")

    # Open Application URL
    def open_url(self):
        self.driver.get(BASE_URL)

    # Enter Username
    def enter_username(self, username):
        element = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        element.clear()
        element.send_keys(username)

    # Enter Password
    def enter_password(self, password):
        element = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        element.clear()
        element.send_keys(password)

    # Click Login
    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    # Complete Login Action
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # Validation: Check Dashboard
    def is_dashboard_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.DASHBOARD_ELEMENT)
        ).is_displayed()

    # Negative Scenario (Invalid Login)
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class,'error')]")

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text
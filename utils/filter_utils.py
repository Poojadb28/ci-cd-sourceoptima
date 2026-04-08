from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def apply_filter(browser, select_element, label_text):
    """
    React-safe dropdown selection
    """

    WebDriverWait(browser, 20).until(lambda d: select_element.is_displayed())

    browser.execute_script(
        """
        const select = arguments[0];
        const label = arguments[1];

        for (let option of select.options) {
            if (option.text.includes(label)) {
                select.value = option.value;
                select.dispatchEvent(new Event('change', { bubbles: true }));
                return true;
            }
        }
        return false;
        """,
        select_element,
        label_text
    )

    # Wait for UI to update after filter
    WebDriverWait(browser, 10).until(lambda d: True)


def safe_clear_filter(browser):
    """
    Click clear filter only if present
    """

    try:
        clear_btn = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@title='Clear filter']")
            )
        )

        browser.execute_script(
            "arguments[0].click();",
            clear_btn
        )

        # Wait for filter reset
        WebDriverWait(browser, 10).until(lambda d: True)

    except Exception as e:
        print(f"[INFO] Clear filter not found: {e}")
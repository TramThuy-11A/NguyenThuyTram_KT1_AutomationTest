# =============================================================================
# pages/base_page.py (Tương đương BasePage.java)
# Thao tác chung: wait, click, type, is_displayed, execute_script, v.v.
# =============================================================================

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class BasePage:
    """
    Lớp BasePage (tương đương BasePage.java).
    Cung cấp các hàm tương tác cơ bản có tích hợp WebDriverWait.
    """

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(
            driver,
            timeout,
            ignored_exceptions=[StaleElementReferenceException]
        )

    def open_url(self, url: str):
        self.driver.get(url)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_title(self) -> str:
        return self.driver.title

    def find_element(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_visible(self, locator: tuple):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator: tuple):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator: tuple):
        element = self.wait_clickable(locator)
        element.click()

    def type(self, locator: tuple, text: str):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self.wait_visible(locator).text

    def get_attribute(self, locator: tuple, attribute: str) -> str:
        return self.find_element(locator).get_attribute(attribute)

    def is_displayed(self, locator: tuple, timeout: int = 3) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_checked(self, locator: tuple) -> bool:
        return self.find_element(locator).is_selected()

    def scroll_into_view(self, locator: tuple):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def execute_script(self, script: str, *args):
        return self.driver.execute_script(script, *args)

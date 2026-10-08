# =============================================================================
# pages/login_page.py (Tương đương LoginPage.java)
# Quản lý Locators và tương tác trên màn hình Đăng nhập UTC
# =============================================================================

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object cho trang Login (vanphongdientu.utc.edu.vn/Login).
    """

    # --- Locators ---
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "userpwd")
    REMEMBER_ME_CB = (By.ID, "persistent")
    REMEMBER_ME_LABEL = (By.CSS_SELECTOR, "label.check")
    SUBMIT_BTN = (By.CSS_SELECTOR, "input.submit_login")
    EMAIL_UTC_BTN = (By.CSS_SELECTOR, "a.button")
    FORGOT_PW_LINK = (By.CSS_SELECTOR, "div.helps a")
    LOGO_IMG = (By.CSS_SELECTOR, "div.left img")
    FORM_CONTAINER = (By.CSS_SELECTOR, "div.form")
    PAGE_BODY = (By.TAG_NAME, "body")
    ERROR_MSG = (By.CSS_SELECTOR, "div.form .alert, div.form .error, .error-msg, div.form > *:first-child")
    SUPPORT_LINK = (By.CSS_SELECTOR, "div.footer a[href*='hotrokythuat']")
    FEEDBACK_LINK = (By.CSS_SELECTOR, "div.footer a[href*='mailto']")

    # --- Actions ---
    def open(self, url="https://vanphongdientu.utc.edu.vn/Login"):
        self.open_url(url)
        self.wait_visible(self.USERNAME_INPUT)
        return self

    def input_username(self, username: str):
        self.type(self.USERNAME_INPUT, username)

    def input_password(self, password: str):
        self.type(self.PASSWORD_INPUT, password)

    def clear_username(self):
        self.wait_visible(self.USERNAME_INPUT).clear()

    def clear_password(self):
        self.wait_visible(self.PASSWORD_INPUT).clear()

    def click_login(self):
        self.click(self.SUBMIT_BTN)

    def login(self, username: str, password: str):
        self.input_username(username)
        self.input_password(password)
        self.click_login()

    def press_enter_on_password(self):
        self.wait_visible(self.PASSWORD_INPUT).send_keys(Keys.RETURN)

    def click_remember_me(self):
        try:
            self.click(self.REMEMBER_ME_LABEL)
        except Exception:
            # Fallback nếu label bị ẩn hoặc tương tác trực tiếp checkbox
            cb = self.find_element(self.REMEMBER_ME_CB)
            self.execute_script("arguments[0].click();", cb)

    def is_remember_me_checked(self) -> bool:
        return self.is_checked(self.REMEMBER_ME_CB)

    def click_email_utc_login(self):
        self.click(self.EMAIL_UTC_BTN)

    def get_email_utc_href(self) -> str:
        return self.get_attribute(self.EMAIL_UTC_BTN, "href")

    def click_forgot_password(self):
        self.click(self.FORGOT_PW_LINK)

    def get_forgot_password_href(self) -> str:
        return self.get_attribute(self.FORGOT_PW_LINK, "href")

    def get_error_message(self) -> str:
        try:
            return self.get_text(self.ERROR_MSG)
        except TimeoutException:
            return self.get_text(self.PAGE_BODY)

    def get_password_field_type(self) -> str:
        return self.get_attribute(self.PASSWORD_INPUT, "type")

    def is_logo_displayed(self) -> bool:
        return self.is_displayed(self.LOGO_IMG)

    def get_logo_src(self) -> str:
        return self.get_attribute(self.LOGO_IMG, "src")

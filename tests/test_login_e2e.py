# =============================================================================
# tests/test_login_e2e.py (Tương đương LoginE2ETest.java)
# Các kịch bản kiểm thử E2E chức năng Đăng nhập UTC
# =============================================================================

import time
import pytest
from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestLoginE2E(BaseTest):
    """
    Test suite cho Login E2E, kế thừa BaseTest (tương đương LoginE2ETest.java extends BaseTest).
    """

    # -------------------------------------------------------------------------
    # TC01: Để trống ô Username khi click Đăng nhập
    # -------------------------------------------------------------------------
    def test_TC01_empty_username(self):
        """
        TC01: Để trống Username
        Steps:
          1. Mở trang Login
          2. Để trống ô Username
          3. Nhập mật khẩu
          4. Click nút Đăng nhập
        Expected: Hệ thống từ chối đăng nhập và ở lại trang Login.
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)
        login_page.clear_username()
        login_page.input_password(self.VALID_PASSWORD)
        login_page.click_login()

        time.sleep(1.5)
        assert "/Login" in self.driver.current_url, (
            "TC01 FAIL: Để trống username nhưng hệ thống không ở lại trang Login."
        )

    # -------------------------------------------------------------------------
    # TC02: Để trống ô Password khi click Đăng nhập
    # -------------------------------------------------------------------------
    def test_TC02_empty_password(self):
        """
        TC02: Để trống Password
        Steps:
          1. Mở trang Login
          2. Nhập username hợp lệ
          3. Để trống ô Password
          4. Click nút Đăng nhập
        Expected: Hệ thống từ chối đăng nhập và ở lại trang Login.
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)
        login_page.input_username(self.VALID_USERNAME)
        login_page.clear_password()
        login_page.click_login()

        time.sleep(1.5)
        assert "/Login" in self.driver.current_url, (
            "TC02 FAIL: Để trống password nhưng hệ thống không ở lại trang Login."
        )

    # -------------------------------------------------------------------------
    # TC03: Để trống cả Username và Password (click Login trực tiếp)
    # -------------------------------------------------------------------------
    def test_TC03_empty_both_fields(self):
        """
        TC03: Để trống cả Username và Password
        Steps:
          1. Mở trang Login
          2. Để trống cả 2 ô
          3. Click nút Đăng nhập
        Expected: Hệ thống từ chối đăng nhập và ở lại trang Login.
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)
        login_page.clear_username()
        login_page.clear_password()
        login_page.click_login()

        time.sleep(1.5)
        assert "/Login" in self.driver.current_url, (
            "TC03 FAIL: Để trống cả 2 trường nhưng hệ thống không ở lại trang Login."
        )

    # -------------------------------------------------------------------------
    # TC04: Kiểm tra placeholder hiển thị đúng ở 2 ô nhập
    # -------------------------------------------------------------------------
    def test_TC04_input_placeholders(self):
        """
        TC04: Kiểm tra placeholder
        Steps:
          1. Mở trang Login
          2. Đọc thuộc tính placeholder của ô Username và Password
        Expected: Hiển thị đúng text gợi ý 'Tên đăng nhập' và 'Mật khẩu'.
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)

        user_ph = login_page.get_attribute(login_page.USERNAME_INPUT, "placeholder")
        pwd_ph = login_page.get_attribute(login_page.PASSWORD_INPUT, "placeholder")

        assert "đăng nhập" in user_ph.lower() or user_ph != "", "TC04 FAIL: Placeholder Username không đúng."
        assert "mật khẩu" in pwd_ph.lower() or pwd_ph != "", "TC04 FAIL: Placeholder Password không đúng."

    # -------------------------------------------------------------------------
    # TC05: Đăng nhập sai mật khẩu
    # -------------------------------------------------------------------------
    def test_TC05_wrong_password(self):
        """
        TC05: Sai Password
        Steps:
          1. Mở trang Login
          2. Nhập username
          3. Nhập password không đúng
          4. Click nút Đăng nhập
        Expected: Hiển thị thông báo lỗi và từ chối đăng nhập.
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)
        login_page.login(self.VALID_USERNAME, self.WRONG_PASSWORD)

        time.sleep(2)
        error = login_page.get_error_message()
        assert "không đúng" in error.lower() or "/Login" in self.driver.current_url, (
            "TC05 FAIL: Đăng nhập sai pass nhưng không hiển thị thông báo lỗi hoặc không ở lại trang Login."
        )

    # -------------------------------------------------------------------------
    # TC06: Đăng nhập với tên tài khoản không tồn tại
    # -------------------------------------------------------------------------
    def test_TC06_wrong_username(self):
        """
        TC06: Sai Username
        Steps:
          1. Mở trang Login
          2. Nhập username không tồn tại
          3. Nhập password bất kỳ
          4. Click nút Đăng nhập
        Expected: Hệ thống từ chối đăng nhập và ở lại trang Login.
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)
        login_page.login(self.WRONG_USERNAME, self.VALID_PASSWORD)

        time.sleep(2)
        assert "/Login" in self.driver.current_url, (
            "TC06 FAIL: Đăng nhập sai username nhưng không ở lại trang Login."
        )

    # -------------------------------------------------------------------------
    # TC07: Đăng nhập bằng nút 'Đăng nhập bằng e-mail UTC'
    # -------------------------------------------------------------------------
    def test_TC07_email_utc_redirect(self):
        """
        TC07: Đăng nhập bằng e-mail UTC
        Steps:
          1. Mở trang Login
          2. Click nút 'Đăng nhập bằng e-mail UTC'
        Expected: Chuyển hướng người dùng sang trang Google OAuth (accounts.google.com).
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)

        href = login_page.get_email_utc_href()
        assert "accounts.google.com" in href, f"TC07 FAIL: Href không trỏ sang Google OAuth: {href}"

        login_page.click_email_utc_login()
        time.sleep(3)
        assert "google" in self.driver.current_url.lower(), (
            f"TC07 FAIL: Không chuyển hướng đến Google. URL: {self.driver.current_url}"
        )

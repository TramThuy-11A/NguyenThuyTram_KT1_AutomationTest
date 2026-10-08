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

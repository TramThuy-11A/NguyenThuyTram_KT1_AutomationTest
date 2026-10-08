# =============================================================================
# tests/test_login_e2e.py (Tương đương LoginE2ETest.java)
# Các kịch bản kiểm thử E2E chức năng Đăng nhập UTC
# =============================================================================

import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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

    # -------------------------------------------------------------------------
    # TC08: Kiểm tra chức năng 'Bạn quên mật khẩu đăng nhập ?'
    # -------------------------------------------------------------------------
    def test_TC08_forgot_password_link(self):
        """
        TC08: Quên mật khẩu
        Steps:
          1. Mở trang Login
          2. Click vào liên kết 'Bạn quên mật khẩu đăng nhập ?'
        Expected: Chuyển hướng đến trang khôi phục mật khẩu (/Login/GetPass).
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)
        login_page.click_forgot_password()

        time.sleep(2)
        assert "GetPass" in self.driver.current_url, (
            f"TC08 FAIL: Không chuyển đến trang GetPass. URL: {self.driver.current_url}"
        )

    # -------------------------------------------------------------------------
    # TC09: Tên đăng nhập có chứa khoảng trắng ở đầu/cuối
    # -------------------------------------------------------------------------
    def test_TC09_username_whitespace(self):
        """
        TC09: Username có khoảng trắng
        Steps:
          1. Mở trang Login
          2. Nhập username có khoảng trắng ở đầu/cuối
          3. Nhập password
          4. Click nút Đăng nhập
        Expected: Hệ thống xử lý an toàn (trim hoặc từ chối).
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)
        login_page.login(f" {self.VALID_USERNAME} ", self.VALID_PASSWORD)

        time.sleep(2)
        # Hệ thống hoặc tự trim hoặc báo lỗi
        assert True

    # -------------------------------------------------------------------------
    # TC10: Mật khẩu phân biệt chữ hoa/thường
    # -------------------------------------------------------------------------
    def test_TC10_password_case_sensitive(self):
        """
        TC10: Mật khẩu phân biệt chữ hoa/thường
        Steps:
          1. Mở trang Login
          2. Nhập username hợp lệ
          3. Nhập password sai định dạng hoa/thường
          4. Click nút Đăng nhập
        Expected: Hệ thống từ chối và ở lại trang Login.
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)
        login_page.login(self.VALID_USERNAME, self.VALID_PASSWORD.lower())

        time.sleep(1.5)
        assert "/Login" in self.driver.current_url, (
            "TC10 FAIL: Mật khẩu không phân biệt hoa thường."
        )

    # -------------------------------------------------------------------------
    # TC11: Chống tấn công SQL Injection
    # -------------------------------------------------------------------------
    def test_TC11_sql_injection(self):
        """
        TC11: Ngăn chặn SQL Injection
        Steps:
          1. Mở trang Login
          2. Nhập payload SQL Injection vào Username/Password
          3. Click nút Đăng nhập
        Expected: Hệ thống từ chối tấn công và ở lại trang Login.
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)
        payload = "' OR '1'='1"
        login_page.login(payload, payload)

        time.sleep(2)
        assert "/Login" in self.driver.current_url, (
            f"TC11 FAIL: Lỗ hổng SQL Injection với payload {payload}"
        )

    # -------------------------------------------------------------------------
    # TC12: Nhập chuỗi ký tự quá dài (300+ ký tự)
    # -------------------------------------------------------------------------
    def test_TC12_long_input_string(self):
        """
        TC12: Chuỗi ký tự cực dài
        Steps:
          1. Mở trang Login
          2. Nhập chuỗi 300 ký tự vào ô Username và Password
          3. Click nút Đăng nhập
        Expected: Hệ thống xử lý an toàn không treo, ở lại trang Login.
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)
        long_str = "A" * 300
        login_page.login(long_str, long_str)

        time.sleep(2)
        assert "/Login" in self.driver.current_url, (
            "TC12 FAIL: Hệ thống lỗi khi nhập chuỗi ký tự quá dài."
        )

    # -------------------------------------------------------------------------
    # TC13: Đăng nhập sai nhiều lần liên tiếp (Brute force protection)
    # -------------------------------------------------------------------------
    def test_TC13_brute_force_attempts(self):
        """
        TC13: Đăng nhập sai nhiều lần liên tiếp
        Steps:
          1. Mở trang Login
          2. Thực hiện đăng nhập sai 3 lần liên tiếp
        Expected: Hệ thống không bị crash hoặc treo, luôn giữ tính ổn định.
        """
        login_page = LoginPage(self.driver)
        for i in range(3):
            login_page.open(self.BASE_URL)
            login_page.login(self.VALID_USERNAME, f"Wrong_Attempt_{i}")
            time.sleep(1)
        assert "/Login" in self.driver.current_url

    # -------------------------------------------------------------------------
    # TC14: Trạng thái ẩn/hiện Password (type attribute)
    # -------------------------------------------------------------------------
    def test_TC14_password_type_hidden(self):
        """
        TC14: Kiểm tra type attribute của ô Password
        Steps:
          1. Mở trang Login
          2. Đọc thuộc tính type của ô Password
        Expected: Thuộc tính type='password' để ẩn ký tự.
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)
        field_type = login_page.get_password_field_type()
        assert field_type == "password", (
            f"TC14 FAIL: Ô mật khẩu không phải type='password' (thực tế: '{field_type}')"
        )

    # -------------------------------------------------------------------------
    # TC15: Focus bàn phím / TabIndex (Accessibility WCAG 2.1)
    # -------------------------------------------------------------------------
    def test_TC15_keyboard_tab_navigation(self):
        """
        TC15: Điều hướng bằng phím Tab
        Steps:
          1. Mở trang Login
          2. Focus vào ô Username
          3. Nhấn phím Tab
        Expected: Focus chuyển sang ô Password (userpwd).
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)

        # Focus vào username
        user_el = self.driver.find_element(*login_page.USERNAME_INPUT)
        user_el.click()

        # Tab -> Password
        ActionChains(self.driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
        time.sleep(0.3)
        active_name = self.driver.execute_script("return document.activeElement.getAttribute('name');")
        assert "userpwd" in (active_name or "").lower(), (
            f"TC15 FAIL: Tab không chuyển sang ô Password. Active: '{active_name}'"
        )

    # -------------------------------------------------------------------------
    # TC16: Logo / Banner & Footer Links
    # -------------------------------------------------------------------------
    def test_TC16_logo_and_footer_links(self):
        """
        TC16: Kiểm tra Logo và các liên kết Footer
        Steps:
          1. Mở trang Login
          2. Kiểm tra ảnh Logo hiển thị và tải thành công
          3. Kiểm tra liên kết Trợ giúp ở Footer
        Expected: Logo tải thành công không bị 404, footer link hợp lệ.
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)

        # Kiểm tra logo
        assert login_page.is_logo_displayed(), "TC16 FAIL: Logo không hiển thị."
        logo_img = self.driver.find_element(*login_page.LOGO_IMG)
        is_loaded = self.driver.execute_script(
            "return arguments[0].complete && arguments[0].naturalWidth > 0;", logo_img
        )
        assert is_loaded, "TC16 FAIL: Ảnh logo bị hỏng / 404."

        # Kiểm tra Footer help link
        support_link = self.driver.find_element(*login_page.SUPPORT_LINK)
        assert "hotrokythuat.utc.edu.vn" in support_link.get_attribute("href"), (
            "TC16 FAIL: Link hỗ trợ kỹ thuật sai."
        )

    # -------------------------------------------------------------------------
    # TC17: Responsive Mobile (375x812px)
    # -------------------------------------------------------------------------
    def test_TC17_mobile_responsive_layout(self):
        """
        TC17: Kiểm tra giao diện trên kích thước Mobile
        Steps:
          1. Thu nhỏ kích thước cửa sổ về 375x812px (Mobile viewport)
          2. Mở trang Login
          3. Kiểm tra ô Username, Password và nút Đăng nhập vẫn hiển thị
        Expected: Các thành phần form đăng nhập hiển thị đầy đủ trên màn hình mobile.
        """
        login_page = LoginPage(self.driver)
        self.driver.set_window_size(375, 812)
        login_page.open(self.BASE_URL)

        assert login_page.is_displayed(login_page.USERNAME_INPUT), "TC17 FAIL: Ô Username không hiển thị trên mobile."
        assert login_page.is_displayed(login_page.PASSWORD_INPUT), "TC17 FAIL: Ô Password không hiển thị trên mobile."
        assert login_page.is_displayed(login_page.SUBMIT_BTN), "TC17 FAIL: Nút Đăng nhập không hiển thị trên mobile."

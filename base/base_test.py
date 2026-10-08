# =============================================================================
# base/base_test.py (Tương đương BaseTest.java)
# Khởi tạo WebDriver, timeout, setup/teardown cho các Test Script
# =============================================================================

import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:
    """
    Lớp BaseTest (tương đương BaseTest.java).
    Mọi class test kế thừa BaseTest để tự động có driver, cấu hình timeout và setup/teardown.
    """
    driver = None
    BASE_URL = "https://vanphongdientu.utc.edu.vn/Login"
    FORGOT_PASS_URL = "https://vanphongdientu.utc.edu.vn/Login/GetPass"
    
    # Credentials mẫu (dùng cho test)
    VALID_USERNAME = "test_user_placeholder"
    VALID_PASSWORD = "test_password_placeholder"
    WRONG_USERNAME = "wrong_user_xyz"
    WRONG_PASSWORD = "WrongPass!999"

    # Timeouts
    IMPLICIT_WAIT = 5
    EXPLICIT_WAIT = 10
    PAGE_LOAD_TIMEOUT = 30
    HEADLESS = False

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, request):
        """
        Setup trước mỗi test method:
        - Khởi tạo Chrome WebDriver
        - Cấu hình timeouts
        - Điều hướng đến BASE_URL
        Teardown sau test:
        - Tự động chụp ảnh nếu test FAIL
        - Đóng browser (quit)
        """
        # --- SETUP ---
        options = ChromeOptions()
        if self.HEADLESS:
            options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(self.IMPLICIT_WAIT)
        self.driver.set_page_load_timeout(self.PAGE_LOAD_TIMEOUT)

        # Gán driver vào class instance để test method truy cập self.driver
        request.cls.driver = self.driver

        yield

        # --- TEARDOWN ---
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            shot_path = os.path.join("screenshots", f"FAIL_{request.node.name}_{timestamp}.png")
            self.driver.save_screenshot(shot_path)
            print(f"\n[FAIL SCREENSHOT] Đã lưu tại: {shot_path}")

        if self.driver:
            self.driver.quit()

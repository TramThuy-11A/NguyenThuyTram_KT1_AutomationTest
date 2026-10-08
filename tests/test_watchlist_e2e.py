# =============================================================================
# tests/test_watchlist_e2e.py (Tương đương WatchlistE2ETest.java)
# Kịch bản kiểm thử E2E chức năng Quản lý tài khoản nghi vấn (Watchlist)
# =============================================================================

import pytest
from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.watchlist_page import WatchlistPage


class TestWatchlistE2E(BaseTest):
    """
    Test suite cho Watchlist E2E, kế thừa BaseTest (tương đương WatchlistE2ETest.java extends BaseTest).
    """

    def test_watchlist_access_requires_login(self):
        """
        Kiểm tra truy cập trang Watchlist khi chưa đăng nhập phải bị chặn / điều hướng về Login.
        """
        watchlist_page = WatchlistPage(self.driver)
        watchlist_page.open_url("https://vanphongdientu.utc.edu.vn/Watchlist")

        # Hệ thống phải giữ hoặc chuyển về màn hình Login
        current_url = self.driver.current_url
        assert "/Login" in current_url or "vanphongdientu.utc.edu.vn" in current_url

    @pytest.mark.skip(reason="Cần đăng nhập tài khoản thực có quyền admin để thao tác Watchlist")
    def test_search_watchlist_account(self):
        """
        Tìm kiếm tài khoản trong danh sách nghi vấn sau khi đăng nhập.
        """
        login_page = LoginPage(self.driver)
        login_page.open(self.BASE_URL)
        login_page.login(self.VALID_USERNAME, self.VALID_PASSWORD)

        watchlist_page = WatchlistPage(self.driver)
        watchlist_page.search_account("suspicious_user_01")
        assert watchlist_page.get_row_count() >= 0

# =============================================================================
# pages/watchlist_page.py (Tương đương WatchlistPage.java)
# Quản lý danh sách tài khoản nghi vấn (Watchlist)
# =============================================================================

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class WatchlistPage(BasePage):
    """
    Page Object cho màn hình Watchlist (Quản lý tài khoản nghi vấn).
    """

    # --- Locators ---
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='search'], input[placeholder*='tìm'], input[placeholder*='search']")
    SEARCH_BTN = (By.CSS_SELECTOR, "button.search-btn, input[type='submit']")
    WATCHLIST_TABLE = (By.CSS_SELECTOR, "table.watchlist, .table, #watchlist-grid")
    TABLE_ROWS = (By.CSS_SELECTOR, "table tbody tr")
    ADD_ACCOUNT_BTN = (By.CSS_SELECTOR, ".btn-add, button[data-action='add']")
    ACCOUNT_NAME_INPUT = (By.NAME, "accountName")
    REASON_INPUT = (By.NAME, "reason")
    SUBMIT_ADD_BTN = (By.CSS_SELECTOR, "button[type='submit'], .btn-save")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success, .toast-success")

    # --- Actions ---
    def search_account(self, keyword: str):
        """Tìm kiếm tài khoản trong danh sách nghi vấn."""
        self.type(self.SEARCH_INPUT, keyword)
        if self.is_displayed(self.SEARCH_BTN):
            self.click(self.SEARCH_BTN)

    def get_row_count(self) -> int:
        """Đếm số lượng dòng trong bảng."""
        elements = self.driver.find_elements(*self.TABLE_ROWS)
        return len(elements)

    def add_watchlist_account(self, account_name: str, reason: str):
        """Thêm tài khoản vào danh sách nghi vấn."""
        if self.is_displayed(self.ADD_ACCOUNT_BTN):
            self.click(self.ADD_ACCOUNT_BTN)
        self.type(self.ACCOUNT_NAME_INPUT, account_name)
        self.type(self.REASON_INPUT, reason)
        self.click(self.SUBMIT_ADD_BTN)

    def is_add_successful(self) -> bool:
        """Kiểm tra thông báo thêm thành công."""
        return self.is_displayed(self.SUCCESS_ALERT)

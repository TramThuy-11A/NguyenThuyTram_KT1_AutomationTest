# =============================================================================
# pages/dashboard_page.py (Tương đương DashboardPage.java)
# Quản lý giao diện Dashboard: Menu, Header, Thông tin User
# =============================================================================

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """
    Page Object cho trang Dashboard / Trang chủ sau khi đăng nhập.
    """

    # --- Locators ---
    HEADER_TITLE = (By.CSS_SELECTOR, "header, .header, .navbar-brand, .title")
    USER_PROFILE_NAME = (By.CSS_SELECTOR, ".user-info, .profile-name, .username, #user-name")
    NAV_MENU = (By.CSS_SELECTOR, "nav, .sidebar, .main-menu, ul.menu")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a[href*='logout'], a[href*='Logout'], .btn-logout")
    WATCHLIST_MENU_ITEM = (By.CSS_SELECTOR, "a[href*='watchlist'], a[href*='Watchlist']")

    # --- Actions ---
    def is_dashboard_loaded(self) -> bool:
        """Kiểm tra xem URL đã thoát khỏi trang /Login hay chưa."""
        return "/Login" not in self.get_current_url()

    def get_user_display_name(self) -> str:
        """Lấy tên user hiển thị trên header."""
        if self.is_displayed(self.USER_PROFILE_NAME):
            return self.get_text(self.USER_PROFILE_NAME)
        return ""

    def click_logout(self):
        """Đăng xuất khỏi hệ thống."""
        if self.is_displayed(self.LOGOUT_BTN):
            self.click(self.LOGOUT_BTN)

    def navigate_to_watchlist(self):
        """Điều hướng sang màn hình Watchlist từ menu chính."""
        if self.is_displayed(self.WATCHLIST_MENU_ITEM):
            self.click(self.WATCHLIST_MENU_ITEM)

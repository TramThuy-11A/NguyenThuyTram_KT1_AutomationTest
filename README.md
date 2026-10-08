# E2E Automation Testing Framework (Python + Selenium)

Dự án được xây dựng chuẩn theo mô hình kiến trúc Page Object Model (POM) và kế thừa `BaseTest`:

## 📁 Cấu trúc thư mục (Ánh xạ chuẩn theo sơ đồ kiến trúc)

```text
e2e/
|-- base/
|   |-- base_test.py         # Khởi tạo WebDriver, timeout, setup/teardown (tương đương BaseTest.java)
|-- pages/                   # CÁC PAGE OBJECTS
|   |-- base_page.py         # Thao tác chung: wait, click, type (tương đương BasePage.java)
|   |-- login_page.py        # Form đăng nhập (tương đương LoginPage.java)
|   |-- watchlist_page.py    # Quản lý tài khoản nghi vấn (tương đương WatchlistPage.java)
|   |-- dashboard_page.py    # Menu, header, thông tin user (tương đương DashboardPage.java)
|-- tests/                   # CÁC TEST SCRIPTS
|   |-- test_login_e2e.py    # Test suite Đăng nhập TC1 - TC20 (tương đương LoginE2ETest.java)
|   |-- test_watchlist_e2e.py # Test suite Watchlist E2E (tương đương WatchlistE2ETest.java)
|-- reports/                 # Báo cáo test_report.html tự động sinh
|-- screenshots/             # Ảnh chụp màn hình khi test thất bại
|-- pytest.ini               # Cấu hình Pytest
```

## 🚀 Hướng dẫn thực thi

Mở Terminal / PowerShell và di chuyển vào thư mục:

```powershell
cd C:\SeleniumTest\e2e
```

### 1. Chạy toàn bộ các kịch bản kiểm thử:
```powershell
pytest
```

### 2. Chạy riêng bộ kiểm thử Login (TC1 - TC20):
```powershell
pytest tests/test_login_e2e.py -v
```

### 3. Chạy riêng bộ kiểm thử Watchlist:
```powershell
pytest tests/test_watchlist_e2e.py -v
```

### 4. Chạy một Test Case cụ thể (ví dụ TC17):
```powershell
pytest tests/test_login_e2e.py::TestLoginE2E::test_TC17_password_field_type_hidden -v
```

### 5. Xem báo cáo kiểm thử HTML:
Sau khi chạy xong, mở file:
```powershell
start reports\test_report.html
```

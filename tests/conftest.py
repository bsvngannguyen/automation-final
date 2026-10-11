import pytest
from playwright.sync_api import Page

from tests.support import BASE_URL, login_as_admin


@pytest.fixture
def app(page: Page) -> Page:
    """Mở trang bài tập. Mỗi test nhận một trang mới, chưa đăng nhập."""
    page.goto(BASE_URL)
    return page


@pytest.fixture
def admin(app: Page) -> Page:
    """Đăng nhập bằng admin/admin123. Dữ liệu được tạo lại mỗi lần đăng nhập."""
    login_as_admin(app)
    return app

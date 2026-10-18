"""Fixture dùng chung. File này là config, nên nằm ngoài folder tests."""

import pytest
from allure_commons import plugin_manager
from allure_commons.model2 import Attachment
from allure_commons.types import AttachmentType
from allure_commons.utils import uuid4
from allure_pytest.listener import AllureListener
from playwright.sync_api import Error, Page

from pages.login_page import LoginPage
from tests.support import URL


@pytest.fixture
def app(page: Page) -> Page:
    """Mở trang bài tập. Mỗi test nhận một trang mới, chưa đăng nhập."""
    page.goto(URL)
    return page


@pytest.fixture
def admin(app: Page) -> Page:
    """Đăng nhập bằng tài khoản trong file .env. Dữ liệu được tạo lại mỗi lần đăng nhập."""
    LoginPage(app).login_as_admin()
    return app


def capture_screenshot(page: Page) -> bytes | None:
    """Chụp toàn màn hình. Trả về None nếu trang đã đóng."""
    try:
        return page.screenshot(full_page=True)
    except Error:
        return None


def _allure_listener() -> AllureListener | None:
    for plugin in plugin_manager.get_plugins():
        if isinstance(plugin, AllureListener):
            return plugin
    return None


def _page_from(item: pytest.Item) -> Page | None:
    funcargs = getattr(item, "funcargs", {})
    for name in ("page", "admin", "app"):
        page = funcargs.get(name)
        if isinstance(page, Page):
            return page
    return None


def attach_screenshot_to_last_step(item: pytest.Item, png: bytes) -> None:
    """Gắn ảnh vào step cuối của test. Không gắn lên chính test case."""
    listener = _allure_listener()
    if listener is None:
        return
    test_result = listener.allure_logger.get_test(listener._cache.get(item.nodeid))
    if test_result is None or not test_result.steps:
        return
    file_name = f"{uuid4()}-attachment.png"
    test_result.steps[-1].attachments.append(
        Attachment(name="screenshot", source=file_name, type=AttachmentType.PNG.mime_type)
    )
    plugin_manager.hook.report_attached_data(body=png, file_name=file_name)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Chụp ảnh và gắn vào step cuối, kể cả khi test fail."""
    outcome = yield
    report = outcome.get_result()
    if report.when != "call":
        return
    page = _page_from(item)
    if page is None:
        return
    png = capture_screenshot(page)
    if png:
        attach_screenshot_to_last_step(item, png)

"""Case 79 — chuyển sang màn thống kê."""

import re

import allure
from playwright.sync_api import Page, expect

from tests.support import open_tab


@allure.feature("統計画面")
@allure.story("遷移画面")
@allure.title("GD01_005: 統計タブで統計画面に切り替わる")
def test_gd01_005_open_stats(admin: Page) -> None:
    """Case 79: bấm tab 統計 thì sang màn thống kê, danh sách ticket bị ẩn."""
    open_tab(admin, "統計")

    expect(admin.locator("#nav_tab_stats")).to_have_class(re.compile(r"nav-tab--active"))
    expect(admin.get_by_role("heading", name="統計")).to_be_visible()
    expect(admin.get_by_role("heading", name="チケット一覧")).to_be_hidden()

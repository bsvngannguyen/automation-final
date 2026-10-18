"""Case 79 — chuyển sang màn thống kê."""

import allure
from playwright.sync_api import Page

from pages.stats_page import StatsPage
from tests.support import description_md


@allure.feature("統計画面")
@allure.story("遷移画面")
@allure.title("GD01_005: 統計タブで統計画面に切り替わる")
@description_md(
    """
    - **前提条件**: ログイン済み
    - **テスト手順**: 1. ヘッダーの「統計」タブを押下する
    - **期待する結果**: 統計画面に遷移し、チケット一覧画面が非表示になる
    """
)
def test_gd01_005_open_stats(admin: Page) -> None:
    """Case 79: bấm tab 統計 thì sang màn thống kê, danh sách ticket bị ẩn."""
    StatsPage(admin).expect_open()

"""Case 8 — ô chữ ký ở màn cài đặt."""

import allure
from playwright.sync_api import Page

from pages.settings_page import SettingsPage
from tests.support import description_md


@allure.feature("設定画面")
@allure.story("文字数カウンター")
@allure.title("GD02.3-001: 署名は100文字で止まりカウンターが100/100になる")
@description_md(
    """
    - **前提条件**: 設定画面を表示中
    - **テスト手順**: 1. 署名欄に100文字を超えるテキストを入力しようとする
    - **期待する結果**: 最大100文字までしか入力できず、カウンター表示が「100/100文字」で止まる
    """
)
def test_gd02_3_001_signature_counter(admin: Page) -> None:
    """Case 8: gõ quá 100 ký tự thì ô ký dừng ở 100 và bộ đếm là 100/100文字."""
    SettingsPage(admin).expect_signature_stops_at_100()

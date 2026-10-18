"""Case 47 — form tạo thông báo."""

import allure
from playwright.sync_api import Page

from pages.notification_page import NotificationPage
from tests.support import description_md


@allure.feature("通知画面")
@allure.story("作成ボタンの非活性")
@allure.title("GD02.8-05: 未入力だと通知の作成ボタンが非活性")
@description_md(
    """
    - **前提条件**: 通知作成モーダルを表示中
    - **テスト手順**: 1. タイトルまたは内容を未入力のままにする
    - **期待する結果**: 「作成する」ボタンが非活性のままである
    """
)
def test_gd02_8_05_notification_create_disabled(admin: Page) -> None:
    """Case 47: để trống tiêu đề và nội dung thì nút 作成する bị khóa."""
    NotificationPage(admin).expect_create_disabled_when_empty()

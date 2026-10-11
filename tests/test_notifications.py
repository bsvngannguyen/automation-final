"""Case 47 — form tạo thông báo."""

import allure
from playwright.sync_api import Page, expect

from tests.support import open_tab


@allure.feature("通知画面")
@allure.story("作成ボタンの非活性")
@allure.title("GD02.8-05: 未入力だと通知の作成ボタンが非活性")
def test_gd02_8_05_notification_create_disabled(admin: Page) -> None:
    """Case 47: để trống tiêu đề và nội dung thì nút 作成する bị khóa.

    Nút 作成する còn có ở màn tạo ticket, nên chỉ tìm trong dialog đang mở.
    """
    open_tab(admin, "通知")
    admin.get_by_role("button", name="通知を作成する").click()

    dialog = admin.get_by_role("dialog", name="通知を作成")
    expect(dialog.get_by_label("タイトル")).to_have_value("")
    expect(dialog.get_by_label("内容")).to_have_value("")
    expect(dialog.get_by_role("button", name="作成する")).to_be_disabled()

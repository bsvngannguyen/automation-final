"""Hàm dùng chung cho các test.

Thứ tự chọn locator (theo rule bài tập):
1. role + chữ trên màn hình
2. label / placeholder
3. id
4. class
"""

from playwright.sync_api import Page, expect

BASE_URL = "https://bsv-nhungnguyen.github.io/bai_tap_17082026.html"

ADMIN_ID = "admin"
ADMIN_PASSWORD = "admin123"
ADMIN_NAME = "田中 太郎（管理者）"


def login_as_admin(page: Page) -> None:
    page.get_by_label("ID", exact=True).fill(ADMIN_ID)
    page.get_by_label("パスワード", exact=True).fill(ADMIN_PASSWORD)
    page.get_by_role("button", name="ログイン").click()
    expect(page.get_by_role("heading", name="チケット一覧")).to_be_visible()


def open_tab(page: Page, name: str) -> None:
    """Bấm tab trên header.

    Chữ 「設定」 và 「通知」 còn xuất hiện ở menu user và trong form,
    nên chỉ tìm trong thanh tab #nav_tabs.
    """
    page.locator("#nav_tabs").get_by_text(name, exact=True).click()

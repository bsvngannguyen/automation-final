"""Case 26, 20, 7, 21, 30 — danh sách ticket."""

import re

import allure
from playwright.sync_api import Page, expect

from tests.support import ADMIN_NAME


@allure.feature("チケット一覧画面")
@allure.story("遷移画面")
@allure.title("GD01_003: ログイン後にチケットが10件表示される")
def test_gd01_003_ticket_list_after_login(admin: Page) -> None:
    """Case 26: sau khi đăng nhập, tab ticket đang mở và bảng hiện 10 dòng."""
    expect(admin.locator("#nav_tab_tickets")).to_have_class(re.compile(r"nav-tab--active"))
    expect(admin.get_by_role("heading", name="チケット一覧")).to_be_visible()
    expect(admin.locator("#ticket_tbody tr")).to_have_count(10)
    expect(admin.locator("#pagination_summary_top")).to_have_text("12件中 1 - 10件目")


@allure.feature("チケット一覧画面")
@allure.story("検索結果0件")
@allure.title("GD02.8-01: 存在しないキーワードでは該当なしと表示される")
def test_gd02_8_01_ticket_search_empty(admin: Page) -> None:
    """Case 20: tìm từ không có thì hiện thông báo không có ticket phù hợp."""
    tickets = admin.locator("#panel_tickets")
    tickets.get_by_placeholder("件名または担当者で検索").fill("zzzz-not-found")
    tickets.get_by_role("button", name="検索").click()

    expect(tickets.get_by_text("該当するチケットがありません")).to_be_visible()


@allure.feature("チケット一覧画面")
@allure.story("優先度絞り込み")
@allure.title("GD02.4-02: 優先度「高」は5件だけ表示される")
def test_gd02_4_02_filter_priority_high(admin: Page) -> None:
    """Case 7: chọn ưu tiên 高 thì chỉ còn 5 ticket mức cao."""
    admin.get_by_label("優先度で絞り込み").select_option(label="優先度：高")

    rows = admin.locator("#ticket_tbody tr")
    expect(rows).to_have_count(5)
    for index in range(5):
        expect(rows.nth(index).locator(".priority-high")).to_have_text("高")


@allure.feature("チケット一覧画面")
@allure.story("ユーザーメニューを閉じる")
@allure.title("GD02.1-07: メニューの外を押すとユーザーメニューが閉じる")
def test_gd02_1_07_close_user_menu(admin: Page) -> None:
    """Case 21: mở menu user rồi bấm ra ngoài thì menu đóng."""
    menu = admin.locator("#user_menu_content")
    admin.get_by_role("button", name=ADMIN_NAME).click()

    expect(menu.get_by_role("button", name="設定")).to_be_visible()
    expect(menu.get_by_role("button", name="ヘルプ")).to_be_visible()
    expect(menu.get_by_role("button", name="ログアウト")).to_be_visible()

    admin.get_by_role("heading", name="チケット一覧").click()
    expect(menu).to_be_hidden()


@allure.feature("チケット一覧画面")
@allure.story("ツールチップ表示")
@allure.title("GD02.5-001: 作成日のヘルプに説明が表示される")
def test_gd02_5_001_created_date_tooltip(admin: Page) -> None:
    """Case 30: đưa chuột vào icon ? cạnh 作成日 thì thấy tooltip.

    Chỉ hover icon. Bấm vào tiêu đề cột sẽ đổi thứ tự sắp xếp.
    Không kiểm tra cả chữ của ô tiêu đề, vì icon sort bị dính vào text.
    """
    help_icon = admin.locator("#th_created .tooltip-wrap")
    help_icon.hover()
    expect(help_icon.locator(".tooltip-content")).to_have_text(
        "チケットが作成された日付を表示します"
    )

"""Case 26, 20, 7, 21, 30 — danh sách ticket."""

import allure
from playwright.sync_api import Page

from pages.ticket_page import TicketPage
from pages.user_menu import UserMenu
from tests.support import description_md


@allure.feature("チケット一覧画面")
@allure.story("遷移画面")
@allure.title("GD01_003: ログイン後にチケットが10件表示される")
@description_md(
    """
    - **前提条件**: admin/admin123でログイン済み
    - **テスト手順**: 1. 画面表示を確認する
    - **期待する結果**: チケット一覧画面（「チケット一覧」タブがアクティブ）が表示され、10件のチケットが表示される
    """
)
def test_gd01_003_ticket_list_after_login(admin: Page) -> None:
    """Case 26: sau khi đăng nhập, tab ticket đang mở và bảng hiện 10 dòng."""
    TicketPage(admin).expect_default_list()


@allure.feature("チケット一覧画面")
@allure.story("検索結果0件")
@allure.title("GD02.8-01: 存在しないキーワードでは該当なしと表示される")
@description_md(
    """
    - **前提条件**: チケット一覧画面を表示中
    - **テスト手順**:
        1. 検索欄に存在しないキーワードを入力する
        2. 「検索」ボタンを押下する
    - **期待する結果**: 「該当するチケットがありません」というメッセージが表示される
    """
)
def test_gd02_8_01_ticket_search_empty(admin: Page) -> None:
    """Case 20: tìm từ không có thì hiện thông báo không có ticket phù hợp."""
    TicketPage(admin).expect_search_empty()


@allure.feature("チケット一覧画面")
@allure.story("優先度絞り込み")
@allure.title("GD02.4-02: 優先度「高」は5件だけ表示される")
@description_md(
    """
    - **前提条件**: チケット一覧画面を表示中
    - **テスト手順**: 1. 優先度プルダウンで「高」を選択する
    - **期待する結果**: 優先度が「高」のチケットのみ表示される（5件）
    """
)
def test_gd02_4_02_filter_priority_high(admin: Page) -> None:
    """Case 7: chọn ưu tiên 高 thì chỉ còn 5 ticket mức cao."""
    TicketPage(admin).expect_only_high_priority()


@allure.feature("チケット一覧画面")
@allure.story("ユーザーメニューを閉じる")
@allure.title("GD02.1-07: メニューの外を押すとユーザーメニューが閉じる")
@description_md(
    """
    - **前提条件**: ユーザーメニューを表示中
    - **テスト手順**: 1. メニュー外の任意の場所を押下する
    - **期待する結果**: ユーザーメニューが閉じる
    """
)
def test_gd02_1_07_close_user_menu(admin: Page) -> None:
    """Case 21: mở menu user rồi bấm ra ngoài thì menu đóng."""
    UserMenu(admin).expect_closes_when_clicking_outside()


@allure.feature("チケット一覧画面")
@allure.story("ツールチップ表示")
@allure.title("GD02.5-001: 作成日のヘルプに説明が表示される")
@description_md(
    """
    - **前提条件**: チケット一覧画面を表示中
    - **テスト手順**: 1. 「作成日」列見出し横のヘルプアイコン（?）にカーソルを合わせる
    - **期待する結果**: 「チケットが作成された日付を表示します」という説明テキストが表示される
    """
)
def test_gd02_5_001_created_date_tooltip(admin: Page) -> None:
    """Case 30: đưa chuột vào icon ? cạnh 作成日 thì thấy tooltip."""
    TicketPage(admin).expect_created_date_tooltip()

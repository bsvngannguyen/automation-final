"""Locator tập trung, tách khỏi test script.

Thứ tự chọn locator (theo rule bài tập):
1. role + chữ trên màn hình
2. label / placeholder
3. id
4. class
"""

from playwright.sync_api import Locator, Page

ADMIN_NAME = "田中 太郎（管理者）"


class LoginLocators:
    def __init__(self, page: Page) -> None:
        self.heading = page.get_by_role("heading", name="ログイン")
        self.id_input = page.get_by_label("ID", exact=True)
        self.password_input = page.get_by_label("パスワード", exact=True)
        self.submit = page.get_by_role("button", name="ログイン")
        self.error = page.get_by_text("IDまたはパスワードが正しくありません。")
        self.main_section = page.locator("#main_section")


class TicketLocators:
    def __init__(self, page: Page) -> None:
        self.heading = page.get_by_role("heading", name="チケット一覧")
        self.tab = page.locator("#nav_tab_tickets")
        self.rows = page.locator("#ticket_tbody tr")
        self.pagination_summary = page.locator("#pagination_summary_top")
        self.panel = page.locator("#panel_tickets")
        self.search_input = self.panel.get_by_placeholder("件名または担当者で検索")
        self.search_button = self.panel.get_by_role("button", name="検索")
        self.empty_message = self.panel.get_by_text("該当するチケットがありません")
        self.priority_filter = page.get_by_label("優先度で絞り込み")
        self.created_help = page.locator("#th_created .tooltip-wrap")
        self.created_tooltip = self.created_help.locator(".tooltip-content")

    def priority_high(self, index: int) -> Locator:
        return self.rows.nth(index).locator(".priority-high")


class UserMenuLocators:
    def __init__(self, page: Page) -> None:
        self.button = page.get_by_role("button", name=ADMIN_NAME)
        self.content = page.locator("#user_menu_content")
        self.settings = self.content.get_by_role("button", name="設定")
        self.help = self.content.get_by_role("button", name="ヘルプ")
        self.logout = self.content.get_by_role("button", name="ログアウト")


class NavLocators:
    def __init__(self, page: Page) -> None:
        self.tabs = page.locator("#nav_tabs")

    def tab(self, name: str) -> Locator:
        return self.tabs.get_by_text(name, exact=True)


class NotificationLocators:
    def __init__(self, page: Page) -> None:
        self.open_button = page.get_by_role("button", name="通知を作成する")
        self.dialog = page.get_by_role("dialog", name="通知を作成")
        self.title = self.dialog.get_by_label("タイトル")
        self.body = self.dialog.get_by_label("内容")
        self.create_button = self.dialog.get_by_role("button", name="作成する")


class SettingsLocators:
    def __init__(self, page: Page) -> None:
        self.heading = page.get_by_role("heading", name="設定")
        self.signature = page.get_by_label("署名")
        self.signature_counter = page.locator("#signature_counter")


class StatsLocators:
    def __init__(self, page: Page) -> None:
        self.tab = page.locator("#nav_tab_stats")
        self.heading = page.get_by_role("heading", name="統計")
        self.ticket_heading = page.get_by_role("heading", name="チケット一覧")

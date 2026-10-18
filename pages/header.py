"""Thao tác trên header, dùng chung cho các màn sau khi đăng nhập."""

import allure
from playwright.sync_api import Page

from tests.locators import NavLocators


class Header:
    def __init__(self, page: Page) -> None:
        self.page = page

    @allure.step("Mở tab trên header")
    def open_tab(self, name: str) -> None:
        """Chữ 「設定」 và 「通知」 còn xuất hiện ở menu user và trong form,
        nên chỉ tìm trong thanh tab #nav_tabs.
        """
        NavLocators(self.page).tab(name).click()

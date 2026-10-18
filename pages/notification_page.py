"""Thao tác trên màn thông báo."""

import allure
from playwright.sync_api import Page, expect

from pages.header import Header
from tests.locators import NotificationLocators


class NotificationPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = NotificationLocators(page)

    @allure.step("Mở modal tạo thông báo")
    def open_create_dialog(self) -> None:
        """Nút 作成する còn có ở màn tạo ticket, nên chỉ tìm trong dialog đang mở."""
        Header(self.page).open_tab("通知")
        self.locators.open_button.click()

    @allure.step("Kiểm tra để trống thì nút tạo thông báo bị khóa")
    def expect_create_disabled_when_empty(self) -> None:
        self.open_create_dialog()
        expect(self.locators.title).to_have_value("")
        expect(self.locators.body).to_have_value("")
        expect(self.locators.create_button).to_be_disabled()

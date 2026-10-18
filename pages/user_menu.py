"""Thao tác trên user menu."""

import allure
from playwright.sync_api import Page, expect

from tests.locators import TicketLocators, UserMenuLocators


class UserMenu:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = UserMenuLocators(page)

    @allure.step("Mở user menu")
    def open(self) -> None:
        self.locators.button.click()

    @allure.step("Kiểm tra các mục trong user menu được hiển thị")
    def expect_open(self) -> None:
        expect(self.locators.settings).to_be_visible()
        expect(self.locators.help).to_be_visible()
        expect(self.locators.logout).to_be_visible()

    @allure.step("Bấm nút ログアウト")
    def logout(self) -> None:
        self.open()
        self.locators.logout.click()

    @allure.step("Kiểm tra bấm ra ngoài thì user menu đóng")
    def expect_closes_when_clicking_outside(self) -> None:
        self.open()
        self.expect_open()
        TicketLocators(self.page).heading.click()
        expect(self.locators.content).to_be_hidden()

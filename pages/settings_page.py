"""Thao tác trên màn cài đặt."""

import allure
from playwright.sync_api import Page, expect

from pages.header import Header
from tests.locators import SettingsLocators


class SettingsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = SettingsLocators(page)

    @allure.step("Nhập chữ vào ô chữ ký")
    def type_signature(self, count: int) -> None:
        self.locators.signature.click()
        # Gõ từng ký tự để trình duyệt chặn đúng maxlength=100.
        self.locators.signature.press_sequentially("a" * count)

    @allure.step("Kiểm tra ô chữ ký dừng ở 100 ký tự và bộ đếm là 100/100文字")
    def expect_signature_stops_at_100(self) -> None:
        Header(self.page).open_tab("設定")
        expect(self.locators.heading).to_be_visible()
        self.type_signature(101)
        expect(self.locators.signature).to_have_value("a" * 100)
        expect(self.locators.signature_counter).to_have_text("100/100文字")

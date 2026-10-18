"""Thao tác trên màn thống kê."""

import re

import allure
from playwright.sync_api import Page, expect

from pages.header import Header
from tests.locators import StatsLocators


class StatsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = StatsLocators(page)

    @allure.step("Kiểm tra bấm tab thống kê thì sang màn thống kê")
    def expect_open(self) -> None:
        Header(self.page).open_tab("統計")
        expect(self.locators.tab).to_have_class(re.compile(r"nav-tab--active"))
        expect(self.locators.heading).to_be_visible()
        expect(self.locators.ticket_heading).to_be_hidden()

"""Thao tác trên màn danh sách ticket."""

import re

import allure
from playwright.sync_api import Page, expect

from tests.locators import TicketLocators


class TicketPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = TicketLocators(page)

    @allure.step("Kiểm tra tab ticket đang mở và hiện 10 dòng")
    def expect_default_list(self) -> None:
        expect(self.locators.tab).to_have_class(re.compile(r"nav-tab--active"))
        expect(self.locators.heading).to_be_visible()
        expect(self.locators.rows).to_have_count(10)
        expect(self.locators.pagination_summary).to_have_text("12件中 1 - 10件目")

    @allure.step("Nhập từ khóa vào ô tìm kiếm rồi bấm tìm")
    def search(self, keyword: str) -> None:
        self.locators.search_input.fill(keyword)
        self.locators.search_button.click()

    @allure.step("Kiểm tra từ khóa không tồn tại thì hiện không có kết quả")
    def expect_search_empty(self) -> None:
        self.search("zzzz-not-found")
        expect(self.locators.empty_message).to_be_visible()

    @allure.step("Lọc theo độ ưu tiên")
    def filter_by_priority(self, label: str) -> None:
        self.locators.priority_filter.select_option(label=label)

    @allure.step("Kiểm tra chỉ hiện 5 ticket ưu tiên cao")
    def expect_only_high_priority(self) -> None:
        self.filter_by_priority("優先度：高")
        expect(self.locators.rows).to_have_count(5)
        for index in range(5):
            expect(self.locators.priority_high(index)).to_have_text("高")

    @allure.step("Kiểm tra icon trợ giúp cột ngày tạo hiện mô tả")
    def expect_created_date_tooltip(self) -> None:
        """Chỉ hover icon. Bấm vào tiêu đề cột sẽ đổi thứ tự sắp xếp.

        Không kiểm tra cả chữ của ô tiêu đề, vì icon sort bị dính vào text.
        """
        self.locators.created_help.hover()
        expect(self.locators.created_tooltip).to_have_text(
            "チケットが作成された日付を表示します"
        )

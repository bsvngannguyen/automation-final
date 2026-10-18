"""Thao tác trên màn đăng nhập."""

import allure
from playwright.sync_api import Page, expect

from pages.user_menu import UserMenu
from tests.locators import LoginLocators, TicketLocators, UserMenuLocators
from tests.support import ADMIN, PASSWORD


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = LoginLocators(page)

    @allure.step("Kiểm tra màn đăng nhập được hiển thị")
    def expect_visible(self) -> None:
        expect(self.locators.heading).to_be_visible()
        expect(self.locators.id_input).to_be_visible()
        expect(self.locators.password_input).to_be_visible()
        expect(self.locators.submit).to_be_visible()

    @allure.step("Kiểm tra chưa nhập thì nút đăng nhập bị khóa")
    def expect_submit_disabled_when_empty(self) -> None:
        expect(self.locators.id_input).to_have_value("")
        expect(self.locators.password_input).to_have_value("")
        expect(self.locators.submit).to_be_disabled()

    @allure.step("Nhập ID, mật khẩu rồi bấm đăng nhập")
    def submit(self, user_id: str, password: str) -> None:
        self.locators.id_input.fill(user_id)
        self.locators.password_input.fill(password)
        self.locators.submit.click()

    @allure.step("Đăng nhập bằng tài khoản admin")
    def login_as_admin(self) -> None:
        self.submit(ADMIN, PASSWORD)
        expect(TicketLocators(self.page).heading).to_be_visible()

    @allure.step("Kiểm tra sai mật khẩu thì hiện lỗi và không chuyển màn")
    def login_with_wrong_password(self) -> None:
        self.submit(ADMIN, "wrongpass")
        expect(self.locators.error).to_be_visible()
        expect(self.locators.heading).to_be_visible()
        expect(self.locators.main_section).to_be_hidden()

    @allure.step("Kiểm tra vào danh sách ticket và header hiện tên user")
    def expect_login_success(self) -> None:
        expect(TicketLocators(self.page).heading).to_be_visible()
        expect(UserMenuLocators(self.page).button).to_be_visible()

    @allure.step("Kiểm tra đăng xuất thì quay về màn đăng nhập")
    def logout_and_expect_login_screen(self) -> None:
        UserMenu(self.page).logout()
        expect(self.locators.heading).to_be_visible()
        expect(self.locators.main_section).to_be_hidden()

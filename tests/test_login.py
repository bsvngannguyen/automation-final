"""Case 14, 61, 44, 66, 37 — màn đăng nhập và đăng xuất."""

import allure
from playwright.sync_api import Page, expect

from tests.support import ADMIN_NAME, login_as_admin


@allure.feature("ログイン画面")
@allure.story("画面表示")
@allure.title("GD01_002: ログイン画面が表示される")
def test_gd01_002_login_screen(app: Page) -> None:
    """Case 14: mở trang thì thấy màn đăng nhập."""
    expect(app.get_by_role("heading", name="ログイン")).to_be_visible()
    expect(app.get_by_label("ID", exact=True)).to_be_visible()
    expect(app.get_by_label("パスワード", exact=True)).to_be_visible()
    expect(app.get_by_role("button", name="ログイン")).to_be_visible()


@allure.feature("ログイン画面")
@allure.story("入力チェック（未入力）")
@allure.title("GD02.8-09: 未入力だとログインボタンが非活性")
def test_gd02_8_09_login_disabled_when_empty(app: Page) -> None:
    """Case 61: chưa nhập ID và mật khẩu thì nút ログイン bị khóa."""
    expect(app.get_by_label("ID", exact=True)).to_have_value("")
    expect(app.get_by_label("パスワード", exact=True)).to_have_value("")
    expect(app.get_by_role("button", name="ログイン")).to_be_disabled()


@allure.feature("ログイン画面")
@allure.story("異常系ログイン")
@allure.title("GD02.8-04: パスワードが違うとエラーになり遷移しない")
def test_gd02_8_04_login_wrong_password(app: Page) -> None:
    """Case 44: sai mật khẩu thì hiện lỗi và không sang màn khác."""
    app.get_by_label("ID", exact=True).fill("admin")
    app.get_by_label("パスワード", exact=True).fill("wrongpass")
    app.get_by_role("button", name="ログイン").click()

    expect(app.get_by_text("IDまたはパスワードが正しくありません。")).to_be_visible()
    expect(app.get_by_role("heading", name="ログイン")).to_be_visible()
    expect(app.locator("#main_section")).to_be_hidden()


@allure.feature("ログイン画面")
@allure.story("正常系ログイン")
@allure.title("GD02.3-007: adminでログインできる")
def test_gd02_3_007_login_success(app: Page) -> None:
    """Case 66: đăng nhập admin đúng thì vào danh sách ticket và thấy tên user."""
    login_as_admin(app)
    expect(app.get_by_role("heading", name="チケット一覧")).to_be_visible()
    expect(app.get_by_role("button", name=ADMIN_NAME)).to_be_visible()


@allure.feature("ログイン画面")
@allure.story("ログアウト")
@allure.title("GD02.1-13: ログアウトするとログイン画面に戻る")
def test_gd02_1_13_logout(admin: Page) -> None:
    """Case 37: bấm ログアウト thì quay về màn đăng nhập."""
    admin.get_by_role("button", name=ADMIN_NAME).click()
    admin.locator("#user_menu_content").get_by_role("button", name="ログアウト").click()

    expect(admin.get_by_role("heading", name="ログイン")).to_be_visible()
    expect(admin.locator("#main_section")).to_be_hidden()

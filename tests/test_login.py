"""Case 14, 61, 44, 66, 37 — màn đăng nhập và đăng xuất."""

import allure
from playwright.sync_api import Page

from pages.login_page import LoginPage
from tests.support import description_md


@allure.feature("ログイン画面")
@allure.story("画面表示")
@allure.title("GD01_002: ログイン画面が表示される")
@description_md(
    """
    - **前提条件**: ブラウザでページを開く
    - **テスト手順**: 1. ページを開く
    - **期待する結果**: ログイン画面が表示される（ID・パスワード入力欄、ログインボタン）
    """
)
def test_gd01_002_login_screen(app: Page) -> None:
    """Case 14: mở trang thì thấy màn đăng nhập."""
    LoginPage(app).expect_visible()


@allure.feature("ログイン画面")
@allure.story("入力チェック（未入力）")
@allure.title("GD02.8-09: 未入力だとログインボタンが非活性")
@description_md(
    """
    - **前提条件**: ログイン画面を表示中
    - **テスト手順**: 1. IDとパスワードをどちらも未入力のままにする
    - **期待する結果**: 「ログイン」ボタンが非活性（disabled）のままである
    """
)
def test_gd02_8_09_login_disabled_when_empty(app: Page) -> None:
    """Case 61: chưa nhập ID và mật khẩu thì nút ログイン bị khóa."""
    LoginPage(app).expect_submit_disabled_when_empty()


@allure.feature("ログイン画面")
@allure.story("異常系ログイン")
@allure.title("GD02.8-04: パスワードが違うとエラーになり遷移しない")
@description_md(
    """
    - **前提条件**: ログイン画面を表示中
    - **テスト手順**:
        1. IDに「admin」を入力する
        2. パスワードに「wrongpass」を入力する
        3. 「ログイン」ボタンを押下する
    - **期待する結果**: 「IDまたはパスワードが正しくありません。」というエラーメッセージが表示され、画面遷移しない
    """
)
def test_gd02_8_04_login_wrong_password(app: Page) -> None:
    """Case 44: sai mật khẩu thì hiện lỗi và không sang màn khác."""
    LoginPage(app).login_with_wrong_password()


@allure.feature("ログイン画面")
@allure.story("正常系ログイン")
@allure.title("GD02.3-007: adminでログインできる")
@description_md(
    """
    - **前提条件**: ログイン画面を表示中
    - **テスト手順**:
        1. IDに「admin」を入力する
        2. パスワードに「admin123」を入力する
        3. 「ログイン」ボタンを押下する
    - **期待する結果**: チケット一覧画面に遷移し、ヘッダーにログインユーザー名が表示される
    """
)
def test_gd02_3_007_login_success(app: Page) -> None:
    """Case 66: đăng nhập admin đúng thì vào danh sách ticket và thấy tên user."""
    login = LoginPage(app)
    login.login_as_admin()
    login.expect_login_success()


@allure.feature("ログイン画面")
@allure.story("ログアウト")
@allure.title("GD02.1-13: ログアウトするとログイン画面に戻る")
@description_md(
    """
    - **前提条件**: ユーザーメニューを表示中
    - **テスト手順**: 1. 「ログアウト」を押下する
    - **期待する結果**: ログイン画面に戻り、メイン画面が表示されなくなる
    """
)
def test_gd02_1_13_logout(admin: Page) -> None:
    """Case 37: bấm ログアウト thì quay về màn đăng nhập."""
    LoginPage(admin).logout_and_expect_login_screen()

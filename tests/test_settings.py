"""Case 8 — ô chữ ký ở màn cài đặt."""

import allure
from playwright.sync_api import Page, expect

from tests.support import open_tab


@allure.feature("設定画面")
@allure.story("文字数カウンター")
@allure.title("GD02.3-001: 署名は100文字で止まりカウンターが100/100になる")
def test_gd02_3_001_signature_counter(admin: Page) -> None:
    """Case 8: gõ quá 100 ký tự thì ô ký dừng ở 100 và bộ đếm là 100/100文字."""
    open_tab(admin, "設定")
    expect(admin.get_by_role("heading", name="設定")).to_be_visible()

    signature = admin.get_by_label("署名")
    signature.click()
    # Gõ từng ký tự để trình duyệt chặn đúng maxlength=100.
    signature.press_sequentially("a" * 101)

    expect(signature).to_have_value("a" * 100)
    expect(admin.locator("#signature_counter")).to_have_text("100/100文字")

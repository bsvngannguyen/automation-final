"""Biến môi trường và mô tả Allure dùng chung."""

import os
import textwrap
from pathlib import Path

import allure
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


def _required(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Thiếu biến {name}. Hãy khai báo trong file .env.")
    return value


URL = _required("URL")
ADMIN = _required("ADMIN")
PASSWORD = _required("PASSWORD")


def description_md(text: str):
    """Gắn mô tả markdown vào Allure: 前提条件 / テスト手順 / 期待する結果."""
    return allure.description(textwrap.dedent(text).strip())

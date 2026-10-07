"""Oddiy smoke-test.

Modelni to'liq yuklamasdan loyiha fayllari mavjudligini tekshiradi.
"""

from pathlib import Path


def test_project_files():
    assert Path("app.py").exists()
    assert Path("requirements.txt").exists()
    assert Path("README.md").exists()

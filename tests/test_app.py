import pytest

from app import get_numbers, info, main


def test_get_numbers_default():
    assert get_numbers() == [1, 2, 3, 4, 5]


def test_get_numbers_custom():
    assert get_numbers(3) == [1, 2, 3]


def test_info_contains_versions():
    env = info()
    assert "greeting" in env
    assert "numpy" in env
    assert "pandas" in env
    assert env["greeting"] == "Hello from Python inside Docker!"


def test_main_returns_numbers(monkeypatch, capsys):
    result = main()
    captured = capsys.readouterr()
    assert "Hello from Python inside Docker!" in captured.out
    assert result == [1, 2, 3, 4, 5]

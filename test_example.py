import pytest

def format_username(name):
    """Приводить ім'я до нижнього регістру та видаляє зайві пробіли."""
    if not isinstance(name, str):
        return ""
    return name.strip().lower()

def test_format_username_basic():
    assert format_username("  Admin  ") == "admin"

def test_format_username_empty():
    assert format_username(None) == ""
    assert format_username(123) == ""

def test_format_username_lowercase():
    assert format_username("PYTHON") == "python"

@pytest.mark.parametrize("input_str, expected", [
    ("  User1 ", "user1"),
    ("TEST", "test"),
    ("   ", ""),
])
def test_format_username_multiple(input_str, expected):
    assert format_username(input_str) == expected
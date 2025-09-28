import pytest
from string_utils import StringUtils

def test_capitalize():
    utils = StringUtils()
    assert utils.capitalize("test") == "Test"
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "


def test_trim():
    utils = StringUtils()
    assert utils.trim("   Test ") == "Test "
    assert utils.trim("Test") == "Test"
    assert utils.trim("   ") == ""
    assert utils.trim("") == ""


def test_contains():
    utils = StringUtils()
    assert utils.contains("Test", "T") is True
    assert utils.contains("Test", "e") is True
    assert utils.contains("Test", "Z") is False
    assert utils.contains("", "A") is False


def test_delete_symbol():
    utils = StringUtils()
    assert utils.delete_symbol("Hello World", "l") == "Heo Word"
    assert utils.delete_symbol("Test", "T") == "est"
    assert utils.delete_symbol("Test", "z") == "Test"
    assert utils.delete_symbol("", "a") == ""
    assert utils.delete_symbol(" ", " ") == ""
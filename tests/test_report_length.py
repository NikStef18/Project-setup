from lib.report_length import *

def test_report_length():
    result = report_length("banana")
    assert result == "This string was 6 characters long."

def test_report_length_with_zero_length():
    result = report_length("")
    assert result == "This string was 0 characters long."

def test_report_length_with_number():
    result = report_length("5")
    assert result == "This string was 1 characters long."

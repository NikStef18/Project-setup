import pytest
from lib.password_checker import *

'''
When we add an 8 chars-password,
it returns True.
'''
def test_password_check_with_8_chars():
    password_checker = PasswordChecker()     
    assert password_checker.check("12345678") == True

'''
When we add a longer than 8-chars-password,
it returns True
'''
def test_password_check_with_more_than_8_chars():
    password_checker = PasswordChecker()     
    assert password_checker.check("123456789") == True

'''
When we add a shorter than 8-chars-password,
it gives error.
'''
def test_password_check_with_less_than_8_chars():
    password_checker = PasswordChecker()  
    with pytest.raises(Exception) as e:
        password_checker.check("123456")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."


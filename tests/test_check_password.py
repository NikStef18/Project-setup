from lib.check_codeword import *

# if codeword correct returns "Correct! Come in."

def test_with_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

'''
if codeword incorrect returns "WRONG!"
'''
def test_with_incorrect_codeword():
    result = check_codeword("rain")
    assert result == "WRONG!"

'''
if codeword quite correct returns "Close, but nope."
'''
def test_with_close_codeword():
    result = check_codeword("house")
    assert result == "Close, but nope."

"""
If the codeword has the right first letter and the wrong last one, returns "WRONG!"
"""

def test_with_right_first_letter_and_wrong_last_letter():
    result = check_codeword("hello")
    assert result == "WRONG!"

"""
If the codeword has the wrong first letter and the right last one, returns "WRONG!"
"""
def test_with_wrong_first_letter_and_right_last_letter():
    result = check_codeword("mouse")
    assert result == "WRONG!"
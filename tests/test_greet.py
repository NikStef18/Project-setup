from lib.greet import *
def test_greets_person_of_given_name():
    result = greet("Niki")
    assert result == "Hello, Niki!"

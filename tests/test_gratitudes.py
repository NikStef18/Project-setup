from lib.gratitudes import *

'''
When there is no addition 
to the gratitudes.
'''
def test_gratitudes_to_noone():
    gratitudes = Gratitudes() 
    assert gratitudes.format() == "Be grateful for: "

'''
When we add a single string
in the list, it reflects to the format.
'''
def test_gratitudes_by_adding_a_single_string():
    gratitudes = Gratitudes() 
    gratitudes.add("family")
    assert gratitudes.format() == "Be grateful for: family"

'''
When we add multiple string
to the list, it reflects to the format.
'''

def test_gratitudes_by_adding_multiple_strings():
    gratitudes = Gratitudes() 
    gratitudes.add("family")
    gratitudes.add("education")
    assert gratitudes.format() == "Be grateful for: family, education"



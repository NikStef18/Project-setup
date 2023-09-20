from lib.string_builder import StringBuilder

def test_string_builder_with_empty_string():
    stringbuilder = StringBuilder()
    assert stringbuilder.output() == ""



def test_string_builder_with_multiple_strings():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    stringbuilder.add(" ")
    stringbuilder.add("world")
    assert stringbuilder.output() == "hello world"



def test_string_builder_with_multiple_strings_size():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    stringbuilder.add(" ")
    stringbuilder.add("world")
    assert stringbuilder.size() == 11
   

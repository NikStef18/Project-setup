import pytest
from lib.present import *

'''
When we wrap a present,
we get it back when we unwrap it.
'''
def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap("watch")
    assert present.unwrap() == "watch"  

'''
If we unwrap before wrapping,
we get an error message.
'''
def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped." 

'''
If we try to wrap an already wrapped present,
we get an error message.
'''
def test_wrapping_an_already_wrapped_present_throws_error():
    present = Present()
    present.wrap("watch")
    with pytest.raises(Exception) as e:
        present.wrap("ipad")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped." 

'''
If we try to wrap an already wrapped present,
the first wrapped values is unchanged.
'''
def test_wrapping_an_already_wrapped_preserves_value():
    present = Present()
    present.wrap("watch")
    with pytest.raises(Exception) as e:
        present.wrap("ipad")
    assert present.unwrap() == "watch"    



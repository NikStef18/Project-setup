from lib.counter import *


'''
Initially, reports a count of 0.
'''

def test_counter_initially_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."
    
'''
When we add a single number to the counter, 
it is reflected to the final count.
'''
def test_counter_adds_a_single_number_to_the_count():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."
'''
When we add multiple numbers to the counter, 
it is reflected to the final count.
'''
def test_counter_adds_multiple_numbers_to_the_count():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    assert counter.report() == "Counted to 8 so far."
'''
When we add negative numbers to the counter, 
it is reflected to the final count.
'''
def test_counter_adds_negative_numbers_to_the_count():
    counter = Counter()
    counter.add(-5)
    counter.add(8)
    assert counter.report() == "Counted to 3 so far."
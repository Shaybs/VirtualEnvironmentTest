import pytest
from python_exercises import count

sequence1 = [0,0,1,0,1,1,0]
item1 = 1
sequence2 = ["b", "c", "c", "a", "e"]
item2 = "a"

def test_count_zeros():
    assert count.count(sequence1, item1)==3

def test_count_string():
    assert count.count(sequence2, item2)==1

import pytest
from python_exercises import multiply_list

def test_product_list1():
    assert multiply_list.product([1,4,5,9])==180

def test_product_list2():
    assert multiply_list.product([5,9,7,22])==6930

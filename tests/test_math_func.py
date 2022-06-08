import sys
from src import math_func
import pytest

@pytest.mark.number
def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9

@pytest.mark.number
def test_product():
    assert math_func.product(7,3) == 21
    assert math_func.product(7) == 14
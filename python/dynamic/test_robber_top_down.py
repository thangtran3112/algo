import pytest
from robber_top_down import Solution

@pytest.fixture
def solutions():
    return Solution()

def test_example1(solutions):
    assert solutions.rob([1, 2, 3, 1]) == 4

def test_example2(solutions):
    assert solutions.rob([2, 7, 9, 3, 1]) == 12

def test_empty(solutions):
    assert solutions.rob([]) == 0

def test_single_house(solutions):
    assert solutions.rob([5]) == 5

def test_two_houses(solutions):
    assert solutions.rob([1, 2]) == 2

def test_consecutive_increasing(solutions):
    assert solutions.rob([1, 2, 3, 4, 5]) == 9  # 1 + 3 + 5 = 9

def test_all_same_value(solutions):
    assert solutions.rob([5, 5, 5, 5]) == 10  # 5 + 5 = 10

def test_alternating_values(solutions):
    assert solutions.rob([10, 1, 10, 1, 10]) == 30  # 10 + 10 + 10 = 30
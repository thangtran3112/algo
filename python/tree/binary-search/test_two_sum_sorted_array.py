import pytest
from typing import List
from two_sum_sorted_array import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    numbers = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(numbers, target) == [1, 2]

def test_example_2(solution):
    """Test the second example from the problem statement."""
    numbers = [2, 3, 4]
    target = 6
    assert solution.twoSum(numbers, target) == [1, 3]

def test_example_3(solution):
    """Test the third example from the problem statement."""
    numbers = [-1, 0]
    target = -1
    assert solution.twoSum(numbers, target) == [1, 2]

def test_minimum_length(solution):
    """Test with minimum length array (2 elements)."""
    numbers = [1, 3]
    target = 4
    assert solution.twoSum(numbers, target) == [1, 2]

def test_duplicate_values(solution):
    """Test with duplicate values in the array."""
    numbers = [1, 2, 2, 4]
    target = 4
    assert solution.twoSum(numbers, target) == [2, 3]

def test_target_at_extremes(solution):
    """Test with a target that requires the first and last elements."""
    numbers = [1, 3, 5, 7, 9]
    target = 10
    assert solution.twoSum(numbers, target) == [1, 5]

def test_edge_case_boundary_values(solution):
    """Test with boundary values from the constraints."""
    numbers = [-1000, 1000]
    target = 0
    assert solution.twoSum(numbers, target) == [1, 2]

def test_larger_target(solution):
    """Test with a target larger than any individual element."""
    numbers = [1, 2, 3, 4, 5]
    target = 9
    assert solution.twoSum(numbers, target) == [4, 5]

def test_smaller_target(solution):
    """Test with a target smaller than most elements."""
    numbers = [5, 10, 15, 20]
    target = 15
    assert solution.twoSum(numbers, target) == [1, 2]
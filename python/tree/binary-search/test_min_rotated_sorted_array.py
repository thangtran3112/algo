import pytest
from min_rotated_sorted_array import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    nums = [3, 4, 5, 1, 2]
    assert solution.findMin(nums) == 1

def test_example_2(solution):
    """Test the second example from the problem statement."""
    nums = [4, 5, 6, 7, 0, 1, 2]
    assert solution.findMin(nums) == 0

def test_example_3(solution):
    """Test the third example from the problem statement."""
    nums = [11, 13, 15, 17]
    assert solution.findMin(nums) == 11

def test_single_element(solution):
    """Test with a single element array."""
    nums = [5]
    assert solution.findMin(nums) == 5

def test_two_elements_rotated(solution):
    """Test with a two-element rotated array."""
    nums = [2, 1]
    assert solution.findMin(nums) == 1

def test_two_elements_not_rotated(solution):
    """Test with a two-element array that is not rotated."""
    nums = [1, 2]
    assert solution.findMin(nums) == 1

def test_three_elements_rotated_once(solution):
    """Test with a three-element array rotated once."""
    nums = [3, 1, 2]
    assert solution.findMin(nums) == 1

def test_three_elements_rotated_twice(solution):
    """Test with a three-element array rotated twice."""
    nums = [2, 3, 1]
    assert solution.findMin(nums) == 1

def test_not_rotated(solution):
    """Test with an array that is not rotated."""
    nums = [1, 2, 3, 4, 5]
    assert solution.findMin(nums) == 1

def test_rotated_once(solution):
    """Test with an array rotated exactly once."""
    nums = [5, 1, 2, 3, 4]
    assert solution.findMin(nums) == 1

def test_rotated_n_minus_1_times(solution):
    """Test with an array rotated n-1 times."""
    nums = [2, 3, 4, 5, 1]
    assert solution.findMin(nums) == 1

def test_negative_numbers(solution):
    """Test with negative numbers."""
    nums = [-3, -2, -1, -5, -4]
    assert solution.findMin(nums) == -5

def test_mixed_positive_negative(solution):
    """Test with a mix of positive and negative numbers."""
    nums = [2, 3, -5, -4, -3, -2, -1, 0, 1]
    assert solution.findMin(nums) == -5

def test_boundary_values(solution):
    """Test with boundary values from constraints."""
    nums = [5000, -5000]
    assert solution.findMin(nums) == -5000

def test_larger_array(solution):
    """Test with a larger array to verify binary search efficiency."""
    nums = list(range(100, 1000)) + list(range(0, 100))
    assert solution.findMin(nums) == 0

def test_edge_case_min_at_beginning(solution):
    """Test edge case where minimum is at the beginning."""
    nums = [0, 1, 2, 3, 4, 5]
    assert solution.findMin(nums) == 0

def test_edge_case_min_at_end(solution):
    """Test edge case where minimum is at the end after rotation."""
    nums = [1, 2, 3, 4, 5, 0]
    assert solution.findMin(nums) == 0
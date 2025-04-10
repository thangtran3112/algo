import pytest
from find_in_rotated_array import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    assert solution.search(nums, target) == 4

def test_example_2(solution):
    """Test the second example from the problem statement."""
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    assert solution.search(nums, target) == -1

def test_example_3(solution):
    """Test the third example from the problem statement."""
    nums = [1]
    target = 0
    assert solution.search(nums, target) == -1

def test_single_element_found(solution):
    """Test with a single element array where target exists."""
    nums = [5]
    target = 5
    assert solution.search(nums, target) == 0

def test_two_elements_rotated_target_first(solution):
    """Test with a two-element rotated array, target is first element."""
    nums = [2, 1]
    target = 2
    assert solution.search(nums, target) == 0

def test_two_elements_rotated_target_second(solution):
    """Test with a two-element rotated array, target is second element."""
    nums = [2, 1]
    target = 1
    assert solution.search(nums, target) == 1

def test_two_elements_not_rotated(solution):
    """Test with a two-element array that is not rotated."""
    nums = [1, 2]
    target = 1
    assert solution.search(nums, target) == 0

def test_not_rotated_array(solution):
    """Test with an array that is not rotated."""
    nums = [1, 2, 3, 4, 5]
    target = 3
    assert solution.search(nums, target) == 2

def test_rotated_once(solution):
    """Test with an array rotated exactly once."""
    nums = [5, 1, 2, 3, 4]
    target = 5
    assert solution.search(nums, target) == 0

def test_rotated_multiple_times(solution):
    """Test with an array rotated multiple times."""
    nums = [3, 4, 5, 1, 2]
    target = 1
    assert solution.search(nums, target) == 3

def test_target_at_middle(solution):
    """Test when target is at the middle position."""
    nums = [6, 7, 8, 9, 1, 2, 3, 4, 5]
    target = 9
    assert solution.search(nums, target) == 3

def test_target_at_start(solution):
    """Test when target is at the start position after rotation."""
    nums = [4, 5, 6, 7, 0, 1, 2, 3]
    target = 4
    assert solution.search(nums, target) == 0

def test_target_at_end(solution):
    """Test when target is at the end position after rotation."""
    nums = [4, 5, 6, 7, 0, 1, 2, 3]
    target = 3
    assert solution.search(nums, target) == 7

def test_split_in_left_half(solution):
    """Test when the rotation split is in the left half of the array."""
    nums = [4, 5, 0, 1, 2, 3]
    target = 5
    assert solution.search(nums, target) == 1

def test_split_in_right_half(solution):
    """Test when the rotation split is in the right half of the array."""
    nums = [2, 3, 4, 5, 0, 1]
    target = 0
    assert solution.search(nums, target) == 4

def test_negative_numbers(solution):
    """Test with negative numbers in the array."""
    nums = [-3, -2, -1, -7, -6, -5, -4]
    target = -6
    assert solution.search(nums, target) == 4

def test_mixed_positive_negative(solution):
    """Test with a mix of positive and negative numbers."""
    nums = [-1, 0, 1, 2, -4, -3, -2]
    target = -2
    assert solution.search(nums, target) == 6

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    nums = [-10000, 10000]
    target = 10000
    assert solution.search(nums, target) == 1

def test_larger_array(solution):
    """Test with a larger array to verify efficiency."""
    # Create a larger rotated array
    nums = list(range(100, 1000)) + list(range(100))
    target = 50
    assert solution.search(nums, target) == 950
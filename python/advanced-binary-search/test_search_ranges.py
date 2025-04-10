import pytest
from search_ranges import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    assert solution.searchRange(nums, target) == [3, 4]

def test_example_2(solution):
    """Test the second example from the problem statement."""
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    assert solution.searchRange(nums, target) == [-1, -1]

def test_example_3(solution):
    """Test the third example from the problem statement."""
    nums = []
    target = 0
    assert solution.searchRange(nums, target) == [-1, -1]

def test_single_element_found(solution):
    """Test with a single element array where the target exists."""
    nums = [5]
    target = 5
    assert solution.searchRange(nums, target) == [0, 0]

def test_single_element_not_found(solution):
    """Test with a single element array where the target does not exist."""
    nums = [5]
    target = 6
    assert solution.searchRange(nums, target) == [-1, -1]

def test_two_elements_same(solution):
    """Test with two identical elements."""
    nums = [5, 5]
    target = 5
    assert solution.searchRange(nums, target) == [0, 1]

def test_two_elements_different_found(solution):
    """Test with two different elements, target found."""
    nums = [5, 6]
    target = 5
    assert solution.searchRange(nums, target) == [0, 0]

def test_two_elements_different_not_found(solution):
    """Test with two different elements, target not found."""
    nums = [5, 6]
    target = 7
    assert solution.searchRange(nums, target) == [-1, -1]

def test_all_same_elements(solution):
    """Test with all elements being the same as target."""
    nums = [8, 8, 8, 8, 8]
    target = 8
    assert solution.searchRange(nums, target) == [0, 4]

def test_target_at_boundaries(solution):
    """Test with target at both boundaries."""
    nums = [5, 6, 7, 8, 9]
    target = 5
    assert solution.searchRange(nums, target) == [0, 0]
    
    target = 9
    assert solution.searchRange(nums, target) == [4, 4]

def test_multiple_occurrences_at_beginning(solution):
    """Test with multiple occurrences of target at the beginning."""
    nums = [5, 5, 5, 6, 7, 8]
    target = 5
    assert solution.searchRange(nums, target) == [0, 2]

def test_multiple_occurrences_at_end(solution):
    """Test with multiple occurrences of target at the end."""
    nums = [5, 6, 7, 8, 8, 8]
    target = 8
    assert solution.searchRange(nums, target) == [3, 5]

def test_multiple_occurrences_in_middle(solution):
    """Test with multiple occurrences of target in the middle."""
    nums = [5, 6, 7, 7, 7, 8]
    target = 7
    assert solution.searchRange(nums, target) == [2, 4]

def test_large_array(solution):
    """Test with a large array to verify efficiency."""
    nums = [i // 10 for i in range(1000)]  # Creates [0,0,0,...,1,1,1,...,99,99,99]
    target = 50
    assert solution.searchRange(nums, target) == [500, 509]

def test_negative_numbers(solution):
    """Test with negative numbers."""
    nums = [-5, -5, -3, -2, -1]
    target = -5
    assert solution.searchRange(nums, target) == [0, 1]

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    nums = [-10**9, 0, 10**9]
    target = -10**9
    assert solution.searchRange(nums, target) == [0, 0]
    
    target = 10**9
    assert solution.searchRange(nums, target) == [2, 2]
import pytest
from peak_element import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    nums = [1, 2, 3, 1]
    result = solution.findPeakElement(nums)
    assert result == 2
    assert nums[result] > nums[result-1]  # Verify it's greater than left neighbor
    assert result == len(nums)-1 or nums[result] > nums[result+1]  # Verify it's greater than right neighbor

def test_example_2(solution):
    """Test the second example from the problem statement."""
    nums = [1, 2, 1, 3, 5, 6, 4]
    result = solution.findPeakElement(nums)
    # Could be either index 1 (value 2) or index 5 (value 6)
    assert result in [1, 5]
    assert nums[result] > nums[result-1]  # Verify it's greater than left neighbor
    assert result == len(nums)-1 or nums[result] > nums[result+1]  # Verify it's greater than right neighbor

def test_single_element(solution):
    """Test with a single element array."""
    nums = [5]
    assert solution.findPeakElement(nums) == 0

def test_two_elements_ascending(solution):
    """Test with a two-element ascending array."""
    nums = [1, 2]
    assert solution.findPeakElement(nums) == 1

def test_two_elements_descending(solution):
    """Test with a two-element descending array."""
    nums = [2, 1]
    assert solution.findPeakElement(nums) == 0

def test_strictly_ascending(solution):
    """Test with a strictly ascending array."""
    nums = [1, 2, 3, 4, 5]
    assert solution.findPeakElement(nums) == 4

def test_strictly_descending(solution):
    """Test with a strictly descending array."""
    nums = [5, 4, 3, 2, 1]
    assert solution.findPeakElement(nums) == 0

def test_multiple_peaks(solution):
    """Test with multiple peaks in the array."""
    nums = [1, 3, 2, 4, 1, 5, 2]
    result = solution.findPeakElement(nums)
    # Could be either index 1 (value 3), index 3 (value 4), or index 5 (value 5)
    assert result in [1, 3, 5]
    assert nums[result] > nums[result-1]  # Verify it's greater than left neighbor
    assert result == len(nums)-1 or nums[result] > nums[result+1]  # Verify it's greater than right neighbor

def test_peak_at_beginning(solution):
    """Test when the peak is at the beginning of the array."""
    nums = [5, 4, 3, 2, 1]
    assert solution.findPeakElement(nums) == 0

def test_peak_at_end(solution):
    """Test when the peak is at the end of the array."""
    nums = [1, 2, 3, 4, 5]
    assert solution.findPeakElement(nums) == 4

def test_alternating_elements(solution):
    """Test with alternating elements (zigzag pattern)."""
    nums = [1, 3, 1, 3, 1, 3]
    result = solution.findPeakElement(nums)
    # Could be index 1, 3, or 5
    assert result in [1, 3, 5]
    assert nums[result] > nums[result-1]  # Verify it's greater than left neighbor
    assert result == len(nums)-1 or nums[result] > nums[result+1]  # Verify it's greater than right neighbor

def test_negative_values(solution):
    """Test with negative values."""
    nums = [-5, -4, -3, -6, -7]
    assert solution.findPeakElement(nums) == 2

def test_large_array(solution):
    """Test with a larger array to verify binary search efficiency."""
    # Create a large array with a peak in the middle
    nums = list(range(500)) + [1000] + list(range(499, -1, -1))
    assert solution.findPeakElement(nums) == 500

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    # Create array with max and min values
    nums = [-2**31, 2**31 - 1, -2**31]
    assert solution.findPeakElement(nums) == 1
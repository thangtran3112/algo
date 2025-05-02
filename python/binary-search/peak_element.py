# https://leetcode.com/problems/find-peak-element/description/
"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""
from typing import List


class Solution:
    """
    * If mid is in a ascending slope, there is a peak within [mid+1, right]
    * If mid is in a descending slop, mid could be a peak, or the peak will be on the left
    """
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # check for ascending or descending
            if mid + 1 <= right:
                if nums[mid + 1] > nums[mid]:
                    # ascending slop
                    left = mid + 1
                else:
                    # descending slop. mid could be a peak, or the peak is on the left
                    right = mid
            # else:
            # if there is no right element (mid+1), we have reached the end.
            # left=mid=right, right will be the current peak

        return right

# TEST CASES
import pytest  # noqa: E402

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
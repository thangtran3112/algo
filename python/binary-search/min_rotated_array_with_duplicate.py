# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.
 

Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?


"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Case 1: nums[mid] > nums[right]. Eg: 4, 5, 6, 7, 0, 1, 4  
        # mid_val = 7, mid_val > right_val, it means there is flipping between [mid,right]

        # Case 2: nums[mid] < nums[right]. Eg: 6, 7, 0, 1, 4, 4, 5  
        # mid_val = 1, mid_val < left_val, there is flipping between [left, mid]

        # Case 3: nums[mid] == nums[right] . Eg: 2, 2, 2, 2, 1, 2, 2
        # we can’t decide, so we safely reduce right (right -= 1). Worst case O(n)
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:  # nums[mid] == nums[right]
                # avoid skipping the correct value
                right -= 1  # shrink search space conservatively
        # since we use left < right in while loop, left and right will converse into one
        return nums[left]
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Provides an instance of the Solution class."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description (no rotation)."""
    nums = [1, 3, 5]
    assert solution.findMin(nums) == 1

def test_example2(solution):
    """Test Example 2 from the problem description."""
    nums = [2, 2, 2, 0, 1]
    assert solution.findMin(nums) == 0

def test_no_rotation_duplicates(solution):
    """Test with no rotation and duplicates."""
    nums = [1, 1, 2, 2, 3, 3]
    assert solution.findMin(nums) == 1

def test_all_duplicates(solution):
    """Test with all elements being duplicates."""
    nums = [3, 3, 3, 3, 3, 3]
    assert solution.findMin(nums) == 3

def test_rotation_point_middle(solution):
    """Test where the minimum is in the middle after rotation."""
    nums = [4, 5, 6, 7, 0, 1, 2]
    assert solution.findMin(nums) == 0

def test_rotation_point_middle_with_duplicates(solution):
    """Test rotation with duplicates around the minimum."""
    nums = [3, 3, 1, 3]
    assert solution.findMin(nums) == 1

    nums = [4, 5, 1, 1, 2, 3]
    assert solution.findMin(nums) == 1

def test_duplicates_at_ends_case1(solution):
    """Test duplicates at both ends, min is not at ends."""
    nums = [10, 1, 10, 10, 10]
    assert solution.findMin(nums) == 1

def test_duplicates_at_ends_case2(solution):
    """Test duplicates at both ends, min is at the start (before rotation)."""
    nums = [1, 1, 1, 0, 1]
    assert solution.findMin(nums) == 0

def test_duplicates_at_ends_case3(solution):
    """Test duplicates at both ends, min is at the start (no effective rotation)."""
    nums = [1, 1, 1, 1, 1]
    assert solution.findMin(nums) == 1

def test_worst_case_linear_scan(solution):
    """Test cases that might degrade to O(n) due to nums[mid] == nums[right]."""
    nums = [1] * 1000 + [0] + [1] * 1000
    assert solution.findMin(nums) == 0

    nums = [1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
    assert solution.findMin(nums) == 0

    nums = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    assert solution.findMin(nums) == 0

def test_single_element(solution):
    """Test with a single element array."""
    nums = [5]
    assert solution.findMin(nums) == 5

def test_two_elements_rotated(solution):
    """Test with two elements, rotated."""
    nums = [2, 1]
    assert solution.findMin(nums) == 1

def test_two_elements_not_rotated(solution):
    """Test with two elements, not rotated."""
    nums = [1, 2]
    assert solution.findMin(nums) == 1

def test_two_elements_duplicates(solution):
    """Test with two duplicate elements."""
    nums = [1, 1]
    assert solution.findMin(nums) == 1

def test_negative_numbers(solution):
    """Test with negative numbers."""
    nums = [1, 2, -3, -2, -1] # Rotated from [-3, -2, -1, 1, 2]
    assert solution.findMin(nums) == -3

    nums = [-2, -1, 0, -4, -3] # Rotated from [-4, -3, -2, -1, 0]
    assert solution.findMin(nums) == -4
    
    nums = [-1, -1, -1, 0, -1] # Min is -1
    assert solution.findMin(nums) == -1


def test_larger_range(solution):
    """Test with values near constraints."""
    nums = [4999, 5000, -5000, -4999]
    assert solution.findMin(nums) == -5000

    nums = [0, 0, 0, 0, -1, 0]
    assert solution.findMin(nums) == -1

def test_complex_duplicates(solution):
    """Test more complex duplicate patterns."""
    nums = [3, 1, 3, 3, 3, 3]
    assert solution.findMin(nums) == 1

    nums = [3, 3, 3, 3, 1, 3]
    assert solution.findMin(nums) == 1
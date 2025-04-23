# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # splitting point within [left, mid]
            if nums[left] > nums[mid]:
                # [4,0,1,2,3]
                if target > nums[mid] and target <= nums[right]:
                    # there is no split in [mid, right]
                    # find target from [mid+1, right]
                    left = mid + 1
                    continue
                else:
                    # target will be within [left, mid - 1]
                    right = mid - 1
                    continue

            # there is a split point within (mid, right]
            if nums[mid] > nums[right]:
                # [2,3,4,0,1]
                if target < nums[mid] and target >= nums[left]:
                    # there is no split within [left, mid]
                    # and target is within [left, mid]. For instance target = 3
                    right = mid - 1
                    continue
                else:
                    # target is within [mid+1, right], For instance target = 1
                    left = mid + 1
                    continue

            # this is a normal range, without splitting point
            # [2,3,4], a sub array of original [2,3,4,0,1]
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # cannot find the target
        return -1

import pytest  # noqa: E402

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
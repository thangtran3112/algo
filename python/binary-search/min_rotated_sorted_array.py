# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            # [3, 1, 2]
            if mid - 1 >= left and mid + 1 <= right and nums[mid - 1] > nums[mid] < nums[mid + 1]:
                return nums[mid]

            # [3,4,5,1,2]
            if nums[mid] > nums[right]:
                # reversing is from [mid, right]
                left = mid + 1
                continue
            # [5,1,2,3,4]
            if nums[left] > nums[mid]:
                right = mid - 1
                continue

            # this is a normal range
            # [1,2,3,4]
            return nums[left]

import pytest  # noqa: E402

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
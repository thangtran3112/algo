# https://leetcode.com/problems/find-pivot-index/description/
"""
    Given an array of integers nums, calculate the pivot index of this array.

    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

    Return the leftmost pivot index. If no such index exists, return -1.

    

    Example 1:

    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
    The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
    Right sum = nums[4] + nums[5] = 5 + 6 = 11
    Example 2:

    Input: nums = [1,2,3]
    Output: -1
    Explanation:
    There is no index that satisfies the conditions in the problem statement.
    Example 3:

    Input: nums = [2,1,-1]
    Output: 0
    Explanation:
    The pivot index is 0.
    Left sum = 0 (no elements to the left of index 0)
    Right sum = nums[1] + nums[2] = 1 + -1 = 0
    

    Constraints:

    1 <= nums.length <= 104
    -1000 <= nums[i] <= 1000
"""
from collections import defaultdict
from typing import List

class Solution:
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

class SolutionTwoHashmaps:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        # 2 pointers, going from left to right and right to bisect_left
        # polulate 2 hashtable, <index, sumLeft> and <index, sumRight>

        left_sums = defaultdict(int)
        right_sums = defaultdict(int)

        for j in range(len(nums) - 1, 0, -1):
            right_sums[j - 1] = right_sums[j] + nums[j]

        # special case: at index 0
        if right_sums[0] == 0:
            return 0

        for i in range(0, len(nums) - 1):
            left_sums[i + 1] = left_sums[i] + nums[i]

            # early exit
            if left_sums[i + 1] == right_sums[i + 1]:
                return i + 1

        # special case: index at len(nums) - 1
        if left_sums[len(nums) - 1] == 0:
            return len(nums) - 1

        return -1


import pytest  # noqa: E402

@pytest.fixture(params=[Solution, SolutionTwoHashmaps])
def solution(request):
    """Fixture that provides both solution implementations."""
    return request.param()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    nums = [1, 7, 3, 6, 5, 6]
    assert solution.pivotIndex(nums) == 3

def test_example_2(solution):
    """Test the second example from the problem statement."""
    nums = [1, 2, 3]
    assert solution.pivotIndex(nums) == -1

def test_example_3(solution):
    """Test the third example from the problem statement."""
    nums = [2, 1, -1]
    assert solution.pivotIndex(nums) == 0

def test_single_element(solution):
    """Test with an array containing a single element."""
    nums = [5]
    assert solution.pivotIndex(nums) == 0

def test_two_elements_with_pivot(solution):
    """Test with two elements that have a pivot."""
    nums = [0, 0]
    assert solution.pivotIndex(nums) == 0

def test_two_elements_without_pivot(solution):
    """Test with two elements that don't have a pivot."""
    nums = [1, 2]
    assert solution.pivotIndex(nums) == -1

def test_all_zeros(solution):
    """Test with an array of all zeros."""
    nums = [0, 0, 0, 0, 0]
    assert solution.pivotIndex(nums) == 0

def test_all_negative(solution):
    """Test with all negative numbers."""
    nums = [-1, -1, -1, -1, -1]
    assert solution.pivotIndex(nums) == 2

def test_large_numbers(solution):
    """Test with large numbers within constraints."""
    nums = [1000, -1000, 1000, -1000, 1000]
    assert solution.pivotIndex(nums) == 0

def test_off_by_one_error_case(solution):
    """Test a case that might have off-by-one errors in implementation."""
    nums = [1, 2, 3, 4, 5]
    # Sum is 15, no pivot index exists
    assert solution.pivotIndex(nums) == -1

def test_edge_cases_with_negative_numbers(solution):
    """Test edge cases with negative numbers."""
    # Case where negative numbers create a pivot
    nums = [1, -1, 2]
    assert solution.pivotIndex(nums) == 2
    
    nums = [2, -2, 2, -2]
    assert solution.pivotIndex(nums) == -1

def test_multiple_possible_pivots(solution):
    """Test when there are multiple possible pivots."""
    nums = [1, 2, 3, 0, 3, 2, 1]
    # Return leftmost pivot as per problem statement
    assert solution.pivotIndex(nums) == 3

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    # Min value: -1000, Max value: 1000
    nums = [-1000, -1000, 1000, 1000, -1000]
    assert solution.pivotIndex(nums) == 0

def test_zero_sum_both_sides(solution):
    """Test with subarrays summing to zero on both sides."""
    nums = [0, 0, 0, 1, 0, 0, 0]
    assert solution.pivotIndex(nums) == 3

def test_alternating_positive_negative(solution):
    """Test with alternating positive and negative numbers."""
    nums = [1, -1, 1, -1, 1, -1, 1]
    assert solution.pivotIndex(nums) == 0
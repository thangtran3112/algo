# https://leetcode.com/problems/continuous-subarray-sum/description/
"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
"""

# O(n)
# Similar to above, we calculate prefix_sum array, where prefix_sum[i] = Sum(nums[0], ..,nums[i])
# Subarray between (i, j) will be prefix_sum[j] - prefix_sum[i - 1]
# prefix_sum[j] - prefix_sum[i] = (n * k + Rj) - (m * k + Ri)
# Because Ri and Rj are modulo of k, so they are within [0, k)
# So when Rj - Ri = 0, or Ri == Rj, we will have a perfect subarray
# Safe modulo for negative number: mod = (prefix_sum % k + k) % k
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_map = {0: -1}  # (mod value) -> (earliest index)
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            mod = (prefix_sum % k + k) % k  # Safe modulo for negative numbers

            if mod in mod_map:
                if i - mod_map[mod] >= 2:
                    return True
            else:
                mod_map[mod] = i  # only record the first occurrence

        return False
    
import pytest  # noqa: E402

@pytest.fixture
def solution_instance():
    return Solution()

def test_example1(solution_instance):
    """Input: nums = [23,2,4,6,7], k = 6 -> Output: True"""
    nums = [23, 2, 4, 6, 7]
    k = 6
    assert solution_instance.checkSubarraySum(nums, k) is True

def test_example2(solution_instance):
    """Input: nums = [23,2,6,4,7], k = 6 -> Output: True"""
    nums = [23, 2, 6, 4, 7]
    k = 6
    assert solution_instance.checkSubarraySum(nums, k) is True

def test_example3(solution_instance):
    """Input: nums = [23,2,6,4,7], k = 13 -> Output: False"""
    nums = [23, 2, 6, 4, 7]
    k = 13
    assert solution_instance.checkSubarraySum(nums, k) is False

def test_entire_array_is_valid(solution_instance):
    """Input: nums = [6,6], k = 6 -> Output: True"""
    nums = [6, 6]
    k = 6
    assert solution_instance.checkSubarraySum(nums, k) is True

def test_large_k(solution_instance):
    """Input: nums = [1,2,3], k = 100 -> Output: False"""
    nums = [1, 2, 3]
    k = 100
    assert solution_instance.checkSubarraySum(nums, k) is False

def test_zero_in_array(solution_instance):
    """Input: nums = [0,0], k = 1 -> Output: True"""
    nums = [0, 0]
    k = 1
    assert solution_instance.checkSubarraySum(nums, k) is True

def test_single_element_array(solution_instance):
    """Input: nums = [1], k = 2 -> Output: False"""
    nums = [1]
    k = 2
    assert solution_instance.checkSubarraySum(nums, k) is False

def test_multiple_valid_subarrays(solution_instance):
    """Input: nums = [5,0,0,0], k = 5 -> Output: True"""
    nums = [5, 0, 0, 0]
    k = 5
    assert solution_instance.checkSubarraySum(nums, k) is True

def test_negative_numbers(solution_instance):
    """Input: nums = [-1,-1,-1], k = 2 -> Output: True"""
    nums = [-1, -1, -1]
    k = 2
    assert solution_instance.checkSubarraySum(nums, k) is True

def test_large_input(solution_instance):
    """Test with a large input."""
    nums = [1] * 10**5
    k = 2
    assert solution_instance.checkSubarraySum(nums, k) is True

def test_zero_k(solution_instance):
    """Input: nums = [0,0], k = 0 -> Output: False (k cannot be zero)"""
    nums = [0, 0]
    k = 0
    with pytest.raises(ZeroDivisionError):
        solution_instance.checkSubarraySum(nums, k)

# To run these tests:
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest
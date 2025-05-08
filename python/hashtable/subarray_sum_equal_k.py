# https://leetcode.com/problems/subarray-sum-equals-k/description/
"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
# Using prefix_sums, we have subarraySum(i, j) = prefix_sums[j] - prefix_sums[i - 1]
# Use hashmap to store { prefix_sum : frequencies_of_prefix_sum }
# For a given index, if we have a prefix_sum == prefix_sum[index] - k
# There will exist a subarray with sum == k
# if we want to print out the subarray, we can also have another map
# to keep track of { prefix_sum: list_of_indexes }
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # The frequency of prefix_sum to value 0 is intially 1
        # This entry will match with any prefix_sum == k
        # When prefix_sum == k, we have a subArray from 0 to current index
        # We can also use this trick to setup sum_frequencies_map = {0: 1}
        sum_frequencies_map = {}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            if curr_sum == k:
                count += 1
            # even when curr_sum == k, it is possbile that there are other
            # prefix_sum in hashmap, which also has prefix_sum == 0
            target = curr_sum - k
            if target in sum_frequencies_map:
                frequency = sum_frequencies_map[target]
                count += frequency
            if curr_sum in sum_frequencies_map:
                sum_frequencies_map[curr_sum] += 1
            else:
                sum_frequencies_map[curr_sum] = 1
        return count
    
import pytest  # noqa: E402

@pytest.fixture
def solution_instance():
    return Solution()

def test_example1(solution_instance):
    """Input: nums = [1,1,1], k = 2 -> Output: 2"""
    nums = [1, 1, 1]
    k = 2
    assert solution_instance.subarraySum(nums, k) == 2

def test_example2(solution_instance):
    """Input: nums = [1,2,3], k = 3 -> Output: 2"""
    nums = [1, 2, 3]
    k = 3
    assert solution_instance.subarraySum(nums, k) == 2

def test_no_subarray(solution_instance):
    """Input: nums = [1,2,3], k = 10 -> Output: 0"""
    nums = [1, 2, 3]
    k = 10
    assert solution_instance.subarraySum(nums, k) == 0

def test_single_element_equal_to_k(solution_instance):
    """Input: nums = [5], k = 5 -> Output: 1"""
    nums = [5]
    k = 5
    assert solution_instance.subarraySum(nums, k) == 1

def test_single_element_not_equal_to_k(solution_instance):
    """Input: nums = [5], k = 10 -> Output: 0"""
    nums = [5]
    k = 10
    assert solution_instance.subarraySum(nums, k) == 0

def test_multiple_subarrays(solution_instance):
    """Input: nums = [1,2,1,2,1], k = 3 -> Output: 4"""
    nums = [1, 2, 1, 2, 1]
    k = 3
    assert solution_instance.subarraySum(nums, k) == 4

def test_negative_numbers(solution_instance):
    """Input: nums = [-1,-1,1], k = 0 -> Output: 1"""
    nums = [-1, -1, 1]
    k = 0
    assert solution_instance.subarraySum(nums, k) == 1

def test_large_input(solution_instance):
    """Test with a large input."""
    nums = [1] * 10000
    k = 2
    assert solution_instance.subarraySum(nums, k) == 9999

def test_zero_k(solution_instance):
    """Input: nums = [0,0,0], k = 0 -> Output: 6"""
    nums = [0, 0, 0]
    k = 0
    assert solution_instance.subarraySum(nums, k) == 6

def test_mixed_positive_and_negative(solution_instance):
    """Input: nums = [3,4,-7,1,3,3,1,-4], k = 7 -> Output: 4"""
    nums = [3, 4, -7, 1, 3, 3, 1, -4]
    k = 7
    assert solution_instance.subarraySum(nums, k) == 4

def test_all_zeros(solution_instance):
    """Input: nums = [0,0,0,0], k = 0 -> Output: 10"""
    nums = [0, 0, 0, 0]
    k = 0
    assert solution_instance.subarraySum(nums, k) == 10

def test_large_k(solution_instance):
    """Input: nums = [1,2,3], k = 100 -> Output: 0"""
    nums = [1, 2, 3]
    k = 100
    assert solution_instance.subarraySum(nums, k) == 0

def test_prefix_sum_matches_k(solution_instance):
    """Input: nums = [3,4,7,2,-3,1,4,2], k = 7 -> Output: 4"""
    nums = [3, 4, 7, 2, -3, 1, 4, 2]
    k = 7
    assert solution_instance.subarraySum(nums, k) == 4

# To run these tests:
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest
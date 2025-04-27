# https://leetcode.com/explore/interview/card/facebook/55/dynamic-programming-3/3038/
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
from typing import List
import pytest


# O(n)
# Similar to above, we calculate prefix_sum array, where prefix_sum[i] = Sum(nums[0], ..,nums[i])
# Subarray between (i, j) will be prefix_sum[j] - prefix_sum[i - 1]
# prefix_sum[j] - prefix_sum[i] = (n * k + Rj) - (m * k + Ri)
# Because Ri and Rj are modulo of k, so they are within [0, k)
# So when Rj - Ri = 0, or Ri == Rj, we will have a perfect subarray
# Safe modulo for negative number: mod = (prefix_sum % k + k) % k
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
    

# O(n*n) - Not Accepted
class SolutionDynamicProgramming:
    # eg [23,2,4,6,7]  modulo by k = 6 => [5, 2, 5, 0, 1]
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # maintain dp array, where dp[i] = sum(nums[i] + ...+ nums[0])
        # dp[i] = dp[i-1] + 1
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] + nums[i]

        # Total sum between [left, right] is equal to [0, right] - [0, left - 1]
        def getSum(left, right):
            if left == 0:
                return dp[right]
            return dp[right] - dp[left - 1]

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                curr_sum = getSum(i, j)
                if curr_sum % k == 0:
                    return True

        return False



# === TEST CASES ===
# --- Fixtures ---

@pytest.fixture(params=[Solution, SolutionDynamicProgramming],
               ids=["Optimized", "DP_SmallInput"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    # Only run DP solution on tests marked specifically for it or small inputs
    if request.node.get_closest_marker("skip_dp") and request.param == SolutionDynamicProgramming:
        pytest.skip("Skipping DP solution for this large/complex test case")
    return request.param()

@pytest.fixture
def optimized_solution():
    """Fixture specifically for the optimized Solution."""
    return Solution()

@pytest.fixture
def dp_solution():
    """Fixture specifically for the SolutionDynamicProgramming."""
    return SolutionDynamicProgramming()

# --- Test Cases ---

# Basic Examples (Suitable for both)
def test_example1(solution_instance):
    nums = [23, 2, 4, 6, 7]
    k = 6
    assert solution_instance.checkSubarraySum(nums, k) is True

def test_example2(solution_instance):
    nums = [23, 2, 6, 4, 7]
    k = 6
    assert solution_instance.checkSubarraySum(nums, k) is True

def test_example3(solution_instance):
    nums = [23, 2, 6, 4, 7]
    k = 13
    assert solution_instance.checkSubarraySum(nums, k) is False

# Edge Cases (Suitable for both)
def test_length_two_true(solution_instance):
    nums = [1, 5]
    k = 6
    assert solution_instance.checkSubarraySum(nums, k) is True

def test_length_two_false(solution_instance):
    nums = [1, 6]
    k = 6
    assert solution_instance.checkSubarraySum(nums, k) is False # Sum is 7

def test_last_two_elements(solution_instance):
    nums = [1, 2, 3, 3]
    k = 6
    assert solution_instance.checkSubarraySum(nums, k) is True # [3, 3] sum 6

def test_contains_zero_true(solution_instance):
    nums = [5, 0, 0, 0]
    k = 3
    assert solution_instance.checkSubarraySum(nums, k) is True # [0, 0] sum 0, multiple of 3

def test_contains_zero_false(solution_instance):
    nums = [1, 0]
    k = 2
    assert solution_instance.checkSubarraySum(nums, k) is False # [1, 0] sum 1

def test_single_zero_not_enough(solution_instance):
    nums = [0]
    k = 1
    assert solution_instance.checkSubarraySum(nums, k) is False # Length must be >= 2

def test_k_is_one(solution_instance):
    nums = [1, 2, 3]
    k = 1
    assert solution_instance.checkSubarraySum(nums, k) is True # Any subarray of length >= 2 will have sum > 0, multiple of 1
    nums = [0, 0]
    k = 1
    assert solution_instance.checkSubarraySum(nums, k) is True # [0, 0] sum 0, multiple of 1

def test_k_is_one_single_element(solution_instance):
    nums = [5]
    k = 1
    assert solution_instance.checkSubarraySum(nums, k) is False # Length must be >= 2

def test_prefix_mod_zero_at_end(solution_instance):
    nums = [1, 2, 3]
    k = 6
    assert solution_instance.checkSubarraySum(nums, k) is True # Full array sum is 6

def test_prefix_mod_zero_mid(solution_instance):
    nums = [6, 1, 2]
    k = 6
    assert solution_instance.checkSubarraySum(nums, k) is False # [6] is not long enough

def test_repeated_mod_value(solution_instance):
    # prefix sums: 23, 25, 29, 35, 42
    # mods (k=6): 5,  1,  5,  5,  0
    nums = [23, 2, 4, 6, 7]
    k = 6
    # mod 5 appears at index 0 and index 2. i - mod_map[mod] = 2 - 0 = 2 >= 2. True.
    # mod 5 appears at index 2 and index 3. i - mod_map[mod] = 3 - 0 = 3 >= 2. True.
    assert solution_instance.checkSubarraySum(nums, k) is True

def test_repeated_mod_value_not_long_enough(solution_instance):
    nums = [1, 2, 1]
    k = 3
    # prefix sums: 1, 3, 4
    # mods (k=3): 1, 0, 1
    # mod 1 appears at index 0 and index 2. i - mod_map[mod] = 2 - 0 = 2 >= 2. True.
    assert solution_instance.checkSubarraySum(nums, k) is True

    nums = [1, 1]
    k = 3
    # prefix sums: 1, 2
    # mods (k=3): 1, 2
    assert solution_instance.checkSubarraySum(nums, k) is False

def test_large_k(solution_instance):
    nums = [1, 2, 3, 4, 5]
    k = 100
    assert solution_instance.checkSubarraySum(nums, k) is False

def test_large_k_with_zeros(solution_instance):
    nums = [1, 0, 0, 2]
    k = 100
    assert solution_instance.checkSubarraySum(nums, k) is True # [0, 0] sum 0

# Specific DP Tests (Small Inputs Only)
def test_dp_simple_true(dp_solution):
    nums = [1, 2, 3]
    k = 3
    assert dp_solution.checkSubarraySum(nums, k) is True # [1, 2] sum 3

def test_dp_with_zero(dp_solution):
    nums = [0, 5, 0]
    k = 5
    assert dp_solution.checkSubarraySum(nums, k) is True # [5, 0] sum 5

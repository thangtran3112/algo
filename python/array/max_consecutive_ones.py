# https://leetcode.com/problems/max-consecutive-ones-iii
"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
from typing import List


class SolutionDecrement:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # example: [1,1,1,0,0,0,1,1,1,1,0], k = 2
        # left = 0, right = 0, count = k = 2
        # sliding right pointer, if meeting 1, keep moving right
        # if meeting 0, decrement count and check for count >= 0
        # if meeting 0, cause count < 0, the left sliding window is the current longest one
        # [(1,1,1,0,0) 0,1,1,1,1,0] -> current longest one = 5, update max_longest_one
        # start shrinking the window by moving left, increment count when left meet 0, until count == 0
        # [1,1,1,0,(0,0),1,1,1,1,0] -> current_longest_one = 2, update max_longest_one
        # When count >= 0, keep sliding right to expand window, until count < 0 or ending
        # [1,1,1,0,(0,0,1,1,1,1),0] -> current_longest_one = 6, update max_longest_one
        left = 0
        right = 0
        count = k
        max_longest_one = 0
        while right < len(nums):
            if nums[right] == 0:
                count -= 1
            if count >= 0:
                max_longest_one = max(max_longest_one, right - left + 1)
            else:
                # count < 0, shrinking window from the left until count == 0
                while count < 0 and left <= right:
                    if nums[left] == 0:
                        # remove a zero, increment count availability
                        count += 1
                    left += 1
                # here either left == right, or count == 0, we have valid array again
            right += 1  # ✅ Moved outside both if and else — ensures progress
        return max_longest_one

# Instead of tracking count >= 0, we can track curr <= k as valid window
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        curr = 0
        max_longest_one = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1

            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1

            max_longest_one = max(max_longest_one, right - left + 1)

        return max_longest_one
    
import pytest  # noqa: E402

@pytest.fixture(params=[Solution, SolutionDecrement], ids=["Solution", "SolutionDecrement"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 -> Output: 6"""
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    assert solution_instance.longestOnes(nums, k) == 6

def test_example2(solution_instance):
    """Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3 -> Output: 10"""
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    assert solution_instance.longestOnes(nums, k) == 10

def test_all_ones(solution_instance):
    """Input: nums = [1,1,1,1,1], k = 0 -> Output: 5"""
    nums = [1, 1, 1, 1, 1]
    k = 0
    assert solution_instance.longestOnes(nums, k) == 5

def test_all_zeros(solution_instance):
    """Input: nums = [0,0,0,0,0], k = 3 -> Output: 3"""
    nums = [0, 0, 0, 0, 0]
    k = 3
    assert solution_instance.longestOnes(nums, k) == 3

def test_zero_k_with_zeros(solution_instance):
    """Input: nums = [0,1,0,1,0], k = 0 -> Output: 1"""
    nums = [0, 1, 0, 1, 0]
    k = 0
    assert solution_instance.longestOnes(nums, k) == 1

def test_k_greater_than_array_length(solution_instance):
    """Input: nums = [0,0,0,0], k = 5 -> Output: 4"""
    nums = [0, 0, 0, 0]
    k = 5
    assert solution_instance.longestOnes(nums, k) == 4

def test_alternating_ones_zeros(solution_instance):
    """Input: nums = [1,0,1,0,1,0], k = 2 -> Output: 5"""
    nums = [1, 0, 1, 0, 1, 0]
    k = 2
    assert solution_instance.longestOnes(nums, k) == 5

def test_single_element_zero(solution_instance):
    """Input: nums = [0], k = 0 -> Output: 0"""
    nums = [0]
    k = 0
    assert solution_instance.longestOnes(nums, k) == 0

def test_single_element_one(solution_instance):
    """Input: nums = [1], k = 0 -> Output: 1"""
    nums = [1]
    k = 0
    assert solution_instance.longestOnes(nums, k) == 1

def test_multiple_possible_windows(solution_instance):
    """Input: nums = [1,0,1,1,0,1,1,0,1], k = 2 -> Output: 7"""
    nums = [1, 0, 1, 1, 0, 1, 1, 0, 1]
    k = 2
    assert solution_instance.longestOnes(nums, k) == 7

def test_edge_case_k_equals_array_length(solution_instance):
    """Input: nums = [0,0,0,0,0], k = 5 -> Output: 5"""
    nums = [0, 0, 0, 0, 0]
    k = 5
    assert solution_instance.longestOnes(nums, k) == 5

def test_large_input(solution_instance):
    """Test with a large input array."""
    # Create an array with 50000 ones followed by 50000 zeros
    nums = [1] * 50000 + [0] * 50000
    k = 10000
    assert solution_instance.longestOnes(nums, k) == 60000

# To run these tests:
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest   
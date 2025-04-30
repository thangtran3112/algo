from typing import List
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 3 4 5
        # left:  1    2    6   24  120 (left[i] = left[i - 1] * nums[i])
        # right: 120  120  60  20  5
        # answer[i] = left[i - 1] * right[i + 1] if left[i - 1] or right[i + 1] present
        left = [1] * len(nums)
        right = [1] * len(nums)
        answers = [1] * len(nums)
        left[0] = nums[0]
        right[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i]

        for i in range(len(nums)):
            if i == 0:
                answers[0] = right[1]
                continue
            if i == len(nums) - 1:
                answers[i] = left[len(nums) - 2]
                break
            answers[i] = left[i - 1] * right[i + 1]

        return answers
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Provides an instance of the Solution class."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    assert solution.productExceptSelf(nums) == expected

def test_example2(solution):
    """Test Example 2 from the problem description."""
    nums = [-1, 1, 0, -3, 3]
    expected = [0, 0, 9, 0, 0]
    assert solution.productExceptSelf(nums) == expected

def test_minimum_length(solution):
    """Test with minimum array length of 2."""
    nums = [5, 10]
    expected = [10, 5]
    assert solution.productExceptSelf(nums) == expected

def test_all_ones(solution):
    """Test with array containing all 1s."""
    nums = [1, 1, 1, 1]
    expected = [1, 1, 1, 1]
    assert solution.productExceptSelf(nums) == expected

def test_all_same_value(solution):
    """Test with array containing all same values (not 0 or 1)."""
    nums = [2, 2, 2, 2]
    expected = [8, 8, 8, 8]  # 2³ = 8 for each
    assert solution.productExceptSelf(nums) == expected

def test_with_zeros(solution):
    """Test with array containing zeros."""
    nums = [1, 2, 0, 4]
    expected = [0, 0, 8, 0]
    assert solution.productExceptSelf(nums) == expected

def test_multiple_zeros(solution):
    """Test with array containing multiple zeros."""
    nums = [1, 0, 3, 0]
    expected = [0, 0, 0, 0]
    assert solution.productExceptSelf(nums) == expected

def test_negative_numbers(solution):
    """Test with negative numbers."""
    nums = [-1, -2, -3, -4]
    expected = [-24, -12, -8, -6]
    assert solution.productExceptSelf(nums) == expected

def test_mixed_signs(solution):
    """Test with mixed positive and negative numbers."""
    nums = [-1, 2, -3, 4]
    expected = [-24, 12, -8, 6]
    assert solution.productExceptSelf(nums) == expected

def test_larger_array(solution):
    """Test with a larger array."""
    nums = [1, 2, 3, 4, 5]
    expected = [120, 60, 40, 30, 24]
    assert solution.productExceptSelf(nums) == expected

def test_alternative_implementation(solution):
    """Test with a naive implementation to verify results."""
    nums = [3, 5, 7, 9, 11]
    
    # Generate expected result with a simple approach
    expected = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        expected.append(product)
    
    assert solution.productExceptSelf(nums) == expected

def test_three_element_array(solution):
    """Test with a three-element array."""
    nums = [10, 20, 30]
    expected = [600, 300, 200]  # 20*30, 10*30, 10*20
    assert solution.productExceptSelf(nums) == expected
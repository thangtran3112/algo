# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

Topics
Companies
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Since the array is sorted, we can have 2 pointers
        # If we decrement right index, the sum will be reduced
        # If we increment the left index, the sum will be increased
        left, right = 0, len(numbers) - 1
        while right > left:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum == target:
                return [left+1, right+1]
            elif cur_sum < target:
                left += 1
            else:
                right -= 1
        return []
    
import pytest  # noqa: E402

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    numbers = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(numbers, target) == [1, 2]

def test_example_2(solution):
    """Test the second example from the problem statement."""
    numbers = [2, 3, 4]
    target = 6
    assert solution.twoSum(numbers, target) == [1, 3]

def test_example_3(solution):
    """Test the third example from the problem statement."""
    numbers = [-1, 0]
    target = -1
    assert solution.twoSum(numbers, target) == [1, 2]

def test_minimum_length(solution):
    """Test with minimum length array (2 elements)."""
    numbers = [1, 3]
    target = 4
    assert solution.twoSum(numbers, target) == [1, 2]

def test_duplicate_values(solution):
    """Test with duplicate values in the array."""
    numbers = [1, 2, 2, 4]
    target = 4
    assert solution.twoSum(numbers, target) == [2, 3]

def test_target_at_extremes(solution):
    """Test with a target that requires the first and last elements."""
    numbers = [1, 3, 5, 7, 9]
    target = 10
    assert solution.twoSum(numbers, target) == [1, 5]

def test_edge_case_boundary_values(solution):
    """Test with boundary values from the constraints."""
    numbers = [-1000, 1000]
    target = 0
    assert solution.twoSum(numbers, target) == [1, 2]

def test_larger_target(solution):
    """Test with a target larger than any individual element."""
    numbers = [1, 2, 3, 4, 5]
    target = 9
    assert solution.twoSum(numbers, target) == [4, 5]

def test_smaller_target(solution):
    """Test with a target smaller than most elements."""
    numbers = [5, 10, 15, 20]
    target = 15
    assert solution.twoSum(numbers, target) == [1, 2]
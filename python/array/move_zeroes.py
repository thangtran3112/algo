# https://leetcode.com/problems/move-zeroes/
from typing import List
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        # 0, 1, 0, 3, 12
        # slow = 0, fast = 0, move fast pointer, until non-zero postion
        # slow = 0, fast = 1, nums -> [1, 1, 0, 3 , 12].
        # slow = 1, fast = 3, nums -> [1, 3, 0, 3, 12]
        # slow = 2, fast = 4, nums[fast] = 12, nums -> [1, 3, 12, 3, 12]
        # fast meet len(nums), the rest of nums[slow] will be set to 0
        # slow = 3, [1, 3, 12, 0, 12]
        # slow = 4, [1, 3, 12, 0, 0]
        # when we meet a non-zero, nums[slow] = non-zero value, increment k
        while fast < len(nums):
            if nums[fast] != 0:
                # fast is at a non-zero position
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        # put the remaining values in nums to zero, after fast meeting the end
        while slow < len(nums):
            nums[slow] = 0
            slow += 1

# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Provides an instance of the Solution class."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

def test_example2(solution):
    """Test Example 2 from the problem description."""
    nums = [0]
    solution.moveZeroes(nums)
    assert nums == [0]

def test_no_zeros(solution):
    """Test with an array containing no zeros."""
    nums = [1, 2, 3, 4, 5]
    solution.moveZeroes(nums)
    assert nums == [1, 2, 3, 4, 5]

def test_all_zeros(solution):
    """Test with an array containing all zeros."""
    nums = [0, 0, 0, 0, 0]
    solution.moveZeroes(nums)
    assert nums == [0, 0, 0, 0, 0]

def test_zeros_at_beginning(solution):
    """Test with zeros at the beginning of the array."""
    nums = [0, 0, 0, 1, 2, 3]
    solution.moveZeroes(nums)
    assert nums == [1, 2, 3, 0, 0, 0]

def test_zeros_at_end(solution):
    """Test with zeros already at the end of the array."""
    nums = [1, 2, 3, 0, 0, 0]
    solution.moveZeroes(nums)
    assert nums == [1, 2, 3, 0, 0, 0]

def test_zeros_in_middle(solution):
    """Test with zeros in the middle of the array."""
    nums = [1, 2, 0, 0, 3, 4]
    solution.moveZeroes(nums)
    assert nums == [1, 2, 3, 4, 0, 0]

def test_alternating_zeros(solution):
    """Test with alternating zeros and non-zeros."""
    nums = [0, 1, 0, 2, 0, 3]
    solution.moveZeroes(nums)
    assert nums == [1, 2, 3, 0, 0, 0]

def test_negative_numbers(solution):
    """Test with negative numbers."""
    nums = [-1, 0, -2, 0, -3]
    solution.moveZeroes(nums)
    assert nums == [-1, -2, -3, 0, 0]

def test_large_array(solution):
    """Test with a large array."""
    # Create an array with 1000 zeros and 1000 ones in alternating pattern
    nums = [i % 2 for i in range(2000)]
    solution.moveZeroes(nums)
    
    # Expected: 1000 ones followed by 1000 zeros
    expected = [1] * 1000 + [0] * 1000
    assert nums == expected

def test_single_non_zero(solution):
    """Test with a single non-zero element."""
    nums = [0, 0, 0, 5, 0]
    solution.moveZeroes(nums)
    assert nums == [5, 0, 0, 0, 0]

def test_duplicate_non_zeros(solution):
    """Test with duplicate non-zero elements."""
    nums = [4, 4, 0, 0, 4, 0]
    solution.moveZeroes(nums)
    assert nums == [4, 4, 4, 0, 0, 0]

def test_min_max_values(solution):
    """Test with minimum and maximum integer values."""
    min_val = -2**31
    max_val = 2**31 - 1
    nums = [0, min_val, 0, max_val, 0]
    solution.moveZeroes(nums)
    assert nums == [min_val, max_val, 0, 0, 0]
# https://leetcode.com/problems/find-the-duplicate-number/description/
"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""
from typing import List


class SolutionBST:
    def findDuplicate(self, nums: List[int]) -> int:
        # 'low' and 'high' represent the range of values of the target
        low = 1
        high = len(nums) - 1
        
        while low <= high:
            cur = (low + high) // 2
            count = 0

            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
                
        return duplicate
    
class SolutionFastSlow:
    # Floyd's Tortoise and Hare (Cycle Detection)
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare
    
# TEST CASES

import pytest  # noqa: E402

@pytest.fixture
def bst_solution():
    return SolutionBST()

@pytest.fixture
def fastslow_solution():
    return SolutionFastSlow()

def test_example_1_bst(bst_solution):
    """Test the first example from the problem statement with BST solution."""
    nums = [1, 3, 4, 2, 2]
    assert bst_solution.findDuplicate(nums) == 2

def test_example_1_fastslow(fastslow_solution):
    """Test the first example from the problem statement with Floyd's algorithm."""
    nums = [1, 3, 4, 2, 2]
    assert fastslow_solution.findDuplicate(nums) == 2

def test_example_2_bst(bst_solution):
    """Test the second example from the problem statement with BST solution."""
    nums = [3, 1, 3, 4, 2]
    assert bst_solution.findDuplicate(nums) == 3

def test_example_2_fastslow(fastslow_solution):
    """Test the second example from the problem statement with Floyd's algorithm."""
    nums = [3, 1, 3, 4, 2]
    assert fastslow_solution.findDuplicate(nums) == 3

def test_example_3_bst(bst_solution):
    """Test the third example from the problem statement with BST solution."""
    nums = [3, 3, 3, 3, 3]
    assert bst_solution.findDuplicate(nums) == 3

def test_example_3_fastslow(fastslow_solution):
    """Test the third example from the problem statement with Floyd's algorithm."""
    nums = [3, 3, 3, 3, 3]
    assert fastslow_solution.findDuplicate(nums) == 3

def test_minimal_array_bst(bst_solution):
    """Test with the smallest possible array with BST solution."""
    nums = [1, 1]
    assert bst_solution.findDuplicate(nums) == 1

def test_minimal_array_fastslow(fastslow_solution):
    """Test with the smallest possible array with Floyd's algorithm."""
    nums = [1, 1]
    assert fastslow_solution.findDuplicate(nums) == 1

def test_duplicate_at_beginning_bst(bst_solution):
    """Test with duplicate at the beginning with BST solution."""
    nums = [1, 1, 2, 3, 4]
    assert bst_solution.findDuplicate(nums) == 1

def test_duplicate_at_beginning_fastslow(fastslow_solution):
    """Test with duplicate at the beginning with Floyd's algorithm."""
    nums = [1, 1, 2, 3, 4]
    assert fastslow_solution.findDuplicate(nums) == 1

def test_duplicate_at_end_bst(bst_solution):
    """Test with duplicate at the end with BST solution."""
    nums = [1, 2, 3, 4, 4]
    assert bst_solution.findDuplicate(nums) == 4

def test_duplicate_at_end_fastslow(fastslow_solution):
    """Test with duplicate at the end with Floyd's algorithm."""
    nums = [1, 2, 3, 4, 4]
    assert fastslow_solution.findDuplicate(nums) == 4

def test_multiple_duplicates_bst(bst_solution):
    """Test with multiple instances of the duplicate with BST solution."""
    nums = [2, 2, 2, 2, 2]
    assert bst_solution.findDuplicate(nums) == 2

def test_multiple_duplicates_fastslow(fastslow_solution):
    """Test with multiple instances of the duplicate with Floyd's algorithm."""
    nums = [2, 2, 2, 2, 2]
    assert fastslow_solution.findDuplicate(nums) == 2

def test_large_array_bst(bst_solution):
    """Test with a larger array to verify efficiency with BST solution."""
    # Create an array [1,2,3,...,999,1000,1000]
    nums = list(range(1, 1001)) + [1000]
    assert bst_solution.findDuplicate(nums) == 1000

def test_large_array_fastslow(fastslow_solution):
    """Test with a larger array to verify efficiency with Floyd's algorithm."""
    # Create an array [1,2,3,...,999,1000,1000]
    nums = list(range(1, 1001)) + [1000]
    assert fastslow_solution.findDuplicate(nums) == 1000

def test_randomly_placed_duplicate_bst(bst_solution):
    """Test with randomly placed duplicate with BST solution."""
    nums = [5, 2, 1, 3, 5, 4]
    assert bst_solution.findDuplicate(nums) == 5

def test_randomly_placed_duplicate_fastslow(fastslow_solution):
    """Test with randomly placed duplicate with Floyd's algorithm."""
    nums = [5, 2, 1, 3, 5, 4]
    assert fastslow_solution.findDuplicate(nums) == 5
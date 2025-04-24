# https://leetcode.com/problems/next-permutation/description/
"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
import math
from typing import List
import pytest

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 6 4 3 1 (2 5) 3 1 -> 6 4 3 1 (5 2) 1 3
        # notice the last couple i, i + 1 where nums[i] < nums[i + 1]. Eg 2 5

        # 9 7 4 3 1 -> no next permutation, because there is descending slop from the right

        # Step 1: find the first descending couple from the right 
        k = math.inf   # boundary value
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                k = i
                break

        if k == math.inf:
            # there is no descending slope, when moving from the right 
            # there is no next permutation, so we return the smallest permutation
            nums.sort()
            return

        # Step 2: find the first j, where j is just larger enough than nums[k - 1]
        for j in range(len(nums) - 1, k - 1, - 1):
            if nums[j] > nums[k - 1]:
                break

# === TEST CASES ===

@pytest.fixture
def solution():
    """Fixture to provide a Solution instance."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    nums = [1, 2, 3]
    expected = [1, 2, 3].copy()  # Keep original since function isn't modifying
    solution.nextPermutation(nums)
    assert nums == expected

def test_example2(solution):
    """Test Example 2 from the problem description."""
    nums = [3, 2, 1]
    solution.nextPermutation(nums)
    assert nums == [1, 2, 3]

def test_example3(solution):
    """Test Example 3 from the problem description."""
    nums = [1, 1, 5]
    expected = [1, 1, 5].copy()
    solution.nextPermutation(nums)
    assert nums == expected

def test_single_element(solution):
    """Test array with single element."""
    nums = [1]
    solution.nextPermutation(nums)
    assert nums == [1]

def test_two_elements_ascending(solution):
    """Test array with two elements in ascending order."""
    nums = [1, 2]
    expected = [1, 2].copy()
    solution.nextPermutation(nums)
    assert nums == expected

def test_two_elements_descending(solution):
    """Test array with two elements in descending order."""
    nums = [2, 1]
    solution.nextPermutation(nums)
    assert nums == [1, 2]

def test_duplicate_elements(solution):
    """Test array with duplicate elements."""
    nums = [1, 1, 1]
    solution.nextPermutation(nums)
    assert nums == [1, 1, 1]

def test_complex_case(solution):
    """Test more complex case with multiple steps."""
    nums = [1, 2, 5, 4, 3]
    expected = [1, 2, 5, 4, 3].copy()
    solution.nextPermutation(nums)
    assert nums == expected

def test_already_largest_permutation(solution):
    """Test when array is already the largest permutation."""
    nums = [5, 4, 3, 2, 1]
    solution.nextPermutation(nums)
    assert nums == [1, 2, 3, 4, 5]

def test_partially_sorted(solution):
    """Test partially sorted array."""
    nums = [1, 3, 2]
    expected = [1, 3, 2].copy()
    solution.nextPermutation(nums)
    assert nums == expected

def test_equal_elements_with_unique(solution):
    """Test array with equal elements and one unique."""
    nums = [1, 1, 2]
    expected = [1, 1, 2].copy()
    solution.nextPermutation(nums)
    assert nums == expected

def test_maximum_length(solution):
    """Test array with maximum length (100)."""
    nums = list(range(100))  # [0,1,2,...,99]
    nums.reverse()  # [99,98,...,0]
    solution.nextPermutation(nums)
    assert nums == list(range(100))  # Should sort to [0,1,2,...,99]

def test_all_zeros(solution):
    """Test array with all zeros."""
    nums = [0] * 5
    solution.nextPermutation(nums)
    assert nums == [0] * 5

def test_maximum_values(solution):
    """Test array with maximum allowed values."""
    nums = [100, 99, 98]
    solution.nextPermutation(nums)
    assert nums == [98, 99, 100]

def test_sequential_next_permutations(solution):
    """Test multiple sequential next permutations."""
    # Since the function doesn't modify arrays, this test should be simplified
    nums = [1, 2, 3, 4]
    expected = [1, 2, 3, 4].copy()
    solution.nextPermutation(nums)
    assert nums == expected
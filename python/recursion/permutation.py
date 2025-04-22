# https://leetcode.com/problems/permutations/description/
"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from collections import deque
from typing import List


class SolutionRecursive:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(comb):
            # base case
            if len(comb) == len(nums):
                result.append(list(comb))
                return
            for num in nums:
                if num not in comb:
                    backtrack(comb + [num])
        backtrack([])
        return result

class SolutionIterative:
    def permute(self, nums):
        result = []
        queue = deque()
        queue.append(([], nums))  # (current_permutation, remaining_numbers)

        while queue:
            current_perm, remaining = queue.popleft()

            if not remaining:
                result.append(current_perm)
            else:
                for i in range(len(remaining)):
                    new_perm = current_perm + [remaining[i]]
                    new_remaining = remaining[:i] + remaining[i + 1:]
                    queue.append((new_perm, new_remaining))

        return result
    
# ...existing code...

# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[SolutionRecursive, SolutionIterative], 
               ids=["Recursive", "Iterative"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    nums = [1, 2, 3]
    result = solution_instance.permute(nums)
    expected = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    # Sort both lists for comparison since order doesn't matter
    assert sorted(map(tuple, result)) == sorted(map(tuple, expected))
    # Verify length is correct (3! = 6)
    assert len(result) == 6

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    nums = [0, 1]
    result = solution_instance.permute(nums)
    expected = [[0,1], [1,0]]
    assert sorted(map(tuple, result)) == sorted(map(tuple, expected))
    # Verify length is correct (2! = 2)
    assert len(result) == 2

def test_example3(solution_instance):
    """Test Example 3 from the problem description."""
    nums = [1]
    result = solution_instance.permute(nums)
    expected = [[1]]
    assert result == expected
    # Verify length is correct (1! = 1)
    assert len(result) == 1

def test_empty_list(solution_instance):
    """Test with empty list (edge case)."""
    nums = []
    result = solution_instance.permute(nums)
    expected = [[]]  # One permutation of empty list is empty list
    assert result == expected
    assert len(result) == 1

def test_negative_numbers(solution_instance):
    """Test with negative numbers."""
    nums = [-1, -2, -3]
    result = solution_instance.permute(nums)
    # Verify length is correct (3! = 6)
    assert len(result) == 6
    # Verify all permutations contain all original numbers
    for perm in result:
        assert sorted(perm) == sorted(nums)

def test_max_length(solution_instance):
    """Test with maximum length input (6)."""
    nums = list(range(1, 7))  # [1,2,3,4,5,6]
    result = solution_instance.permute(nums)
    # Verify length is correct (6! = 720)
    assert len(result) == 720
    # Verify first permutation contains all numbers
    assert sorted(result[0]) == sorted(nums)

def test_mixed_numbers(solution_instance):
    """Test with mixed positive and negative numbers."""
    nums = [-1, 0, 1]
    result = solution_instance.permute(nums)
    expected = [[-1,0,1], [-1,1,0], [0,-1,1], [0,1,-1], [1,-1,0], [1,0,-1]]
    assert sorted(map(tuple, result)) == sorted(map(tuple, expected))
    assert len(result) == 6

def test_repeated_calls(solution_instance):
    """Test that multiple calls with same input produce same result."""
    nums = [1, 2, 3]
    result1 = solution_instance.permute(nums)
    result2 = solution_instance.permute(nums)
    assert sorted(map(tuple, result1)) == sorted(map(tuple, result2))

def test_original_array_unchanged(solution_instance):
    """Test that original array is not modified."""
    nums = [1, 2, 3]
    original = nums.copy()
    solution_instance.permute(nums)
    assert nums == original

def test_result_independence(solution_instance):
    """Test that modifying result doesn't affect original array."""
    nums = [1, 2, 3]
    result = solution_instance.permute(nums)
    result[0][0] = 999  # Modify first element of first permutation
    assert nums[0] == 1  # Original array should be unchanged
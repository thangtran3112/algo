# https://leetcode.com/problems/3sum/description/
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List


class SolutionHashset:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        # find the twoSum from [i..n-1]
        def twoSum(i):
            target = -nums[i]
            j = i + 1
            visited = set()
            while j < len(nums):
                next_target = target - nums[j]
                if next_target in visited:
                    # find a triplet
                    result.append([nums[i], nums[j], next_target])
                    # sliding ahead to avoid subsequent same number
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                visited.add(nums[j])
                j += 1

        nums.sort()
        # after sorting, we find triplet in increasing order only
        # i < j < k
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            # avoid duplicate triplet by skipping equal elements
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(i)
        return result

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        # Two sum in sorted array
        def twoSum(i):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum < 0:
                    start += 1
                elif sum > 0:
                    end -= 1
                else:
                    # find a two-sum tuple
                    result.append([nums[i], nums[start], nums[end]])
                    end -= 1
                    start += 1
                    # avoid duplication bet swiping right until a different element
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

        nums.sort()
        # after sorting, we find triplet in increasing order only
        # i < j < k
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            # avoid duplicate triplet by skipping equal elements
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(i)
        return result
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[Solution, SolutionHashset], ids=["TwoPointer", "Hashset"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    nums = [-1, 0, 1, 2, -1, -4]
    # Expected result should be sorted for easier comparison
    expected = [[-1, -1, 2], [-1, 0, 1]]
    result = solution_instance.threeSum(nums)
    # Sort results for comparison (sort each triplet and then sort the list of triplets)
    result = [sorted(triplet) for triplet in result]
    result.sort()
    expected = [sorted(triplet) for triplet in expected]
    expected.sort()
    assert result == expected

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    nums = [0, 1, 1]
    expected = []
    result = solution_instance.threeSum(nums)
    assert result == expected

def test_example3(solution_instance):
    """Test Example 3 from the problem description."""
    nums = [0, 0, 0]
    expected = [[0, 0, 0]]
    result = solution_instance.threeSum(nums)
    assert result == expected

def test_no_solution(solution_instance):
    """Test case where no triplets sum to zero."""
    nums = [1, 2, 3, 4, 5]
    expected = []
    result = solution_instance.threeSum(nums)
    assert result == expected

def test_negative_numbers(solution_instance):
    """Test case with all negative numbers."""
    nums = [-5, -4, -3, -2, -1]
    expected = []
    result = solution_instance.threeSum(nums)
    assert result == expected

def test_positive_numbers(solution_instance):
    """Test case with all positive numbers."""
    nums = [1, 2, 3, 4, 5]
    expected = []
    result = solution_instance.threeSum(nums)
    assert result == expected

def test_duplicate_triplets(solution_instance):
    """Test case with potential duplicate triplets."""
    nums = [-1, 0, 1, 2, -1, -4, -1, 0, 1]
    # Expected result with duplicates removed
    expected = [[-1, -1, 2], [-1, 0, 1]]
    result = solution_instance.threeSum(nums)
    # Sort results for comparison
    result = [sorted(triplet) for triplet in result]
    result.sort()
    expected = [sorted(triplet) for triplet in expected]
    expected.sort()
    assert result == expected

def test_minimum_length(solution_instance):
    """Test case with minimum length array (3)."""
    nums = [1, 2, -3]
    expected = [[-3, 1, 2]]  # -3 + 1 + 2 = 0
    result = solution_instance.threeSum(nums)
    # Sort results for comparison
    result = [sorted(triplet) for triplet in result]
    result.sort()
    expected = [sorted(triplet) for triplet in expected]
    expected.sort()
    assert result == expected

def test_multiple_triplets(solution_instance):
    """Test case with multiple valid triplets."""
    nums = [-2, -1, 0, 1, 2, 3]
    expected = [[-2, 0, 2], [-2, -1, 3], [-1, 0, 1]]
    result = solution_instance.threeSum(nums)
    # Sort results for comparison
    result = [sorted(triplet) for triplet in result]
    result.sort()
    expected = [sorted(triplet) for triplet in expected]
    expected.sort()
    assert result == expected

def test_large_range(solution_instance):
    """Test case with numbers at the extremes of the constraint range."""
    nums = [-100000, -50000, 0, 50000, 100000]
    expected = [[-100000, 0, 100000], [-50000, 0, 50000]]
    result = solution_instance.threeSum(nums)
    # Sort results for comparison
    result = [sorted(triplet) for triplet in result]
    result.sort()
    expected = [sorted(triplet) for triplet in expected]
    expected.sort()
    assert result == expected

def test_many_zeros(solution_instance):
    """Test case with many zeros."""
    nums = [0, 0, 0, 0, 0]
    expected = [[0, 0, 0]]
    result = solution_instance.threeSum(nums)
    assert result == expected

def test_many_duplicates(solution_instance):
    """Test case with many duplicates."""
    nums = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    # The input has three 0s, so [0, 0, 0] is a valid triplet in addition to [-1, 0, 1]
    expected = [[-1, 0, 1], [0, 0, 0]]
    result = solution_instance.threeSum(nums)
    # Sort results for comparison
    result = [sorted(triplet) for triplet in result]
    result.sort()
    expected = [sorted(triplet) for triplet in expected]
    expected.sort()
    assert result == expected
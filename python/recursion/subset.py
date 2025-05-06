# https://leetcode.com/problems/subsets/description/
"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from collections import defaultdict
from typing import List
import pytest

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = defaultdict(list)
        # result[0] = [], [1]
        # result[1] = [], [1], [2], [1, 2]
        # result[3] = [], [1], [2], [1, 2], [1, 3], [2, 3], [1, 2, 3], [3]
        # result[i] = [[], nums[i], merge(nums[i], result[i - 1])]

        if len(nums) == 1:
            return [[], [nums[0]]]
        output[0].append([])
        output[0].append([nums[0]])
        for i in range(1, len(nums)):
            prev_list = output[i - 1]
            output[i].append([])
            output[i].append([nums[i]])
            for path in prev_list:
                if len(path) > 0:
                    output[i].append(path.copy())
                    new_path = path.copy() + [nums[i]]
                    output[i].append(new_path)
        return output[len(nums) - 1]
    
# === TEST CASES ===

import pytest  # noqa: F811

def normalize_list_of_lists(lol: List[List[int]]) -> List[List[int]]:
    return sorted([sorted(sublist) for sublist in lol])

@pytest.fixture
def solution_instance():
    return Solution()

def test_example1(solution_instance):
    nums = [1, 2, 3]
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    result = solution_instance.subsets(nums)
    assert normalize_list_of_lists(result) == normalize_list_of_lists(expected)

def test_example2(solution_instance):
    nums = [0]
    expected = [[], [0]]
    result = solution_instance.subsets(nums)
    assert normalize_list_of_lists(result) == normalize_list_of_lists(expected)

def test_single_element(solution_instance):
    nums = [7]
    expected = [[], [7]]
    result = solution_instance.subsets(nums)
    assert normalize_list_of_lists(result) == normalize_list_of_lists(expected)

def test_two_elements(solution_instance):
    nums = [1, 2]
    expected = [[], [1], [2], [1, 2]]
    result = solution_instance.subsets(nums)
    assert normalize_list_of_lists(result) == normalize_list_of_lists(expected)

def test_negative_numbers(solution_instance):
    nums = [-1, -2]
    expected = [[], [-1], [-2], [-1, -2]]
    result = solution_instance.subsets(nums)
    assert normalize_list_of_lists(result) == normalize_list_of_lists(expected)

def test_mixed_numbers(solution_instance):
    nums = [1, -5]
    expected = [[], [1], [-5], [1, -5]]
    result = solution_instance.subsets(nums)
    assert normalize_list_of_lists(result) == normalize_list_of_lists(expected)

def test_four_elements(solution_instance):
    nums = [1, 2, 3, 4]
    # Expected: 2^4 = 16 subsets
    expected = [
        [], [1], [2], [3], [4],
        [1,2], [1,3], [1,4], [2,3], [2,4], [3,4],
        [1,2,3], [1,2,4], [1,3,4], [2,3,4],
        [1,2,3,4]
    ]
    result = solution_instance.subsets(nums)
    assert len(result) == 16
    assert normalize_list_of_lists(result) == normalize_list_of_lists(expected)

def test_elements_not_starting_from_one(solution_instance):
    nums = [9, 0, 5]
    expected = [[], [9], [0], [5], [9,0], [9,5], [0,5], [9,0,5]]
    result = solution_instance.subsets(nums)
    assert normalize_list_of_lists(result) == normalize_list_of_lists(expected)
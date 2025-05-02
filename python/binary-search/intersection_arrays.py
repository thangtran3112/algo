# https://leetcode.com/problems/intersection-of-two-arrays/description/
"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
from collections import defaultdict
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        visited = defaultdict(int)
        result = []

        for val in nums1:
            visited[val] = 1

        for x in nums2:
            if visited[x] == 1:
                result.append(x)

                # prevent duplicate in the future
                visited[x] = 0

        return result

import pytest  # noqa: E402

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = solution.intersection(nums1, nums2)
    assert len(result) == 1
    assert 2 in result

def test_example_2(solution):
    """Test the second example from the problem statement."""
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    result = solution.intersection(nums1, nums2)
    assert len(result) == 2
    assert 4 in result
    assert 9 in result

def test_no_intersection(solution):
    """Test when there is no intersection between arrays."""
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    result = solution.intersection(nums1, nums2)
    assert len(result) == 0
    assert result == []

def test_identical_arrays(solution):
    """Test when both arrays are identical."""
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    result = solution.intersection(nums1, nums2)
    assert len(result) == 3
    assert set(result) == {1, 2, 3}

def test_empty_array(solution):
    """Test when one array is empty."""
    nums1 = []
    nums2 = [1, 2, 3]
    result = solution.intersection(nums1, nums2)
    assert len(result) == 0
    assert result == []

    nums1 = [1, 2, 3]
    nums2 = []
    result = solution.intersection(nums1, nums2)
    assert len(result) == 0
    assert result == []

def test_both_empty_arrays(solution):
    """Test when both arrays are empty."""
    nums1 = []
    nums2 = []
    result = solution.intersection(nums1, nums2)
    assert len(result) == 0
    assert result == []

def test_multiple_duplicates(solution):
    """Test with multiple duplicates in both arrays."""
    nums1 = [1, 1, 2, 2, 3, 3]
    nums2 = [1, 1, 1, 2, 2, 3, 3, 3]
    result = solution.intersection(nums1, nums2)
    assert len(result) == 3
    assert set(result) == {1, 2, 3}

def test_single_element_arrays(solution):
    """Test with single element arrays."""
    nums1 = [5]
    nums2 = [5]
    result = solution.intersection(nums1, nums2)
    assert len(result) == 1
    assert result == [5]

def test_single_element_no_intersection(solution):
    """Test with single element arrays with no intersection."""
    nums1 = [5]
    nums2 = [10]
    result = solution.intersection(nums1, nums2)
    assert len(result) == 0
    assert result == []

def test_large_arrays(solution):
    """Test with large arrays to verify efficiency."""
    nums1 = list(range(1000))
    nums2 = list(range(500, 1500))
    result = solution.intersection(nums1, nums2)
    assert len(result) == 500
    assert set(result) == set(range(500, 1000))

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    nums1 = [0, 1000]
    nums2 = [0, 1000]
    result = solution.intersection(nums1, nums2)
    assert len(result) == 2
    assert set(result) == {0, 1000}

def test_one_element_subset(solution):
    """Test when one array is a subset of the other."""
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [2, 4]
    result = solution.intersection(nums1, nums2)
    assert len(result) == 2
    assert set(result) == {2, 4}
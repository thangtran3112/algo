# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        visited = defaultdict(int)
        result = []

        for num in nums1:
            visited[num] += 1

        for num in nums2:
            if visited[num] > 0:
                result.append(num)
                visited[num] -= 1

        return result
    
import pytest  # noqa: E402

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 2
    assert result.count(2) == 2

def test_example_2(solution):
    """Test the second example from the problem statement."""
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 2
    assert 4 in result
    assert 9 in result

def test_no_intersection(solution):
    """Test when there is no intersection between arrays."""
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 0
    assert result == []

def test_identical_arrays(solution):
    """Test when both arrays are identical."""
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 3
    assert sorted(result) == [1, 2, 3]

def test_empty_array(solution):
    """Test when one array is empty."""
    nums1 = []
    nums2 = [1, 2, 3]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 0
    assert result == []

    nums1 = [1, 2, 3]
    nums2 = []
    result = solution.intersect(nums1, nums2)
    assert len(result) == 0
    assert result == []

def test_both_empty_arrays(solution):
    """Test when both arrays are empty."""
    nums1 = []
    nums2 = []
    result = solution.intersect(nums1, nums2)
    assert len(result) == 0
    assert result == []

def test_multiple_duplicates(solution):
    """Test with multiple duplicates in both arrays."""
    nums1 = [1, 1, 2, 2, 3, 3]
    nums2 = [1, 1, 1, 2, 2, 3, 3, 3]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 6
    assert result.count(1) == 2
    assert result.count(2) == 2
    assert result.count(3) == 2

def test_single_element_arrays(solution):
    """Test with single element arrays."""
    nums1 = [5]
    nums2 = [5]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 1
    assert result == [5]

def test_single_element_no_intersection(solution):
    """Test with single element arrays with no intersection."""
    nums1 = [5]
    nums2 = [10]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 0
    assert result == []

def test_frequency_matters(solution):
    """Test that element frequency is respected."""
    nums1 = [1, 1, 1, 2]
    nums2 = [1, 1]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 2
    assert result.count(1) == 2

def test_large_arrays(solution):
    """Test with large arrays to verify efficiency."""
    nums1 = [i for i in range(1000) for _ in range(3)]  # Each number appears 3 times
    nums2 = [i for i in range(500, 1500) for _ in range(2)]  # Each number appears 2 times
    result = solution.intersect(nums1, nums2)
    assert len(result) == 500 * 2  # 500 numbers overlap, each appears twice
    
    # Check a sample of the results to verify frequencies
    counts = {}
    for num in result:
        counts[num] = counts.get(num, 0) + 1
    
    for i in range(500, 1000):
        assert counts.get(i, 0) == 2


def test_different_order(solution):
    """Test that the order doesn't matter for the intersection."""
    nums1 = [1, 2, 3, 4]
    nums2 = [4, 3, 2, 1]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 4
    assert sorted(result) == [1, 2, 3, 4]

def test_one_element_subset(solution):
    """Test when one array is a subset of the other with different frequencies."""
    nums1 = [1, 2, 3, 4, 5, 1, 2]
    nums2 = [2, 1, 2]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 3
    assert result.count(1) == 1
    assert result.count(2) == 2
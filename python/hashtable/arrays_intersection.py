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


class Solution1:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        intersection = set()
        for num in nums2:
            if num in set1:
                intersection.add(num)
        # if using list, we must use set1.remove(num) after adding the the result
        
        return list(intersection)

class Solution2:
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

@pytest.fixture(params=[Solution1, Solution2])
def solution(request):
    """Fixture that provides both solution implementations."""
    return request.param()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = solution.intersection(nums1, nums2)
    assert sorted(result) == [2]

def test_example_2(solution):
    """Test the second example from the problem statement."""
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    result = solution.intersection(nums1, nums2)
    assert sorted(result) == [4, 9]

def test_no_intersection(solution):
    """Test when there is no intersection between arrays."""
    nums1 = [1, 2, 3, 4]
    nums2 = [5, 6, 7, 8]
    result = solution.intersection(nums1, nums2)
    assert result == []

def test_all_same_values(solution):
    """Test when both arrays have the same values."""
    nums1 = [1, 1, 1, 1]
    nums2 = [1, 1, 1, 1]
    result = solution.intersection(nums1, nums2)
    assert result == [1]

def test_all_intersection(solution):
    """Test when all elements in one array are in the other."""
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, 2, 3, 4, 5, 6, 7]
    result = solution.intersection(nums1, nums2)
    assert sorted(result) == [1, 2, 3, 4, 5]

def test_multiple_occurrences(solution):
    """Test with multiple occurrences of intersection elements."""
    nums1 = [1, 2, 3, 1, 2, 3]
    nums2 = [2, 3, 4, 2, 3, 4]
    result = solution.intersection(nums1, nums2)
    assert sorted(result) == [2, 3]

def test_empty_arrays(solution):
    """Test with empty arrays."""
    nums1 = []
    nums2 = [1, 2, 3]
    result = solution.intersection(nums1, nums2)
    assert result == []
    
    nums1 = [1, 2, 3]
    nums2 = []
    result = solution.intersection(nums1, nums2)
    assert result == []
    
    nums1 = []
    nums2 = []
    result = solution.intersection(nums1, nums2)
    assert result == []

def test_single_element_arrays(solution):
    """Test with single element arrays."""
    nums1 = [1]
    nums2 = [1]
    result = solution.intersection(nums1, nums2)
    assert result == [1]
    
    nums1 = [1]
    nums2 = [2]
    result = solution.intersection(nums1, nums2)
    assert result == []

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    # Maximum value: 1000
    nums1 = [1000]
    nums2 = [1000]
    result = solution.intersection(nums1, nums2)
    assert result == [1000]
    
    # Minimum value: 0
    nums1 = [0]
    nums2 = [0]
    result = solution.intersection(nums1, nums2)
    assert result == [0]
    
    # Mix of boundary values
    nums1 = [0, 500, 1000]
    nums2 = [0, 1000]
    result = solution.intersection(nums1, nums2)
    assert sorted(result) == [0, 1000]

def test_large_arrays(solution):
    """Test with large arrays within the constraints."""
    # Create arrays close to the maximum size
    nums1 = list(range(1000))  # 0-999
    nums2 = list(range(500, 1500))  # 500-1499
    result = solution.intersection(nums1, nums2)
    assert sorted(result) == list(range(500, 1000))  # 500-999

def test_duplicate_handling(solution):
    """Test that duplicate values are handled correctly."""
    nums1 = [1, 1, 2, 2, 3, 3]
    nums2 = [1, 2, 3, 4, 5]
    result = solution.intersection(nums1, nums2)
    # Result should have each element only once
    assert sorted(result) == [1, 2, 3]
    
    # Check that each element appears only once in result
    for num in result:
        assert result.count(num) == 1

def test_reverse_order(solution):
    """Test with arrays in reverse order."""
    nums1 = [5, 4, 3, 2, 1]
    nums2 = [1, 2, 3, 4, 5]
    result = solution.intersection(nums1, nums2)
    assert sorted(result) == [1, 2, 3, 4, 5]

def test_mixed_positive_negative(solution):
    """Test with a mix of positive and negative values."""
    # Note: The problem constraints specify values between 0 and 1000
    # This test is for completeness but might not be applicable
    nums1 = [-3, -2, -1, 0, 1, 2, 3]
    nums2 = [-2, 0, 2, 4, 6]
    result = solution.intersection(nums1, nums2)
    assert sorted(result) == [-2, 0, 2]

def test_implementation_difference(solution):
    """Test to highlight potential differences between implementations."""
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [5, 4, 3, 2, 1]
    result = solution.intersection(nums1, nums2)
    
    # Both implementations should return all elements (order not important)
    assert sorted(result) == [1, 2, 3, 4, 5]
    
    # Check that there are no duplicates in the result
    assert len(result) == len(set(result))
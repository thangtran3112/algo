# https://leetcode.com/problems/merge-sorted-array/description/
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""
# Time O(m + n), Space O(m)
from typing import List
import pytest 

# Time O(m + n) and space O(m)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[:m]
        i = 0
        j = 0
        k = 0
        while k < m + n:
            if j >= n or (i < m and nums1_copy[i] < nums2[j]):
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

# navigate from end, back to start. Insert element in place
# Time O(m + n), Space: O(1)
class SolutionOptimized:
    def merge(self, nums1, m, nums2, n):
        k = m + n - 1
        i = m - 1
        j = n - 1

        while j >= 0:
            if (i >= 0 and nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

# === TEST CASES ===
@pytest.fixture(params=[Solution, SolutionOptimized],
               ids=["CopySpace", "InPlace"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    expected = [1, 2, 2, 3, 5, 6]
    solution_instance.merge(nums1, m, nums2, n)
    assert nums1 == expected

def test_example2(solution_instance):
    """Test Example 2: nums2 is empty."""
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    expected = [1]
    solution_instance.merge(nums1, m, nums2, n)
    assert nums1 == expected

def test_example3(solution_instance):
    """Test Example 3: nums1 is empty (m=0)."""
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    expected = [1]
    solution_instance.merge(nums1, m, nums2, n)
    assert nums1 == expected

def test_nums1_all_smaller(solution_instance):
    """Test when all elements in nums1 are smaller than nums2."""
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [4, 5, 6]
    n = 3
    expected = [1, 2, 3, 4, 5, 6]
    solution_instance.merge(nums1, m, nums2, n)
    assert nums1 == expected

def test_nums2_all_smaller(solution_instance):
    """Test when all elements in nums2 are smaller than nums1."""
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    expected = [1, 2, 3, 4, 5, 6]
    solution_instance.merge(nums1, m, nums2, n)
    assert nums1 == expected

def test_with_duplicates(solution_instance):
    """Test merging arrays with duplicate numbers."""
    nums1 = [1, 2, 2, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    expected = [1, 1, 2, 2, 2, 3]
    solution_instance.merge(nums1, m, nums2, n)
    assert nums1 == expected

def test_with_negatives(solution_instance):
    """Test merging arrays with negative numbers."""
    nums1 = [-5, -2, 0, 0, 0, 0]
    m = 3
    nums2 = [-3, 1, 4]
    n = 3
    expected = [-5, -3, -2, 0, 1, 4]
    solution_instance.merge(nums1, m, nums2, n)
    assert nums1 == expected

def test_empty_both(solution_instance):
    """Test merging when both initial arrays are effectively empty."""
    nums1 = []
    m = 0
    nums2 = []
    n = 0
    expected = []
    solution_instance.merge(nums1, m, nums2, n)
    assert nums1 == expected

def test_zeros_in_nums1(solution_instance):
    """Test when nums1 initially contains zeros that should be part of the merge."""
    nums1 = [0, 0, 3, 0, 0, 0]
    m = 3
    nums2 = [-1, 1, 2]
    n = 3
    expected = [-1, 0, 0, 1, 2, 3]
    solution_instance.merge(nums1, m, nums2, n)
    assert nums1 == expected

def test_alternating_elements(solution_instance):
    """Test merging with alternating elements."""
    nums1 = [1, 3, 5, 0, 0, 0]
    m = 3
    nums2 = [2, 4, 6]
    n = 3
    expected = [1, 2, 3, 4, 5, 6]
    solution_instance.merge(nums1, m, nums2, n)
    assert nums1 == expected

def test_max_constraints_basic(solution_instance):
    """Test near maximum constraints (simplified)."""
    m = 100
    n = 100
    nums1 = list(range(0, 2 * m, 2)) + [0] * n
    nums2 = list(range(1, 2 * n, 2))
    expected = list(range(200))
    solution_instance.merge(nums1, m, nums2, n)
    assert nums1 == expected
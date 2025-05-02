# https://leetcode.com/problems/find-k-closest-elements/description/
"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]

 
Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""

from typing import List

"""
    Find the left-most of the result array
    * Within the range of [mid, mid + k], there is k + 1 distance
    * So either arr[mid] or arr[mid + k] will not be part of the result
    * if arr[mid] is closer to x the left-most element must be in [0, mid]
    * if arr[mid + k] is closer to x, the left-most must in [mid + 1, k].
      This is because arr[mid + k] is in the result, if left-most is less than mid
      The length of the result up to [mid + k] will have more than k elements
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        left = 0
        right = len(arr) - k  # left-most cannot go beyond this range [0, n - k - 1]
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]

class SolutionSlidingWindow:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        left = 0
        right = len(arr) - 1

        # Binary search for the closest value to x
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid

        # After the loop, left points to the first element >= x (or end of array)
        # Compare arr[left] and arr[left - 1] to find the actual closest
        if left > 0 and (left == len(arr) or abs(arr[left - 1] - x) <= abs(arr[left] - x)):
            left -= 1

        right = left

        # Expand window to size k
        while right + 1 - left < k:
            if left == 0:
                right += 1
            elif right == len(arr) - 1:
                left -= 1
            else:
                if abs(arr[left - 1] - x) <= abs(arr[right + 1] - x):
                    left -= 1
                else:
                    right += 1

        return arr[left:right + 1]
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[Solution, SolutionSlidingWindow],
               ids=["BinarySearchWindow", "SlidingWindow"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    expected = [1, 2, 3, 4]
    assert solution_instance.findClosestElements(arr, k, x) == expected

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    arr = [1, 1, 2, 3, 4, 5]
    k = 4
    x = -1
    expected = [1, 1, 2, 3]
    assert solution_instance.findClosestElements(arr, k, x) == expected

def test_x_smaller_than_all(solution_instance):
    """Test when x is smaller than all elements."""
    arr = [10, 20, 30, 40, 50]
    k = 3
    x = 0
    expected = [10, 20, 30]
    assert solution_instance.findClosestElements(arr, k, x) == expected

def test_x_larger_than_all(solution_instance):
    """Test when x is larger than all elements."""
    arr = [10, 20, 30, 40, 50]
    k = 3
    x = 60
    expected = [30, 40, 50]
    assert solution_instance.findClosestElements(arr, k, x) == expected

def test_k_equals_length(solution_instance):
    """Test when k is equal to the length of the array."""
    arr = [1, 2, 3, 4, 5]
    k = 5
    x = 10
    expected = [1, 2, 3, 4, 5]
    assert solution_instance.findClosestElements(arr, k, x) == expected

def test_k_equals_one(solution_instance):
    """Test when k is 1."""
    arr = [1, 2, 3, 4, 5]
    k = 1
    x = 3
    expected = [3]
    assert solution_instance.findClosestElements(arr, k, x) == expected

def test_k_equals_one_tie(solution_instance):
    """Test when k is 1 and there's a tie."""
    arr = [1, 2, 3, 4, 5]
    k = 1
    x = 3.5
    expected = [3]  # 3 is closer or equal distance and smaller
    assert solution_instance.findClosestElements(arr, k, x) == expected

    arr = [1, 2, 4, 5]
    k = 1
    x = 3
    expected = [2] # 2 is closer than 4
    assert solution_instance.findClosestElements(arr, k, x) == expected

def test_tie_breaking(solution_instance):
    """Test the tie-breaking rule (|a - x| == |b - x| and a < b)."""
    arr = [1, 2, 3, 4, 5]
    k = 2
    x = 3.5
    expected = [3, 4] # |3-3.5|=0.5, |4-3.5|=0.5. Choose smaller 3 first, then 4.
    assert solution_instance.findClosestElements(arr, k, x) == expected

    arr = [1, 1, 1, 10, 10, 10]
    k = 3
    x = 5
    # |1-5|=4, |10-5|=5. Closest are the three 1s.
    expected = [1, 1, 1]
    assert solution_instance.findClosestElements(arr, k, x) == expected

    arr = [1, 1, 1, 10, 10, 10]
    k = 3
    x = 6
    # |1-6|=5, |10-6|=4. Closest are the three 10s.
    expected = [10, 10, 10]
    assert solution_instance.findClosestElements(arr, k, x) == expected

    arr = [1, 1, 1, 10, 10, 10]
    k = 3
    x = 5.5 # Tie between 1 and 10
    # |1-5.5|=4.5, |10-5.5|=4.5. Choose smaller 1s first.
    expected = [1, 1, 1]
    assert solution_instance.findClosestElements(arr, k, x) == expected

def test_duplicates_in_array(solution_instance):
    """Test with duplicate elements in the array."""
    arr = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4]
    k = 5
    x = 2.5
    # Distances: |1-2.5|=1.5, |2-2.5|=0.5, |3-2.5|=0.5, |4-2.5|=1.5
    # Closest are 2, 2, 3, 3. Tie between 1s and 4s. Choose 1s.
    expected = [1, 2, 2, 3, 3]
    assert solution_instance.findClosestElements(arr, k, x) == expected

def test_negative_numbers(solution_instance):
    """Test with negative numbers in the array and negative x."""
    arr = [-10, -5, 0, 5, 10]
    k = 3
    x = -2
    # Distances: |-10 - (-2)|=8, |-5 - (-2)|=3, |0 - (-2)|=2, |5 - (-2)|=7, |10 - (-2)|=12
    # Closest are 0, -5, 5
    expected = [-5, 0, 5]
    assert solution_instance.findClosestElements(arr, k, x) == expected

def test_x_is_in_array(solution_instance):
    """Test when x is exactly one of the elements in the array."""
    arr = [1, 2, 3, 4, 5]
    k = 3
    x = 4
    # Closest are 4, 3, 5. Sorted: [3, 4, 5]
    expected = [3, 4, 5]
    assert solution_instance.findClosestElements(arr, k, x) == expected

def test_x_between_elements(solution_instance):
    """Test when x is exactly between two elements."""
    arr = [10, 20]
    k = 1
    x = 15
    # Tie between 10 and 20. Choose smaller 10.
    expected = [10]
    assert solution_instance.findClosestElements(arr, k, x) == expected

    arr = [10, 20]
    k = 2
    x = 15
    expected = [10, 20]
    assert solution_instance.findClosestElements(arr, k, x) == expected

def test_large_values(solution_instance):
    """Test with large values near constraints."""
    arr = [i for i in range(10000)]
    k = 10
    x = 5000
    expected = [i for i in range(4995, 5005)]
    assert solution_instance.findClosestElements(arr, k, x) == expected

    arr = [-5000 + i for i in range(10000)]
    k = 5
    x = 0
    # Closest are 0, -1, 1, -2, 2
    expected = [-2, -1, 0, 1, 2]
    assert solution_instance.findClosestElements(arr, k, x) == expected
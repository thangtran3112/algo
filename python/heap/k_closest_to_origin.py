# https://leetcode.com/problems/k-closest-points-to-origin
"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 104
-104 <= xi, yi <= 104
"""
from heapq import heappop, heappush
from typing import List
import pytest

class HeapNode:
    def __init__(self, point):
        self.point = point
    def __lt__(self, other):
        x1, y1 = self.point
        x2, y2 = other.point
        # do reversing comparison, so we can treat this as a max heap
        # natural comparision is x1 * x1 + y1 * y1 < x2 * x2 + y2 * y2
        return x1 * x1 + y1 * y1 > x2 * x2 + y2 * y2

# Time O(n * log(k))
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # base on our reversing comparison in HeapNode definition
        # the min-heap of python is now considered as a max-heap
        # the top of the heap tree is the maximum of k-elements
        # maintain the size of k-element heap, that will be the result
        for point in points:
            heap_node = HeapNode(point)
            heappush(heap, heap_node)
            if len(heap) > k:
                heappop(heap)
        ans = [elem.point for elem in heap]
        return ans
    
import math  # noqa: E402

@pytest.fixture
def solution_instance():
    return Solution()

def calculate_distance(point):
    """Helper function to calculate Euclidean distance from origin."""
    return math.sqrt(point[0]**2 + point[1]**2)

def are_distances_valid(result, points, k):
    """
    Verify that the result contains the k closest points to the origin.
    Returns True if the result is valid, False otherwise.
    """
    # Sort all points by distance
    sorted_points = sorted(points, key=lambda p: p[0]**2 + p[1]**2)
    k_closest = sorted_points[:k]
    
    # Check if all points in result are among the k closest
    result_distances = set(p[0]**2 + p[1]**2 for p in result)
    k_closest_distances = set(p[0]**2 + p[1]**2 for p in k_closest)
    
    # If there are ties at the k-th position, we need to make sure
    # the result includes the correct number of points
    if len(result) != k:
        return False
    
    # Verify that each point in the result is a valid k-closest point
    for point in result:
        distance = point[0]**2 + point[1]**2
        if distance > max(k_closest_distances):
            return False
    
    return True

def test_example1(solution_instance):
    """Input: points = [[1,3],[-2,2]], k = 1 -> Output: [[-2,2]]"""
    points = [[1, 3], [-2, 2]]
    k = 1
    result = solution_instance.kClosest(points, k)
    assert len(result) == k
    assert are_distances_valid(result, points, k)

def test_example2(solution_instance):
    """Input: points = [[3,3],[5,-1],[-2,4]], k = 2 -> Output: [[3,3],[-2,4]] or equivalent"""
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    result = solution_instance.kClosest(points, k)
    assert len(result) == k
    assert are_distances_valid(result, points, k)

def test_k_equals_length(solution_instance):
    """Test when k equals the length of points."""
    points = [[1, 1], [2, 2], [3, 3], [4, 4]]
    k = 4
    result = solution_instance.kClosest(points, k)
    assert len(result) == k
    assert sorted(result) == sorted(points)

def test_all_same_distance(solution_instance):
    """Test when all points have the same distance."""
    points = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    k = 2
    result = solution_instance.kClosest(points, k)
    assert len(result) == k
    assert all(calculate_distance(point) == 1 for point in result)

def test_k_equals_one(solution_instance):
    """Test when k = 1."""
    points = [[3, 4], [5, 12], [1, 2], [10, 10]]
    k = 1
    result = solution_instance.kClosest(points, k)
    assert len(result) == k
    assert result[0] == [1, 2]  # Closest point

def test_origin_in_points(solution_instance):
    """Test when one of the points is the origin."""
    points = [[3, 4], [0, 0], [5, 12], [10, 10]]
    k = 1
    result = solution_instance.kClosest(points, k)
    assert len(result) == k
    assert result[0] == [0, 0]  # Origin is closest

def test_negative_coordinates(solution_instance):
    """Test with negative coordinates."""
    points = [[-3, -4], [5, 12], [-1, -2], [10, 10]]
    k = 2
    result = solution_instance.kClosest(points, k)
    assert len(result) == k
    assert are_distances_valid(result, points, k)

def test_large_coordinates(solution_instance):
    """Test with large coordinate values."""
    points = [[10000, 10000], [-10000, -10000], [1, 1], [0, 0]]
    k = 2
    result = solution_instance.kClosest(points, k)
    assert len(result) == k
    assert sorted(result) == sorted([[1, 1], [0, 0]])

def test_large_number_of_points(solution_instance):
    """Test with a large number of points."""
    points = [[i, i] for i in range(1000)]
    k = 10
    result = solution_instance.kClosest(points, k)
    assert len(result) == k
    assert are_distances_valid(result, points, k)

def test_ties_at_kth_position(solution_instance):
    """Test when there are ties at the k-th position."""
    points = [[1, 0], [0, 1], [1, 0], [0, 1]]  # All points at distance 1
    k = 2
    result = solution_instance.kClosest(points, k)
    assert len(result) == k
    assert all(calculate_distance(point) == 1 for point in result)

# To run these tests:
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest
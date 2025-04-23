# https://leetcode.com/problems/merge-intervals/description/
import heapq
from typing import List


class SolutionHeap:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)
        result = []
        while intervals:
            x, y = heapq.heappop(intervals)
            if len(result) == 0:
                result.append([x, y])
            else:
                prev_x, prev_y = result[-1]
                # try to merge prev with result
                if prev_y < x:
                    # cannot merge
                    result.append([x, y])
                else:
                    # can merge
                    new_y = max(prev_y, y)
                    result[-1] = [prev_x, new_y]

        return result

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []
        for interval in sorted(intervals):
            # result[-1] gives us the last interval in the result array
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[Solution, SolutionHeap], 
               ids=["Sorting", "Heap"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    expected = [[1,6],[8,10],[15,18]]
    assert solution_instance.merge(intervals) == expected

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    intervals = [[1,4],[4,5]]
    expected = [[1,5]]
    assert solution_instance.merge(intervals) == expected

def test_empty_list(solution_instance):
    """Test with empty list."""
    intervals = []
    expected = []
    assert solution_instance.merge(intervals) == expected

def test_single_interval(solution_instance):
    """Test with a single interval."""
    intervals = [[1,3]]
    expected = [[1,3]]
    assert solution_instance.merge(intervals) == expected

def test_no_overlap(solution_instance):
    """Test intervals with no overlaps."""
    intervals = [[1,2],[4,5],[7,8]]
    expected = [[1,2],[4,5],[7,8]]
    assert solution_instance.merge(intervals) == expected

def test_complete_overlap(solution_instance):
    """Test intervals that completely overlap."""
    intervals = [[1,4],[2,3]]
    expected = [[1,4]]
    assert solution_instance.merge(intervals) == expected

def test_multiple_overlaps(solution_instance):
    """Test multiple overlapping intervals."""
    intervals = [[1,4],[4,5],[5,6],[6,7],[7,8]]
    expected = [[1,8]]
    assert solution_instance.merge(intervals) == expected

def test_unsorted_intervals(solution_instance):
    """Test with unsorted intervals."""
    intervals = [[4,5],[1,4],[8,10],[2,6]]
    expected = [[1,6],[8,10]]
    assert solution_instance.merge(intervals) == expected

def test_nested_intervals(solution_instance):
    """Test with nested intervals."""
    intervals = [[1,6],[2,5],[3,4]]
    expected = [[1,6]]
    assert solution_instance.merge(intervals) == expected

def test_adjacent_intervals(solution_instance):
    """Test with adjacent intervals."""
    intervals = [[1,2],[2,3],[3,4],[4,5]]
    expected = [[1,5]]
    assert solution_instance.merge(intervals) == expected

def test_large_numbers(solution_instance):
    """Test with large number intervals."""
    intervals = [[1,1000],[2,999],[2000,3000]]
    expected = [[1,1000],[2000,3000]]
    assert solution_instance.merge(intervals) == expected

def test_negative_numbers(solution_instance):
    """Test with negative number intervals."""
    intervals = [[-4,-1],[-3,-2],[0,2],[1,3]]
    expected = [[-4,-1],[0,3]]
    assert solution_instance.merge(intervals) == expected

def test_single_point_intervals(solution_instance):
    """Test intervals that are single points."""
    intervals = [[1,1],[2,2],[3,3]]
    expected = [[1,1],[2,2],[3,3]]
    assert solution_instance.merge(intervals) == expected

def test_mixed_intervals(solution_instance):
    """Test mix of overlapping and non-overlapping intervals."""
    intervals = [[1,5],[2,3],[4,6],[7,8],[8,9],[10,10]]
    expected = [[1,6],[7,9],[10,10]]
    assert solution_instance.merge(intervals) == expected

def test_duplicate_intervals(solution_instance):
    """Test with duplicate intervals."""
    intervals = [[1,4],[1,4],[1,4]]
    expected = [[1,4]]
    assert solution_instance.merge(intervals) == expected
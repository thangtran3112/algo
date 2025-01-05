import pytest
from merge_interval import Solution1

@pytest.fixture
def solution():
    return Solution1()

# Then modify each test function to use the fixture:
def test_example_1(solution):
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    expected = [[1,6],[8,10],[15,18]]
    assert solution.merge(intervals) == expected

def test_example_2(solution):
    intervals = [[1,4],[4,5]]
    expected = [[1,5]]
    assert solution.merge(intervals) == expected

def test_single_interval(solution):
    intervals = [[1,1]]
    expected = [[1,1]]
    assert solution.merge(intervals) == expected

def test_no_overlap(solution):
    intervals = [[1,2],[4,5],[7,8]]
    expected = [[1,2],[4,5],[7,8]]
    assert solution.merge(intervals) == expected

def test_complete_overlap(solution):
    intervals = [[1,4],[2,3]]
    expected = [[1,4]]
    assert solution.merge(intervals) == expected

def test_multiple_overlaps(solution):
    intervals = [[1,4],[2,3],[3,6],[5,7],[8,10],[9,11]]
    expected = [[1,7],[8,11]]
    assert solution.merge(intervals) == expected

def test_same_intervals(solution):
    intervals = [[1,1],[1,1]]
    expected = [[1,1]]
    assert solution.merge(intervals) == expected

def test_nested_intervals(solution):
    intervals = [[1,6],[2,4],[3,5]]
    expected = [[1,6]]
    assert solution.merge(intervals) == expected

def test_unsorted_intervals(solution):
    intervals = [[3,6],[1,3],[2,5]]
    expected = [[1,6]]
    assert solution.merge(intervals) == expected

def test_large_numbers(solution):
    intervals = [[1000,2000],[2000,3000]]
    expected = [[1000,3000]]
    assert solution.merge(intervals) == expected

def test_zero_included(solution):
    intervals = [[0,1],[1,2]]
    expected = [[0,2]]
    assert solution.merge(intervals) == expected

def test_multiple_same_start(solution):
    intervals = [[1,3],[1,4],[1,5]]
    expected = [[1,5]]
    assert solution.merge(intervals) == expected

def test_multiple_same_end(solution):
    intervals = [[1,5],[2,5],[3,5]]
    expected = [[1,5]]
    assert solution.merge(intervals) == expected

def test_chain_merge(solution):
    intervals = [[1,2],[2,3],[3,4],[4,5]]
    expected = [[1,5]]
    assert solution.merge(intervals) == expected

def test_no_merge_needed(solution):
    intervals = [[1,2],[3,4],[5,6],[7,8]]
    expected = [[1,2],[3,4],[5,6],[7,8]]
    assert solution.merge(intervals) == expected

def test_partial_overlap_chain(solution):
    intervals = [[1,3],[2,4],[3,5],[4,6]]
    expected = [[1,6]]
    assert solution.merge(intervals) == expected

def test_mixed_overlap_types(solution):
    intervals = [[1,5],[2,3],[4,7],[6,8],[9,10]]
    expected = [[1,8],[9,10]]
    assert solution.merge(intervals) == expected

def test_edge_case_max_values(solution):
    intervals = [[0,10000],[9999,10000]]
    expected = [[0,10000]]
    assert solution.merge(intervals) == expected

def test_alternating_overlap(solution):
    intervals = [[1,4],[2,3],[5,8],[6,7]]
    expected = [[1,4],[5,8]]
    assert solution.merge(intervals) == expected

def test_single_point_connections(solution):
    intervals = [[1,2],[2,3],[3,4],[4,5]]
    expected = [[1,5]]
    assert solution.merge(intervals) == expected 
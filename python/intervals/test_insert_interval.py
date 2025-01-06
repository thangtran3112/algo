import pytest
from insert_interval import Solution1, Solution2

@pytest.fixture
def solutions():
    return Solution1(), Solution2()

def test_example1(solutions):
    solution1, solution2 = solutions
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    expected = [[1,5],[6,9]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_example2(solutions):
    solution1, solution2 = solutions
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    expected = [[1,2],[3,10],[12,16]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_empty_intervals(solutions):
    solution1, solution2 = solutions
    intervals = []
    newInterval = [5,7]
    expected = [[5,7]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_insert_at_beginning(solutions):
    solution1, solution2 = solutions
    intervals = [[3,5],[6,9]]
    newInterval = [1,2]
    expected = [[1,2],[3,5],[6,9]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_insert_at_end(solutions):
    solution1, solution2 = solutions
    intervals = [[1,2],[3,5]]
    newInterval = [6,8]
    expected = [[1,2],[3,5],[6,8]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_merge_all_intervals(solutions):
    solution1, solution2 = solutions
    intervals = [[1,3],[4,6],[7,9]]
    newInterval = [2,8]
    expected = [[1,9]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_overlapping_multiple_intervals(solutions):
    solution1, solution2 = solutions
    intervals = [[1,3], [4,6], [8,10], [11,15]]
    newInterval = [2,12]
    expected = [[1,15]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_non_overlapping_insert_middle(solutions):
    solution1, solution2 = solutions
    intervals = [[1,2], [7,8]]
    newInterval = [4,5]
    expected = [[1,2], [4,5], [7,8]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_exact_overlap_start(solutions):
    solution1, solution2 = solutions
    intervals = [[1,5], [6,8]]
    newInterval = [1,3]
    expected = [[1,5], [6,8]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_exact_overlap_end(solutions):
    solution1, solution2 = solutions
    intervals = [[1,5], [6,8]]
    newInterval = [3,5]
    expected = [[1,5], [6,8]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_single_point_interval(solutions):
    solution1, solution2 = solutions
    intervals = [[1,5], [7,8]]
    newInterval = [6,6]
    expected = [[1,5], [6,6], [7,8]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_touching_intervals_start(solutions):
    solution1, solution2 = solutions
    intervals = [[3,5], [6,8]]
    newInterval = [1,3]
    expected = [[1,5], [6,8]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_touching_intervals_end(solutions):
    solution1, solution2 = solutions
    intervals = [[1,3], [6,8]]
    newInterval = [3,5]
    expected = [[1,5], [6,8]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_large_gap_between_intervals(solutions):
    solution1, solution2 = solutions
    intervals = [[1,2], [100,101]]
    newInterval = [50,51]
    expected = [[1,2], [50,51], [100,101]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_single_existing_interval(solutions):
    solution1, solution2 = solutions
    intervals = [[5,7]]
    newInterval = [2,3]
    expected = [[2,3], [5,7]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_completely_encompassing_interval(solutions):
    solution1, solution2 = solutions
    intervals = [[1,2], [3,4], [5,6]]
    newInterval = [0,7]
    expected = [[0,7]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_partial_overlap_multiple(solutions):
    solution1, solution2 = solutions
    intervals = [[1,4], [6,8], [10,12]]
    newInterval = [3,11]
    expected = [[1,12]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_adjacent_intervals(solutions):
    solution1, solution2 = solutions
    intervals = [[1,2], [2,3], [3,4]]
    newInterval = [2,3]
    expected = [[1,4]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_negative_numbers(solutions):
    solution1, solution2 = solutions
    intervals = [[-5,-3], [-2,-1], [0,2]]
    newInterval = [-4,0]
    expected = [[-5,2]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_same_start_different_end(solutions):
    solution1, solution2 = solutions
    intervals = [[1,4], [6,8]]
    newInterval = [1,7]
    expected = [[1,8]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected

def test_different_start_same_end(solutions):
    solution1, solution2 = solutions
    intervals = [[1,4], [6,8]]
    newInterval = [2,4]
    expected = [[1,4], [6,8]]
    
    assert solution1.insert(intervals.copy(), newInterval.copy()) == expected
    assert solution2.insert(intervals.copy(), newInterval.copy()) == expected
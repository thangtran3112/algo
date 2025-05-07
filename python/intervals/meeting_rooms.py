# https://leetcode.com/problems/meeting-rooms-ii/description/
# related: https://leetcode.com/problems/car-pooling/description/
"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""
import heapq
from typing import List
import pytest

class SolutionSortingTimestamp:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        timestamp = []
        for start, end in intervals:
            timestamp.append((start, 1))
            timestamp.append((end, -1))
        # sort by time, and sort key is cost (1, -1)
        # for each equal time in timestamp, prioritize release a room,
        # by putting negative sort key first. Eg priorize (2, -1) over (2, 1)
        timestamp.sort()
        capacity = 0
        used_capacity = 0
        for time, cost in timestamp:
            used_capacity += cost
            capacity = max(capacity, used_capacity)
        return capacity

class SolutionHeap:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        free_rooms = []

        intervals.sort(key=lambda x: x[0])

        # Add the end time of the first meeting
        heapq.heappush(free_rooms, intervals[0][1])

        for start, end in intervals[1:]:
            if free_rooms[0] <= start:
                # we only pop the heap, when the top-element can be free
                heapq.heappop(free_rooms)

            # add the end time of the new interval into the heap
            # keep the earliest end-time at top of the min-heap
            heapq.heappush(free_rooms, end)

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)
    
# === TEST CASES ===

@pytest.fixture(params=[SolutionHeap, SolutionSortingTimestamp],
               ids=["HeapSolution", "SortingTimestampSolution"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Input: intervals = [[0,30],[5,10],[15,20]] -> Output: 2"""
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert solution_instance.minMeetingRooms(intervals) == 2

def test_example2(solution_instance):
    """Input: intervals = [[7,10],[2,4]] -> Output: 1"""
    intervals = [[7, 10], [2, 4]]
    assert solution_instance.minMeetingRooms(intervals) == 1

def test_no_meetings(solution_instance):
    """Input: intervals = [] -> Output: 0"""
    intervals = []
    assert solution_instance.minMeetingRooms(intervals) == 0

def test_single_meeting(solution_instance):
    """Input: intervals = [[0,10]] -> Output: 1"""
    intervals = [[0, 10]]
    assert solution_instance.minMeetingRooms(intervals) == 1

def test_all_non_overlapping(solution_instance):
    """Input: intervals = [[0,5],[6,10],[11,15]] -> Output: 1"""
    intervals = [[0, 5], [6, 10], [11, 15]]
    assert solution_instance.minMeetingRooms(intervals) == 1

def test_all_overlapping_at_one_point(solution_instance):
    """Input: intervals = [[0,10],[0,10],[0,10]] -> Output: 3"""
    intervals = [[0, 10], [0, 10], [0, 10]]
    assert solution_instance.minMeetingRooms(intervals) == 3

def test_sequential_meetings_touching(solution_instance):
    """Input: intervals = [[0,5],[5,10],[10,15]] -> Output: 1"""
    # At time 5, room 1 becomes free and can be used by [5,10]
    # At time 10, room 1 becomes free and can be used by [10,15]
    intervals = [[0, 5], [5, 10], [10, 15]]
    assert solution_instance.minMeetingRooms(intervals) == 1

def test_complex_overlap1(solution_instance):
    """Input: intervals = [[1,4],[2,5],[6,8],[7,9]]"""
    # [1,4] -> Room1
    # [2,5] -> Room2 (Room1 busy until 4)
    # [6,8] -> Room1 (Room1 free at 4, Room2 free at 5)
    # [7,9] -> Room2 (Room1 busy until 8)
    # Max rooms = 2
    intervals = [[1, 4], [2, 5], [6, 8], [7, 9]]
    assert solution_instance.minMeetingRooms(intervals) == 2

def test_complex_overlap2(solution_instance):
    """Input: intervals = [[1,5],[2,6],[3,7],[4,8]]"""
    # [1,5] -> R1
    # [2,6] -> R2 (R1 busy)
    # [3,7] -> R3 (R1, R2 busy)
    # [4,8] -> R4 (R1, R2, R3 busy)
    # Max rooms = 4
    intervals = [[1, 5], [2, 6], [3, 7], [4, 8]]
    assert solution_instance.minMeetingRooms(intervals) == 4

def test_meetings_inside_other_meetings(solution_instance):
    """Input: intervals = [[0,10],[1,2],[3,4]]"""
    # [0,10] -> R1
    # [1,2]  -> R2 (R1 busy)
    # [3,4]  -> R3 (R1, R2 busy)
    # Max rooms = 2
    intervals = [[0, 10], [1, 2], [3, 4]]
    assert solution_instance.minMeetingRooms(intervals) == 2

def test_meetings_start_same_time(solution_instance):
    """Input: intervals = [[0,5],[0,10],[0,15]] -> Output: 3"""
    intervals = [[0, 5], [0, 10], [0, 15]]
    assert solution_instance.minMeetingRooms(intervals) == 3

def test_meetings_end_same_time(solution_instance):
    """Input: intervals = [[0,10],[2,10],[5,10]] -> Output: 3"""
    intervals = [[0, 10], [2, 10], [5, 10]]
    assert solution_instance.minMeetingRooms(intervals) == 3

def test_long_meeting_short_meetings_overlap(solution_instance):
    """Input: intervals = [[0,100],[10,20],[20,30],[30,40]]"""
    # [0,100] -> R1
    # [10,20] -> R2 (R1 busy)
    # [20,30] -> R2 (R1 busy, R2 becomes free at 20)
    # [30,40] -> R2 (R1 busy, R2 becomes free at 30)
    # Max rooms = 2
    intervals = [[0, 100], [10, 20], [20, 30], [30, 40]]
    assert solution_instance.minMeetingRooms(intervals) == 2

def test_from_leetcode_discussion1(solution_instance):
    intervals = [[13,15],[1,13]]
    assert solution_instance.minMeetingRooms(intervals) == 1

def test_from_leetcode_discussion2(solution_instance):
    intervals = [[2,15],[36,45],[9,29],[16,23],[4,9]]
    # Sorted by start:
    # [2,15] R1
    # [4,9]  R2
    # [9,29] R1 (R2 free at 9, R1 free at 15. R2 is used)
    # [16,23] R2 (R1 busy until 29)
    # [36,45] R1 (R1 free at 29, R2 free at 23)
    #
    # Heap solution trace:
    # Sort: [[2,15], [4,9], [9,29], [16,23], [36,45]]
    # 1. [2,15]: push(15). free_rooms = [15]
    # 2. [4,9]: 15 > 4. push(9). free_rooms = [9, 15] (size 2)
    # 3. [9,29]: 9 <= 9. pop(). push(29). free_rooms = [15, 29] (size 2)
    # 4. [16,23]: 15 <= 16. pop(). push(23). free_rooms = [23, 29] (size 2)
    # 5. [36,45]: 23 <= 36. pop(). push(45). free_rooms = [29, 45] (size 2)
    # Result: 2
    #
    # Timestamp solution trace:
    # (2,1), (4,1), (9,-1)*, (9,1)*, (15,-1), (16,1), (23,-1), (29,-1), (36,1), (45,-1)
    # *Sorted: (2,1), (4,1), (9,-1), (9,1), (15,-1), (16,1), (23,-1), (29,-1), (36,1), (45,-1)
    # Time | Event | Used | Max_Used
    # 2    | (2,1) | 1    | 1
    # 4    | (4,1) | 2    | 2
    # 9    | (9,-1)| 1    | 2
    # 9    | (9,1) | 2    | 2
    # 15   | (15,-1)| 1   | 2
    # 16   | (16,1)| 2    | 2
    # 23   | (23,-1)| 1   | 2
    # 29   | (29,-1)| 0   | 2
    # 36   | (36,1)| 1    | 2
    # 45   | (45,-1)| 0   | 2
    # Result: 2
    assert solution_instance.minMeetingRooms(intervals) == 2

def test_max_constraints_values(solution_instance):
    # This test is more about handling large values than large number of intervals
    intervals = [[0, 1000000], [1, 2], [1000000-1, 1000000]]
    # [0, 1M] -> R1
    # [1, 2] -> R2
    # [1M-1, 1M] -> R3 (R1 busy, R2 free)
    # Max rooms = 2
    assert solution_instance.minMeetingRooms(intervals) == 2

# To run these tests (if they were in a separate file like test_meeting_rooms.py):
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest
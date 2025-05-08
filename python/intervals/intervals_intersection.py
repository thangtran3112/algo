# https://leetcode.com/problems/interval-list-intersections/description/
"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

Example 1:


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
 

Constraints:

0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109 
endj < startj+1
"""
# Corner case: One interval intersectable with multiple intervals of the other list.
# Eg. firstList = [[3,5],[9,20]], secondList = [[4,5],[7,10],[11,12],[14,15],[16,20]]
# The interval of [9, 20] can be intersected with [7,10], [11,12], [14,15], [16,20]
# Final result: [[4,5],[9,10],[11,12],[14,15],[16,20]]
from typing import List, Tuple
import pytest

class Solution:
    # 2 intervals can only be merged if max(first_interval[0], second_interval[0])
    # is less than min(first_interval[1], second_interval[1])
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        first = second = 0
        while first < len(firstList) and second < len(secondList):
            first_interval = firstList[first]
            second_interval = secondList[second]
            # check if 2 intervals are intersected
            # low: the start point of the intersection
            # high: the end point of the intersection
            low = max(first_interval[0], second_interval[0])
            high = min(first_interval[1], second_interval[1])

            if low <= high:
                ans.append([low, high])
            # remove the interval with the smallest endpoint
            if first_interval[1] < second_interval[1]:
                first += 1
            else:
                second += 1
        return ans

class SolutionTwoPointer:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        def merge(first_interval: List[int], second_interval: Tuple[int]):
            a1, b1 = first_interval
            a2, b2 = second_interval
            # [0, 2] and [1, 5]. [0, 5] and [1, 3]
            if a1 <= a2 and a2 <= b1:
                return (a2, min(b1, b2))
            # [1, 4] and [0, 3]
            if a2 <= a1 and a1 <= b2:
                return (a1, min(b1, b2))
            # not possible to merge
            return None

        first = 0
        second = 0
        result = []
        seen = set()
        prev_first_interval = None
        prev_second_interval = None
        while first < len(firstList) and second < len(secondList):
            first_interval = firstList[first]
            second_interval = secondList[second]

            # special case check, for [1,5] and [5,10] -> [5, 5]
            if prev_first_interval:
                if prev_first_interval[1] == second_interval[0]:
                    temp = (second_interval[0], second_interval[0])
                    if temp not in seen:
                        result.append(temp)
                        seen.add((second_interval[0], second_interval[0]))
            elif prev_second_interval:
                # special case check for same reason above
                if prev_second_interval[1] == first_interval[0]:
                    temp = (first_interval[0], first_interval[0])
                    if temp not in seen:
                        result.append(temp)
                        seen.add((first_interval[0], first_interval[0]))

            merged_interval = merge(first_interval, second_interval)
            # cannot merge
            if not merged_interval:
                if first_interval[0] < second_interval[0]:
                    # first_interval is less than second_interval and they are disjoint
                    first += 1
                else:
                    # second_interval is less than first_interval and they are disjoint
                    second += 1
            if merged_interval:
                # can merge. The merged interval is within both first_interval and 2nd interval
                # so the merged_interval cannot have any overlap with next interval in both lists
                if merged_interval not in seen:
                    result.append(merged_interval)
                    seen.add(merged_interval)
                if first_interval[1] < second_interval[1]:
                    # first_interval is less than second_interval and they are disjoint
                    prev_first_interval = first_interval
                    first += 1
                else:
                    # second_interval is less than first_interval and they are disjoint
                    prev_second_interval = second_interval
                    second += 1


        # it is possible that there are leftover from firstList or secondList
        return result

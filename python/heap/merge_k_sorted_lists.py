# https://leetcode.com/problems/merge-k-sorted-lists
"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
from heapq import heappop, heappush
from typing import List, Optional
import pytest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time O(n*log(k)), where k is the number of linked list, n is the total nodes
# This solution redefine the __lt__ method of heap
class HeapNode:
    def __init__(self, node: Optional[ListNode]):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sentinel = ListNode(-1)
        prev = sentinel
        heap = []

        for list_start in lists:
            if list_start:
                heap_node = HeapNode(list_start)
                # put the current node of each list into the heap after conversion
                heappush(heap, heap_node)

        while heap:
            heap_node = heappop(heap)
            list_node = heap_node.node
            prev.next = list_node
            prev = prev.next
            # move the pointer of the just-processed list to next node
            if list_node.next:
                heappush(heap, HeapNode(list_node.next))

        return sentinel.next

# Time O(n*log(k)), where k is the number of linked list, n is the total nodes
class SolutionPureHeap:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # keep track of the start for each sub linked list
        starts = [None] * len(lists)
        for i, curr_list in enumerate(lists):
            starts[i] = curr_list

        # keep track of the number of linked-lists, which have successfully added to result
        finished = [False] * len(lists)
        # a set to keep track of current participant linked list
        in_processed = set()
        # create a sentinel node
        sen = ListNode(-1)
        prev = sen
        heap = []
        total_finished = 0
        while total_finished < len(lists):
            # populate heap with iteration
            for index, listNode in enumerate(lists):
                if finished[index]:
                    # this linked-list has already done processing
                    continue
                # the first element of this linked list is already in heap
                elif index in in_processed:
                    continue
                else:
                    curr_start_node = starts[index]
                    if not curr_start_node:
                        total_finished += 1
                        finished[index] = True
                        continue
                    heappush(heap, (curr_start_node.val, index))
                    in_processed.add(index)
                    # point to next node of this linked-list, waiting to be processed
                    starts[index] = curr_start_node.next
            # pop the smallest element from the heap
            if not heap:
                break
            smallestValue, listIndex = heappop(heap)
            prev.next = ListNode(smallestValue)
            prev = prev.next
            # we just processed linked list at listIndex, remove this list from in_processed
            in_processed.discard(listIndex)
        return sen.next

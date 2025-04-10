# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
"""
You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
 

Example 1:

Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output: [null, 4, 5, 5, 8, 8]

Explanation:

KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // return 4
kthLargest.add(5); // return 5
kthLargest.add(10); // return 5
kthLargest.add(9); // return 8
kthLargest.add(4); // return 8

Example 2:

Input:
["KthLargest", "add", "add", "add", "add"]
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

Output: [null, 7, 7, 7, 8]

Explanation:

KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // return 7
kthLargest.add(10); // return 7
kthLargest.add(9); // return 7
kthLargest.add(9); // return 8
 

Constraints:

0 <= nums.length <= 104
1 <= k <= nums.length + 1
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
"""
# Not as good as keeping a heap of k elements
from typing import List
from heapq import heapify, heappop, heappush

class KthLargestSortedArray:
    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.k = k
        self.arr.sort()

    def getIndex(self, val: int) -> int:
        left = 0
        right = len(self.arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] == val:
                return mid
            if self.arr[mid] < val:
                left = mid + 1
            else:
                right = mid - 1

        # at this point, either we get mid, or left, as right may be 1 point behind left
        return left


    def add(self, val: int) -> int:
        index = self.getIndex(val)
        self.arr.insert(index, val)
        return self.arr[-self.k]

"""
Maintains a min-heap of the top k largest elements.

The root (heap[0]) is always the k-th largest.

O(log k) time per add() call — very efficient.
"""
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = list(nums)
        self.k = k
        heapify(self.heap)
        # only maintain k elements in heap. the kth largest will be heap[0]
        # remove all smallest values until the heap only has k elements
        while len(self.heap) > k:
            heappop(self.heap)


    def add(self, val: int) -> int:
        heappush(self.heap, val)
        # remove all smallest values until the heap only has k elements
        while len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
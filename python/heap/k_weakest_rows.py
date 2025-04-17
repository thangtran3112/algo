# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/
"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].
Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
"""
import heapq
from typing import List


# Approach 2: Using maxHeap to keep track of k smallest elements
# Trick: multiply all elements with -1, to use negative minHeap as
# corresponding max heap. 
# https://leetcode.com/explore/learn/card/heap/645/applications-of-heap/4031/
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # optimized sum function, as all soldiers are in the left-side (TODO)

        # convert the original matrix into a dict of { index: totalSoldiers}
        solders_map = {i: sum(mat[i]) for i in range(len(mat))}

        # keep a heap of k minimum elements, by using max heap
        neg_arr = [(-1) * val for val in solders_map.values()]
        heap = []
        # keep a k-size heap, and replace element if needed
        for val in neg_arr:
            heapq.heappush(heap, val)
            # Notes: if top element is equal incoming val. Both of them will stay
            if len(heap) > k:
                heapq.heappop(heap)

        # do not forget to convert the negative value back to positive
        boundary = (-1) * heap[0]
        indexes = []
        for i in range(len(mat)):
            if len(indexes) == k:
                # result is sufficient
                break
            else:
                if solders_map[i] < boundary:
                    indexes.append(i)

        # if the indexes list is not filled with enough of k elements
        # it means, there are few more rows with value = boundary
        temp_set = set(indexes)  # for quick checking
        for i in range(len(mat)):
            if len(indexes) == k:
                # result is sufficient
                break
            if i not in temp_set and solders_map[i] == boundary:
                indexes.append(i)
        # sorting the indexes, by weakest row to strongest row 
        indexes.sort(key=lambda x: solders_map[x])
        return indexes



# Approach 1: Using minHeap to keep track of k smallest elements
# this is less efficient than using a maxHeap to do this calculation
# Using max heap with heapq, will need to multiply with negative -1
class Solution2:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # optimized sum function (TODO)

        # convert the original matrix into a dict of { index: totalSoldiers}
        solders_map = {i: sum(mat[i]) for i in range(len(mat))}

        # keep a heap of k minimum elements, by using min heap
        arr = list(solders_map.values())
        heapq.heapify(arr)

        min_arr = []
        # pick the k smallest elements from the min heap.
        # current complexity: k.log(n)
        # todo: use maxHeap to keep complexity to O(n.logk)
        while len(min_arr) < k:
            cur_min = heapq.heappop(arr)
            min_arr.append(cur_min)

        boundary = max(min_arr)
        indexes = []
        for i in range(len(mat)):
            if len(indexes) == k:
                # result is sufficient
                break
            else:
                if solders_map[i] < boundary:
                    indexes.append(i)

        # if the indexes list is not filled with enough of k elements
        # it means, there are few more rows with value = boundary
        temp_set = set(indexes)  # for quick checking
        for i in range(len(mat)):
            if len(indexes) == k:
                # result is sufficient
                break
            if i not in temp_set and solders_map[i] == boundary:
                indexes.append(i)
        # sorting the indexes, by weakest row to strongest row 
        indexes.sort(key=lambda x: solders_map[x])
        return indexes
    
import pytest  # noqa: E402

# Use parametrize to test both Solution and Solution2 classes
@pytest.mark.parametrize("SolutionClass", [Solution, Solution2])
def test_example_1(SolutionClass):
    """Test the first example from the problem description."""
    solution = SolutionClass()
    mat = [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ]
    k = 3
    expected = [2, 0, 3]
    assert solution.kWeakestRows(mat, k) == expected

@pytest.mark.parametrize("SolutionClass", [Solution, Solution2])
def test_example_2(SolutionClass):
    """Test the second example from the problem description."""
    solution = SolutionClass()
    mat = [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
    ]
    k = 2
    expected = [0, 2]
    assert solution.kWeakestRows(mat, k) == expected

@pytest.mark.parametrize("SolutionClass", [Solution, Solution2])
def test_k_equals_num_rows(SolutionClass):
    """Test when k is equal to the number of rows."""
    solution = SolutionClass()
    mat = [
        [1, 1, 0],
        [1, 0, 0],
        [1, 1, 1],
    ]
    k = 3
    # Expected order: [1 (1 soldier), 0 (2 soldiers), 2 (3 soldiers)]
    expected = [1, 0, 2]
    assert solution.kWeakestRows(mat, k) == expected

@pytest.mark.parametrize("SolutionClass", [Solution, Solution2])
def test_k_equals_1(SolutionClass):
    """Test when k is 1."""
    solution = SolutionClass()
    mat = [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0], # Weakest row
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ]
    k = 1
    expected = [2]
    assert solution.kWeakestRows(mat, k) == expected

@pytest.mark.parametrize("SolutionClass", [Solution, Solution2])
def test_all_zeros(SolutionClass):
    """Test with a matrix containing only zeros."""
    solution = SolutionClass()
    mat = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    k = 2
    # All rows have 0 soldiers, order by index
    expected = [0, 1]
    assert solution.kWeakestRows(mat, k) == expected

@pytest.mark.parametrize("SolutionClass", [Solution, Solution2])
def test_all_ones(SolutionClass):
    """Test with a matrix containing only ones."""
    solution = SolutionClass()
    mat = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    k = 2
    # All rows have 3 soldiers, order by index
    expected = [0, 1]
    assert solution.kWeakestRows(mat, k) == expected

@pytest.mark.parametrize("SolutionClass", [Solution, Solution2])
def test_tie_breaking(SolutionClass):
    """Test tie-breaking rule (same number of soldiers, lower index first)."""
    solution = SolutionClass()
    mat = [
        [1, 1, 0], # 2 soldiers, index 0
        [1, 0, 0], # 1 soldier, index 1
        [1, 1, 0], # 2 soldiers, index 2
        [1, 1, 1], # 3 soldiers, index 3
        [1, 0, 0], # 1 soldier, index 4
    ]
    k = 4
    # Order: [1 (1s), 4 (1s), 0 (2s), 2 (2s)]
    expected = [1, 4, 0, 2]
    assert solution.kWeakestRows(mat, k) == expected

@pytest.mark.parametrize("SolutionClass", [Solution, Solution2])
def test_single_row(SolutionClass):
    """Test with a matrix having only one row."""
    solution = SolutionClass()
    mat = [[1, 1, 0, 0]]
    k = 1
    expected = [0]
    assert solution.kWeakestRows(mat, k) == expected

@pytest.mark.parametrize("SolutionClass", [Solution, Solution2])
def test_single_column(SolutionClass):
    """Test with a matrix having only one column."""
    solution = SolutionClass()
    mat = [
        [1],
        [0],
        [1],
        [0],
    ]
    k = 3
    # Order: [1 (0s), 3 (0s), 0 (1s)]
    expected = [1, 3, 0]
    assert solution.kWeakestRows(mat, k) == expected
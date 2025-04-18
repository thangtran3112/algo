"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
"""
import heapq
from typing import List
import pytest

# let X=min(K,N); Time O(X+Klog(X)), Space: O(X)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)  # square matrix

        minHeap = []

        # since the matrix is sorted in both row and collum direction
        # we start from [0,0] the smallest element in the whole matrix
        # we consider min(n, k) rows only, because if there is
        # more than k rows, the result will only be in the first k rows.

        # Putting the first available element in each row into the heap
        # and move the pointer to the right (col + 1), when ever an
        # element is getting picked from the minHeap

        # initially, the minHeap will be all first value of each row
        for row in range(min(n, k)):
            elem = matrix[row][0]
            minHeap.append((elem, row, 0))  # add extra info on triplet (value,row,col)

        heapq.heapify(minHeap)

        while k:
            elem, row, col = heapq.heappop(minHeap)
            # not the last collumn in this square matrix, reheapify
            if col < n - 1:
                next_elem = matrix[row][col + 1]
                heapq.heappush(minHeap, (next_elem, row, col + 1))
            k -= 1
        return elem


# space complexity O(k)
class SolutionUnoptimized:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # keep a k-size heap for k-smallest element
        # for space-complexity less than O(n^2), we need to use max heap 
        # each max heap insertion/deletion is only log(k)
        # if we push all elements into a min-heap instead, each insert will be log(n^2)

        # to use max heap in python, we need to multiply elements with -1
        heap = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                elem = matrix[row][col]
                heapq.heappush(heap, elem * (-1))
                if len(heap) > k:
                    heapq.heappop(heap)

        # we inverted positive value to negative
        # top of the heap will be the most negative element (max value in positive)
        result = heap[0]
        return result * (-1)

# TEST CASES

@pytest.fixture(params=[Solution, SolutionUnoptimized], ids=["OptimizedHeap", "UnoptimizedHeap"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

# --- Individual Test Functions ---

def test_example1(solution_instance):
    """Test Example 1 from problem description."""
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    expected = 13
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_example2_single_negative(solution_instance):
    """Test Example 2: Single negative element."""
    matrix = [[-5]]
    k = 1
    expected = -5
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_k1_smallest_element(solution_instance):
    """Test k=1, should return the smallest element."""
    matrix = [[1, 2], [3, 4]]
    k = 1
    expected = 1
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_k_n_squared_largest_element(solution_instance):
    """Test k=n*n, should return the largest element."""
    matrix = [[1, 2], [3, 4]]
    k = 4
    expected = 4
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_duplicates_k3(solution_instance):
    """Test with duplicates, k=3."""
    matrix = [[1, 3, 5], [6, 7, 12], [11, 14, 14]]
    k = 3
    expected = 5
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_duplicates_k8_second_14(solution_instance):
    """Test with duplicates, k=8 (expecting the second 14)."""
    matrix = [[1, 3, 5], [6, 7, 12], [11, 14, 14]]
    k = 8
    expected = 14
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_negative_numbers_k1(solution_instance):
    """Test with negative numbers, k=1."""
    matrix = [[-10, -5, 0], [-2, -1, 1], [5, 10, 15]]
    k = 1
    expected = -10
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_negative_numbers_k5(solution_instance):
    """Test with negative numbers, k=5."""
    matrix = [[-10, -5, 0], [-2, -1, 1], [5, 10, 15]]
    k = 5
    expected = 0
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_negative_numbers_k9(solution_instance):
    """Test with negative numbers, k=9."""
    matrix = [[-10, -5, 0], [-2, -1, 1], [5, 10, 15]]
    k = 9
    expected = 15
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_larger_matrix_k5(solution_instance):
    """Test with a larger matrix, k=5."""
    matrix = [
        [1,  4,  7, 11, 15],
        [2,  5,  8, 12, 19],
        [3,  6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    k = 5
    expected = 5
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_larger_matrix_k13(solution_instance):
    """Test with a larger matrix, k=13."""
    matrix = [
        [1,  4,  7, 11, 15],
        [2,  5,  8, 12, 19],
        [3,  6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    k = 13
    expected = 13
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_larger_matrix_k25_largest(solution_instance):
    """Test with a larger matrix, k=25 (largest element)."""
    matrix = [
        [1,  4,  7, 11, 15],
        [2,  5,  8, 12, 19],
        [3,  6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    k = 25
    expected = 30
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_all_same_elements_k1(solution_instance):
    """Test with all same elements, k=1."""
    matrix = [[7, 7, 7], [7, 7, 7], [7, 7, 7]]
    k = 1
    expected = 7
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_all_same_elements_k5(solution_instance):
    """Test with all same elements, k=5."""
    matrix = [[7, 7, 7], [7, 7, 7], [7, 7, 7]]
    k = 5
    expected = 7
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_all_same_elements_k9(solution_instance):
    """Test with all same elements, k=9."""
    matrix = [[7, 7, 7], [7, 7, 7], [7, 7, 7]]
    k = 9
    expected = 7
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_boundary_values_k1(solution_instance):
    """Test with boundary values, k=1."""
    min_val = -10**9
    max_val = 10**9
    matrix = [[min_val, min_val + 1], [max_val - 1, max_val]]
    k = 1
    expected = min_val
    assert solution_instance.kthSmallest(matrix, k) == expected

def test_boundary_values_k4(solution_instance):
    """Test with boundary values, k=4."""
    min_val = -10**9
    max_val = 10**9
    matrix = [[min_val, min_val + 1], [max_val - 1, max_val]]
    k = 4
    expected = max_val
    assert solution_instance.kthSmallest(matrix, k) == expected
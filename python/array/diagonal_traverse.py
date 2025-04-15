# https://leetcode.com/problems/diagonal-traverse/description/
"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
"""
from typing import List


class Solution:
    """
        1  2  3  4  5 
        6  7  8  9  4
        4  3  3  2  3
        1  2  3  4  6
        2  6  4  8  9
    """
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        row_size, col_size = len(mat), len(mat[0])
        direction = 1 # 1 for up, -1 for down
        result = []

        DIAG_UP = (-1, 1)
        DIAG_DOWN = (1, -1)
        RIGHT = (0, 1)
        DOWN = (1, 0)

        move = None
        row, col = 0, 0
        for _ in range(row_size * col_size):
            result.append(mat[row][col])
            if direction == 1: # move up
                if col == col_size - 1:
                    # have to move down
                    direction = -1
                    move = DOWN
                elif row == 0:
                    # have to move right
                    direction = -1
                    move = RIGHT
                else:
                    # can still go diagonally up
                    move = DIAG_UP
            else: # move down
                if row == row_size - 1:
                    direction = 1
                    move = RIGHT
                elif col == 0:
                    direction = 1
                    move = DOWN
                else:
                    # can still go diagonally down
                    move = DIAG_DOWN
            row += move[0]
            col += move[1]
        
        return result


import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Fixture that provides the solution implementation."""
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [1, 2, 4, 7, 5, 3, 6, 8, 9]
    assert solution.findDiagonalOrder(mat) == expected

def test_example_2(solution):
    """Test the second example from the problem statement."""
    mat = [[1, 2], [3, 4]]
    expected = [1, 2, 3, 4]
    assert solution.findDiagonalOrder(mat) == expected

def test_empty_matrix(solution):
    """Test with an empty matrix."""
    mat = []
    assert solution.findDiagonalOrder(mat) == []
    
    mat = [[]]
    assert solution.findDiagonalOrder(mat) == []

def test_single_element(solution):
    """Test with a matrix containing a single element."""
    mat = [[5]]
    assert solution.findDiagonalOrder(mat) == [5]

def test_single_row(solution):
    """Test with a matrix having only one row."""
    mat = [[1, 2, 3, 4, 5]]
    assert solution.findDiagonalOrder(mat) == [1, 2, 3, 4, 5]

def test_single_column(solution):
    """Test with a matrix having only one column."""
    mat = [[1], [2], [3], [4], [5]]
    assert solution.findDiagonalOrder(mat) == [1, 2, 3, 4, 5]

def test_large_square_matrix(solution):
    """Test with a larger square matrix."""
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    expected = [1, 2, 5, 9, 6, 3, 4, 7, 10, 13, 14, 11, 8, 12, 15, 16]
    assert solution.findDiagonalOrder(mat) == expected

def test_wide_matrix(solution):
    """Test with a wide matrix (more columns than rows)."""
    mat = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ]
    expected = [1, 2, 6, 7, 3, 4, 8, 9, 5, 10]
    assert solution.findDiagonalOrder(mat) == expected

def test_tall_matrix(solution):
    """Test with a tall matrix (more rows than columns)."""
    mat = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10]
    ]
    expected = [1, 2, 3, 5, 4, 6, 7, 9, 8, 10]
    assert solution.findDiagonalOrder(mat) == expected

def test_negative_values(solution):
    """Test with negative values in the matrix."""
    mat = [
        [-1, -2, -3],
        [-4, -5, -6],
        [-7, -8, -9]
    ]
    expected = [-1, -2, -4, -7, -5, -3, -6, -8, -9]
    assert solution.findDiagonalOrder(mat) == expected

def test_mixed_values(solution):
    """Test with mixed positive and negative values."""
    mat = [
        [1, -2, 3],
        [-4, 5, -6],
        [7, -8, 9]
    ]
    expected = [1, -2, -4, 7, 5, 3, -6, -8, 9]
    assert solution.findDiagonalOrder(mat) == expected

def test_large_values(solution):
    """Test with values at the extremes of the constraints."""
    mat = [
        [10**5, -(10**5)],
        [-(10**5), 10**5]
    ]
    expected = [10**5, -(10**5), -(10**5), 10**5]
    assert solution.findDiagonalOrder(mat) == expected
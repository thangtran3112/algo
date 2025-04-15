# https://leetcode.com/problems/spiral-matrix/description/
"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
            1  2  3  4  5
            16 17 18 19 6
            15 24 25 20 7
            14 23 22 21 8
            13 12 11 10 9
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix

        col_size, row_size = len(matrix[0]), len(matrix)
        UP = (-1, 0)
        DOWN = (1, 0)
        RIGHT = (0, 1)
        LEFT = (0, -1)
        result = []

        move = RIGHT  # initial move
        row, col = 0, 0
        visited = set()
        for _ in range(row_size * col_size):
            result.append(matrix[row][col])
            visited.add((row, col))

            if move == RIGHT:
                # if next cell is the right-most, or already visited
                if col + 1 == col_size or (row, col + 1) in visited:
                    move = DOWN
                # can still move right, direction unchanged
            elif move == DOWN:
                # if next cell is the bottom-most, or already visited
                if row + 1 == row_size or (row + 1, col) in visited:
                    move = LEFT
                # can still move DOWN, direction unchanged
            elif move == LEFT:
                # if next cell is the left-most, or already visited
                if col - 1 == -1 or (row, col - 1) in visited:
                    move = UP
                # can still move LEFT, direction unchanged
            else:
                # current move = UP
                if (row - 1, col) in visited:
                    move = RIGHT
                # can still move UP, direction unchanged
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
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert solution.spiralOrder(matrix) == expected

def test_example_2(solution):
    """Test the second example from the problem statement."""
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert solution.spiralOrder(matrix) == expected

def test_empty_matrix(solution):
    """Test with an empty matrix."""
    matrix = []
    assert solution.spiralOrder(matrix) == []
    
    matrix = [[]]
    assert solution.spiralOrder(matrix) == [[]]

def test_single_element(solution):
    """Test with a matrix containing a single element."""
    matrix = [[5]]
    assert solution.spiralOrder(matrix) == [5]

def test_single_row(solution):
    """Test with a matrix having only one row."""
    matrix = [[1, 2, 3, 4, 5]]
    assert solution.spiralOrder(matrix) == [1, 2, 3, 4, 5]

def test_single_column(solution):
    """Test with a matrix having only one column."""
    matrix = [[1], [2], [3], [4], [5]]
    assert solution.spiralOrder(matrix) == [1, 2, 3, 4, 5]

def test_large_square_matrix(solution):
    """Test with a larger square matrix."""
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    assert solution.spiralOrder(matrix) == expected

def test_wide_matrix(solution):
    """Test with a wide matrix (more columns than rows)."""
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ]
    expected = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
    assert solution.spiralOrder(matrix) == expected

def test_tall_matrix(solution):
    """Test with a tall matrix (more rows than columns)."""
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10]
    ]
    expected = [1, 2, 4, 6, 8, 10, 9, 7, 5, 3]
    assert solution.spiralOrder(matrix) == expected

def test_negative_values(solution):
    """Test with negative values in the matrix."""
    matrix = [
        [-1, -2, -3],
        [-4, -5, -6],
        [-7, -8, -9]
    ]
    expected = [-1, -2, -3, -6, -9, -8, -7, -4, -5]
    assert solution.spiralOrder(matrix) == expected

def test_mixed_values(solution):
    """Test with mixed positive and negative values."""
    matrix = [
        [1, -2, 3],
        [-4, 5, -6],
        [7, -8, 9]
    ]
    expected = [1, -2, 3, -6, 9, -8, 7, -4, 5]
    assert solution.spiralOrder(matrix) == expected

def test_example_from_comments(solution):
    """Test the example matrix from the code comments."""
    matrix = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
    ]
    # Expected traversal in spiral order
    expected = list(range(1, 26))
    assert solution.spiralOrder(matrix) == expected

def test_maximum_size(solution):
    """Test a matrix at the maximum size constraint."""
    # Create a 10x10 matrix (maximum size per constraints)
    matrix = [[i*10 + j + 1 for j in range(10)] for i in range(10)]
    
    # Compute expected spiral order manually
    expected = []
    top, bottom = 0, 9
    left, right = 0, 9
    
    while top <= bottom and left <= right:
        # Traverse right
        for j in range(left, right + 1):
            expected.append(matrix[top][j])
        top += 1
        
        # Traverse down
        for i in range(top, bottom + 1):
            expected.append(matrix[i][right])
        right -= 1
        
        # Traverse left (if there are rows left)
        if top <= bottom:
            for j in range(right, left - 1, -1):
                expected.append(matrix[bottom][j])
            bottom -= 1
        
        # Traverse up (if there are columns left)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                expected.append(matrix[i][left])
            left += 1
    
    assert solution.spiralOrder(matrix) == expected

def test_irregular_shape(solution):
    """Test with a matrix of irregular shape."""
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [17, 18, 19, 20]
    ]
    expected = [1, 2, 3, 4, 8, 12, 16, 20, 19, 18, 17, 13, 9, 5, 6, 7, 11, 15, 14, 10]
    assert solution.spiralOrder(matrix) == expected
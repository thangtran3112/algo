# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
"""
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

 

Example 1:


Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-104 <= matrix[i][j] <= 104
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.
"""
from typing import List
import pytest

class NumMatrix:
    # avoid out of range for indexes
    def getVal(self, row, col):
        if 0 <= row < self.row_size and 0 <= col < self.col_size:
            return self.dp[row][col]
        else:
            return 0

    def __init__(self, matrix: List[List[int]]):
        self.row_size = len(matrix)
        self.col_size = len(matrix[0])

        # add a 1 buffer row and col to relax edge cases
        self.dp = [[0] * (self.col_size + 1) for _ in range(self.row_size + 1)]

        for row in range(self.row_size):
            for col in range(self.col_size):
                if row == 0 and col == 0:
                    # base case
                    self.dp[0][0] = matrix[0][0]
                else:
                    self.dp[row][col] = matrix[row][col] + self.getVal(row - 1, col) + self.getVal(row, col - 1) - self.getVal(row - 1, col - 1)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.getVal(row2, col2) - self.getVal(row1 - 1, col2) - self.getVal(row2, col1 - 1) + self.getVal(row1 - 1, col1 - 1)
    
# === TEST CASES ===

# Assuming the standard prefix sum implementation for NumMatrix
# If the user's implementation differs slightly, expected values might need adjustment
# Standard implementation:
class NumMatrixStandard:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.dp = [[0]] # Handle empty case
            return

        rows, cols = len(matrix), len(matrix[0])
        # dp table is (rows+1) x (cols+1)
        self.dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                # dp[r+1][c+1] stores sum of rectangle from (0,0) to (r,c)
                self.dp[r + 1][c + 1] = matrix[r][c] + self.dp[r][c + 1] + self.dp[r + 1][c] - self.dp[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.dp or not self.dp[0] or len(self.dp)==1 and len(self.dp[0])==1: return 0

        # Adjust to dp indices (which are 1-based relative to original matrix)
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        # Sum(ABCD) = Sum(OD) - Sum(OB) - Sum(OC) + Sum(OA)
        return self.dp[r2][c2] - self.dp[r1 - 1][c2] - self.dp[r2][c1 - 1] + self.dp[r1 - 1][c1 - 1]


# --- Test Fixtures ---
@pytest.fixture
def matrix1():
    return [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]

@pytest.fixture
def num_matrix1(matrix1):
    """Provides a NumMatrix instance initialized with matrix1."""
    # Use the standard implementation for testing, replace if needed
    return NumMatrixStandard(matrix1) 
    # return NumMatrix(matrix1) # Use this if testing the user's exact code

@pytest.fixture
def matrix2():
    return [
        [-1, -2, -3],
        [-4, -5, -6]
    ]

@pytest.fixture
def num_matrix2(matrix2):
    """Provides a NumMatrix instance initialized with matrix2."""
    return NumMatrixStandard(matrix2)
    # return NumMatrix(matrix2)

@pytest.fixture
def matrix3():
    return [[10]]

@pytest.fixture
def num_matrix3(matrix3):
    """Provides a NumMatrix instance initialized with matrix3."""
    return NumMatrixStandard(matrix3)
    # return NumMatrix(matrix3)

# --- Test Cases ---

def test_example1_queries(num_matrix1):
    """Test the specific queries from Example 1."""
    assert num_matrix1.sumRegion(2, 1, 4, 3) == 8
    assert num_matrix1.sumRegion(1, 1, 2, 2) == 11
    assert num_matrix1.sumRegion(1, 2, 2, 4) == 12

def test_single_cell(num_matrix1):
    """Test summing a region of a single cell."""
    assert num_matrix1.sumRegion(0, 0, 0, 0) == 3
    assert num_matrix1.sumRegion(2, 2, 2, 2) == 0
    assert num_matrix1.sumRegion(4, 4, 4, 4) == 5

def test_single_row(num_matrix1):
    """Test summing a region within a single row."""
    assert num_matrix1.sumRegion(0, 1, 0, 3) == 0 + 1 + 4 # 5
    assert num_matrix1.sumRegion(2, 0, 2, 4) == 1 + 2 + 0 + 1 + 5 # 9

def test_single_column(num_matrix1):
    """Test summing a region within a single column."""
    assert num_matrix1.sumRegion(1, 0, 3, 0) == 5 + 1 + 4 # 10
    assert num_matrix1.sumRegion(0, 4, 4, 4) == 2 + 1 + 5 + 7 + 5 # 20

def test_top_left_corner(num_matrix1):
    """Test summing a region starting from (0, 0)."""
    assert num_matrix1.sumRegion(0, 0, 1, 1) == 3 + 0 + 5 + 6 # 14
    assert num_matrix1.sumRegion(0, 0, 0, 4) == 3 + 0 + 1 + 4 + 2 # 10
    assert num_matrix1.sumRegion(0, 0, 4, 0) == 3 + 5 + 1 + 4 + 1 # 14

def test_full_matrix(num_matrix1, matrix1):
    """Test summing the entire matrix."""
    total_sum = sum(sum(row) for row in matrix1)
    rows, cols = len(matrix1), len(matrix1[0])
    assert num_matrix1.sumRegion(0, 0, rows - 1, cols - 1) == total_sum

def test_negative_values(num_matrix2):
    """Test with a matrix containing negative values."""
    assert num_matrix2.sumRegion(0, 0, 0, 0) == -1
    assert num_matrix2.sumRegion(1, 1, 1, 2) == -5 + -6 # -11
    assert num_matrix2.sumRegion(0, 1, 1, 1) == -2 + -5 # -7
    assert num_matrix2.sumRegion(0, 0, 1, 2) == -1 + -2 + -3 + -4 + -5 + -6 # -21

def test_1x1_matrix(num_matrix3):
    """Test with a 1x1 matrix."""
    assert num_matrix3.sumRegion(0, 0, 0, 0) == 10

def test_zeros_matrix():
    """Test with a matrix containing only zeros."""
    matrix = [[0, 0], [0, 0]]
    num_matrix = NumMatrixStandard(matrix)
    # num_matrix = NumMatrix(matrix)
    assert num_matrix.sumRegion(0, 0, 0, 0) == 0
    assert num_matrix.sumRegion(0, 0, 1, 1) == 0
    assert num_matrix.sumRegion(0, 1, 1, 1) == 0
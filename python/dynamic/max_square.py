from functools import lru_cache
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        # No need for +1 padding since we're iterating in reverse
        dp = [[0] * cols for _ in range(rows)]
        max_side = 0

        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                if matrix[i][j] == '1':
                    if i == rows - 1 or j == cols - 1:
                        # Edge cells can only form 1x1 square if '1'
                        dp[i][j] = 1
                    else:
                        # If we're not on the last row or col, consider neighbors
                        dp[i][j] = min(
                            dp[i][j + 1],      # right
                            dp[i + 1][j],      # down
                            dp[i + 1][j + 1]   # diagonal (down-right)
                        ) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side

class SolutionTopDown:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0

        # for convenience, we add an extra all zero column and row
        # outside of the actual dp table, to simpify the transition
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == '1':
                    top = dp[i][j - 1]
                    left = dp[i - 1][j]
                    diag = dp[i - 1][j - 1]
                    dp[i][j] = min(top, left, diag) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side


class SolutionRecursive:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
                0  1  2  3  4  5
            0
            1      2  2
            2      1  1
            3
            * start from the top-left 0 -> n , 0 -> m.
            * if meeting 0, dp[i][j] = 0
            * if meeting 1, we have dp[i][j] = min(top, left, top-left) + 1
            * Idea: Check for the min coverage square can be covered by all 3 neighbors

        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i >= m or j >= n:
                return 0
            if matrix[i][j] == "1":
                down = dp(i + 1, j)
                right = dp(i, j + 1)
                diag = dp(i + 1, j + 1)
                return min(down, right, diag) + 1
            else:
                return 0

        max_side = 0
        for i in range(m):
            for j in range(n):
                max_side = max(max_side, dp(i, j))

        return max_side * max_side


# TEST CASES
import pytest  # noqa: E402

@pytest.fixture(params=[Solution, SolutionTopDown, SolutionRecursive])
def solution(request):
    """Fixture that provides all solution implementations."""
    return request.param()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    assert solution.maximalSquare(matrix) == 4

def test_example_2(solution):
    """Test the second example from the problem statement."""
    matrix = [
        ["0", "1"],
        ["1", "0"]
    ]
    assert solution.maximalSquare(matrix) == 1

def test_example_3(solution):
    """Test the third example from the problem statement."""
    matrix = [["0"]]
    assert solution.maximalSquare(matrix) == 0

def test_empty_matrix(solution):
    """Test with an empty matrix."""
    matrix = []
    assert solution.maximalSquare(matrix) == 0

def test_empty_rows(solution):
    """Test with a matrix that has empty rows."""
    matrix = [[], []]
    assert solution.maximalSquare(matrix) == 0

def test_all_ones(solution):
    """Test with a matrix filled with all ones."""
    matrix = [
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"]
    ]
    assert solution.maximalSquare(matrix) == 9

def test_all_zeros(solution):
    """Test with a matrix filled with all zeros."""
    matrix = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]
    assert solution.maximalSquare(matrix) == 0

def test_single_one(solution):
    """Test with a matrix containing a single '1'."""
    matrix = [
        ["0", "0", "0"],
        ["0", "1", "0"],
        ["0", "0", "0"]
    ]
    assert solution.maximalSquare(matrix) == 1

def test_large_square(solution):
    """Test with a matrix containing a large square."""
    # Create a 5x5 matrix of ones
    matrix = [["1" for _ in range(5)] for _ in range(5)]
    assert solution.maximalSquare(matrix) == 25

def test_irregular_shape(solution):
    """Test with an irregular-shaped matrix."""
    matrix = [
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"]
    ]
    assert solution.maximalSquare(matrix) == 9  # 3x3 is the largest square

def test_multiple_squares(solution):
    """Test with a matrix containing multiple squares."""
    matrix = [
        ["1", "1", "0", "1", "1"],
        ["1", "1", "0", "1", "1"],
        ["0", "0", "0", "0", "0"],
        ["1", "1", "0", "1", "1"],
        ["1", "1", "0", "1", "1"]
    ]
    assert solution.maximalSquare(matrix) == 4  # Four 2x2 squares

def test_single_row(solution):
    """Test with a single row matrix."""
    matrix = [["1", "1", "1", "0", "1"]]
    assert solution.maximalSquare(matrix) == 1

def test_single_column(solution):
    """Test with a single column matrix."""
    matrix = [["1"], ["1"], ["1"], ["0"], ["1"]]
    assert solution.maximalSquare(matrix) == 1

def test_corner_square(solution):
    """Test with a square in the corner."""
    matrix = [
        ["1", "1", "0"],
        ["1", "1", "0"],
        ["0", "0", "0"]
    ]
    assert solution.maximalSquare(matrix) == 4

def test_center_square(solution):
    """Test with a square in the center."""
    matrix = [
        ["0", "0", "0", "0", "0"],
        ["0", "1", "1", "1", "0"],
        ["0", "1", "1", "1", "0"],
        ["0", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert solution.maximalSquare(matrix) == 9

def test_alternating_pattern(solution):
    """Test with an alternating pattern of 1s and 0s."""
    matrix = [
        ["1", "0", "1", "0"],
        ["0", "1", "0", "1"],
        ["1", "0", "1", "0"],
        ["0", "1", "0", "1"]
    ]
    assert solution.maximalSquare(matrix) == 1

def test_large_matrix(solution):
    """Test with a larger matrix."""
    # 10x10 matrix with a 7x7 square of ones in the middle
    matrix = [["0" for _ in range(10)] for _ in range(10)]
    for i in range(2, 9):
        for j in range(2, 9):
            matrix[i][j] = "1"
    
    assert solution.maximalSquare(matrix) == 49  # 7x7 square

def test_border_matrix(solution):
    """Test with ones only on the border."""
    # Create a matrix with ones only on the border
    n = 5
    matrix = [["0" for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[0][i] = "1"  # Top row
        matrix[n-1][i] = "1"  # Bottom row
        matrix[i][0] = "1"  # Left column
        matrix[i][n-1] = "1"  # Right column
    
    assert solution.maximalSquare(matrix) == 1  # Can only form 1x1 squares
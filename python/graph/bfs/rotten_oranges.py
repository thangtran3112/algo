# https://leetcode.com/problems/rotting-oranges/description/
"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_size = len(grid)
        col_size = len(grid[0])
        # Layer traversing with BFS
        rotten = deque()
        total_oranges = 0
        FRESH, ROTTEN = 1, 2
        for row in range(row_size):
            for col in range(col_size):
                val = grid[row][col]
                if val == ROTTEN:
                    rotten.append((row, col))
                    total_oranges += 1
                elif val == FRESH:
                    total_oranges += 1

        if total_oranges == len(rotten):
            # all oranages are rotten from the beginning
            return 0
        elif len(rotten) == 0:
            # there is no rotten orange
            return -1

        # get fresh orange neighbors
        def getNeighborOrange(row, col):
            initials = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            result = []
            for row, col in initials:
                if 0 <= row <= row_size - 1 and 0 <= col <= col_size - 1:
                    if grid[row][col] == FRESH:
                        result.append((row, col))
            return result

        minute = 0
        visited = set()
        # 2D BFS parallel traversal
        while rotten:
            # layer traversal
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                visited.add((row, col))
                for nei_row, nei_col in getNeighborOrange(row, col):
                    if (nei_row, nei_col) not in visited:
                        rotten.append((nei_row, nei_col))

            if len(visited) == total_oranges:
                return minute
            else:
                minute += 1

        return -1

# === TEST CASES ===

import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Fixture to provide a Solution instance."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    expected = 4
    assert solution.orangesRotting(grid) == expected

def test_example2_impossible(solution):
    """Test Example 2 from the problem description - impossible to rot all oranges."""
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    expected = -1
    assert solution.orangesRotting(grid) == expected

def test_example3_no_fresh_oranges(solution):
    """Test Example 3 from the problem description - no fresh oranges at start."""
    grid = [[0, 2]]
    expected = 0
    assert solution.orangesRotting(grid) == expected

def test_no_oranges(solution):
    """Test case with no oranges at all (all empty cells)."""
    grid = [[0, 0], [0, 0]]
    expected = 0
    assert solution.orangesRotting(grid) == expected

def test_all_fresh_oranges(solution):
    """Test case with all fresh oranges and no rotten ones."""
    grid = [[1, 1], [1, 1]]
    expected = -1
    assert solution.orangesRotting(grid) == expected

def test_all_rotten_oranges(solution):
    """Test case with all rotten oranges and no fresh ones."""
    grid = [[2, 2], [2, 2]]
    expected = 0
    assert solution.orangesRotting(grid) == expected

def test_single_orange(solution):
    """Test case with a single fresh orange."""
    grid = [[1]]
    expected = -1
    assert solution.orangesRotting(grid) == expected

def test_single_rotten_orange(solution):
    """Test case with a single rotten orange."""
    grid = [[2]]
    expected = 0
    assert solution.orangesRotting(grid) == expected

def test_complex_grid(solution):
    """Test case with a more complex grid layout."""
    grid = [
        [2, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 2, 1],
        [1, 1, 1, 0, 1]
    ]
    expected = 4  # Takes 4 minutes for all fresh oranges to rot
    assert solution.orangesRotting(grid) == expected

def test_multiple_rotten_sources(solution):
    """Test case with multiple rotten oranges as starting points."""
    grid = [
        [2, 1, 1, 1, 2],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    expected = 4  # Takes 4 minutes for all oranges to rot
    assert solution.orangesRotting(grid) == expected

def test_isolated_oranges(solution):
    """Test case with fresh oranges isolated by empty cells."""
    grid = [
        [2, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]
    expected = -1  # Bottom right and top right oranges are isolated
    assert solution.orangesRotting(grid) == expected

def test_spiral_pattern(solution):
    """Test case with a spiral pattern of oranges."""
    grid = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [2, 1, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    expected = 14  # Takes 14 minutes to rot the farthest corner
    assert solution.orangesRotting(grid) == expected

def test_grid_boundary(solution):
    """Test case with oranges on the grid boundaries."""
    grid = [
        [1, 1, 1],
        [1, 2, 1],
        [1, 1, 1]
    ]
    expected = 2  # Takes 2 minutes to reach corners
    assert solution.orangesRotting(grid) == expected

def test_large_grid(solution):
    """Test case with a large grid (10x10)."""
    # Create a 10x10 grid with a single rotten orange in the center
    # and fresh oranges everywhere else
    grid = [[1 for _ in range(10)] for _ in range(10)]
    grid[5][5] = 2  # Center rotten orange
    
    expected = 10  # Takes 10 minutes to reach the farthest corners
    assert solution.orangesRotting(grid) == expected
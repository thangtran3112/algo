# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""

# BFS and with some greedier picking of neighbor
from collections import deque
from heapq import heappop, heappush
from typing import List, Tuple
import pytest

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        queue = deque()
        queue.append((0, 0))

        def possible_neighbor(row, col) -> List[Tuple[int, int]]:
            my_set = set()
            # update() takes an array of elements, while add() only take 1 element
            # be greedy by adding positve directions first
            my_set.update([
                (row + 1, col + 1),  # prefered route
                (row + 1, col),  # prefered route
                (row, col + 1),  # prefered route
                (row + 1, col - 1),
                (row - 1, col + 1),
                (row, col - 1),
                (row - 1, col),
                (row - 1, col - 1)
            ])
            result = []
            for new_row, new_col in my_set:
                if 0 <= new_row <= n - 1 and 0 <= new_col <= n - 1:
                    if grid[new_row][new_col] == 0:
                        result.append((new_row, new_col))
            return result

        # 0  0  0
        # 1  0  0
        # 1  1  0
        visited = set()
        iteration = 0

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == n - 1 and col == n - 1:
                    return iteration + 1
                else:
                    zero_neighbors = possible_neighbor(row, col)
                    for nei_row, nei_col in zero_neighbors:
                        if (nei_row, nei_col) not in visited:
                            visited.add((nei_row, nei_col))
                            queue.append((nei_row, nei_col))
            iteration += 1

        return -1

# this does not improve the Time Complexity
class SolutionHeapBFS:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        queue = []
        heappush(queue, (1, 0, 0))  # (path_length, row, col)

        def possible_neighbor(row, col) -> List[Tuple[int, int]]:
            my_set = set()
            my_set.update([
                (row + 1, col + 1),
                (row + 1, col - 1),
                (row - 1, col - 1),
                (row - 1, col + 1),
                (row + 1, col),
                (row, col + 1),
                (row, col - 1),
                (row - 1, col)
            ])
            result = []
            for new_row, new_col in my_set:
                if 0 <= new_row <= n - 1 and 0 <= new_col <= n - 1:
                    if grid[new_row][new_col] == 0:
                        result.append((new_row, new_col))
            return result

        visited = set()
        visited.add((0, 0))

        while queue:
            path_len, row, col = heappop(queue)
            if row == n - 1 and col == n - 1:
                return path_len
            for nei_row, nei_col in possible_neighbor(row, col):
                if (nei_row, nei_col) not in visited:
                    visited.add((nei_row, nei_col))
                    heappush(queue, (path_len + 1, nei_row, nei_col))

        return -1
    
# --- TEST CASES ---

@pytest.fixture(params=[Solution, SolutionHeapBFS], ids=["StandardBFS", "HeapBFS"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

# --- Individual Test Functions ---

def test_example1(solution_instance):
    """Test Example 1 from LeetCode."""
    grid = [[0, 1], [1, 0]]
    expected = 2
    assert solution_instance.shortestPathBinaryMatrix(grid) == expected

def test_example2(solution_instance):
    """Test Example 2 from LeetCode."""
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    expected = 4
    assert solution_instance.shortestPathBinaryMatrix(grid) == expected

def test_example3_start_blocked(solution_instance):
    """Test Example 3 from LeetCode (start blocked)."""
    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    expected = -1
    assert solution_instance.shortestPathBinaryMatrix(grid) == expected

def test_end_blocked(solution_instance):
    """Test case where the end cell is blocked."""
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 1]]
    expected = -1
    assert solution_instance.shortestPathBinaryMatrix(grid) == expected

def test_no_path_exists(solution_instance):
    """Test case where no clear path exists between start and end."""
    grid = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    expected = -1
    assert solution_instance.shortestPathBinaryMatrix(grid) == expected

def test_1x1_grid_clear(solution_instance):
    """Test a 1x1 grid with a clear path."""
    grid = [[0]]
    expected = 1
    assert solution_instance.shortestPathBinaryMatrix(grid) == expected

def test_1x1_grid_blocked(solution_instance):
    """Test a 1x1 grid that is blocked."""
    grid = [[1]]
    expected = -1
    assert solution_instance.shortestPathBinaryMatrix(grid) == expected

def test_straight_path(solution_instance):
    """Test a grid where the shortest path is straight down."""
    grid = [[0, 1, 1], [0, 1, 1], [0, 0, 0]]
    expected = 4
    assert solution_instance.shortestPathBinaryMatrix(grid) == expected

def test_diagonal_path(solution_instance):
    """Test a grid where the shortest path is purely diagonal."""
    grid = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    expected = 3
    assert solution_instance.shortestPathBinaryMatrix(grid) == expected

def test_complex_path_with_detour(solution_instance):
    """Test a grid requiring navigation around obstacles."""
    grid = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0]
    ]
    expected = 5
    assert solution_instance.shortestPathBinaryMatrix(grid) == expected

def test_larger_grid_open(solution_instance):
    """Test a larger grid that is completely open."""
    n = 5
    grid = [[0] * n for _ in range(n)]
    expected = n # Diagonal path is shortest
    assert solution_instance.shortestPathBinaryMatrix(grid) == expected

def test_larger_grid_blocked_center(solution_instance):
    """Test a larger grid with a block in the center."""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    expected = 6
    assert solution_instance.shortestPathBinaryMatrix(grid) == expected

def test_grid_forcing_non_diagonal(solution_instance):
    """Test a grid where the diagonal is blocked, forcing a longer path."""
    grid = [
        [0, 1, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    expected = -1 # No path possible
    assert solution_instance.shortestPathBinaryMatrix(grid) == expected

    grid2 = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]
    expected = 4
    assert solution_instance.shortestPathBinaryMatrix(grid2) == expected
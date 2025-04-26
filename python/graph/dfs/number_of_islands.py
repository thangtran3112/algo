# https://leetcode.com/problems/number-of-islands/description/
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from collections import deque
from typing import List


class SolutionDFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        # find all locations of 1
        LAND = "1"
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        m = len(grid)
        n = len(grid[0])

        unvisited = set()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == LAND:
                    unvisited.add((row, col))

        def dfs(row, col):
            # has visited
            if (row, col) not in unvisited:
                return
            unvisited.discard((row, col))
            for dr, dc in DIRECTIONS:
                next_row = row + dr
                next_col = col + dc
                if next_row < m and next_row >= 0 and next_col >= 0 and next_col < n:
                    if grid[next_row][next_col] == LAND:
                        dfs(next_row, next_col)

        islands = 0
        # unvisited set will be modified during operation, we must traverse on immutable list
        for row, col in list(unvisited):
            if (row, col) in unvisited:
                dfs(row, col)
                islands += 1

        return islands
    
class SolutionBFS:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row_size = len(grid)
        col_size = len(grid[0])

        ISLAND = "1"
        WATER = "0"

        def getNeighbors(row, col):
            possible_neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col -1)]
            neighbors = []
            for r, c in possible_neighbors:
                if 0 <= r < row_size and 0 <= c < col_size:
                    neighbors.append((r, c))
            return neighbors

        def bfs(row, col):
            # find all neighbors, and start expanding, until we cannot find 1
            queue = deque()
            queue.append((row, col))
            while queue:
                row, col = queue.popleft()
                neighbors = getNeighbors(row, col)
                for nei_row, nei_col in neighbors:
                    if grid[nei_row][nei_col] == ISLAND:
                        grid[nei_row][nei_col] = WATER
                        queue.append((nei_row, nei_col))

        nums_islands = 0
        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == ISLAND:
                    nums_islands += 1
                    grid[row][col] = WATER  # marked as visited
                    bfs(row, col)

        return nums_islands
    
# === TEST CASES ===
import pytest
import copy

@pytest.fixture(params=[SolutionDFS, SolutionBFS],
               ids=["DFS", "BFS"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    # Create a deep copy since the solution modifies the grid
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 1

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 3

def test_single_island(solution_instance):
    """Test with a single island covering the entire grid."""
    grid = [
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"]
    ]
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 1

def test_no_islands(solution_instance):
    """Test with no islands (all water)."""
    grid = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 0

def test_all_separate_islands(solution_instance):
    """Test with all separate islands (no adjacent land)."""
    grid = [
        ["1", "0", "1"],
        ["0", "1", "0"],
        ["1", "0", "1"]
    ]
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 5

def test_single_row(solution_instance):
    """Test with a single row grid."""
    grid = [["1", "0", "1", "0", "1"]]
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 3

def test_single_column(solution_instance):
    """Test with a single column grid."""
    grid = [
        ["1"],
        ["0"],
        ["1"],
        ["0"],
        ["1"]
    ]
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 3

def test_minimum_grid(solution_instance):
    """Test with minimum grid size (1x1)."""
    grid = [["1"]]
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 1
    
    grid = [["0"]]
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 0

def test_complex_shapes(solution_instance):
    """Test with islands of complex shapes."""
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "0", "0", "0", "1"],
        ["0", "0", "1", "1", "1"],
        ["0", "1", "1", "0", "1"]
    ]
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 2

def test_diagonal_not_connected(solution_instance):
    """Test that diagonal cells are not considered connected."""
    grid = [
        ["1", "0", "1"],
        ["0", "0", "0"],
        ["1", "0", "1"]
    ]
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 4

def test_large_grid(solution_instance):
    """Test with a larger grid (close to constraint limit)."""
    # Create a 100x100 grid with alternating rows of 1s and 0s
    grid = []
    for i in range(100):
        if i % 2 == 0:
            grid.append(["1"] * 100)
        else:
            grid.append(["0"] * 100)
    
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 50  # 50 separate rows of islands

def test_snake_shaped_island(solution_instance):
    """Test with a snake-shaped island."""
    grid = [
        ["1", "1", "1", "1", "1"],
        ["0", "0", "0", "0", "1"],
        ["1", "1", "1", "0", "1"],
        ["1", "0", "1", "0", "1"],
        ["1", "1", "1", "1", "1"]
    ]
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 1

def test_spiral_shaped_island(solution_instance):
    """Test with a spiral-shaped island."""
    grid = [
        ["1", "1", "1", "1", "1"],
        ["0", "0", "0", "0", "1"],
        ["1", "1", "1", "0", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1"]
    ]
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 1

def test_island_with_hole(solution_instance):
    """Test with an island that has a hole in it."""
    grid = [
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "0", "1", "0", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1"]
    ]
    grid_copy = copy.deepcopy(grid)
    assert solution_instance.numIslands(grid_copy) == 2  # The outer ring and the center cell
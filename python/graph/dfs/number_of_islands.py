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
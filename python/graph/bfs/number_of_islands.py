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


class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        # find all locations of 1
        LAND = "1"
        DIRECTIONS = [(1,0), (-1, 0), (0,1), (0, -1)]

        m, n = len(grid), len(grid[0])

        unvisited = set()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == LAND:
                    unvisited.add((row, col))

        if len(unvisited) == 0:
            return 0

        # can optimize further by combining visited with unvisited
        visited = set()
        islands = 0

        def processNode(r, c):
            q = deque()
            q.append((r, c))
            while q:
                row, col = q.popleft()
                if (row, col) in visited:
                    continue
                visited.add((row, col))
                # try to visit all 1 form this node:
                for dr, dc in DIRECTIONS:
                    next_row = row + dr
                    next_col = col + dc
                    if (next_row >= 0) and next_row < m and next_col >= 0 and next_col < n:
                        if grid[next_row][next_col] == LAND:
                            q.append((next_row, next_col))


        for row, col in unvisited:
            if (row, col) not in visited:
                processNode(row, col)
                islands += 1
        return islands

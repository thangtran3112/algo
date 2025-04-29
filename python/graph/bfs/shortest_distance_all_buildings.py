"""
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

 

Example 1:


Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
Example 2:

Input: grid = [[1,0]]
Output: 1
Example 3:

Input: grid = [[1]]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0, 1, or 2.
There will be at least one building in the grid.
"""
from collections import deque
import math
from typing import List

"""
* BFS from all houses, overwrite the original grid with INVALID,
if a LAND is not reached, by any iteration of BFS
* For each LAND, keep track of distance_sum[row][col], and houses_reach[row][col]
* For all the final lands, find out, which one has the lowest distance_sum 
and houses_reach == total_hours
"""
class SolutionEarlyPruning:
    def shortestDistance(self, grid):
        row_size = len(grid)
        col_size = len(grid[0])
        HOUSE = 1
        LAND = 0
        OBSTACLE = 2
        INVALID = -1  # Mark unreachable lands
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        distance_sum = [[0] * col_size for _ in range(row_size)]
        reach = [[0] * col_size for _ in range(row_size)]
        total_houses = 0

        def bfs(start_row, start_col):
            visited = [[False] * col_size for _ in range(row_size)]
            queue = deque()
            queue.append((start_row, start_col, 0))
            visited[start_row][start_col] = True

            while queue:
                row, col, dist = queue.popleft()
                for row_move, col_move in directions:
                    nei_row = row + row_move
                    nei_col = col + col_move
                    if (0 <= nei_row < row_size and 0 <= nei_col < col_size and
                        not visited[nei_row][nei_col] and grid[nei_row][nei_col] == LAND):
                        visited[nei_row][nei_col] = True
                        reach[nei_row][nei_col] += 1
                        distance_sum[nei_row][nei_col] += dist + 1
                        queue.append((nei_row, nei_col, dist + 1))

            # After BFS from this house: invalidate unreachable lands
            for r in range(row_size):
                for c in range(col_size):
                    if grid[r][c] == LAND and not visited[r][c]:
                        grid[r][c] = INVALID

        # Step 1: Start BFS from every house
        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == HOUSE:
                    total_houses += 1
                    bfs(row, col)

        # Step 2: Find the minimum distance
        min_dist = float('inf')
        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == LAND and reach[row][col] == total_houses:
                    min_dist = min(min_dist, distance_sum[row][col])

        return min_dist if min_dist != float('inf') else -1

# Unoptimized BFS
class SolutionBFSFromBuildings:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        row_size = len(grid)
        col_size = len(grid[0])
        HOUSE = 1
        LAND = 0
        OBSTACLE = 2
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def getNeigbhor(row, col):
            possible_neighbors = []
            for row_move, col_move in directions:
                next_row = row + row_move
                next_col = col + col_move
                if 0 <= next_row < row_size and 0 <= next_col < col_size:
                    if grid[next_row][next_col] == LAND:
                        possible_neighbors.append((next_row, next_col))
            return possible_neighbors

        lands = []
        total_houses = 0
        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == 1:
                    lands.append((row, col))
                    total_houses += 1
        # 2D matrix of 2-element list (house_reached, total_cost)
        matrix = [[[0, 0] for _ in range(col_size)] for _ in range(row_size)]

        # From all house positions, try to reach out to meet all LANDS
        # For each LAND, we will keep track of (houses_reached, total_cost)
        def bfs(start_row, start_col):
            visited = set()
            queue = deque()
            queue.append((start_row, start_col, 0))
            while queue:
                row, col, distance = queue.popleft()
                visited.add((row, col))
                possible_neighbors = getNeigbhor(row, col)
                for nei_row, nei_col in possible_neighbors:
                    if (nei_row, nei_col) not in visited:
                        visited.add((nei_row, nei_col))
                        matrix[nei_row][nei_col][0] += 1  # update houses_reached
                        matrix[nei_row][nei_col][1] += distance + 1  # update total distances
                        queue.append((nei_row, nei_col, distance + 1))

        for start_row, start_col in lands:
            bfs(start_row, start_col)

        min_cost = math.inf
        for row in range(row_size):
            for col in range(col_size):
                houses_reach, total_cost = matrix[row][col]
                if houses_reach == total_houses and total_cost < min_cost:
                    min_cost = total_cost

        return min_cost if min_cost != math.inf else -1
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[SolutionEarlyPruning, SolutionBFSFromBuildings],
               ids=["EarlyPruning", "BFSFromBuildings"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    grid = [
        [1, 0, 2, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    expected = 7
    assert solution_instance.shortestDistance(grid) == expected

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    grid = [[1, 0]]
    expected = 1
    assert solution_instance.shortestDistance(grid) == expected

def test_example3(solution_instance):
    """Test Example 3 from the problem description."""
    grid = [[1]]
    expected = -1
    assert solution_instance.shortestDistance(grid) == expected

def test_single_house_no_land(solution_instance):
    """Test with a single house and no empty land."""
    grid = [[1]]
    expected = -1
    assert solution_instance.shortestDistance(grid) == expected

def test_single_house_with_land(solution_instance):
    """Test with a single house and one unit of empty land."""
    grid = [[1, 0]]
    expected = 1
    assert solution_instance.shortestDistance(grid) == expected

def test_multiple_houses_no_common_land(solution_instance):
    """Test with multiple houses but no common land to reach all."""
    grid = [
        [1, 0, 1],
        [0, 2, 0],
        [1, 0, 1]
    ]
    expected = -1
    assert solution_instance.shortestDistance(grid) == expected

def test_houses_separated_by_obstacle(solution_instance):
    """Test with houses separated by obstacles."""
    grid = [
        [1, 2, 1],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # Since there's a path around the obstacle, the minimum distance is 4
    expected = 4
    assert solution_instance.shortestDistance(grid) == expected

def test_obstacles_blocking_all_paths(solution_instance):
    """Test with obstacles completely blocking access to some houses."""
    grid = [
        [1, 0, 0],
        [2, 2, 2],
        [0, 0, 1]
    ]
    expected = -1
    assert solution_instance.shortestDistance(grid) == expected

def test_larger_grid(solution_instance):
    """Test with a larger grid with multiple optimal locations."""
    grid = [
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1]
    ]
    expected = 6
    assert solution_instance.shortestDistance(grid) == expected

def test_diagonal_houses(solution_instance):
    """Test with houses placed diagonally."""
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    expected = 4
    assert solution_instance.shortestDistance(grid) == expected

def test_houses_in_corners(solution_instance):
    """Test with houses in corners."""
    grid = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]
    expected = 6
    assert solution_instance.shortestDistance(grid) == expected

def test_complex_layout(solution_instance):
    """Test with a complex layout of houses, obstacles, and empty land."""
    grid = [
        [1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 2, 2, 0, 0],
        [0, 0, 2, 2, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1]
    ]
    # The actual minimum distance to reach all four houses
    # considering obstacle paths is 20
    expected = 20
    assert solution_instance.shortestDistance(grid) == expected

def test_obstacle_surrounded_house(solution_instance):
    """Test with a house surrounded by obstacles."""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
        [2, 2, 2]
    ]
    # The minimum distance to the single house is 1
    expected = 1
    assert solution_instance.shortestDistance(grid) == expected

def test_line_of_houses(solution_instance):
    """Test with houses arranged in a line."""
    grid = [
        [1, 0, 1, 0, 1]
    ]
    # No common empty land can reach all houses in this case
    expected = -1
    assert solution_instance.shortestDistance(grid) == expected

def test_minimum_distance_equal(solution_instance):
    """Test where multiple positions have the same minimum distance."""
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    expected = 4
    assert solution_instance.shortestDistance(grid) == expected

def test_only_houses_and_obstacles(solution_instance):
    """Test grid with only houses and obstacles, no empty land."""
    grid = [
        [1, 2, 1],
        [2, 1, 2],
        [1, 2, 1]
    ]
    expected = -1
    assert solution_instance.shortestDistance(grid) == expected
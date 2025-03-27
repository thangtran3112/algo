import pytest
from min_cost_connect import KrutsalSolution

@pytest.fixture
def solution():
    return KrutsalSolution()

def test_empty_points(solution):
    points = []
    assert solution.minCostConnectPoints(points) == 0

def test_single_point(solution):
    points = [[0, 0]]
    assert solution.minCostConnectPoints(points) == 0

def test_two_points(solution):
    points = [[0, 0], [2, 2]]
    assert solution.minCostConnectPoints(points) == 4  # Manhattan distance: |0-2| + |0-2| = 4

def test_three_points(solution):
    points = [[3, 12], [-2, 5], [-4, 1]]
    assert solution.minCostConnectPoints(points) == 18  # Minimum cost to connect all points

def test_five_points(solution):
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    assert solution.minCostConnectPoints(points) == 20  # Minimum cost to connect all points

def test_large_coordinates(solution):
    points = [[-1000000, -1000000], [1000000, 1000000]]
    assert solution.minCostConnectPoints(points) == 4000000  # Manhattan distance: |x1-x2| + |y1-y2|

def test_duplicate_points(solution):
    points = [[0, 0], [0, 0], [1, 1]]
    assert solution.minCostConnectPoints(points) == 2  # Only unique points matter

def test_all_points_in_line(solution):
    points = [[0, 0], [1, 0], [2, 0], [3, 0]]
    assert solution.minCostConnectPoints(points) == 3  # Connect sequentially along the line

def test_all_points_in_grid(solution):
    points = [[0, 0], [0, 1], [1, 0], [1, 1]]
    assert solution.minCostConnectPoints(points) == 3  # Minimum cost to connect all points in a grid

def test_large_number_of_points(solution):
    points = [[i, i] for i in range(100)]
    assert solution.minCostConnectPoints(points) > 0  # Ensure it runs without errors for large inputs
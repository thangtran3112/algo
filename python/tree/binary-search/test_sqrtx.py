import pytest
from sqrtx import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    x = 4
    assert solution.mySqrt(x) == 2

def test_example_2(solution):
    """Test the second example from the problem statement."""
    x = 8
    assert solution.mySqrt(x) == 2

def test_zero(solution):
    """Test with input x = 0."""
    x = 0
    assert solution.mySqrt(x) == 0

def test_one(solution):
    """Test with input x = 1."""
    x = 1
    assert solution.mySqrt(x) == 1

def test_perfect_squares(solution):
    """Test with perfect square inputs."""
    perfect_squares = [(4, 2), (9, 3), (16, 4), (25, 5), (36, 6), (100, 10)]
    for x, expected in perfect_squares:
        assert solution.mySqrt(x) == expected

def test_non_perfect_squares(solution):
    """Test with non-perfect square inputs."""
    non_perfect_squares = [(2, 1), (3, 1), (5, 2), (10, 3), (99, 9), (101, 10)]
    for x, expected in non_perfect_squares:
        assert solution.mySqrt(x) == expected

def test_large_number(solution):
    """Test with a large input within constraints."""
    x = 2**31 - 1  # Maximum value allowed by constraints
    # √(2^31 - 1) ≈ 46340.95
    assert solution.mySqrt(x) == 46340

def test_boundary_values(solution):
    """Test with boundary values of the constraints."""
    assert solution.mySqrt(0) == 0
    assert solution.mySqrt(2**31 - 1) == 46340

def test_performance_large_values(solution):
    """Test performance with large values."""
    large_values = [10**6, 10**8, 10**9]
    expected_results = [1000, 10000, 31622]
    for x, expected in zip(large_values, expected_results):
        assert solution.mySqrt(x) == expected
import pytest
from valid_square import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    assert solution.isPerfectSquare(16) == True

def test_example_2(solution):
    """Test the second example from the problem statement."""
    assert solution.isPerfectSquare(14) == False

def test_small_perfect_squares(solution):
    """Test small perfect square numbers."""
    for i in range(1, 10):
        assert solution.isPerfectSquare(i * i) == True

def test_small_non_perfect_squares(solution):
    """Test small non-perfect square numbers."""
    non_squares = [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15]
    for num in non_squares:
        assert solution.isPerfectSquare(num) == False

def test_edge_case_one(solution):
    """Test edge case: num = 1."""
    assert solution.isPerfectSquare(1) == True

def test_large_perfect_square(solution):
    """Test with a large perfect square."""
    assert solution.isPerfectSquare(10000) == True  # 100^2

def test_large_non_perfect_square(solution):
    """Test with a large non-perfect square."""
    assert solution.isPerfectSquare(10001) == False

def test_boundary_value_max(solution):
    """Test with largest perfect square within constraints."""
    # 46340^2 = 2,147,395,600 which is less than 2^31-1
    assert solution.isPerfectSquare(46340 * 46340) == True

def test_boundary_value_max_plus_one(solution):
    """Test with largest perfect square within constraints plus one."""
    # 46340^2 + 1 = 2,147,395,601 which is not a perfect square
    assert solution.isPerfectSquare(46340 * 46340 + 1) == False

def test_near_boundary(solution):
    """Test with a value close to the maximum constraint."""
    # 2^31-1 = 2,147,483,647
    assert solution.isPerfectSquare(2147483647) == False

def test_large_range(solution):
    """Test a range of perfect squares with larger values."""
    for i in range(100, 110):
        assert solution.isPerfectSquare(i * i) == True
        if i * i < 2147483647:  # Ensure we don't exceed int max
            assert solution.isPerfectSquare(i * i + 1) == False
            assert solution.isPerfectSquare(i * i - 1) == False

def test_performance_large_number(solution):
    """Test performance with a large number close to the constraint."""
    # This tests that the binary search approach is efficient
    # A naive approach would time out
    assert solution.isPerfectSquare(2000000000) == False
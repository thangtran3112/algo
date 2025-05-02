# https://leetcode.com/problems/valid-perfect-square/
"""
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 

Constraints:

1 <= num <= 231 - 1

"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 1:
            return True
        
        def binarySearch(left, right):
            if left > right:
                return False
            mid = (left + right) // 2
            cur = mid * mid

            if cur == num:
                return True
            if cur < num:
                return binarySearch(mid + 1, right)
            if cur > num:
                return binarySearch(left, mid - 1)
            return False

        return binarySearch(0, num // 2 + 1)
    
import pytest  # noqa: E402

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    assert solution.isPerfectSquare(16) is True

def test_example_2(solution):
    """Test the second example from the problem statement."""
    assert solution.isPerfectSquare(14) is False

def test_small_perfect_squares(solution):
    """Test small perfect square numbers."""
    for i in range(1, 10):
        assert solution.isPerfectSquare(i * i) is True

def test_small_non_perfect_squares(solution):
    """Test small non-perfect square numbers."""
    non_squares = [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15]
    for num in non_squares:
        assert solution.isPerfectSquare(num) is False

def test_edge_case_one(solution):
    """Test edge case: num = 1."""
    assert solution.isPerfectSquare(1) is True

def test_large_perfect_square(solution):
    """Test with a large perfect square."""
    assert solution.isPerfectSquare(10000) is True  # 100^2

def test_large_non_perfect_square(solution):
    """Test with a large non-perfect square."""
    assert solution.isPerfectSquare(10001) is False

def test_boundary_value_max(solution):
    """Test with largest perfect square within constraints."""
    # 46340^2 = 2,147,395,600 which is less than 2^31-1
    assert solution.isPerfectSquare(46340 * 46340) is True

def test_boundary_value_max_plus_one(solution):
    """Test with largest perfect square within constraints plus one."""
    # 46340^2 + 1 = 2,147,395,601 which is not a perfect square
    assert solution.isPerfectSquare(46340 * 46340 + 1) is False

def test_near_boundary(solution):
    """Test with a value close to the maximum constraint."""
    # 2^31-1 = 2,147,483,647
    assert solution.isPerfectSquare(2147483647) is False

def test_large_range(solution):
    """Test a range of perfect squares with larger values."""
    for i in range(100, 110):
        assert solution.isPerfectSquare(i * i) is True
        if i * i < 2147483647:  # Ensure we don't exceed int max
            assert solution.isPerfectSquare(i * i + 1) is False
            assert solution.isPerfectSquare(i * i - 1) is False

def test_performance_large_number(solution):
    """Test performance with a large number close to the constraint."""
    # This tests that the binary search approach is efficient
    # A naive approach would time out
    assert solution.isPerfectSquare(2000000000) is False
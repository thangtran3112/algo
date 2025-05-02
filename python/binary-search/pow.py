# https://leetcode.com/problems/powx-n/description/
"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = abs(n)

        # binary recursion
        def helper(k: int) -> float:
            if k == 0:
                return 1
            half = k // 2
            remainder = k % 2
            half_result = helper(half)
            if remainder == 1:
                return half_result * half_result * x
            return half_result * half_result

        result = helper(N)
        return result if n > 0 else (1 / result)

import pytest  # noqa: E402

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    x = 2.00000
    n = 10
    assert solution.myPow(x, n) == pytest.approx(1024.00000)

def test_example_2(solution):
    """Test the second example from the problem statement."""
    x = 2.10000
    n = 3
    assert solution.myPow(x, n) == pytest.approx(9.26100)

def test_example_3(solution):
    """Test the third example from the problem statement."""
    x = 2.00000
    n = -2
    assert solution.myPow(x, n) == pytest.approx(0.25000)

def test_zero_power(solution):
    """Test any number raised to power 0."""
    x = 42.12345
    n = 0
    assert solution.myPow(x, n) == pytest.approx(1.0)

def test_one_power(solution):
    """Test any number raised to power 1."""
    x = 7.5
    n = 1
    assert solution.myPow(x, n) == pytest.approx(7.5)

def test_negative_one_power(solution):
    """Test any number raised to power -1."""
    x = 4.0
    n = -1
    assert solution.myPow(x, n) == pytest.approx(0.25)

def test_negative_base_odd_power(solution):
    """Test with negative base and odd power."""
    x = -2.0
    n = 3
    assert solution.myPow(x, n) == pytest.approx(-8.0)

def test_negative_base_even_power(solution):
    """Test with negative base and even power."""
    x = -2.0
    n = 4
    assert solution.myPow(x, n) == pytest.approx(16.0)

def test_fractional_base_power(solution):
    """Test with fractional base."""
    x = 0.5
    n = 3
    assert solution.myPow(x, n) == pytest.approx(0.125)

def test_near_boundary_value_max(solution):
    """Test with near maximum value of x."""
    x = 99.9
    n = 2
    assert solution.myPow(x, n) == pytest.approx(9980.01)

def test_near_boundary_value_min(solution):
    """Test with near minimum value of x."""
    x = -99.9
    n = 2
    assert solution.myPow(x, n) == pytest.approx(9980.01)

def test_max_power_positive(solution):
    """Test with maximum positive power in constraints."""
    x = 1.001
    n = 2**31 - 1
    # This is an extremely large calculation, so we're just checking it runs
    # without error rather than checking the exact value
    result = solution.myPow(x, n)
    assert result > 0

def test_edge_case_close_to_one(solution):
    """Test with x very close to 1."""
    x = 0.9999999999
    n = 1000
    assert solution.myPow(x, n) == pytest.approx(0.9999, abs=1e-2)
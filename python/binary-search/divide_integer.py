# https://leetcode.com/problems/divide-two-integers/description/
"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""
# Try reducing dividend by (2, 4, 8, 16) * divisor
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend <= 0) != (divisor <= 0)
        dividend, divisor = abs(dividend), abs(divisor)

        quotidient = 0

        # example: 255 / 3, 3 * 2^6 = 192
        while dividend >= divisor:
            temp_divisor = divisor
            x = 1

            # check for x, where x * divisor go near dividend. x = 2, 4, 8, 16, etc
            while dividend >= temp_divisor + temp_divisor:
                temp_divisor += temp_divisor
                x += x
            # first round x = 2, temp_divisor = 6
            # second round x = 4, temp_divisor = 12
            # ... 6th round x = 64, temp_divisor = 192

            # first big loop, quotidient = 64
            quotidient += x
            dividend -= temp_divisor  # reset dividend to 255 - 192, and continue the loop

        return quotidient if not negative else -quotidient
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Fixture to provide a Solution instance."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    assert solution.divide(10, 3) == 3

def test_example2(solution):
    """Test Example 2 from the problem description."""
    assert solution.divide(7, -3) == -2

def test_edge_cases(solution):
    """Test edge cases involving INT_MIN and INT_MAX."""
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    # Special case mentioned in problem
    assert solution.divide(INT_MIN, -1) == INT_MAX
    
    # Other edge cases
    assert solution.divide(INT_MIN, 1) == INT_MIN
    assert solution.divide(INT_MAX, 1) == INT_MAX
    assert solution.divide(INT_MIN, INT_MIN) == 1

def test_zero_dividend(solution):
    """Test with zero dividend."""
    assert solution.divide(0, 1) == 0
    assert solution.divide(0, -1) == 0
    assert solution.divide(0, 2) == 0

def test_one_divisor(solution):
    """Test with divisor of 1 or -1."""
    assert solution.divide(5, 1) == 5
    assert solution.divide(5, -1) == -5
    assert solution.divide(-5, 1) == -5
    assert solution.divide(-5, -1) == 5

def test_equal_numbers(solution):
    """Test when dividend and divisor are equal."""
    assert solution.divide(7, 7) == 1
    assert solution.divide(-7, -7) == 1
    assert solution.divide(-7, 7) == -1
    assert solution.divide(7, -7) == -1

def test_power_of_two(solution):
    """Test with powers of two."""
    assert solution.divide(8, 2) == 4
    assert solution.divide(32, 2) == 16
    assert solution.divide(512, 2) == 256
    assert solution.divide(-1024, 2) == -512

def test_larger_numbers(solution):
    """Test with larger numbers."""
    assert solution.divide(255, 3) == 85
    assert solution.divide(10000, 50) == 200
    assert solution.divide(1000000, 1000) == 1000

def test_negative_numbers(solution):
    """Test various combinations of negative numbers."""
    assert solution.divide(-10, -5) == 2
    assert solution.divide(-15, 3) == -5
    assert solution.divide(15, -3) == -5
    assert solution.divide(-20, -4) == 5

def test_truncation(solution):
    """Test cases where decimal results should be truncated."""
    assert solution.divide(5, 2) == 2  # 2.5 truncated to 2
    assert solution.divide(7, 3) == 2  # 2.33... truncated to 2
    assert solution.divide(-7, 3) == -2  # -2.33... truncated to -2
    assert solution.divide(8, 5) == 1  # 1.6 truncated to 1

def test_consecutive_numbers(solution):
    """Test with consecutive numbers."""
    assert solution.divide(15, 4) == 3
    assert solution.divide(16, 4) == 4
    assert solution.divide(17, 4) == 4
    assert solution.divide(18, 4) == 4
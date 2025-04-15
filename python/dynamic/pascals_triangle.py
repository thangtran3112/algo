# https://leetcode.com/problems/pascals-triangle/description/
"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""
from functools import lru_cache
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        @lru_cache(maxsize=None)
        def dp(row) -> List[int]:
            # base cases
            if row == 1:
                return [1]
            if row == 2:
                return [1, 1]
            if row == 3:
                return [1, 2, 1]

            prev_dp = dp(row - 1)
            cur_dp = [1]
            for i in range(0, len(prev_dp) - 1):
                cur_dp.append(prev_dp[i] + prev_dp[i + 1])
            cur_dp.append(1)
            return cur_dp

        result = []
        for row in range(1, numRows + 1):
            result.append(dp(row))
        return result

import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Fixture that provides the solution implementation."""
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    numRows = 5
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert solution.generate(numRows) == expected

def test_example_2(solution):
    """Test the second example from the problem statement."""
    numRows = 1
    expected = [[1]]
    assert solution.generate(numRows) == expected

def test_minimum_rows(solution):
    """Test with the minimum number of rows (1)."""
    numRows = 1
    expected = [[1]]
    assert solution.generate(numRows) == expected

def test_two_rows(solution):
    """Test with 2 rows."""
    numRows = 2
    expected = [[1], [1, 1]]
    assert solution.generate(numRows) == expected

def test_three_rows(solution):
    """Test with 3 rows."""
    numRows = 3
    expected = [[1], [1, 1], [1, 2, 1]]
    assert solution.generate(numRows) == expected

def test_six_rows(solution):
    """Test with 6 rows."""
    numRows = 6
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1]
    ]
    assert solution.generate(numRows) == expected

def test_ten_rows(solution):
    """Test with 10 rows."""
    numRows = 10
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]
    assert solution.generate(numRows) == expected

def test_caching_efficiency(solution):
    """Test the efficiency of the memoization by calling the function multiple times."""
    # First call
    result1 = solution.generate(15)
    
    # Second call should use cached results
    import time
    start = time.time()
    result2 = solution.generate(15)
    end = time.time()
    
    # Verify results are the same
    assert result1 == result2
    
    # The second call should be very fast due to caching
    # This is more of a performance check than a correctness check
    assert end - start < 0.001  # Should be near-instantaneous with caching

def test_row_properties(solution):
    """Test various properties of Pascal's triangle rows."""
    numRows = 20
    triangle = solution.generate(numRows)
    
    # Each row should start and end with 1
    for row in triangle:
        assert row[0] == 1
        assert row[-1] == 1
    
    # Each row should have a length equal to its row number
    for i, row in enumerate(triangle, 1):
        assert len(row) == i
    
    # Sum of elements in row n is 2^(n-1)
    for i, row in enumerate(triangle, 1):
        assert sum(row) == 2**(i-1)
    
    # Row is symmetric
    for row in triangle:
        assert row == row[::-1]

def test_adjacent_sums(solution):
    """Test that each element is the sum of the two elements above it."""
    numRows = 15
    triangle = solution.generate(numRows)
    
    for i in range(2, numRows):  # Start from the third row (index 2)
        for j in range(1, i):  # Skip the first and last elements
            # Each element should be the sum of the two elements above it
            assert triangle[i][j] == triangle[i-1][j-1] + triangle[i-1][j]

def test_maximum_rows(solution):
    """Test with the maximum number of rows allowed (30)."""
    numRows = 30
    result = solution.generate(numRows)
    
    # Verify basic properties
    assert len(result) == 30
    assert result[0] == [1]
    assert result[1] == [1, 1]
    assert result[29][0] == 1
    assert result[29][29] == 1
    
    # Verify a known value from the 30th row
    # The central element in the 30th row is the combination C(29,14) = 77558760
    mid_index = 15  # 0-indexed, so 15th element is the middle of 30
    assert result[29][mid_index] == 77558760

def test_binomial_coefficient(solution):
    """Test specific binomial coefficients in the triangle."""
    triangle = solution.generate(21)
    
    # C(n, k) = n! / (k! * (n-k)!) is the value at row n, position k (0-indexed)
    # Verify some well-known binomial coefficients
    assert triangle[5][2] == 10  # C(5,2) = 10
    assert triangle[10][5] == 252  # C(10,5) = 252
    assert triangle[20][10] == 184756  # C(20,10) = 184756
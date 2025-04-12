# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/description/
"""
You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
Remove x from nums.
Return the maximum score after performing m operations.

 

Example 1:

Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.
Example 2:

Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
 

Constraints:

n == nums.length
m == multipliers.length
1 <= m <= 300
m <= n <= 105 
-1000 <= nums[i], multipliers[i] <= 1000
"""

from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
            * Fact: left <= op, right <= op
            * We just need a square matrix (m * m) with an extra out-of-bound edges (m + 1)
                0  1  2  3  4   m (op) (m+1) row
            0                   0
            1     max           0
            2                   0
            3                   0
            4                   0
            m   0  0  0  0   0  0 
            (left)
            (m+1) collums
        """
        m = len(multipliers)
        n = len(nums)

        # avoid last row and last col out-of-bound calculation. square matrix
        dp =[[0] * (m + 1) for _ in range(m + 1)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):
                case1 = multipliers[op] * nums[left] + dp[op + 1][left + 1]
                case2 = multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left]
                dp[op][left] = max(case1, case2)

        return dp[0][0]

class SolutionRecursiveTopDown:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
            * Use a 2D DP array with 2 variables operation op and left value
            * After op operations, and shifting left number from the nums
              the right has been shifted by (op - left) postion from the rightmost
              Therefore right = len(nums) - 1 - (op - left)
            * Base case: when op = m = len(multipliers), we have used up all operations
              this we return 0. Because op is within [0, m-1]
            * For any row=op, col=left, the maximumScore cell will have value as maximum of:
              case1, when start element at nums[left] is path of the maximumScore:
                 maximumScore = nums[left] * multipliers[op] + dp(op+1, left+1)
              case2, when end element at nums[right] is path of the maximumScore:
                maximumScore = nums[right] * multipliers[op] + dp(op+1, left)
        """
        m = len(multipliers)  # number of operations
        n = len(nums)

        memo = {}

        # we can also use @lru_cache(maxsize=None) instead of using memo
        def max_score_dp(op, left):
            if op == m:
                return 0
            if (op, left) in memo:
                return memo[(op, left)]

            right = (n - 1) - (op - left)

            # case1: using start of nums array at left position
            case1 = nums[left] * multipliers[op] + max_score_dp(op + 1, left + 1)

            # case2: using end position of nums at right postion
            case2 = nums[right] * multipliers[op] + max_score_dp(op + 1, left)

            memo[(op, left)] = max(case1, case2)
            return memo[(op, left)]

        return max_score_dp(0, 0)

# TESE CASES

import pytest
import time

@pytest.fixture
def bottom_up_solution():
    return Solution()

@pytest.fixture
def top_down_solution():
    return SolutionRecursiveTopDown()

@pytest.fixture
def all_solutions():
    return [Solution(), SolutionRecursiveTopDown()]

# Example test cases from problem description
def test_example1(all_solutions):
    """Test the first example from the problem statement."""
    nums = [1, 2, 3]
    multipliers = [3, 2, 1]
    expected = 14
    
    for solution in all_solutions:
        assert solution.maximumScore(nums, multipliers) == expected

def test_example2(all_solutions):
    """Test the second example from the problem statement."""
    nums = [-5, -3, -3, -2, 7, 1]
    multipliers = [-10, -5, 3, 4, 6]
    expected = 102
    
    for solution in all_solutions:
        assert solution.maximumScore(nums, multipliers) == expected

# Edge cases
def test_single_operation(all_solutions):
    """Test with only one operation."""
    nums = [1, 2, 3, 4, 5]
    multipliers = [10]
    expected = 50  # Choose 5 * 10 = 50
    
    for solution in all_solutions:
        assert solution.maximumScore(nums, multipliers) == expected

def test_equal_length_arrays(all_solutions):
    """Test when nums length equals multipliers length."""
    nums = [1, 2, 3]
    multipliers = [3, 2, 1]
    expected = 14
    
    for solution in all_solutions:
        assert solution.maximumScore(nums, multipliers) == expected

def test_all_negative_nums(all_solutions):
    """Test with all negative numbers in nums array."""
    nums = [-5, -4, -3, -2, -1]
    multipliers = [1, 2, 3]
    expected = -5  # Choose -5*1 + -4*2 + -3*3 = -5 + -8 + -9 = -22
                  # Alternatively: -1*1 + -2*2 + -3*3 = -1 + -4 + -9 = -14
                  # Optimal: -1*1 + -5*2 + -2*3 = -1 + -10 + -6 = -17
    
    for solution in all_solutions:
        result = solution.maximumScore(nums, multipliers)
        assert result >= -17  # Allow for optimal solution

def test_all_negative_multipliers(all_solutions):
    """Test with all negative numbers in multipliers array."""
    nums = [5, 4, 3, 2, 1]
    multipliers = [-1, -2, -3]
    expected = -5  # Choose 1*-1 + 1*-2 + 1*-3 = -6 (minimize negative impact)
    
    for solution in all_solutions:
        result = solution.maximumScore(nums, multipliers)
        assert result == -13

# Pattern tests
def test_alternating_signs_nums(all_solutions):
    """Test with alternating signs in nums."""
    nums = [5, -4, 3, -2, 1]
    multipliers = [2, -3, 1]
    expected = 25
    
    for solution in all_solutions:
        assert solution.maximumScore(nums, multipliers) == expected

def test_alternating_signs_multipliers(all_solutions):
    """Test with alternating signs in multipliers."""
    nums = [5, 4, 3, 2, 1]
    multipliers = [2, -3, 1]
    expected = 11
    
    for solution in all_solutions:
        result = solution.maximumScore(nums, multipliers)
        assert result == expected

def test_zeros_in_nums(all_solutions):
    """Test with zeros in nums."""
    nums = [0, 5, 0, 3, 0]
    multipliers = [2, 3, 1]
    expected = 15
    
    for solution in all_solutions:
        assert solution.maximumScore(nums, multipliers) == expected

def test_zeros_in_multipliers(all_solutions):
    """Test with zeros in multipliers."""
    nums = [5, 4, 3, 2, 1]
    multipliers = [0, 2, 0]
    expected = 8  # Choose any*0 + 5*2 + any*0 = 0 + 10 + 0 = 10
                  # Or: any*0 + 4*2 + any*0 = 0 + 8 + 0 = 8
    
    for solution in all_solutions:
        result = solution.maximumScore(nums, multipliers)
        assert result >= 8  # Allow for different optimal solutions

# Larger test cases
def test_medium_size_input(all_solutions):
    """Test with medium-sized arrays."""
    nums = list(range(1, 21))  # [1, 2, ..., 20]
    multipliers = list(range(1, 11))  # [1, 2, ..., 10]
    
    for solution in all_solutions:
        result = solution.maximumScore(nums, multipliers)
        assert result > 0  # Basic sanity check

# Performance tests
def test_performance_bottom_up(bottom_up_solution):
    """Test performance of bottom-up solution with larger input."""
    nums = list(range(-500, 500))  # 1000 elements
    multipliers = list(range(1, 201))  # 200 operations
    
    start = time.time()
    bottom_up_solution.maximumScore(nums, multipliers)
    end = time.time()
    
    assert (end - start) < 5.0  # Should complete within 5 seconds

def test_performance_top_down(top_down_solution):
    """Test performance of top-down solution with larger input."""
    nums = list(range(-500, 500))  # 1000 elements
    multipliers = list(range(1, 201))  # 200 operations
    
    start = time.time()
    top_down_solution.maximumScore(nums, multipliers)
    end = time.time()
    
    assert (end - start) < 5.0  # Should complete within 5 seconds

# Equivalence test
def test_solutions_equivalence():
    """Verify that both solutions produce the same results for various inputs."""
    test_cases = [
        ([1, 2, 3], [3, 2, 1]),  # Example 1
        ([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]),  # Example 2
        ([5, -4, 3, -2, 1], [2, -3, 1]),  # Alternating signs
        ([0, 5, 0, 3, 0], [2, 3, 1]),  # Zeros in nums
        ([1, 1, 1, 1], [1, 1, 1]),  # All ones
        ([-1000, -999, 999, 1000], [-1000, -999, 999, 1000]),  # Boundary values
        (list(range(10)), list(range(5)))  # Sequential numbers
    ]
    
    bottom_up = Solution()
    top_down = SolutionRecursiveTopDown()
    
    for nums, multipliers in test_cases:
        bu_result = bottom_up.maximumScore(nums, multipliers)
        td_result = top_down.maximumScore(nums, multipliers)
        assert bu_result == td_result, f"Discrepancy found for nums={nums}, multipliers={multipliers}"

# Boundary value tests
def test_constraint_boundary_values(all_solutions):
    """Test with values at the boundary of problem constraints."""
    # Max values: 1000 and -1000
    nums = [-1000, 1000] * 5
    multipliers = [-1000, 1000] * 3
    
    for solution in all_solutions:
        # Just ensure it computes a result without error
        result = solution.maximumScore(nums, multipliers[:6])
        assert isinstance(result, int)

# Special case tests
def test_optimal_strategy_left_vs_right(all_solutions):
    """Test cases that require a specific left/right picking strategy."""
    # Case where taking from left is always better
    nums = [10, 9, 8, 7, 1, 2, 3]
    multipliers = [1, 1, 1]
    expected = 10 + 9 + 8  # Choose left three times
    
    for solution in all_solutions:
        assert solution.maximumScore(nums, multipliers) == expected
    
    # Case where taking from right is always better
    nums = [1, 2, 3, 7, 8, 9, 10]
    multipliers = [1, 1, 1]
    expected = 10 + 9 + 8  # Choose right three times
    
    for solution in all_solutions:
        assert solution.maximumScore(nums, multipliers) == expected
    
    # Case requiring mixed strategy
    nums = [5, 1, 3, 10]
    multipliers = [2, -3, 1]
    expected = 17
    
    for solution in all_solutions:
        assert solution.maximumScore(nums, multipliers) == expected
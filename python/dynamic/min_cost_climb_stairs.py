# https://leetcode.com/problems/min-cost-climbing-stairs/description/
"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""
from functools import cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[n - 2], dp[n - 1])

class SolutionTopDown:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(i: int) -> int:
            # base case
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]

            return min(dp(i - 1), dp(i - 2)) + cost[i]
        n = len(cost)
        return min(dp(n - 1), dp(n - 2))

# TEST CASES
    
import pytest
import time

@pytest.fixture
def bottom_up_solution():
    return Solution()

@pytest.fixture
def top_down_solution():
    return SolutionTopDown()

def test_example1_bottom_up(bottom_up_solution):
    """Test first example from problem statement with bottom-up solution."""
    assert bottom_up_solution.minCostClimbingStairs([10, 15, 20]) == 15

def test_example1_top_down(top_down_solution):
    """Test first example from problem statement with top-down solution."""
    assert top_down_solution.minCostClimbingStairs([10, 15, 20]) == 15

def test_example2_bottom_up(bottom_up_solution):
    """Test second example from problem statement with bottom-up solution."""
    assert bottom_up_solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

def test_example2_top_down(top_down_solution):
    """Test second example from problem statement with top-down solution."""
    assert top_down_solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

def test_minimum_length_bottom_up(bottom_up_solution):
    """Test with minimum length array with bottom-up solution."""
    assert bottom_up_solution.minCostClimbingStairs([1, 2]) == 1

def test_minimum_length_top_down(top_down_solution):
    """Test with minimum length array with top-down solution."""
    assert top_down_solution.minCostClimbingStairs([1, 2]) == 1

def test_all_same_cost_bottom_up(bottom_up_solution):
    """Test with all steps having same cost with bottom-up solution."""
    assert bottom_up_solution.minCostClimbingStairs([5, 5, 5, 5, 5]) == 10

def test_all_same_cost_top_down(top_down_solution):
    """Test with all steps having same cost with top-down solution."""
    assert top_down_solution.minCostClimbingStairs([5, 5, 5, 5, 5]) == 10

def test_alternating_costs_bottom_up(bottom_up_solution):
    """Test with alternating high and low costs with bottom-up solution."""
    assert bottom_up_solution.minCostClimbingStairs([1, 10, 1, 10, 1, 10]) == 3

def test_alternating_costs_top_down(top_down_solution):
    """Test with alternating high and low costs with top-down solution."""
    assert top_down_solution.minCostClimbingStairs([1, 10, 1, 10, 1, 10]) == 3

def test_increasing_costs_bottom_up(bottom_up_solution):
    """Test with increasing costs with bottom-up solution."""
    assert bottom_up_solution.minCostClimbingStairs([1, 2, 3, 4, 5]) == 6

def test_increasing_costs_top_down(top_down_solution):
    """Test with increasing costs with top-down solution."""
    assert top_down_solution.minCostClimbingStairs([1, 2, 3, 4, 5]) == 6

def test_decreasing_costs_bottom_up(bottom_up_solution):
    """Test with decreasing costs with bottom-up solution."""
    assert bottom_up_solution.minCostClimbingStairs([5, 4, 3, 2, 1]) == 6

def test_decreasing_costs_top_down(top_down_solution):
    """Test with decreasing costs with top-down solution."""
    assert top_down_solution.minCostClimbingStairs([5, 4, 3, 2, 1]) == 6

def test_solutions_equivalent():
    """Test that both solutions produce the same results for various inputs."""
    top_down = SolutionTopDown()
    bottom_up = Solution()
    
    test_cases = [
        [10, 15, 20],
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
        [1, 2],
        [5, 5, 5, 5, 5],
        [1, 10, 1, 10, 1, 10],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [0, 0, 0, 0],
        [999, 999, 0, 0, 999, 999]
    ]
    
    for case in test_cases:
        assert top_down.minCostClimbingStairs(case) == bottom_up.minCostClimbingStairs(case)

def test_zero_cost_steps_bottom_up(bottom_up_solution):
    """Test with some steps having zero cost with bottom-up solution."""
    assert bottom_up_solution.minCostClimbingStairs([0, 0, 0, 0]) == 0

def test_zero_cost_steps_top_down(top_down_solution):
    """Test with some steps having zero cost with top-down solution."""
    assert top_down_solution.minCostClimbingStairs([0, 0, 0, 0]) == 0

def test_boundary_values_bottom_up(bottom_up_solution):
    """Test with boundary values from the constraints with bottom-up solution."""
    # Maximum allowed value in constraint is 999
    assert bottom_up_solution.minCostClimbingStairs([999, 999, 0, 0, 999, 999]) == 1998

def test_boundary_values_top_down(top_down_solution):
    """Test with boundary values from the constraints with top-down solution."""
    assert top_down_solution.minCostClimbingStairs([999, 999, 0, 0, 999, 999]) == 1998

def test_large_input_performance_bottom_up(bottom_up_solution):
    """Test performance with larger inputs for bottom-up solution."""
    # Create a long staircase with alternating costs
    cost = [i % 2 for i in range(900)]
    
    start = time.time()
    result = bottom_up_solution.minCostClimbingStairs(cost)
    end = time.time()
    
    # Verify result is correct (should be around 450 for this alternating pattern)
    assert result <= 450
    # Verify computation time is reasonable
    assert (end - start) < 1.0

def test_large_input_performance_top_down(top_down_solution):
    """Test performance with larger inputs for top-down solution."""
    # Create a long staircase with alternating costs
    cost = [i % 2 for i in range(900)]
    
    start = time.time()
    result = top_down_solution.minCostClimbingStairs(cost)
    end = time.time()
    
    # Verify result is correct (should be around 450 for this alternating pattern)
    assert result <= 450
    # Verify computation time is reasonable
    assert (end - start) < 1.0

def test_large_input_comparison():
    """Compare both solutions with a large input."""
    top_down = SolutionTopDown()
    bottom_up = Solution()
    
    # Create a challenging staircase with 900 steps
    cost = [(i * 37) % 1000 for i in range(900)]
    
    # Measure top-down performance
    start_td = time.time()
    result_td = top_down.minCostClimbingStairs(cost)
    end_td = time.time()
    time_td = end_td - start_td
    
    # Measure bottom-up performance
    start_bu = time.time()
    result_bu = bottom_up.minCostClimbingStairs(cost)
    end_bu = time.time()
    time_bu = end_bu - start_bu
    
    # Verify both solutions produce the same result
    assert result_td == result_bu
    
    # Both should be efficient
    assert time_td < 1.0
    assert time_bu < 1.0
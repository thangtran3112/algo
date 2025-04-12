from functools import cache

class SolutionMemorizedTopDown:
    def climbStairs(self, n: int) -> int:
        # how many way to reach i steps
        # with @cache, we do not need to use a memo dictionary to store computed result
        @cache
        def dp(i: int):
            # base case
            if i <= 2:
                return i

            return dp(i - 2) + dp(i - 1)

        return dp(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        # calculate from small steps first
        dp = []
        dp.append(1)
        dp.append(2)
        # since we start the dp array from index 0, we just need to calculate to index n-1
        for i in range(2, n):
            result = dp[i - 1] + dp[i - 2]
            dp.append(result)

        return dp[n - 1]
    
import pytest
import time

@pytest.fixture
def top_down_solution():
    return SolutionMemorizedTopDown()

@pytest.fixture
def bottom_up_solution():
    return Solution()

def test_base_cases_top_down(top_down_solution):
    """Test base cases with top-down solution."""
    assert top_down_solution.climbStairs(1) == 1
    assert top_down_solution.climbStairs(2) == 2

def test_base_cases_bottom_up(bottom_up_solution):
    """Test base cases with bottom-up solution."""
    assert bottom_up_solution.climbStairs(1) == 1
    assert bottom_up_solution.climbStairs(2) == 2

def test_example_cases_top_down(top_down_solution):
    """Test example cases with top-down solution."""
    assert top_down_solution.climbStairs(3) == 3  # 1+1+1, 1+2, 2+1
    assert top_down_solution.climbStairs(4) == 5  # 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2
    assert top_down_solution.climbStairs(5) == 8

def test_example_cases_bottom_up(bottom_up_solution):
    """Test example cases with bottom-up solution."""
    assert bottom_up_solution.climbStairs(3) == 3
    assert bottom_up_solution.climbStairs(4) == 5
    assert bottom_up_solution.climbStairs(5) == 8

def test_solutions_equivalent():
    """Test that both solutions produce the same results for various inputs."""
    top_down = SolutionMemorizedTopDown()
    bottom_up = Solution()
    
    for n in range(1, 20):
        assert top_down.climbStairs(n) == bottom_up.climbStairs(n)

def test_fibonacci_sequence(top_down_solution):
    """Test that the sequence follows the Fibonacci pattern."""
    # The stair climbing problem follows the Fibonacci sequence
    # F(n) = F(n-1) + F(n-2) where F(1) = 1 and F(2) = 2
    fib_values = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    for i, expected in enumerate(fib_values, 1):
        assert top_down_solution.climbStairs(i) == expected

def test_large_input_top_down(top_down_solution):
    """Test performance with larger inputs for top-down solution."""
    start = time.time()
    result = top_down_solution.climbStairs(35)
    end = time.time()
    
    assert result == 14930352  # Known value for n=35
    assert (end - start) < 1.0  # Should be fast with memoization

def test_large_input_bottom_up(bottom_up_solution):
    """Test performance with larger inputs for bottom-up solution."""
    start = time.time()
    result = bottom_up_solution.climbStairs(35)
    end = time.time()
    
    assert result == 14930352  # Known value for n=35
    assert (end - start) < 1.0  # Should be fast with bottom-up DP

def test_very_large_input_comparison():
    """Compare both solutions with a very large input."""
    n = 45  # Large enough to test performance but not overflow
    
    top_down = SolutionMemorizedTopDown()
    bottom_up = Solution()
    
    # Measure top-down performance
    start_td = time.time()
    result_td = top_down.climbStairs(n)
    end_td = time.time()
    time_td = end_td - start_td
    
    # Measure bottom-up performance
    start_bu = time.time()
    result_bu = bottom_up.climbStairs(n)
    end_bu = time.time()
    time_bu = end_bu - start_bu
    
    # Verify both solutions produce the same result
    assert result_td == result_bu
    
    # Both should be efficient but bottom-up typically faster
    assert time_td < 1.0
    assert time_bu < 1.0

def test_zero_steps():
    """Test edge case: zero steps. This is not defined in the problem statement
    but we should have a clear behavior."""
    # For zero steps, by convention we'll say there's 1 way (don't climb at all)
    # But this might fail since problem didn't specify behavior for n=0
    top_down = SolutionMemorizedTopDown()
    try:
        assert top_down.climbStairs(0) == 1
    except:
        # Alternatively, it might cause an error or return 0
        pass
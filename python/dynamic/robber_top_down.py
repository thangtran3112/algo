# https://leetcode.com/problems/house-robber/description/
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
# Top-down Dynamic Programming with memorized dictionary

class SolutionTopDown(object):
    def rob(self, nums) -> int:
        if (len(nums) == 0):
            return 0
        memo = {}
        def dp(i):
            # Base case
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i not in memo:
                memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            
            return memo[i]
        
        return dp(len(nums)-1)

# Bottom up with array
class SolutionBottomUp:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        # since we start from 0, we will only calculate to n-1
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]


    
# TEST CASES
import pytest

@pytest.fixture
def top_down_solution():
    return SolutionTopDown()

@pytest.fixture
def bottom_up_solution():
    return SolutionBottomUp()

def test_example1_top_down(top_down_solution):
    assert top_down_solution.rob([1, 2, 3, 1]) == 4

def test_example1_bottom_up(bottom_up_solution):
    assert bottom_up_solution.rob([1, 2, 3, 1]) == 4

def test_example2_top_down(top_down_solution):
    assert top_down_solution.rob([2, 7, 9, 3, 1]) == 12

def test_example2_bottom_up(bottom_up_solution):
    assert bottom_up_solution.rob([2, 7, 9, 3, 1]) == 12

def test_empty_top_down(top_down_solution):
    assert top_down_solution.rob([]) == 0

def test_empty_bottom_up(bottom_up_solution):
    assert bottom_up_solution.rob([]) == 0

def test_single_house_top_down(top_down_solution):
    assert top_down_solution.rob([5]) == 5

def test_single_house_bottom_up(bottom_up_solution):
    assert bottom_up_solution.rob([5]) == 5

def test_two_houses_top_down(top_down_solution):
    assert top_down_solution.rob([1, 2]) == 2

def test_two_houses_bottom_up(bottom_up_solution):
    assert bottom_up_solution.rob([1, 2]) == 2

def test_consecutive_increasing_top_down(top_down_solution):
    assert top_down_solution.rob([1, 2, 3, 4, 5]) == 9  # 1 + 3 + 5 = 9

def test_consecutive_increasing_bottom_up(bottom_up_solution):
    assert bottom_up_solution.rob([1, 2, 3, 4, 5]) == 9  # 1 + 3 + 5 = 9

def test_all_same_value_top_down(top_down_solution):
    assert top_down_solution.rob([5, 5, 5, 5]) == 10  # 5 + 5 = 10

def test_all_same_value_bottom_up(bottom_up_solution):
    assert bottom_up_solution.rob([5, 5, 5, 5]) == 10  # 5 + 5 = 10

def test_alternating_values_top_down(top_down_solution):
    assert top_down_solution.rob([10, 1, 10, 1, 10]) == 30  # 10 + 10 + 10 = 30

def test_alternating_values_bottom_up(bottom_up_solution):
    assert bottom_up_solution.rob([10, 1, 10, 1, 10]) == 30  # 10 + 10 + 10 = 30

def test_solutions_equivalent():
    """Test that both solutions produce the same results for various inputs."""
    top_down = SolutionTopDown()
    bottom_up = SolutionBottomUp()
    
    test_cases = [
        [],
        [5],
        [1, 2],
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [1, 2, 3, 4, 5],
        [5, 5, 5, 5],
        [10, 1, 10, 1, 10],
        [6, 7, 1, 3, 8, 2, 4],
        [114, 117, 207, 117, 235, 82, 90, 67, 143, 146, 53, 108, 200]
    ]
    
    for case in test_cases:
        assert top_down.rob(case) == bottom_up.rob(case)

def test_boundary_values_top_down(top_down_solution):
    """Test with boundary values from the constraints with top-down solution."""
    # Maximum allowed value in constraint is 400
    assert top_down_solution.rob([400, 400, 400, 400]) == 800  # 400 + 400 = 800

def test_boundary_values_bottom_up(bottom_up_solution):
    """Test with boundary values from the constraints with bottom-up solution."""
    # Maximum allowed value in constraint is 400
    assert bottom_up_solution.rob([400, 400, 400, 400]) == 800  # 400 + 400 = 800

def test_longer_sequence_top_down(top_down_solution):
    """Test with a longer sequence to verify performance with top-down solution."""
    # Create an array of alternating values
    nums = [i % 2 * 10 for i in range(50)]
    assert top_down_solution.rob(nums) == 250  # Sum of 25 values of 10

def test_longer_sequence_bottom_up(bottom_up_solution):
    """Test with a longer sequence to verify performance with bottom-up solution."""
    # Create an array of alternating values
    nums = [i % 2 * 10 for i in range(50)]
    assert bottom_up_solution.rob(nums) == 250  # Sum of 25 values of 10
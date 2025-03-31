# https://leetcode.com/problems/target-sum/description/
"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""
from collections import defaultdict
from typing import List

class SolutionTopDownRecursion:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        cached = {}

        def dfs(i: int, cur_target: int) -> int:
            # there are 2 options +cur_target or -cur_target
            # it could be possible that there is no Solution

            if (i, cur_target) in cached:
                return cached[(i, cur_target)]

            # base case
            if (i == n - 1):
                if cur_target == 0 and nums[i] == 0:
                    # special case, when we have last element as 0, target is also 0
                    # we can use either way of  +0, or -0
                    return 2
                if nums[i] == cur_target:
                    return 1
                if nums[i] == -cur_target:
                    return 1
                return 0

            # Recursion
            val = nums[i]
            first_target = cur_target - val
            second_target = cur_target + val

            result = dfs(i + 1, first_target) + dfs(i + 1, second_target)
            cached[(i, cur_target)] = result
            return result

        return dfs(0, target)

class SolutionBottomUp:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        # If target is outside the possible sum range, return 0
        if abs(target) > total:
            return 0

        dp = defaultdict(int)
        dp[0] = 1  # There's one way to reach sum 0 using no elements

        # First 1:
        # next_dp = {1: 1, -1: 1} (Adding and subtracting 1 from 0).
        # There is 1 way to reach sum 1, and there is 1 way to reach sum -1
        # Second 1:
        # next_dp = {2: 1, 0: 2, -2: 1} (Adding and subtracting 1 from each key in dp).
        # There is 1 way to reach sum 2, 2 ways to reach sum 0, and 1 way to reach sum -2
        # Third 1:
        # next_dp = {3: 1, 1: 3, -1: 3, -3: 1}.
        # Fourth 1:
        # next_dp = {4: 1, 2: 4, 0: 6, -2: 4, -4: 1}.
        # Fifth 1:
        # next_dp = {5: 1, 3: 5, 1: 10, -1: 10, -3: 5, -5: 1}.
        # Result:

        # dp[target] = dp[3] = 5.
        for num in nums:
            next_dp = defaultdict(int)
            for prev_sum in dp:
                ways_to_prev_sum = dp[prev_sum]
                next_dp[prev_sum + num] += ways_to_prev_sum
                next_dp[prev_sum - num] += ways_to_prev_sum
            dp = next_dp

        return dp[target]
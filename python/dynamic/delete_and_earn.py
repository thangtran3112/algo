
"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
"""
# Bottom-up solution
from collections import defaultdict


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        points = defaultdict(lambda: 0) # default value is 0 for invalid key
        max_num = 0

        for num in nums:
            points[num] = points[num] + num
            max_num = max(num, max_num)

        # dp[i]: maximum we can earn, when consider between [0,..,i]
        dp = [0] * (max_num + 1) # [0,0,...,0] for (max_num + 1) length
        
        # Base case
        dp[0] = 0
        dp[1] = points[1] # will be 0, if 1 is not an element in nums array

        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-2] + points[i], dp[i-1])
        
        return dp[-1]

        
class TopdownSolution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        points = defaultdict(int) # default dict will return 0 for int type of key is invalid
        max_num = 0
        memo = {}

        for num in nums:
            points[num] = points[num] + num
            max_num = max(num, max_num)

        memo[0] = 0
        memo[1] = points[1] # default to 0 if nums does not contains 1

        # dp(i): maximum we can earn, when consider between [0,..,i]
        def dp(i):
            if i in memo:
                return memo[i]
            # there could be i or not inside points dictionary
            memo[i] = max(dp(i-1), dp(i-2) + points[i])
            return memo[i]

        return dp(max_num)

import pytest
import time

@pytest.fixture
def solution_classes():
    """Return both solution classes to test."""
    return [Solution(), TopdownSolution()]

# Test cases in format: (input, expected_output, description)
TEST_CASES = [
    ([3, 4, 2], 6, "Example 1 from problem statement"),
    ([2, 2, 3, 3, 3, 4], 9, "Example 2 from problem statement"),
    ([5], 5, "Single element array"),
    ([1, 1, 1, 2, 2, 3], 6, "Array with duplicate elements"),
    ([1, 2, 3, 4, 5], 9, "Consecutive integers"),
    ([2, 4, 6, 8], 20, "Non-consecutive integers"),
    ([1, 5, 10, 15, 20], 51, "Spread out integers"),
    ([1, 3, 5, 7, 9], 25, "Alternating odd elements"),
    ([2, 4, 6, 8, 10], 30, "Alternating even elements"),
    ([8, 3, 4, 7, 6, 6, 9, 2, 5, 8, 2, 4, 9, 5, 9, 1, 5, 7, 1, 4], 61, "Challenging case")
]

@pytest.mark.parametrize("nums, expected, description", TEST_CASES)
def test_delete_and_earn(solution_classes, nums, expected, description):
    """Test both solution implementations with all test cases."""
    for solution in solution_classes:
        solution_name = solution.__class__.__name__
        assert solution.deleteAndEarn(nums) == expected, f"{solution_name} failed: {description}"

def test_solutions_equivalent():
    """Test that both solutions produce the same results for various inputs."""
    top_down = TopdownSolution()
    bottom_up = Solution()
    
    test_cases = [
        [3, 4, 2],
        [2, 2, 3, 3, 3, 4],
        [5],
        [1, 1, 1, 2, 2, 3],
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8],
        [1, 5, 10, 15, 20],
        [1, 2, 3, 1, 1],
        [8, 7, 3, 8, 1, 4, 10, 10, 10, 2]
    ]
    
    for case in test_cases:
        assert top_down.deleteAndEarn(case) == bottom_up.deleteAndEarn(case)
# Top-down Dynamic Programming with memorized dictionary
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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
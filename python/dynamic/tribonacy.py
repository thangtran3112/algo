class BottomUpSolution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1

        dp = [0] * (n + 1)  # n + 1 elements, when n >= 3
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

        return dp[n]


# Recursion with memoization
class TopDownSolution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        def dp(i):
            # Base case
            if i in memo:
                return memo[i]
            memo[i] = dp(i - 3) + dp(i - 2) + dp(i - 1)
            return memo[i]

        return dp(n)

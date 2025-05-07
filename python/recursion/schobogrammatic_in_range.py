# https://leetcode.com/problems/strobogrammatic-number-iii/description/
"""
Given two strings low and high that represent two integers low and high where low <= high, return the number of strobogrammatic numbers in the range [low, high].

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: low = "50", high = "100"
Output: 3
Example 2:

Input: low = "0", high = "0"
Output: 1
 

Constraints:

1 <= low.length, high.length <= 15
low and high consist of only digits.
low <= high
low and high do not contain any leading zeros except for zero itself.
"""
from collections import defaultdict


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        # calculate the dp array of possible strobogrammatic with n letters
        # https://leetcode.com/problems/strobogrammatic-number-ii
        # To calculate dp[n], we pad all elements from dp[n - 2] with possible edges
        # possible padding includes (0, 0) , (1, 1), (6, 9), (8, 8) and (9, 6)
        # Notes: we need to calculate (0, 0) into dp array, even they are invalid
        # Example: n = 4 (letters), we use dp[2] = (00, 11, 69, 96, 88)
        # We have [1001, 6009, 9006, 8008, 0000] created by padding to dp[2][0] = 00
        # When we have th final dp[] array, we can start remove all number with leading 0
        dp = defaultdict(list)
        dp[0] = [""]
        dp[1] = ["0", "1", "8"]

        n = len(high)
        possible_edges = [("0", "0"), ("1", "1"), ("6", "9"), ("9", "6"), ("8", "8")]

        for i in range(2, n + 1):
            for middle in dp[i - 2]:
                for a, b in possible_edges:
                    dp[i].append(a + middle + b)

        # now we are filtering out all number between low and high,
        count = 0
        for i in range(len(low), n + 1):
            curr_list = dp[i]
            for value in curr_list:
                # remove number with leading zero, except for i = 1, when [0,1,8]
                if value[0] == "0" and i != 1:
                    continue
                else:
                    if int(low) <= int(value) <= int(high):
                        count += 1

        return count
    

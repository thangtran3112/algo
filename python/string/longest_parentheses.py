# https://leetcode.com/explore/interview/card/facebook/55/dynamic-programming-3/3035/
"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = []
        start = -1  # index of last unmatched ')'

        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        max_len = max(max_len, i - stack[-1])
                    else:
                        max_len = max(max_len, i - start)
                else:
                    # we meet a ')' but with no previous '('
                    start = i  # unmatched ')', reset base

        return max_len

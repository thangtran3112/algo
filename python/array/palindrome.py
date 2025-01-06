# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

'''
examples = [
    "radar",
    "A man a plan a canal Panama",
    "race a car",
    "Madam Im Adam",
    "noon",
    "level"
]
'''

def build_center_expansion(s, left, right, center):
    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            center = s[left] + center + s[right]
            left -= 1
            right += 1
        else:
            break
    return center

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Find the longest palindrome with center expansion
        longest = ""
        # Center expansion with odd length
        for i in range(len(s)):
            left = i - 1
            right = i + 1
            center = s[i]
            tmp = build_center_expansion(s, left, right, center)
            if len(tmp) > len(longest):
                longest = tmp
                
        # Center expansion with even length, empty center
        for i in range(len(s)-1):
            left = i
            right = i + 1
            center = ""
            tmp = build_center_expansion(s, left, right, center)
            if len(tmp) > len(longest):
                longest = tmp
                
        return longest

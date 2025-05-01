# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
"""
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 

Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # maintain a dictionary as dic to keep track of { character: count }
        # keep sliding right until len(dic) <= k
        # if meeting a position, where len(dic) = k + 1
        # update max_length of current_length [left, right - 1] < max_length
        # start sliding left, until len(dic) = k 
        # start sliding right, again, until len(dic) = k + 1
        # keep doing so, and update max_length
        if k == 0:
            return 0
        dic = {}
        left = 0
        right = 0
        max_length = 0
        while right < len(s):
            letter = s[right]
            if letter not in dic:
                dic[letter] = 0
            dic[letter] += 1
            if len(dic) > k:
                # there are k + 1 letters in dic
                while left < right and len(dic) > k:
                    dic[s[left]] -= 1
                    if dic[s[left]] == 0:
                        # discard s[left] from the dictionary, if its frequency becomes zero
                        dic.pop(s[left])
                    left += 1
                # either left == right now or len(dic) == k at this position
            else:
                # whenever len(dic) <= k, we update max_length
                # this would relax many corner cases, such as right reach the end
                # we just do updating max_length inside the above while loop
                max_length = max(max_length, right - left + 1)
            right += 1

        return max_length
    

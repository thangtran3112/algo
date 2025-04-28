# https://leetcode.com/problems/minimum-window-substring/description/
"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
import math
from typing import Counter
import pytest

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        # keep a counter of character in t
        need = Counter(t)
        window = {}
        need_count = len(need)
        have = 0
        # we use have to keep track of total characters in need, which appears in window

        res = [-1, -1]
        res_len = math.inf   # invalid marker
        left = 0

        for right in range(len(s)):
            c = s[right]
            # increment the count of c in window hash map
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            # if condition is met, all letters in t has been appeared in window
            while have == need_count:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # sliding from the left, compress the window until t is not in s
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l: r + 1] if res_len != math.inf else ""

# === TEST CASES ===

@pytest.fixture
def solution():
    """Provides an instance of the Solution class."""
    return Solution()

# --- Basic Examples ---
def test_example1(solution):
    s = "ADOBECODEBANC"
    t = "ABC"
    expected = "BANC"
    assert solution.minWindow(s, t) == expected

def test_example2(solution):
    s = "a"
    t = "a"
    expected = "a"
    assert solution.minWindow(s, t) == expected

def test_example3(solution):
    s = "a"
    t = "aa"
    expected = ""
    assert solution.minWindow(s, t) == expected

# --- No Match Cases ---
def test_no_match_simple(solution):
    s = "abc"
    t = "d"
    expected = ""
    assert solution.minWindow(s, t) == expected

def test_no_match_partial(solution):
    s = "ADOBECODEBANC"
    t = "ABZ"
    expected = ""
    assert solution.minWindow(s, t) == expected

def test_no_match_t_longer_than_s(solution):
    s = "abc"
    t = "abcd"
    expected = ""
    assert solution.minWindow(s, t) == expected

# --- Duplicate Character Handling ---
def test_duplicates_in_t_found(solution):
    s = "aabbcc"
    t = "abc"
    expected = "abbc" # or "aabc" or "bbcc" - problem says unique, but let's test logic
    # Rerun with a case guaranteed by problem statement
    s = "aaaaaaaaaaaabbbbbcdddddddd"
    t = "abc"
    expected = "abbbbbc" # Smallest window containing a, b, c
    assert solution.minWindow(s, t) == expected # Re-evaluating based on implementation

    s = "abacaba"
    t = "aab"
    expected = "abacaba" # Need two 'a's and one 'b'
    # Let's trace:
    # a -> have=0, need={'a':2, 'b':1}
    # ab -> have=0
    # aba -> have=1 ('b' count met)
    # abac -> have=1
    # abaca -> have=1
    # abacab -> have=1
    # abacaba -> have=2 ('a' count met), window [0,6], len 7. res=[0,6], res_len=7
    # shrink left 'a': window={'b':1,'a':1,'c':1}, have=1. left=1
    # Result: s[0:7] = "abacaba" - Seems correct, let's try a better example
    s = "cabwefgewcwaefgcf"
    t = "cae"
    # c -> have=0
    # ca -> have=0
    # cab -> have=0
    # cabw -> have=0
    # cabwe -> have=1 ('e' met)
    # cabwef -> have=1
    # cabwefg -> have=1
    # cabwefge -> have=1
    # cabwefgew -> have=1
    # cabwefgewc -> have=2 ('c' met)
    # cabwefgewcw -> have=2
    # cabwefgewcwa -> have=3 ('a' met). Window [0,11], len 12. res=[0,11], res_len=12
    # shrink left 'c': window={'a':1,'b':1,'w':2,'e':1,'f':1,'g':1,'c':1}, have=2 ('c' unmet). left=1
    # ... eventually find "cwae"
    expected = "cwae"
    assert solution.minWindow(s, t) == expected


def test_duplicates_in_t_not_enough_in_s(solution):
    s = "banana"
    t = "baa" # Need two 'a's
    expected = "bana" # Contains 'b', 'a', 'n', 'a'
    assert solution.minWindow(s, t) == expected

    s = "abc"
    t = "aa"
    expected = ""
    assert solution.minWindow(s, t) == expected

def test_duplicates_in_s(solution):
    s = "aaabbbccc"
    t = "abc"
    expected = "abbbc" # Smallest window containing a, b, c
    assert solution.minWindow(s, t) == expected

# --- Edge Cases ---
def test_empty_s(solution):
    s = ""
    t = "a"
    expected = ""
    assert solution.minWindow(s, t) == expected

def test_empty_t(solution):
    s = "abc"
    t = ""
    expected = ""
    assert solution.minWindow(s, t) == expected

def test_s_equals_t(solution):
    s = "hello"
    t = "hello"
    expected = "hello"
    assert solution.minWindow(s, t) == expected

def test_window_at_beginning(solution):
    s = "bancadexyz"
    t = "abc"
    expected = "banc"
    assert solution.minWindow(s, t) == expected

def test_window_at_end(solution):
    s = "xyzadebanc"
    t = "abc"
    expected = "banc"
    assert solution.minWindow(s, t) == expected

def test_case_sensitivity_t(solution):
    s = "abcABC"
    t = "aB"
    expected = "abcAB" # Smallest window with 'a' and 'B'
    assert solution.minWindow(s, t) == expected

# --- Longer Strings ---
def test_longer_strings(solution):
    s = "thisisalongstringcontainingthetargetsubstringsomewhere"
    t = "target"
    expected = "target"
    assert solution.minWindow(s, t) == expected

    s = "aaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbcccccccccccccccccccccc"
    t = "abc"
    expected = "abbbbbbbbbbbbbbbbbbcccccccccccccccccccccc" # Should be just "abb...bc"
    # Let's rethink: need one 'a', one 'b', one 'c'
    # ...aaaaa'a'bbbbbb...'b'cccc... -> window starts shrinking from left 'a'
    # 'a'bbbbbb...'b'cccc...'c' -> window found
    # shrink left 'a': need 'a' again
    # move right until next 'a' (none)
    # shrink left 'b': need 'b' again
    # move right until next 'b' (none)
    # shrink left 'b': need 'b' again
    # ...
    # The window will eventually be the first 'a', the first 'b', and the first 'c'
    expected = "abbbbbbbbbbbbbbbbbbcccccccccccccccccccccc" # This covers the first a, first b, first c
    # Let's find indices: first 'a' at 16, first 'b' at 17, first 'c' at 35
    # Window "abb...c" starts at index 16, ends at 35. Length 35-16+1 = 20
    expected = s[16:35+1]
    assert solution.minWindow(s, t) == expected

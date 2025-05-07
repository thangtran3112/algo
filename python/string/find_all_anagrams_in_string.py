# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

# We can also use hash map. Python allow direct comparison of two hashmaps with ==
from typing import List
import pytest

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        # there are only 27 letters from 'a' to 'z'
        # we will keep a count array, where count[0] = frequency of 'a'
        # count[26] is the frequency of [z]

        def getIndex(ch: str):
            return ord(ch) - ord('a')

        max_letters = getIndex('z') + 1  # should be 27
        p_count = [0] * max_letters
        for ch in p:
            p_count[getIndex(ch)] += 1

        m = len(p)
        n = len(s)
        result = []
        window_count = [0] * max_letters
        # calculate the first window
        for i in range(m):
            letter = s[i]
            window_count[getIndex(letter)] += 1
        # python allow direct array comparison
        if window_count == p_count:
            result.append(0)

        # sliding window, and update the window_count properly
        for left in range(1, n - m + 1):
            prev_letter = s[left - 1]
            right = left + m - 1
            window_count[getIndex(prev_letter)] -= 1
            window_count[getIndex(s[right])] += 1
            if window_count == p_count:
                result.append(left)
        return result

# === TEST CASES ===

@pytest.fixture
def solution_instance():
    return Solution()

def test_example1(solution_instance):
    s = "cbaebabacd"
    p = "abc"
    expected = [0, 6]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_example2(solution_instance):
    s = "abab"
    p = "ab"
    expected = [0, 1, 2]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_p_longer_than_s(solution_instance):
    s = "a"
    p = "ab"
    expected = []
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_no_anagrams_found(solution_instance):
    s = "abc"
    p = "d"
    expected = []
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

    s = "abcdef"
    p = "xyz"
    expected = []
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_s_and_p_are_anagrams(solution_instance):
    s = "abc"
    p = "cba"
    expected = [0]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_s_and_p_are_identical(solution_instance):
    s = "abc"
    p = "abc"
    expected = [0]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_p_has_duplicate_characters(solution_instance):
    s = "abacaba"
    p = "aab" # "aba" is an anagram
    expected = [0, 4] # "aba" at 0, "aba" at 4
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

    s = "baa"
    p = "aa"
    expected = [1]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_s_has_duplicate_characters(solution_instance):
    s = "aaabaaa"
    p = "aab"
    expected = [0, 1, 4, 5] # "aaa" is not "aab". "aab" is not present.
                            # "aa" at 0, "aa" at 1, "aa" at 4, "aa" at 5
                            # If p="aab", then s[0:3]="aaa" (no), s[1:4]="aab" (yes, index 1)
                            # s[2:5]="aba" (yes, index 2), s[3:6]="baa" (yes, index 3)
                            # s[4:7]="aaa" (no)
    # Let's re-evaluate for s = "aaabaaa", p = "aab"
    # p_count: a=2, b=1
    # s[0:3]="aaa" -> a=3, b=0. No.
    # s[1:4]="aab" -> a=2, b=1. Yes. Index 1.
    # s[2:5]="aba" -> a=2, b=1. Yes. Index 2.
    # s[3:6]="baa" -> a=2, b=1. Yes. Index 3.
    # s[4:7]="aaa" -> a=3, b=0. No.
    expected = [1, 2, 3]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)


def test_s_is_just_p(solution_instance):
    s = "abcde"
    p = "abcde"
    expected = [0]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_all_same_characters_in_p(solution_instance):
    s = "aaabaaa"
    p = "aaa"
    expected = [0, 4]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_all_same_characters_in_s_and_p(solution_instance):
    s = "aaaaa"
    p = "aa"
    expected = [0, 1, 2, 3]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

    s = "bbbbb"
    p = "bbb"
    expected = [0, 1, 2]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_p_is_single_character(solution_instance):
    s = "banana"
    p = "a"
    expected = [1, 3, 5]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

    s = "zzzz"
    p = "z"
    expected = [0, 1, 2, 3]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_s_is_single_character_match(solution_instance):
    s = "a"
    p = "a"
    expected = [0]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_s_is_single_character_no_match(solution_instance):
    s = "b"
    p = "a"
    expected = []
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_overlapping_anagrams(solution_instance):
    s = "ababa"
    p = "aba"
    # "aba" at 0
    # "bab" at 1 (no)
    # "aba" at 2
    expected = [0, 2]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_long_p_no_match(solution_instance):
    s = "abcdefghijklm"
    p = "nopqrst"
    expected = []
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_s_ends_with_anagram(solution_instance):
    s = "teststringabc"
    p = "cba"
    expected = [10]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_s_starts_with_anagram(solution_instance):
    s = "abcteststring"
    p = "bca"
    expected = [0]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

def test_p_contains_all_unique_chars_s_has_duplicates(solution_instance):
    s = "abccba"
    p = "abc"
    # "abc" at 0
    # "bcc" at 1 (no)
    # "ccb" at 2 (no)
    # "cba" at 3
    expected = [0,3]
    assert sorted(solution_instance.findAnagrams(s, p)) == sorted(expected)

# To run these tests (if they were in a separate file like test_find_all_anagrams.py):
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest
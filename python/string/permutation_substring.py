# https://leetcode.com/problems/permutation-in-string/description/
"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        # create a set of frequency characters in s1
        s1_count = Counter(s1)
        left = 0
        window_count = Counter()
        # build the initial sliding window
        for i in range(len(s1)):
            window_count[s2[i]] += 1
        # check if the first window has the permutation of s1
        if window_count == s1_count:
            return True
        # start interating from the second sliding windows, and update letter count
        # Input: s1 = "abc" len=3, s2 = "eibdoaoo" len=8, left <= 8 - 3 = 5 
        for left in range(1, len(s2) - len(s1) + 1):
            right = left + len(s1) - 1
            window_count[s2[right]] += 1
            # decrement the count of previous position at left - 1
            window_count[s2[left - 1]] -= 1
            if window_count == s1_count:
                return True

        return False
    
import pytest  # noqa: E402

@pytest.fixture
def solution_instance():
    return Solution()

def test_example1(solution_instance):
    """Input: s1 = "ab", s2 = "eidbaooo" -> Output: True"""
    s1 = "ab"
    s2 = "eidbaooo"
    assert solution_instance.checkInclusion(s1, s2) is True

def test_example2(solution_instance):
    """Input: s1 = "ab", s2 = "eidboaoo" -> Output: False"""
    s1 = "ab"
    s2 = "eidboaoo"
    assert solution_instance.checkInclusion(s1, s2) is False

def test_s1_longer_than_s2(solution_instance):
    """Input: s1 = "abc", s2 = "ab" -> Output: False"""
    s1 = "abc"
    s2 = "ab"
    assert solution_instance.checkInclusion(s1, s2) is False

def test_exact_match(solution_instance):
    """Input: s1 = "abc", s2 = "abc" -> Output: True"""
    s1 = "abc"
    s2 = "abc"
    assert solution_instance.checkInclusion(s1, s2) is True

def test_permutation_at_start(solution_instance):
    """Input: s1 = "abc", s2 = "cbadef" -> Output: True"""
    s1 = "abc"
    s2 = "cbadef"
    assert solution_instance.checkInclusion(s1, s2) is True

def test_permutation_at_end(solution_instance):
    """Input: s1 = "abc", s2 = "defcba" -> Output: True"""
    s1 = "abc"
    s2 = "defcba"
    assert solution_instance.checkInclusion(s1, s2) is True

def test_no_permutation(solution_instance):
    """Input: s1 = "abc", s2 = "defghi" -> Output: False"""
    s1 = "abc"
    s2 = "defghi"
    assert solution_instance.checkInclusion(s1, s2) is False

def test_repeated_characters(solution_instance):
    """Input: s1 = "aabb", s2 = "eidbaabboo" -> Output: True"""
    s1 = "aabb"
    s2 = "eidbaabboo"
    assert solution_instance.checkInclusion(s1, s2) is True

def test_single_character_match(solution_instance):
    """Input: s1 = "a", s2 = "a" -> Output: True"""
    s1 = "a"
    s2 = "a"
    assert solution_instance.checkInclusion(s1, s2) is True

def test_single_character_no_match(solution_instance):
    """Input: s1 = "a", s2 = "b" -> Output: False"""
    s1 = "a"
    s2 = "b"
    assert solution_instance.checkInclusion(s1, s2) is False

def test_empty_s2(solution_instance):
    """Input: s1 = "abc", s2 = "" -> Output: False"""
    s1 = "abc"
    s2 = ""
    assert solution_instance.checkInclusion(s1, s2) is False

def test_large_input_with_match(solution_instance):
    """Test with large input where a match exists."""
    s1 = "abc"
    s2 = "a" * 10000 + "bca" + "d" * 10000
    assert solution_instance.checkInclusion(s1, s2) is True

def test_large_input_no_match(solution_instance):
    """Test with large input where no match exists."""
    s1 = "abc"
    s2 = "a" * 10000 + "d" * 10000
    assert solution_instance.checkInclusion(s1, s2) is False

# To run these tests:
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest
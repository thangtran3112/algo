# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0

        my_map = defaultdict(int)
        temp = ''
        max_length = 0
        while end < len(s):
            ch = s[end]
            temp += ch
            my_map[ch] += 1

            # case (abcd)c -> keep dropping left until resetting to "dc"
            while my_map[ch] > 1:
                my_map[s[start]] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
            end += 1

        return max_length
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Fixture to provide a solution instance."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    s = "abcabcbb"
    expected = 3  # "abc"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_example2(solution):
    """Test Example 2 from the problem description."""
    s = "bbbbb"
    expected = 1  # "b"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_example3(solution):
    """Test Example 3 from the problem description."""
    s = "pwwkew"
    expected = 3  # "wke"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_empty_string(solution):
    """Test with an empty string."""
    s = ""
    expected = 0
    assert solution.lengthOfLongestSubstring(s) == expected

def test_single_character(solution):
    """Test with a single character."""
    s = "a"
    expected = 1  # "a"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_all_unique_characters(solution):
    """Test with all unique characters."""
    s = "abcdefg"
    expected = 7  # "abcdefg"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_repeated_sequence(solution):
    """Test with repeated sequence."""
    s = "abcdabcd"
    expected = 4  # "abcd"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_substring_at_end(solution):
    """Test where longest substring is at the end."""
    s = "abcdefabcdefghi"
    expected = 9  # "defabcghi"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_substring_at_beginning(solution):
    """Test where longest substring is at the beginning."""
    s = "abcdefghiabcde"
    expected = 9  # "abcdefghi"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_with_spaces(solution):
    """Test with spaces."""
    s = "hello world"
    expected = 6  # "hello w" or " world"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_with_digits(solution):
    """Test with digits."""
    s = "abc123def"
    expected = 9  # "abc123def"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_with_special_characters(solution):
    """Test with special characters."""
    s = "a!b@c#d$"
    expected = 8  # "a!b@c#d$"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_alternating_characters(solution):
    """Test with alternating characters."""
    s = "abababa"
    expected = 2  # "ab"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_complex_pattern(solution):
    """Test with complex pattern."""
    s = "abba"
    expected = 2  # "ab" or "ba"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_long_string(solution):
    """Test with a long string."""
    s = "a" * 10000 + "b" * 10000
    expected = 2  # "ab"
    assert solution.lengthOfLongestSubstring(s) == expected

def test_unicode_characters(solution):
    """Test with Unicode characters."""
    s = "你好世界hello"
    expected = 7  # "你好世界hel" or "世界hello"
    assert solution.lengthOfLongestSubstring(s) == expected
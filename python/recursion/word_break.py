from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        refined = s + '$'  # relax edge case handling
        # check if s[i:] is segmentable

        @lru_cache(maxsize=None)
        def check(i):
            # base case: empty string is segmentable
            if i == len(s):
                return True
            # for all substring from i, check if they are a word in wordDict
            for end in range(i, len(s)):
                if refined[i:end + 1] in wordSet:
                    if check(end + 1):
                        return True
            return False


        return check(0)


# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Fixture to provide a Solution instance."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    s = "leetcode"
    wordDict = ["leet", "code"]
    assert solution.wordBreak(s, wordDict) is True

def test_example2(solution):
    """Test Example 2 from the problem description."""
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    assert solution.wordBreak(s, wordDict) is True

def test_example3(solution):
    """Test Example 3 from the problem description."""
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    assert solution.wordBreak(s, wordDict) is False

def test_empty_string(solution):
    """Test with empty string."""
    s = ""
    wordDict = ["a", "b"]
    assert solution.wordBreak(s, wordDict) is True  # Empty string should be considered breakable

def test_single_character(solution):
    """Test with a single character."""
    s = "a"
    wordDict = ["a"]
    assert solution.wordBreak(s, wordDict) is True

def test__possible_break(solution):
    """Test string that cannot be broken according to wordDict."""
    s = "aaaaaaa"
    wordDict = ["aaa", "aaaa"]
    assert solution.wordBreak(s, wordDict) is True

def test_multiple_ways_to_break(solution):
    """Test string that can be broken in multiple ways."""
    s = "abcd"
    wordDict = ["a", "abc", "b", "cd", "d"]
    assert solution.wordBreak(s, wordDict) is True

def test_overlapping_words(solution):
    """Test with overlapping words in wordDict."""
    s = "abcdef"
    wordDict = ["ab", "cd", "abcd", "ef"]
    assert solution.wordBreak(s, wordDict) is True

def test_repeated_words(solution):
    """Test with repeated words in the string."""
    s = "ababab"
    wordDict = ["ab", "aba"]
    assert solution.wordBreak(s, wordDict) is True

def test_long_string(solution):
    """Test with a longer string."""
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"  # 70 'a's + 'b'
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa"]
    assert solution.wordBreak(s, wordDict) is False  # Cannot form 'b' at the end

def test_dictionary_with_empty_string(solution):
    """Test wordDict containing an empty string."""
    s = "abc"
    wordDict = ["", "a", "b", "c"]
    # This depends on the problem definition, but generally an empty string in wordDict shouldn't change the result
    assert solution.wordBreak(s, wordDict) is True

def test_substring_vs_full_string(solution):
    """Test where wordDict contains substrings but not the full required string."""
    s = "abc"
    wordDict = ["a", "b", "c"]
    assert solution.wordBreak(s, wordDict) is True

def test_case_sensitivity(solution):
    """Test case sensitivity."""
    s = "Abc"
    wordDict = ["abc", "Abc", "ABC"]
    assert solution.wordBreak(s, wordDict) is True
    
    s = "abc"
    wordDict = ["Abc"]
    assert solution.wordBreak(s, wordDict) is False

def test_special_characters(solution):
    """Test with special characters."""
    s = "ab-cd"
    wordDict = ["ab-", "cd"]
    assert solution.wordBreak(s, wordDict) is True
    
    s = "ab-cd"
    wordDict = ["ab", "-", "cd"]
    assert solution.wordBreak(s, wordDict) is True

def test_maximum_constraints(solution):
    """Test with maximum length constraints."""
    # Create a string of length 300 (max constraint)
    s = "a" * 300
    wordDict = ["a", "aa", "aaa"]
    assert solution.wordBreak(s, wordDict) is True
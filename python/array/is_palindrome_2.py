# https://leetcode.com/problems/valid-palindrome-ii/description/
"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""
class Solution:
    # s = 'abbxa'. We use 2 pointers to iterate and compare
    # if s[left] == s[right], check the inner substring
    # if s[left] != s[right], palindrome starts diverging
    # In this case, we try to delete s[left] and verify if it is a palindrome
    # In this case, we try to delete s[right] and verify if it is a palindrome
    def validPalindrome(self, s: str) -> bool:
        # is normal palindrome within a range [start, end]
        def is_normal_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # start diverging
                # case1: delete left and check
                case1 = is_normal_palindrome(left + 1, right)
                if case1:
                    return True
                else:
                    return is_normal_palindrome(left, right - 1)

        # if the codes comes here, s is a palindrome itself
        return True

import pytest  # noqa: E402

@pytest.fixture
def solution_instance():
    return Solution()

def test_example1(solution_instance):
    """Input: s = "aba" -> Output: True"""
    s = "aba"
    assert solution_instance.validPalindrome(s) is True

def test_example2(solution_instance):
    """Input: s = "abca" -> Output: True"""
    s = "abca"
    assert solution_instance.validPalindrome(s) is True

def test_example3(solution_instance):
    """Input: s = "abc" -> Output: False"""
    s = "abc"
    assert solution_instance.validPalindrome(s) is False

def test_single_character(solution_instance):
    """Input: s = "a" -> Output: True"""
    s = "a"
    assert solution_instance.validPalindrome(s) is True

def test_two_identical_characters(solution_instance):
    """Input: s = "aa" -> Output: True"""
    s = "aa"
    assert solution_instance.validPalindrome(s) is True

def test_two_different_characters(solution_instance):
    """Input: s = "ab" -> Output: True"""
    s = "ab"
    assert solution_instance.validPalindrome(s) is True

def test_long_palindrome(solution_instance):
    """Input: s = "racecar" -> Output: True"""
    s = "racecar"
    assert solution_instance.validPalindrome(s) is True

def test_long_non_palindrome(solution_instance):
    """Input: s = "abcdef" -> Output: False"""
    s = "abcdef"
    assert solution_instance.validPalindrome(s) is False

def test_palindrome_with_one_removal(solution_instance):
    """Input: s = "abccba" -> Output: True"""
    s = "abccba"
    assert solution_instance.validPalindrome(s) is True

def test_non_palindrome_with_no_possible_removal(solution_instance):
    """Input: s = "abcdefg" -> Output: False"""
    s = "abcdefg"
    assert solution_instance.validPalindrome(s) is False

def test_empty_string(solution_instance):
    """Input: s = "" -> Output: True"""
    s = ""
    assert solution_instance.validPalindrome(s) is True

def test_large_palindrome(solution_instance):
    """Test with a large palindrome string."""
    s = "a" * 10**5
    assert solution_instance.validPalindrome(s) is True

def test_large_non_palindrome(solution_instance):
    """Test with a large non-palindrome string."""
    s = "a" * (10**5 - 1) + "b"
    assert solution_instance.validPalindrome(s) is True

def test_large_non_palindrome_no_removal_possible(solution_instance):
    """Test with a large non-palindrome string where no removal makes it valid."""
    s = "a" * (10**5 - 2) + "bc"
    assert solution_instance.validPalindrome(s) is False

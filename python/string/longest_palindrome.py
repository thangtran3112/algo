# https://leetcode.com/problems/longest-palindromic-substring/description/
"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class SolutionInterative:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start:start + length]

        return ""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand_around_center(left: int, right: int) -> tuple:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (left + 1, right - 1)  # return valid window

        for i in range(len(s)):
            # Odd-length palindromes
            l1, r1 = expand_around_center(i, i)
            # Even-length palindromes
            l2, r2 = expand_around_center(i, i + 1)

            # Update the longest one found
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[Solution, SolutionInterative],
               ids=["Expand", "Iterative"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    s = "babad"
    result = solution_instance.longestPalindrome(s)
    assert result in ["bab", "aba"]  # both are valid answers

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    s = "cbbd"
    expected = "bb"
    assert solution_instance.longestPalindrome(s) == expected

def test_empty_string(solution_instance):
    """Test with empty string."""
    s = ""
    expected = ""
    assert solution_instance.longestPalindrome(s) == expected

def test_single_char(solution_instance):
    """Test with single character."""
    s = "a"
    expected = "a"
    assert solution_instance.longestPalindrome(s) == expected

def test_all_same_chars(solution_instance):
    """Test string with all same characters."""
    s = "aaaa"
    expected = "aaaa"
    assert solution_instance.longestPalindrome(s) == expected

def test_no_palindrome_longer_than_one(solution_instance):
    """Test string with no palindrome longer than one character."""
    s = "abcd"
    result = solution_instance.longestPalindrome(s)
    assert len(result) == 1  # any single character is valid

def test_odd_length_palindrome(solution_instance):
    """Test string with odd length palindrome."""
    s = "xababa"
    expected = "ababa"
    assert solution_instance.longestPalindrome(s) == expected

def test_even_length_palindrome(solution_instance):
    """Test string with even length palindrome."""
    s = "xabbay"
    expected = "abba"
    assert solution_instance.longestPalindrome(s) == expected

def test_multiple_palindromes(solution_instance):
    """Test string with multiple palindromes of same length."""
    s = "aabbaa"
    expected = "aabbaa"
    assert solution_instance.longestPalindrome(s) == expected

def test_palindrome_at_start(solution_instance):
    """Test palindrome at start of string."""
    s = "aaaabcd"
    expected = "aaaa"
    assert solution_instance.longestPalindrome(s) == expected

def test_palindrome_at_end(solution_instance):
    """Test palindrome at end of string."""
    s = "abcdaaaa"
    expected = "aaaa"
    assert solution_instance.longestPalindrome(s) == expected

def test_with_numbers(solution_instance):
    """Test string containing numbers."""
    s = "12321abc"
    expected = "12321"
    assert solution_instance.longestPalindrome(s) == expected

def test_long_string(solution_instance):
    """Test with a longer string."""
    s = "a" * 500 + "b" + "a" * 500  # 1001 characters
    expected = s  # whole string is a palindrome
    assert solution_instance.longestPalindrome(s) == expected

def test_multiple_palindromes_different_lengths(solution_instance):
    """Test string with multiple palindromes of different lengths."""
    s = "abbaxxababababa"
    expected = "ababababa"  # longest one
    assert solution_instance.longestPalindrome(s) == expected

def test_overlapping_palindromes(solution_instance):
    """Test string with overlapping palindromes."""
    s = "aabaabaa"
    expected = "aabaabaa"
    assert solution_instance.longestPalindrome(s) == expected
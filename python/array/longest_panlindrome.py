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

import pytest


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

@pytest.fixture
def solution():
    return Solution()

def test_basic_odd_palindrome(solution):
    assert solution.longestPalindrome("babad") in ["bab", "aba"]

def test_basic_even_palindrome(solution):
    assert solution.longestPalindrome("cbbd") == "bb"

def test_single_char(solution):
    assert solution.longestPalindrome("a") == "a"

def test_two_same_chars(solution):
    assert solution.longestPalindrome("aa") == "aa"

def test_two_different_chars(solution):
    assert solution.longestPalindrome("ab") in ["a", "b"]

def test_all_same_chars(solution):
    assert solution.longestPalindrome("aaaa") == "aaaa"

def test_empty_string(solution):
    assert solution.longestPalindrome("") == ""

def test_long_palindrome_odd(solution):
    assert solution.longestPalindrome("racecar") == "racecar"

def test_long_palindrome_even(solution):
    assert solution.longestPalindrome("abccba") == "abccba"

def test_multiple_palindromes(solution):
    # Should return the first occurrence of longest palindrome
    assert solution.longestPalindrome("abaaba") in ["abaaba"]

def test_case_sensitive(solution):
    assert solution.longestPalindrome("Aa") in ["A", "a"]

def test_with_spaces(solution):
    assert solution.longestPalindrome("race car") == "r"

def test_special_characters(solution):
    assert solution.longestPalindrome("a#a") == "a#a"

def test_numbers_and_letters(solution):
    assert solution.longestPalindrome("a1b2b1a") == "a1b2b1a"

def test_overlapping_palindromes(solution):
    # "aaaa" is valid but "aaa" overlaps with it
    assert solution.longestPalindrome("aaaa") == "aaaa"

def test_palindrome_at_start(solution):
    assert solution.longestPalindrome("abbcd") == "bb"

def test_palindrome_at_end(solution):
    assert solution.longestPalindrome("cdbba") == "bb"

def test_multiple_non_overlapping_palindromes(solution):
    # Should return any of the longest palindromes
    assert solution.longestPalindrome("aabbaa") == "aabbaa"

def test_alternating_characters(solution):
    assert solution.longestPalindrome("abababa") == "abababa"

def test_complex_string(solution):
    test_str = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    result = solution.longestPalindrome(test_str)
    assert len(result) == 7  # The longest palindrome in this string is "ranynar" 
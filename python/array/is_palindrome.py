# https://leetcode.com/problems/valid-palindrome/description/
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
import pytest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1

        return True
    
# === TEST CASES ===

@pytest.fixture
def solution():
    """Provides an instance of the Solution class."""
    return Solution()

# --- Basic Palindromes ---
def test_simple_palindrome_lower(solution):
    assert solution.isPalindrome("madam") is True

def test_simple_palindrome_mixed(solution):
    assert solution.isPalindrome("Level") is True

def test_palindrome_with_numbers(solution):
    assert solution.isPalindrome("121") is True

def test_palindrome_alphanumeric(solution):
    assert solution.isPalindrome("A1b2b1A") is True

# --- Basic Non-Palindromes ---
def test_simple_non_palindrome(solution):
    assert solution.isPalindrome("hello") is False

def test_non_palindrome_numbers(solution):
    assert solution.isPalindrome("123") is False

def test_non_palindrome_alphanumeric(solution):
    assert solution.isPalindrome("a1b2c") is False

# --- Handling Non-Alphanumeric Characters ---
def test_example1(solution):
    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True

def test_example2(solution):
    assert solution.isPalindrome("race a car") is False

def test_with_punctuation(solution):
    assert solution.isPalindrome("Was it a car or a cat I saw?") is True

def test_with_various_symbols(solution):
    assert solution.isPalindrome("`./;[].=-~!@#$%^&*()_+{}|:<>?1a1?<>|{}_+)(*&^%$#@!~-=`.;[]/'") is True

def test_non_palindrome_with_symbols(solution):
    assert solution.isPalindrome("No 'x' in Nixon?") is True

# --- Edge Cases ---
def test_example3_empty_string(solution):
    assert solution.isPalindrome("") is True

def test_single_char_alpha(solution):
    assert solution.isPalindrome("a") is True

def test_single_char_num(solution):
    assert solution.isPalindrome("5") is True

def test_single_char_non_alnum(solution):
    assert solution.isPalindrome(".") is True # Becomes empty string ""

def test_all_non_alnum(solution):
    assert solution.isPalindrome(" ,.!?# ") is True # Becomes empty string ""

def test_two_same_chars(solution):
    assert solution.isPalindrome("aa") is True

def test_two_different_chars(solution):
    assert solution.isPalindrome("ab") is False

def test_two_same_chars_case(solution):
    assert solution.isPalindrome("aA") is True

def test_two_chars_with_space(solution):
    assert solution.isPalindrome("a a") is True

def test_long_palindrome(solution):
    s = "abcdefghijklmnopqrstuvwxyzzyxwvu tsrqponmlkjihgfedcba" # Space in middle
    assert solution.isPalindrome(s) is True

def test_long_non_palindrome(solution):
    s = "abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz"
    assert solution.isPalindrome(s) is False

def test_numbers_and_spaces(solution):
    assert solution.isPalindrome("1 2 3 2 1") is True

def test_numbers_and_letters_mixed(solution):
    assert solution.isPalindrome("Race car 1") is False # racecar1
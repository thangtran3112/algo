"""
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
 

Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
 

Constraints:

0 <= s.length, t.length <= 104
s and t consist of lowercase letters, uppercase letters, and digits.
"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return False
        if abs(len(s) - len(t)) > 1:
            return False
        if len(s) == 0 or len(t) == 0:
            return True

        # abcde  -  abcfde, notice the first character d-f, where the two string diverging
        # abcde  -  abmde, the first character c-m, where the two string diverging

        # case 1: replacement check, when len(s) == len(t)
        if len(s) == len(t):
            i = 0
            replacement = 0
            while i < len(s):
                if s[i] != t[i]:
                    replacement = 1
                    break
                i += 1

            # Note: in case of 'c' vs 'c', replacement = 0, so the result is False
            return s[i + 1:] == t[i + 1:] if replacement == 1 else False

        if abs(len(s) - len(t)) != 1:
            return False

        # case2: deletion check, when s and t is 1 character differnt in length
        big_str = s if len(s) > len(t) else t
        small_str = t if len(t) < len(s) else s

        i = 0
        while i < len(small_str):
            if small_str[i] != big_str[i]:
                break
            i += 1
        return big_str[i + 1:] == small_str[i:]
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Provides an instance of the Solution class."""
    return Solution()

# --- Basic Examples ---
def test_examples(solution):
    """Test the examples from the problem description."""
    assert solution.isOneEditDistance("ab", "acb") == True  # Insert 'c'
    assert solution.isOneEditDistance("", "") == False  # Cannot get t from s in one step

# --- Insertion Tests ---
def test_insertions(solution):
    """Test cases where insertion is needed."""
    assert solution.isOneEditDistance("abc", "abcd") == True  # Insert 'd' at end
    assert solution.isOneEditDistance("abc", "dabc") == True  # Insert 'd' at beginning
    assert solution.isOneEditDistance("abc", "abdc") == True  # Insert 'd' in middle

# --- Deletion Tests ---
def test_deletions(solution):
    """Test cases where deletion is needed."""
    assert solution.isOneEditDistance("abcd", "abc") == True  # Delete 'd' at end
    assert solution.isOneEditDistance("abcd", "bcd") == True  # Delete 'a' at beginning
    assert solution.isOneEditDistance("abcd", "abd") == True  # Delete 'c' in middle

# --- Replacement Tests ---
def test_replacements(solution):
    """Test cases where replacement is needed."""
    assert solution.isOneEditDistance("abcd", "abce") == True  # Replace 'd' with 'e'
    assert solution.isOneEditDistance("xbcd", "abcd") == True  # Replace 'x' with 'a'
    assert solution.isOneEditDistance("abxd", "abcd") == True  # Replace 'x' with 'c'

# --- Edge Cases ---
def test_empty_strings(solution):
    """Test with empty strings."""
    assert solution.isOneEditDistance("", "a") == True  # Insert 'a'
    assert solution.isOneEditDistance("a", "") == True  # Delete 'a'
    assert solution.isOneEditDistance("", "") == False  # Not one edit apart

def test_identical_strings(solution):
    """Test with identical strings."""
    assert solution.isOneEditDistance("abc", "abc") == False  # Already identical
    assert solution.isOneEditDistance("x", "x") == False  # Already identical

def test_long_difference(solution):
    """Test with strings that differ by more than one edit."""
    assert solution.isOneEditDistance("abc", "abcde") == False  # More than one edit
    assert solution.isOneEditDistance("abc", "def") == False  # More than one edit

# --- Special Cases ---
def test_single_character_strings(solution):
    """Test with single character strings."""
    assert solution.isOneEditDistance("a", "b") == True  # Replace 'a' with 'b'
    assert solution.isOneEditDistance("a", "ab") == True  # Insert 'b'
    assert solution.isOneEditDistance("ab", "a") == True  # Delete 'b'

def test_different_character_types(solution):
    """Test with different character types (digits, uppercase)."""
    assert solution.isOneEditDistance("abc", "ab1") == True  # Replace 'c' with '1'
    assert solution.isOneEditDistance("abc", "abC") == True  # Replace 'c' with 'C'
    assert solution.isOneEditDistance("123", "1234") == True  # Insert '4'

def test_first_character_diff(solution):
    """Test with differences in the first character."""
    assert solution.isOneEditDistance("abc", "xbc") == True  # Replace 'a' with 'x'
    assert solution.isOneEditDistance("abc", "bc") == True  # Delete 'a'
    assert solution.isOneEditDistance("bc", "abc") == True  # Insert 'a'

def test_last_character_diff(solution):
    """Test with differences in the last character."""
    assert solution.isOneEditDistance("abc", "abx") == True  # Replace 'c' with 'x'
    assert solution.isOneEditDistance("abc", "ab") == True  # Delete 'c'
    assert solution.isOneEditDistance("ab", "abc") == True  # Insert 'c'

def test_multiple_edits_needed(solution):
    """Test cases where multiple edits would be needed."""
    assert solution.isOneEditDistance("abc", "axy") == False  # Need to replace 'b' and 'c'
    assert solution.isOneEditDistance("abc", "xyz") == False  # Need to replace all characters
    assert solution.isOneEditDistance("abc", "abcde") == False  # Need to insert 'd' and 'e'

def test_tricky_cases(solution):
    """Test some tricky edge cases."""
    assert solution.isOneEditDistance("", "a") == True  # Empty to single character
    assert solution.isOneEditDistance("a", "ab") == True  # Single character to two
    assert solution.isOneEditDistance("abcdefg", "abcdefh") == True  # Difference at end
    assert solution.isOneEditDistance("abcdefg", "abcdxfg") == True  # Difference in middle
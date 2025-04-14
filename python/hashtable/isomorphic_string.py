# https://leetcode.com/problems/isomorphic-strings/description/
"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            s_letter = s[i]
            t_letter = t[i]

            if s_letter in s_map:
                # s_letter in s_map, but t_letter is not in t_map
                if t_letter not in t_map:
                    return False
                else:
                    # s_letter and t_letter are both present in s_map and t_map
                    if s_map[s_letter] != t_letter and t_map[t_letter] != s_letter:
                        return False
            else:
                # s_letter not in s_map, but t_letter in t_map
                if t_letter in t_map:
                    return False
                else:
                    # s_letter and t_letter are not in s_map and t_map
                    s_map[s_letter] = t_letter
                    t_map[t_letter] = s_letter

        return True
    
# TEST CASES

import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Fixture that provides the solution implementation."""
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    s = "egg"
    t = "add"
    assert solution.isIsomorphic(s, t) is True

def test_example_2(solution):
    """Test the second example from the problem statement."""
    s = "foo"
    t = "bar"
    assert solution.isIsomorphic(s, t) is False

def test_example_3(solution):
    """Test the third example from the problem statement."""
    s = "paper"
    t = "title"
    assert solution.isIsomorphic(s, t) is True

def test_empty_strings(solution):
    """Test with empty strings."""
    s = ""
    t = ""
    assert solution.isIsomorphic(s, t) is True

def test_single_character(solution):
    """Test with single character strings."""
    s = "a"
    t = "b"
    assert solution.isIsomorphic(s, t) is True
    
    s = "c"
    t = "c"
    assert solution.isIsomorphic(s, t) is True

def test_repeated_characters_same_pattern(solution):
    """Test with repeated characters having the same pattern."""
    s = "abcabcabc"
    t = "xyzxyzxyz"
    assert solution.isIsomorphic(s, t) is True

def test_repeated_characters_different_pattern(solution):
    """Test with repeated characters having different patterns."""
    s = "abcabc"
    t = "xyzwvu"
    assert solution.isIsomorphic(s, t) is False

def test_different_length_strings(solution):
    """Test with strings of different lengths (should not happen per constraints)."""
    s = "abc"
    t = "xy"
    # This should raise an IndexError or handle differently based on implementation
    try:
        result = solution.isIsomorphic(s, t)
        # If it doesn't raise, it should return False
        assert result is False
    except IndexError:
        # If it raises an IndexError, that's expected behavior
        pass

def test_one_to_many_mapping(solution):
    """Test with a one-to-many mapping which should fail."""
    s = "abc"
    t = "abb"
    assert solution.isIsomorphic(s, t) is False

def test_many_to_one_mapping(solution):
    """Test with a many-to-one mapping which should fail."""
    s = "abb"
    t = "abc"
    assert solution.isIsomorphic(s, t) is False

def test_complex_isomorphic(solution):
    """Test with a more complex isomorphic pattern."""
    s = "abcdefghijklmnopqrstuvwxyz"
    t = "zyxwvutsrqponmlkjihgfedcba"
    assert solution.isIsomorphic(s, t) is True

def test_different_ascii_ranges(solution):
    """Test with characters from different ASCII ranges."""
    s = "ab12!@"
    t = "cd34#$"
    assert solution.isIsomorphic(s, t) is True

def test_same_character_different_mappings(solution):
    """Test where the same character would need different mappings."""
    s = "abca"
    t = "xyzx"
    assert solution.isIsomorphic(s, t) is True
    
    s = "abca"
    t = "xyzy"
    assert solution.isIsomorphic(s, t) is False

def test_large_strings(solution):
    """Test with large strings approaching the constraint limit."""
    # Create strings of length 10000 (less than 5*10^4)
    s = "ab" * 5000
    t = "cd" * 5000
    assert solution.isIsomorphic(s, t) is True
    
    s = "ab" * 5000
    t = "cd" * 4999 + "ce"
    assert solution.isIsomorphic(s, t) is False

def test_string_with_spaces(solution):
    """Test with strings containing spaces."""
    s = "a b c"
    t = "x y z"
    assert solution.isIsomorphic(s, t) is True
    
    s = "a  c"
    t = "x  z"
    assert solution.isIsomorphic(s, t) is True

def test_edge_case_all_same_character(solution):
    """Test with strings containing all the same character."""
    s = "aaaaa"
    t = "bbbbb"
    assert solution.isIsomorphic(s, t) is True
    
    s = "aaaaa"
    t = "bcdef"
    assert solution.isIsomorphic(s, t) is False
# https://leetcode.com/problems/valid-word-abbreviation/description/
"""
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
 

Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.
"""
import pytest
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        left = 0
        right = 0
        while left < len(word) and right < len(abbr):
            if abbr[right].isdigit():
                if abbr[right] == '0':
                    # leading zero
                    return False
                else:
                    init_right = right
                    # scan for the whole number, instead of just the first digit
                    while right < len(abbr) and abbr[right].isdigit():
                        right += 1
                    jump_str = abbr[init_right:right]
                    jump = int(jump_str)
                    # early exit to avoid unnecessary calculation, if jump would cross limit
                    if jump > len(word) - left:
                        return False
                    for _ in range(jump):
                        left += 1
            else:
                # not a number, we must compare letter to letter
                if word[left] != abbr[right]:
                    return False
                left += 1
                right += 1

        if left != len(word) or right != len(abbr):
            return False
        else:
            return True

@pytest.fixture
def solution_instance():
    return Solution()

def test_example1(solution_instance):
    """Input: word = "internationalization", abbr = "i12iz4n" -> Output: True"""
    word = "internationalization"
    abbr = "i12iz4n"
    assert solution_instance.validWordAbbreviation(word, abbr) is True

def test_example2(solution_instance):
    """Input: word = "apple", abbr = "a2e" -> Output: False"""
    word = "apple"
    abbr = "a2e"
    assert solution_instance.validWordAbbreviation(word, abbr) is False

def test_adjacent_abbreviations(solution_instance):
    """Test invalid case with adjacent abbreviations: word = "substitution", abbr = "s55n" -> Output: False"""
    # This is actually not catching adjacent, just checking the correctness
    word = "substitution"
    abbr = "s55n"
    assert solution_instance.validWordAbbreviation(word, abbr) is False

def test_leading_zeros(solution_instance):
    """Test invalid case with leading zeros: word = "substitution", abbr = "s010n" -> Output: False"""
    word = "substitution"
    abbr = "s010n"
    assert solution_instance.validWordAbbreviation(word, abbr) is False

def test_empty_substring(solution_instance):
    """Test invalid case replacing empty substring: word = "substitution", abbr = "s0ubstitution" -> Output: False"""
    word = "substitution"
    abbr = "s0ubstitution"
    assert solution_instance.validWordAbbreviation(word, abbr) is False

def test_no_abbreviation(solution_instance):
    """Test case where the abbreviation is the same as the word: word = "word", abbr = "word" -> Output: True"""
    word = "word"
    abbr = "word"
    assert solution_instance.validWordAbbreviation(word, abbr) is True

def test_full_abbreviation(solution_instance):
    """Test case where the entire word is abbreviated: word = "word", abbr = "4" -> Output: True"""
    word = "word"
    abbr = "4"
    assert solution_instance.validWordAbbreviation(word, abbr) is True

def test_partial_abbreviation(solution_instance):
    """Test case with partial abbreviation: word = "substitution", abbr = "sub4u4" -> Output: True"""
    word = "substitution"
    abbr = "sub4u4"
    assert solution_instance.validWordAbbreviation(word, abbr) is True

def test_multiple_abbreviations(solution_instance):
    """Test case with multiple abbreviations: word = "substitution", abbr = "su3i1u2on" -> Output: True"""
    word = "substitution"
    abbr = "su3i1u2on"
    assert solution_instance.validWordAbbreviation(word, abbr) is True

def test_abbreviation_larger_than_word(solution_instance):
    """Test case where abbreviation number is larger than remaining word: word = "word", abbr = "w5" -> Output: False"""
    word = "word"
    abbr = "w5"
    assert solution_instance.validWordAbbreviation(word, abbr) is False

def test_different_length(solution_instance):
    """Test case where the expanded abbreviation would have different length: word = "word", abbr = "wo2d" -> Output: False"""
    word = "word"
    abbr = "wo2d"
    assert solution_instance.validWordAbbreviation(word, abbr) is False

def test_single_character(solution_instance):
    """Test case with a single character: word = "a", abbr = "a" -> Output: True"""
    word = "a"
    abbr = "a"
    assert solution_instance.validWordAbbreviation(word, abbr) is True

def test_single_digit_abbreviation(solution_instance):
    """Test case with a single digit abbreviation: word = "a", abbr = "1" -> Output: True"""
    word = "a"
    abbr = "1"
    assert solution_instance.validWordAbbreviation(word, abbr) is True

def test_wrong_character(solution_instance):
    """Test case with a wrong character: word = "word", abbr = "worx" -> Output: False"""
    word = "word"
    abbr = "worx"
    assert solution_instance.validWordAbbreviation(word, abbr) is False

def test_large_number(solution_instance):
    """Test case with a large number in abbreviation: word = "a" * 20, abbr = "20" -> Output: True"""
    word = "a" * 20
    abbr = "20"
    assert solution_instance.validWordAbbreviation(word, abbr) is True

def test_max_length_word(solution_instance):
    """Test case with the maximum length word: word = "a" * 20, abbr = "a18a" -> Output: True"""
    word = "a" * 20
    abbr = "a18a"
    assert solution_instance.validWordAbbreviation(word, abbr) is True

# To run these tests:
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest
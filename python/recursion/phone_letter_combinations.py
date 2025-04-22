# https://leetcode.com/explore/interview/card/facebook/53/recursion-3/267/
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from collections import deque


class SolutionRecursion:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phones = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        if len(digits) == 0:
            return []
        
        result = []

        def backtrack(index, comb):
            if len(comb) == len(digits):
                result.append(comb)
                return
            cur_digit = digits[index]
            letters = phones[cur_digit]
            for i in range(len(letters)):
                backtrack(index + 1, comb + letters[i])
        
        backtrack(0, '')
        return result

"""
BFS queue solution
"""
class SolutionInterative:
     def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phones = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        if not digits:
            return []

        queue = deque([""])  # Start with an empty combination

        for digit in digits:
            letters = phones[digit]
            # traverse layer on layer
            size = len(queue)
            for _ in range(size):
                comb = queue.popleft()
                for letter in letters:
                    queue.append(comb + letter)

        return list(queue)

# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[SolutionRecursion, SolutionInterative],
               ids=["Recursion", "Iterative"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    digits = "23"
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    result = solution_instance.letterCombinations(digits)
    assert sorted(result) == sorted(expected)  # Order doesn't matter

def test_example2(solution_instance):
    """Test Example 2 - empty string."""
    digits = ""
    expected = []
    assert solution_instance.letterCombinations(digits) == expected

def test_example3(solution_instance):
    """Test Example 3 - single digit."""
    digits = "2"
    expected = ["a", "b", "c"]
    result = solution_instance.letterCombinations(digits)
    assert sorted(result) == sorted(expected)

def test_four_digits(solution_instance):
    """Test with maximum allowed digits (4)."""
    digits = "2345"
    result = solution_instance.letterCombinations(digits)
    assert len(result) == 81  # 3 * 3 * 3 * 3 possibilities
    # Verify some valid combinations that should exist
    assert "adgj" in result
    assert "adgk" in result
    assert "cfil" in result

def test_digits_with_four_letters(solution_instance):
    """Test digits that map to four letters (7, 9)."""
    digits = "79"
    result = solution_instance.letterCombinations(digits)
    assert len(result) == 16  # 4 * 4 possibilities
    # Verify all combinations of "pqrs" with "wxyz"
    for first in "pqrs":
        for second in "wxyz":
            assert first + second in result

def test_repeated_digits(solution_instance):
    """Test with repeated digits."""
    digits = "22"
    result = solution_instance.letterCombinations(digits)
    assert len(result) == 9  # 3 * 3 possibilities
    expected = ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
    assert sorted(result) == sorted(expected)

def test_single_four_letter_digit(solution_instance):
    """Test single digit with four letters."""
    digits = "7"  # maps to "pqrs"
    expected = ["p", "q", "r", "s"]
    result = solution_instance.letterCombinations(digits)
    assert sorted(result) == sorted(expected)

def test_two_digits_different_lengths(solution_instance):
    """Test two digits mapping to different numbers of letters."""
    digits = "27"  # "2" maps to 3 letters, "7" maps to 4 letters
    result = solution_instance.letterCombinations(digits)
    assert len(result) == 12  # 3 * 4 possibilities
    # Verify all combinations exist
    for first in "abc":
        for second in "pqrs":
            assert first + second in result

def test_maximum_length_all_four_letters(solution_instance):
    """Test maximum length input with all four-letter mappings."""
    digits = "7979"
    result = solution_instance.letterCombinations(digits)
    assert len(result) == 256  # 4^4 possibilities
    # Check some random combinations
    assert "pwpw" in result
    assert "qxqx" in result
    assert "ryry" in result
    assert "szsz" in result

def test_invalid_input_handling(solution_instance):
    """Test that the function handles invalid inputs correctly."""
    # Empty string should return empty list
    assert solution_instance.letterCombinations("") == []

def test_all_possible_pairs(solution_instance):
    """Test all possible two-digit combinations."""
    for d1 in "23456789":
        for d2 in "23456789":
            result = solution_instance.letterCombinations(d1 + d2)
            # Calculate expected length based on digit mappings
            len1 = 4 if d1 in "79" else 3
            len2 = 4 if d2 in "79" else 3
            assert len(result) == len1 * len2
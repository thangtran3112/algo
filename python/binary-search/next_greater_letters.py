# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
"""
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
 

Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
"""
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        if left >= len(letters):
            # cannot find the target, or all letters <= target
            return letters[0]
        else:
            return letters[left]
        
import pytest  # noqa: E402

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    letters = ["c", "f", "j"]
    target = "a"
    assert solution.nextGreatestLetter(letters, target) == "c"

def test_example_2(solution):
    """Test the second example from the problem statement."""
    letters = ["c", "f", "j"]
    target = "c"
    assert solution.nextGreatestLetter(letters, target) == "f"

def test_example_3(solution):
    """Test the third example from the problem statement."""
    letters = ["x", "x", "y", "y"]
    target = "z"
    assert solution.nextGreatestLetter(letters, target) == "x"

def test_target_greater_than_all_letters(solution):
    """Test when target is greater than all letters."""
    letters = ["a", "b", "c"]
    target = "z"
    assert solution.nextGreatestLetter(letters, target) == "a"

def test_target_less_than_all_letters(solution):
    """Test when target is less than all letters."""
    letters = ["c", "f", "j"]
    target = "a"
    assert solution.nextGreatestLetter(letters, target) == "c"

def test_target_between_letters(solution):
    """Test when target is between letters."""
    letters = ["c", "f", "j"]
    target = "d"
    assert solution.nextGreatestLetter(letters, target) == "f"

def test_duplicate_letters(solution):
    """Test with duplicate letters in the array."""
    letters = ["a", "a", "b", "b", "c", "c"]
    target = "a"
    assert solution.nextGreatestLetter(letters, target) == "b"

def test_all_same_letter(solution):
    """Test when all letters are the same."""
    letters = ["a", "a", "a", "a"]
    target = "a"
    # Since all letters are 'a' and not greater than target 'a', we wrap around
    assert solution.nextGreatestLetter(letters, target) == "a"

def test_minimum_array_size(solution):
    """Test with minimum array size of 2."""
    letters = ["a", "z"]
    target = "a"
    assert solution.nextGreatestLetter(letters, target) == "z"
    
    letters = ["a", "z"]
    target = "z"
    assert solution.nextGreatestLetter(letters, target) == "a"

def test_target_is_last_letter(solution):
    """Test when target is the last letter in the sorted array."""
    letters = ["a", "b", "c", "d", "e"]
    target = "e"
    assert solution.nextGreatestLetter(letters, target) == "a"

def test_adjacent_letters(solution):
    """Test with adjacent letters in the alphabet."""
    letters = ["a", "b", "c", "d", "e"]
    target = "b"
    assert solution.nextGreatestLetter(letters, target) == "c"

def test_non_adjacent_letters(solution):
    """Test with non-adjacent letters in the alphabet."""
    letters = ["a", "e", "i", "o", "u"]
    target = "e"
    assert solution.nextGreatestLetter(letters, target) == "i"

def test_large_array(solution):
    """Test with a larger array to verify binary search efficiency."""
    letters = [chr(ord('a') + i % 26) for i in range(10000)]  # Generate a large array
    target = "m"
    assert solution.nextGreatestLetter(letters, target) == "n"

def test_edge_case_wrap_around(solution):
    """Test the wrap-around case with edge characters."""
    letters = ["a", "b", "c"]
    target = "c"
    assert solution.nextGreatestLetter(letters, target) == "a"
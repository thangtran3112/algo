from typing import List
"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True
        # convert order into hashmap
        pos_map = {}
        for i, ch in enumerate(order):
            pos_map[ch] = i

        def is_valid(first_word, second_word):
            i = 0
            while i < len(first_word) and i < len(second_word):
                first_letter = first_word[i]
                second_letter = second_word[i]
                if pos_map[first_letter] > pos_map[second_letter]:
                    return False
                elif pos_map[first_letter] < pos_map[second_letter]:
                    return True

                # both first_letter and second_letter are the same
                # compare the next letter
                i += 1
            # if we interate through either first_word or second_word
            # all all letters were the same. if
            return len(second_word) >= len(first_word)

        for i in range(1, len(words)):
            curr_word = words[i]
            prev_word = words[i - 1]
            if not is_valid(prev_word, curr_word):
                return False
        return True
    
import pytest  # noqa: E402

@pytest.fixture
def solution_instance():
    return Solution()

def test_example1(solution_instance):
    """Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz" -> Output: True"""
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    assert solution_instance.isAlienSorted(words, order) is True

def test_example2(solution_instance):
    """Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz" -> Output: False"""
    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    assert solution_instance.isAlienSorted(words, order) is False

def test_example3(solution_instance):
    """Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz" -> Output: False"""
    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert solution_instance.isAlienSorted(words, order) is False

def test_single_word(solution_instance):
    """Input: words = ["single"], order = "abcdefghijklmnopqrstuvwxyz" -> Output: True"""
    words = ["single"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert solution_instance.isAlienSorted(words, order) is True

def test_empty_words(solution_instance):
    """Input: words = [], order = "abcdefghijklmnopqrstuvwxyz" -> Output: True"""
    words = []
    order = "abcdefghijklmnopqrstuvwxyz"
    assert solution_instance.isAlienSorted(words, order) is True

def test_all_words_identical(solution_instance):
    """Input: words = ["same", "same", "same"], order = "abcdefghijklmnopqrstuvwxyz" -> Output: True"""
    words = ["same", "same", "same"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert solution_instance.isAlienSorted(words, order) is True

def test_prefix_case(solution_instance):
    """Input: words = ["abc", "ab"], order = "abcdefghijklmnopqrstuvwxyz" -> Output: False"""
    words = ["abc", "ab"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert solution_instance.isAlienSorted(words, order) is False

def test_valid_order_with_prefix(solution_instance):
    """Input: words = ["ab", "abc"], order = "abcdefghijklmnopqrstuvwxyz" -> Output: True"""
    words = ["ab", "abc"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert solution_instance.isAlienSorted(words, order) is True

def test_large_input(solution_instance):
    """Test with a large input."""
    words = ["a" * i for i in range(1, 101)]  # Words of increasing length
    order = "abcdefghijklmnopqrstuvwxyz"
    assert solution_instance.isAlienSorted(words, order) is True

def test_reverse_order(solution_instance):
    """Input: words = ["z", "y", "x"], order = "zyxwvutsrqponmlkjihgfedcba" -> Output: True"""
    words = ["z", "y", "x"]
    order = "zyxwvutsrqponmlkjihgfedcba"
    assert solution_instance.isAlienSorted(words, order) is True

def test_mixed_order(solution_instance):
    """Input: words = ["apple", "banana", "cherry"], order = "zyxwvutsrqponmlkjihgfedcba" -> Output: False"""
    words = ["apple", "banana", "cherry"]
    order = "zyxwvutsrqponmlkjihgfedcba"
    assert solution_instance.isAlienSorted(words, order) is False

def test_edge_case_empty_order(solution_instance):
    """Input: words = ["a", "b"], order = "" -> Output: False"""
    words = ["a", "b"]
    order = ""
    with pytest.raises(KeyError):  # Should raise an error since the order is empty
        solution_instance.isAlienSorted(words, order)

# To run these tests:
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest
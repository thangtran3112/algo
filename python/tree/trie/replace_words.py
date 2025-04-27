# https://leetcode.com/problems/replace-words/description/
"""
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
 

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
"""
from typing import List, Optional
import pytest

class TrieNode:
    def __init__(self):
        # list of children of this TrieNode
        self.children = {}
        self.is_end = False

    def contains_key(self, ch: str) -> bool:
        return ch in self.children

    def get(self, ch: str) -> 'TrieNode':
        return self.children[ch]

    def put(self, ch: str, node: 'TrieNode') -> 'TrieNode':
        self.children[ch] = node

    def set_end(self) -> None:
        self.is_end = True

class Trie:

    def __init__(self):
        self.root = TrieNode()  # empty string

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if not curr.contains_key(ch):
                curr.put(ch, TrieNode())
            child = curr.get(ch)
            curr = child  # go to check the next child

        # mark the end
        curr.set_end()

    def search_prefix(self, prefix: str) -> Optional[TrieNode]:
        curr = self.root
        for ch in prefix:
            if curr.contains_key(ch):
                # go to check the next child
                curr = curr.get(ch)
            else:
                return None  # search has fail
        return curr  # we find the prefix, but it may not be the end of a word

    # given an input, get shortest possible root, defined in this tree/subtree
    def get_shortest_root(self, input: str) -> str:
        # traverse through input, character by character
        curr = self.root
        curr_str = ""
        for ch in input:
            if curr.contains_key(ch):
                curr = curr.get(ch)
                curr_str += ch
                # if this is the first root we found, it is for sure the shortest root
                if curr.is_end:
                    return curr_str
                # continue with next character
            else:
                # search has failed, there is no possible root
                return None




class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        my_trie = Trie()
        for word in dictionary:
            my_trie.insert(word)
        sentence_words = sentence.split(" ")

        refined_words = []
        for word in sentence_words:
            root = my_trie.get_shortest_root(word)
            if root:
                # if root is not None, we find a shortest root
                refined_words.append(root)
            else:
                refined_words.append(word)

        return " ".join(refined_words)
    
# === TEST CASES ===

@pytest.fixture
def solution():
    """Fixture to provide a Solution instance."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    expected = "the cat was rat by the bat"
    assert solution.replaceWords(dictionary, sentence) == expected

def test_example2(solution):
    """Test Example 2 from the problem description."""
    dictionary = ["a", "b", "c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    expected = "a a b c"
    assert solution.replaceWords(dictionary, sentence) == expected

def test_shortest_root_preference(solution):
    """Test that the shortest root is chosen when multiple roots match."""
    dictionary = ["a", "aa", "aaa"]
    sentence = "aaaaa bbb ccc"
    expected = "a bbb ccc"
    assert solution.replaceWords(dictionary, sentence) == expected

    dictionary = ["catt", "cat", "ca"]
    sentence = "cattle"
    expected = "ca"
    assert solution.replaceWords(dictionary, sentence) == expected

def test_no_replacement(solution):
    """Test when no words in the sentence have roots in the dictionary."""
    dictionary = ["apple", "banana"]
    sentence = "the quick brown fox jumps over the lazy dog"
    expected = "the quick brown fox jumps over the lazy dog"
    assert solution.replaceWords(dictionary, sentence) == expected

def test_empty_dictionary(solution):
    """Test with an empty dictionary."""
    dictionary = []
    sentence = "the cattle was rattled by the battery"
    expected = "the cattle was rattled by the battery"
    assert solution.replaceWords(dictionary, sentence) == expected

def test_word_is_root(solution):
    """Test when a word in the sentence is exactly a root."""
    dictionary = ["cat", "dog"]
    sentence = "the cat saw the dog"
    expected = "the cat saw the dog"
    assert solution.replaceWords(dictionary, sentence) == expected

def test_mixed_replacement(solution):
    """Test a sentence with words that are replaced and words that are not."""
    dictionary = ["inter", "nation", "word"]
    sentence = "international wordsmith nationhood"
    expected = "inter word nation"
    assert solution.replaceWords(dictionary, sentence) == expected

def test_single_word_sentence(solution):
    """Test with a sentence containing only one word."""
    dictionary = ["repl"]
    sentence = "replace"
    expected = "repl"
    assert solution.replaceWords(dictionary, sentence) == expected

    dictionary = ["x"]
    sentence = "replace"
    expected = "replace"
    assert solution.replaceWords(dictionary, sentence) == expected

def test_long_words_and_sentence(solution):
    """Test with longer words and sentence (within reasonable limits for testing)."""
    dictionary = ["longroot"]
    sentence = "this is a longrootderivative and another longrootexample"
    expected = "this is a longroot and another longroot"
    assert solution.replaceWords(dictionary, sentence) == expected

def test_all_words_replaced(solution):
    """Test when all words in the sentence are replaced."""
    dictionary = ["a", "b"]
    sentence = "apple banana apricot berry"
    expected = "a b a b"
    assert solution.replaceWords(dictionary, sentence) == expected

def test_root_at_end_of_word(solution):
    """Test when the root matches the entire word."""
    dictionary = ["help", "ful"]
    sentence = "helpful help ful"
    expected = "help help ful" # "helpful" becomes "help", "help" stays "help", "ful" stays "ful"
    assert solution.replaceWords(dictionary, sentence) == expected
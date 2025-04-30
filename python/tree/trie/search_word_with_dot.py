# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def contains_key(self, ch):
        return ch in self.children
    
    def get(self, ch):
        return self.children[ch]
    
    def put(self, ch, node):
        self.children[ch] = node
    
    def set_end(self):
        self.is_end = True


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for ch in word:
            if not curr.contains_key(ch):
                curr.put(ch, TrieNode())
            child = curr.get(ch)
            # move down the tree to check next child
            curr = child
        
        # finish adding the while word
        curr.set_end()

    def search_from(self, node, word):
        curr = node
        for i, ch in enumerate(word):
            if ch == '.':
                for child_node in curr.children.values():
                    if self.search_from(child_node, word[i+1:]):
                        return True
                return False  # No path matched
            else:
                if not curr.contains_key(ch):
                    return False
                curr = curr.get(ch)
        return curr.is_end
        
    def search(self, word):
        return self.search_from(self.root, word)

# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture
def word_dictionary():
    """Provides an instance of the WordDictionary class."""
    return WordDictionary()

def test_example_from_problem(word_dictionary):
    """Test the example sequence from the problem description."""
    word_dictionary.addWord("bad")
    word_dictionary.addWord("dad")
    word_dictionary.addWord("mad")
    assert word_dictionary.search("pad") is False
    assert word_dictionary.search("bad") is True
    assert word_dictionary.search(".ad") is True
    assert word_dictionary.search("b..") is True

def test_simple_exact_match(word_dictionary):
    """Test exact word matches without wildcards."""
    word_dictionary.addWord("hello")
    word_dictionary.addWord("world")
    
    assert word_dictionary.search("hello") is True
    assert word_dictionary.search("world") is True
    assert word_dictionary.search("hi") is False
    assert word_dictionary.search("helloworld") is False

def test_wildcard_at_start(word_dictionary):
    """Test wildcards at the beginning of search patterns."""
    word_dictionary.addWord("cat")
    word_dictionary.addWord("bat")
    word_dictionary.addWord("rat")
    
    assert word_dictionary.search(".at") is True
    assert word_dictionary.search("..t") is True
    assert word_dictionary.search("...") is True
    assert word_dictionary.search("....") is False

def test_wildcard_in_middle(word_dictionary):
    """Test wildcards in the middle of search patterns."""
    word_dictionary.addWord("apple")
    word_dictionary.addWord("apply")
    
    assert word_dictionary.search("a.ple") is True
    assert word_dictionary.search("ap.le") is True
    assert word_dictionary.search("ap.ly") is True
    assert word_dictionary.search("a..le") is True
    assert word_dictionary.search("a...e") is True
    assert word_dictionary.search("a....") is True
    assert word_dictionary.search("a...") is False

def test_wildcard_at_end(word_dictionary):
    """Test wildcards at the end of search patterns."""
    word_dictionary.addWord("code")
    word_dictionary.addWord("coder")
    
    assert word_dictionary.search("cod.") is True
    assert word_dictionary.search("co..") is True
    assert word_dictionary.search("c...") is True
    assert word_dictionary.search("code.") is True
    assert word_dictionary.search("c....") is True  # Matches "coder"

def test_multiple_wildcards(word_dictionary):
    """Test patterns with multiple wildcards."""
    word_dictionary.addWord("abcdefg")
    
    assert word_dictionary.search("a.c.e.g") is True
    assert word_dictionary.search(".b.d.f.") is True
    assert word_dictionary.search("..c..f..") is False  # Too long
    assert word_dictionary.search("...d...") is True
    assert word_dictionary.search("......g") is True

def test_all_wildcards(word_dictionary):
    """Test patterns consisting entirely of wildcards."""
    word_dictionary.addWord("a")
    word_dictionary.addWord("ab")
    word_dictionary.addWord("abc")
    
    assert word_dictionary.search(".") is True
    assert word_dictionary.search("..") is True
    assert word_dictionary.search("...") is True
    assert word_dictionary.search("....") is False

def test_empty_and_single_character_words(word_dictionary):
    """Test empty and single character words."""
    # Note: Problem says word.length >= 1, so we don't test empty words
    word_dictionary.addWord("a")
    word_dictionary.addWord("b")
    word_dictionary.addWord("c")
    
    assert word_dictionary.search("a") is True
    assert word_dictionary.search("b") is True
    assert word_dictionary.search("d") is False
    assert word_dictionary.search(".") is True

def test_case_sensitivity(word_dictionary):
    """Test case sensitivity of the dictionary."""
    word_dictionary.addWord("hello")
    
    assert word_dictionary.search("hello") is True
    assert word_dictionary.search("Hello") is False
    assert word_dictionary.search("HELLO") is False
    assert word_dictionary.search("h.llo") is True
    assert word_dictionary.search("H.llo") is False

def test_multiple_words_with_same_pattern(word_dictionary):
    """Test patterns that could match multiple stored words."""
    word_dictionary.addWord("bag")
    word_dictionary.addWord("bug")
    word_dictionary.addWord("bog")
    
    assert word_dictionary.search("b.g") is True  # Matches all three
    assert word_dictionary.search(".ag") is True  # Matches "bag"
    assert word_dictionary.search(".ug") is True  # Matches "bug"
    assert word_dictionary.search(".og") is True  # Matches "bog"
    assert word_dictionary.search("..g") is True  # Matches all three

def test_long_words(word_dictionary):
    """Test with longer words (near constraint limits)."""
    long_word = "abcdefghijklmnopqrstuvwxy"  # 25 letters
    word_dictionary.addWord(long_word)
    
    assert word_dictionary.search(long_word) is True
    assert word_dictionary.search("a" + "." * 24) is True
    assert word_dictionary.search("." * 25) is True
    assert word_dictionary.search("." * 24) is False
    assert word_dictionary.search("." * 26) is False

def test_no_words_added(word_dictionary):
    """Test search when no words have been added."""
    assert word_dictionary.search("a") is False
    assert word_dictionary.search(".") is False
    assert word_dictionary.search("...") is False

def test_add_same_word_multiple_times(word_dictionary):
    """Test adding the same word multiple times."""
    word_dictionary.addWord("hello")
    word_dictionary.addWord("hello")  # Add again
    
    # Should still work as expected
    assert word_dictionary.search("hello") is True
    assert word_dictionary.search("h.llo") is True
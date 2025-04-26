# https://leetcode.com/problems/implement-trie-prefix-tree/description/
"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""
class TrieNode:
    def __init__(self):
        # list of children of this TrieNode
        self.links = [None] * 26
        self.is_end = False

    def get_index(self, ch: str) -> int:
        return ord(ch) - ord('a')

    def contains_key(self, ch: str) -> bool:
        return self.links[self.get_index(ch)] is not None

    def get(self, ch: str) -> 'TrieNode':
        return self.links[self.get_index(ch)]

    def put(self, ch: str, node: 'TrieNode') -> 'TrieNode':
        self.links[self.get_index(ch)] = node

    def set_end(self) -> None:
        self.is_end = True

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # Time O(m), Space O(m) where m is the length of the key
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                # create new node for ch, and put the new node as children of node
                node.put(ch, TrieNode())
            # move node to the corresponding child
            node = node.get(ch)
        # we have added all characters of word into the Trie
        # mark the last letter is end
        node.set_end()

    def search_prefix(self, word: str) -> TrieNode:
        node = self.root
        for ch in word:
            if node.contains_key(ch):
                # move node to the corresponding child
                node = node.get(ch)
            else:
                # search fails
                return None
        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        # the word may be a prefix, but is it the end of a words in the Trie ?
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)
        return node is not None

# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture
def trie():
    """Fixture to provide a fresh Trie instance for each test."""
    return Trie()

def test_example1(trie):
    """Test the sequence of operations from Example 1."""
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True

def test_insert_and_search_basic(trie):
    """Test basic insert and search functionality."""
    trie.insert("hello")
    assert trie.search("hello") is True
    assert trie.search("hell") is False
    assert trie.search("helloo") is False
    assert trie.search("world") is False

def test_insert_and_startswith_basic(trie):
    """Test basic insert and startsWith functionality."""
    trie.insert("testing")
    assert trie.startsWith("test") is True
    assert trie.startsWith("testing") is True
    assert trie.startsWith("testi") is True
    assert trie.startsWith("tes") is True
    assert trie.startsWith("t") is True
    assert trie.startsWith("testingg") is False
    assert trie.startsWith("toast") is False

def test_multiple_insertions(trie):
    """Test inserting multiple words with shared prefixes."""
    trie.insert("car")
    trie.insert("card")
    trie.insert("cart")
    trie.insert("cat")

    assert trie.search("car") is True
    assert trie.search("card") is True
    assert trie.search("cart") is True
    assert trie.search("cat") is True
    assert trie.search("ca") is False # "ca" is a prefix, not a full word inserted

    assert trie.startsWith("ca") is True
    assert trie.startsWith("car") is True
    assert trie.startsWith("card") is True
    assert trie.startsWith("cart") is True
    assert trie.startsWith("cat") is True
    assert trie.startsWith("carto") is False
    assert trie.startsWith("dog") is False

def test_insert_same_word_twice(trie):
    """Test inserting the same word multiple times."""
    trie.insert("banana")
    trie.insert("banana")
    assert trie.search("banana") is True
    assert trie.startsWith("bana") is True

def test_empty_trie(trie):
    """Test search and startsWith on an empty trie."""
    assert trie.search("a") is False
    assert trie.startsWith("a") is False
    assert trie.search("") is False # Based on implementation, empty string isn't explicitly inserted/searched
    assert trie.startsWith("") is True # An empty prefix matches the root

def test_search_prefix_as_word(trie):
    """Test searching for a prefix that hasn't been inserted as a full word."""
    trie.insert("application")
    assert trie.search("app") is False
    assert trie.startsWith("app") is True

def test_long_word(trie):
    """Test with a long word."""
    long_word = "a" * 1500
    trie.insert(long_word)
    assert trie.search(long_word) is True
    assert trie.startsWith("a" * 1000) is True
    assert trie.search("a" * 1499) is False
    assert trie.startsWith("a" * 1501) is False

def test_different_branches(trie):
    """Test words that diverge early."""
    trie.insert("apple")
    trie.insert("banana")
    assert trie.search("apple") is True
    assert trie.startsWith("app") is True
    assert trie.search("banana") is True
    assert trie.startsWith("ban") is True
    assert trie.startsWith("b") is True
    assert trie.startsWith("a") is True
    assert trie.startsWith("c") is False

def test_startsWith_empty_string(trie):
    """Test startsWith with an empty string prefix."""
    trie.insert("abc")
    assert trie.startsWith("") is True # Empty prefix should always match

def test_search_empty_string(trie):
    """Test search with an empty string."""
    trie.insert("a")
    # According to constraints, word length >= 1.
    # Testing search("") based on current implementation behavior.
    assert trie.search("") is False # Root node's is_end is likely false unless "" is inserted
    
    # Explicitly test inserting "" if the Trie logic were adapted for it
    # (Current implementation doesn't handle inserting "" gracefully)
    # trie.insert("") # This would need modification in insert
    # assert trie.search("") is True
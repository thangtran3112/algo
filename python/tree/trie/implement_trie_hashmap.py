from typing import Optional


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
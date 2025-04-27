"""
Design a map that allows you to do the following:

Maps a string key to a given value.
Returns the sum of the values that have a key with a prefix equal to a given string.
Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
 

Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
 

Constraints:

1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
"""
from collections import deque
from typing import List, Optional


class TrieNode:
    def __init__(self):
        self.children = {}  # can also be done with array with character positions
        self.is_end = 0

    def get(self, ch) -> Optional['TrieNode']:
        if ch not in self.children:
            return None
        return self.children[ch]

    def put(self, ch, node: 'TrieNode') -> None:
        self.children[ch] = node

    def set_end(self, val) -> None:
        self.is_end = val

    def contain_key(self, ch: str) -> bool:
        return ch in self.children

    # For non-word, self.is_end = 0. For a valid word, is_end >= 1
    def is_end_of_word(self) -> bool:
        return self.is_end != 0

    # Notes: self.children will be a dictionary of characters instead { 'a' : nodeA }
    def get_children_nodes(self) -> List['TrieNode']:
        return self.children.values()

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for ch in key:
            if not curr.contain_key(ch):
                curr.put(ch, TrieNode())
            child = curr.get(ch)
            # iterate to next child and add next letter ch
            curr = child

        # end of word
        curr.set_end(val)

    def search_prefix(self, prefix: str) -> Optional[TrieNode]:
        curr = self.root
        for ch in prefix:
            if curr.contain_key(ch):
                child = curr.get(ch)
                curr = child
            else:
                # not found
                return None
        # if we are here, there exist such a prefix in the trie
        return curr

    def sum(self, prefix: str) -> int:
        prefix_root = self.search_prefix(prefix)
        if not prefix_root:
            return 0
        # found the node corresponding to prefix
        # find all possible words from this prefix_root node
        queue = deque()
        queue.append(prefix_root)
        total = 0
        # BFS approach to traverse to all downstream nodes
        while queue:
            curr = queue.popleft()
            # is_end is either 0 (not a word) or >= 1 (a valid word)
            total += curr.is_end
            queue.extend(curr.get_children_nodes())

        return total
    

# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture
def map_sum():
    """Fixture to provide a fresh MapSum instance for each test."""
    return MapSum()

def test_example1(map_sum):
    """Test the sequence of operations from Example 1."""
    map_sum.insert("apple", 3)
    assert map_sum.sum("ap") == 3
    map_sum.insert("app", 2)
    assert map_sum.sum("ap") == 5
    assert map_sum.sum("apple") == 3 # Prefix matches exactly
    assert map_sum.sum("app") == 5   # Prefix matches exactly

def test_insert_new_key(map_sum):
    """Test inserting a completely new key."""
    map_sum.insert("banana", 10)
    assert map_sum.sum("ban") == 10
    assert map_sum.sum("b") == 10
    assert map_sum.sum("banana") == 10
    assert map_sum.sum("ba") == 10

def test_overwrite_key(map_sum):
    """Test inserting a key that already exists, overwriting the value."""
    map_sum.insert("hello", 5)
    assert map_sum.sum("h") == 5
    map_sum.insert("hello", 15) # Overwrite
    assert map_sum.sum("h") == 15
    assert map_sum.sum("he") == 15
    assert map_sum.sum("hello") == 15

def test_multiple_keys_shared_prefix(map_sum):
    """Test summing with multiple keys sharing the same prefix."""
    map_sum.insert("car", 1)
    map_sum.insert("card", 2)
    map_sum.insert("cart", 3)
    map_sum.insert("cat", 4)

    assert map_sum.sum("car") == 1 + 2 + 3 # car, card, cart
    assert map_sum.sum("ca") == 1 + 2 + 3 + 4 # car, card, cart, cat
    assert map_sum.sum("card") == 2
    assert map_sum.sum("cart") == 3
    assert map_sum.sum("cat") == 4
    assert map_sum.sum("c") == 1 + 2 + 3 + 4

def test_prefix_not_found(map_sum):
    """Test summing with a prefix that doesn't exist."""
    map_sum.insert("apple", 5)
    assert map_sum.sum("orange") == 0
    assert map_sum.sum("appl") == 5 # "appl" is a prefix of "apple"
    assert map_sum.sum("apples") == 0 # "apples" is longer

def test_empty_map(map_sum):
    """Test sum on an empty map."""
    assert map_sum.sum("a") == 0
    assert map_sum.sum("") == 0 # Sum of empty prefix on empty map

def test_sum_after_overwrite_complex(map_sum):
    """Test sum after multiple insertions and overwrites."""
    map_sum.insert("a", 1)
    map_sum.insert("ap", 2)
    map_sum.insert("app", 3)
    map_sum.insert("apple", 4)

    assert map_sum.sum("a") == 1 + 2 + 3 + 4 # a, ap, app, apple
    assert map_sum.sum("ap") == 2 + 3 + 4    # ap, app, apple
    assert map_sum.sum("app") == 3 + 4       # app, apple
    assert map_sum.sum("apple") == 4

    # Overwrite "app"
    map_sum.insert("app", 10)
    assert map_sum.sum("a") == 1 + 2 + 10 + 4 # a, ap, app(new), apple
    assert map_sum.sum("ap") == 2 + 10 + 4    # ap, app(new), apple
    assert map_sum.sum("app") == 10 + 4       # app(new), apple
    assert map_sum.sum("apple") == 4

    # Overwrite "a" (which is only a prefix now)
    map_sum.insert("a", 20)
    assert map_sum.sum("a") == 20 + 2 + 10 + 4 # a(new), ap, app(new), apple
    assert map_sum.sum("ap") == 2 + 10 + 4     # ap, app(new), apple

def test_sum_empty_prefix(map_sum):
    """Test summing with an empty prefix (should sum all values)."""
    map_sum.insert("one", 1)
    map_sum.insert("two", 2)
    map_sum.insert("three", 3)
    map_sum.insert("onetwo", 12)
    assert map_sum.sum("") == 1 + 2 + 3 + 12

def test_long_keys_and_prefixes(map_sum):
    """Test with longer keys and prefixes within constraints."""
    key1 = "a" * 50
    key2 = "a" * 49 + "b"
    prefix = "a" * 49

    map_sum.insert(key1, 100)
    map_sum.insert(key2, 200)
    map_sum.insert("b" * 50, 300)

    assert map_sum.sum(prefix) == 100 + 200 # Matches key1 and key2
    assert map_sum.sum("a" * 50) == 100
    assert map_sum.sum("a" * 51) == 0
    assert map_sum.sum("b") == 300

def test_values_at_constraints(map_sum):
    """Test with minimum and maximum values."""
    map_sum.insert("min", 1)
    map_sum.insert("max", 1000)
    map_sum.insert("mix", 500)

    assert map_sum.sum("m") == 1 + 1000 + 500
    assert map_sum.sum("mi") == 1 + 500
    assert map_sum.sum("min") == 1
    assert map_sum.sum("max") == 1000
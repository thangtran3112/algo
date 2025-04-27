# https://leetcode.com/problems/alien-dictionary/description/
"""
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""
from collections import defaultdict, deque
from typing import List
import pytest

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # adj_list['w'] = 'c, mean 'w' -> 'c', or 'w' is a prerequisite of 'c'
        adj_list = defaultdict(set)
        # { 'w': 0, 'a': 0, ...} by using outer loop and inner loop
        in_degree = {c: 0 for word in words for c in word}

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words. 
        # zip return iterator ((word1, word2), (word2, word3), ...)
        for first_word, second_word in zip(words, words[1:]):
            found_divergence = False
            # zip('wrt', 'cat') => ((w, c), (r, a), 't,c')
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1

                    # we stop when 2 characters in first_word and second_word start diverging
                    found_divergence = True
                    break

            # if the for loop does not break, and the for loop completed
            # Check if second word is not a prefix of first word
            if not found_divergence:
                if len(second_word) < len(first_word):
                    # the alien dictionary is not valid, since the prefix word, is after the bigger word
                    return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        # Kahn topo sorting, we add all nodes with no pre-requisites
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for dependent_node in adj_list[c]:
                in_degree[dependent_node] -= 1
                if in_degree[dependent_node] == 0:
                    # this node is now free to be picked
                    queue.append(dependent_node)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)
    
# Solution without using in_degree of counter, but maintain a reversed map
# for keeping track of prerequisites
class SolutionDict:
    def alienOrder(self, words: List[str]) -> str:
        dependencies = defaultdict(set)
        prerequisites = defaultdict(set)

        all_chars = set()

        # Step 0: build all_chars set and collect edges
        for word in words:
            for c in word:
                all_chars.add(c)

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in dependencies[c]:
                        dependencies[c].add(d)
                        prerequisites[d].add(c)
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""

        # Step 1: Initialize queue with nodes that have no prerequisites
        queue = deque([c for c in all_chars if not prerequisites[c]])
        output = []

        # Step 2: Standard BFS Topological Sort
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in dependencies[c]:
                prerequisites[d].discard(c)
                if not prerequisites[d]:
                    queue.append(d)

        # Step 3: Check if output contains all nodes
        if len(output) < len(all_chars):
            return ""

        return "".join(output)

# === TEST CASES ===

@pytest.fixture(params=[Solution, SolutionDict],
               ids=["InDegree", "PrerequisitesDict"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def is_valid_order(order: str, words: List[str]) -> bool:
    """
    Checks if the generated order satisfies the constraints derived from words.
    Also checks if all unique characters are present.
    """
    if not order and any(len(w) > 0 for w in words): # Handle cases where "" is expected
         # Need to check if "" was genuinely the correct output (cycle or prefix rule)
         # This helper assumes a non-empty order is expected if valid
         pass # Cannot fully validate "" output here easily, rely on direct test comparison

    adj = defaultdict(set)
    all_chars = set(c for word in words for c in word)

    # Build adjacency list based on words
    for w1, w2 in zip(words, words[1:]):
        min_len = min(len(w1), len(w2))
        diff_found = False
        for i in range(min_len):
            if w1[i] != w2[i]:
                if w2[i] not in adj[w1[i]]:
                    adj[w1[i]].add(w2[i])
                diff_found = True
                break
        # Check for prefix rule violation ("abc", "ab")
        if not diff_found and len(w1) > len(w2):
            return False # Invalid input, but the function should return ""

    # Check if all unique characters are in the order
    if set(order) != all_chars:
        return False

    # Check if the order respects the derived constraints
    pos = {char: i for i, char in enumerate(order)}
    for u in adj:
        for v in adj[u]:
            if u not in pos or v not in pos or pos[u] > pos[v]:
                return False
    return True

# --- Basic Tests ---

def test_example1(solution_instance):
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    expected = "wertf"
    result = solution_instance.alienOrder(words)
    assert result == expected or is_valid_order(result, words) # "wertf" is unique here

def test_example2(solution_instance):
    words = ["z", "x"]
    expected = "zx"
    result = solution_instance.alienOrder(words)
    assert result == expected or is_valid_order(result, words) # "zx" is unique

def test_example3(solution_instance):
    words = ["z", "x", "z"]
    expected = ""
    assert solution_instance.alienOrder(words) == expected

# --- Invalid Input Tests ---

def test_prefix_violation(solution_instance):
    words = ["abc", "ab"]
    expected = ""
    assert solution_instance.alienOrder(words) == expected

def test_simple_cycle(solution_instance):
    words = ["a", "b", "a"]
    expected = ""
    assert solution_instance.alienOrder(words) == expected

# --- Valid Order Tests ---

def test_simple_chain(solution_instance):
    words = ["a", "b", "c"]
    expected = "abc"
    result = solution_instance.alienOrder(words)
    assert result == expected or is_valid_order(result, words)

def test_multiple_dependencies(solution_instance):
    words = ["ac", "bc", "bd"] # a->b, c->d
    result = solution_instance.alienOrder(words)
    assert is_valid_order(result, words)
    # Possible orders: "acbd"

def test_no_order_constraints(solution_instance):
    words = ["abc", "abc"]
    result = solution_instance.alienOrder(words)
    assert is_valid_order(result, words)
    # Possible orders: "abc", "acb", "bac", "bca", "cab", "cba"

def test_single_word(solution_instance):
    words = ["hello"]
    result = solution_instance.alienOrder(words)
    assert is_valid_order(result, words)
    # Possible orders: any permutation of "helo"

def test_two_words_no_constraint(solution_instance):
    words = ["hello", "world"] # No constraints derived
    result = solution_instance.alienOrder(words)
    assert is_valid_order(result, words)
    # Possible orders: any permutation of "dehlorw"

def test_disconnected_chars(solution_instance):
    words = ["a", "b", "c", "d"] # a->b, b->c, c->d
    result = solution_instance.alienOrder(words)
    assert result == "abcd" or is_valid_order(result, words)

def test_disconnected_components(solution_instance):
    words = ["ca", "cb", "xd", "xe"] # c->x is not implied, c->a, c->b, x->d, x->e
    result = solution_instance.alienOrder(words)
    assert is_valid_order(result, words)
    # Possible orders: "cabxde", "cbaxde", "xdecab", "xdecba", etc.

def test_all_letters(solution_instance):
    # Generate words to enforce reverse alphabetical order
    words = [chr(ord('a') + i) for i in range(25, -1, -1)] # ["z", "y", ..., "a"]
    expected = "zyxwvutsrqponmlkjihgfedcba"
    result = solution_instance.alienOrder(words)
    assert result == expected or is_valid_order(result, words)

def test_longer_example(solution_instance):
    words = ["zy", "zx"] # y->x
    result = solution_instance.alienOrder(words)
    assert is_valid_order(result, words)
    # Possible orders: "zyx"

def test_from_leetcode_1(solution_instance):
    words = ["ac","ab","b"] # c -> b
    result = solution_instance.alienOrder(words)
    assert is_valid_order(result, words)
    # Possible orders: "acb"

def test_from_leetcode_2(solution_instance):
    words = ["abc","bcd","qwert"] # a->b, b->c, c->d, a->q
    result = solution_instance.alienOrder(words)
    assert is_valid_order(result, words)
    # Possible orders: "abcdqwert", "aqbcdwert", etc.

def test_from_leetcode_3(solution_instance):
    words = ["ab", "adc"] # b->d
    result = solution_instance.alienOrder(words)
    assert is_valid_order(result, words)
    # Possible orders: "abcd", "acbd"

def test_from_leetcode_4(solution_instance):
    words = ["hello", "leetcode"] # h->l, e->l, l->t, o->c, o->d, e->e (no info)
    result = solution_instance.alienOrder(words)
    assert is_valid_order(result, words)
    # Possible orders: "helotcd", "heoltcd", ...

def test_empty_input(solution_instance):
    words = []
    expected = ""
    assert solution_instance.alienOrder(words) == expected

def test_input_with_empty_string(solution_instance):
    # Constraints say 1 <= words[i].length <= 100, but testing defensively
    words = ["a", ""]
    expected = "" # Should be caught by prefix rule
    assert solution_instance.alienOrder(words) == expected

    words = ["", "a"]
    result = solution_instance.alienOrder(words)
    assert is_valid_order(result, words) # No constraints derived, "" is not a char
    # Expected: "a"
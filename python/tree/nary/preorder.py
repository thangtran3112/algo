# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
"""
from typing import List, Optional

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def traverse(node):
            if not node:
                return
            result.append(node.val)
            for child in node.children:
                traverse(child)
        traverse(root)
        return result
    
# === TEST CASES ===
import pytest  # noqa: E402

def build_n_ary_tree(values: List[Optional[int]]) -> Optional[Node]:
    """
    Helper function to build an N-ary tree from a list representation.
    The list format follows LeetCode's convention:
    [rootVal, null, child1, child2, ..., null, grandchild1, grandchild2, ...]
    """
    if not values or len(values) == 0:
        return None
        
    root = Node(values[0], [])
    
    # Map to store nodes at each level
    nodes = {0: root}
    next_index = 1
    node_idx = 0
    
    while next_index < len(values):
        # Null marks the end of children for the current node
        if values[next_index] is None:
            node_idx += 1
            next_index += 1
            continue
        
        # Create the child node and add to current node's children
        if node_idx in nodes:
            child = Node(values[next_index], [])
            nodes[node_idx].children.append(child)
            nodes[next_index] = child
        
        next_index += 1
    
    return root

@pytest.fixture
def solution():
    """Fixture to provide a Solution instance."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    # Create tree: [1,null,3,2,4,null,5,6]
    root = Node(1, [])
    child1 = Node(3, [])
    child2 = Node(2, [])
    child3 = Node(4, [])
    root.children = [child1, child2, child3]
    
    grandchild1 = Node(5, [])
    grandchild2 = Node(6, [])
    child1.children = [grandchild1, grandchild2]
    
    expected = [1, 3, 5, 6, 2, 4]
    assert solution.preorder(root) == expected

def test_example2(solution):
    """Test Example 2 from the problem description."""
    # This is a complex tree from the example, constructing manually
    root = Node(1, [])
    
    # Level 1 children
    child1 = Node(2, [])
    child2 = Node(3, [])
    child3 = Node(4, [])
    child4 = Node(5, [])
    root.children = [child1, child2, child3, child4]
    
    # Level 2 children
    child2.children = [Node(6, []), Node(7, [])]
    child3.children = [Node(8, [])]
    child4.children = [Node(9, []), Node(10, [])]
    
    # Level 3 children
    child2.children[1].children = [Node(11, [])]  # 7's child is 11
    child3.children[0].children = [Node(12, [])]  # 8's child is 12
    child4.children[0].children = [Node(13, [])]  # 9's child is 13
    
    # Level 4 children
    child2.children[1].children[0].children = [Node(14, [])]  # 11's child is 14
    
    expected = [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]
    assert solution.preorder(root) == expected

def test_empty_tree(solution):
    """Test with empty tree."""
    root = None
    assert solution.preorder(root) == []

def test_single_node(solution):
    """Test with a single node tree."""
    root = Node(1, [])
    expected = [1]
    assert solution.preorder(root) == expected

def test_node_without_children(solution):
    """Test with a node that has an empty children list."""
    root = Node(1, [])
    assert solution.preorder(root) == [1]

def test_node_with_empty_children_list(solution):
    """Test with a node that has children property as empty list."""
    root = Node(1, [])
    assert solution.preorder(root) == [1]

def test_two_level_tree(solution):
    """Test with a two-level tree."""
    root = Node(1, [])
    root.children = [Node(2, []), Node(3, []), Node(4, [])]
    expected = [1, 2, 3, 4]
    assert solution.preorder(root) == expected

def test_max_value_nodes(solution):
    """Test with nodes having maximum allowed value (10^4)."""
    root = Node(10000, [])
    child1 = Node(10000, [])
    child2 = Node(10000, [])
    root.children = [child1, child2]
    expected = [10000, 10000, 10000]
    assert solution.preorder(root) == expected

def test_deep_tree(solution):
    """Test with a deep tree approaching the height constraint."""
    # Create a tree with depth close to 1000 (but smaller for practicality)
    current = Node(1, [])
    root = current
    
    # Create a deep path
    for i in range(2, 101):  # 100 levels deep
        child = Node(i, [])
        current.children = [child]
        current = child
    
    # Expected result is [1, 2, 3, ..., 100]
    expected = list(range(1, 101))
    assert solution.preorder(root) == expected

def test_wide_tree(solution):
    """Test with a wide tree (many children at one level)."""
    root = Node(1, [])
    # Add 100 children to root
    root.children = [Node(i, []) for i in range(2, 102)]
    
    expected = [1] + list(range(2, 102))
    assert solution.preorder(root) == expected

def test_uneven_tree(solution):
    """Test with an uneven tree (different depths)."""
    root = Node(1, [])
    
    # First child has deep structure
    child1 = Node(2, [])
    root.children = [child1, Node(3, [])]
    
    # Create a deep path under child1
    current = child1
    for i in range(4, 10):
        child = Node(i, [])
        current.children = [child]
        current = child
    
    expected = [1, 2, 4, 5, 6, 7, 8, 9, 3]
    assert solution.preorder(root) == expected
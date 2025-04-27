# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # turn into "1, 2, 3, None, None, 4, None, None, 5, None, None"
    # preorder traversal
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        res = []

        def dfs(node):
            if not node:
                res.append("None")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    # convert "1, 2, 3, None, None, 4, None, None, 5, None, None" back
    # preorder traversal
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        vals = data.split(",")
        vals = vals[::-1]  # reverse the list

        def dfs():
            if not vals:
                return None
            val = vals.pop()
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

# === TEST CASES ===
import pytest # noqa: E402
from typing import List, Optional # noqa: E402
from collections import deque  # noqa: E402

# Helper function to build a binary tree from a list (LeetCode format)
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
        
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
            
    return root

# Helper function to compare two binary trees
def compare_trees(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.val != node2.val:
        return False
    
    return compare_trees(node1.left, node2.left) and \
           compare_trees(node1.right, node2.right)

@pytest.fixture
def codec():
    """Fixture to provide a Codec instance."""
    return Codec()

def test_example1(codec):
    """Test Example 1 from the problem description."""
    original_root = build_tree([1, 2, 3, None, None, 4, 5])
    serialized_data = codec.serialize(original_root)
    deserialized_root = codec.deserialize(serialized_data)
    assert compare_trees(original_root, deserialized_root)

def test_empty_tree(codec):
    """Test serialization and deserialization of an empty tree."""
    original_root = None
    serialized_data = codec.serialize(original_root)
    # Expected serialization for None root based on the implementation
    assert serialized_data == "None" 
    deserialized_root = codec.deserialize(serialized_data)
    assert deserialized_root is None
    assert compare_trees(original_root, deserialized_root)

def test_single_node(codec):
    """Test a tree with only a single node."""
    original_root = build_tree([1])
    serialized_data = codec.serialize(original_root)
    deserialized_root = codec.deserialize(serialized_data)
    assert compare_trees(original_root, deserialized_root)

def test_complete_tree(codec):
    """Test a complete binary tree."""
    original_root = build_tree([1, 2, 3, 4, 5, 6, 7])
    serialized_data = codec.serialize(original_root)
    deserialized_root = codec.deserialize(serialized_data)
    assert compare_trees(original_root, deserialized_root)

def test_left_skewed_tree(codec):
    """Test a left-skewed tree."""
    original_root = build_tree([1, 2, None, 3, None, 4])
    serialized_data = codec.serialize(original_root)
    deserialized_root = codec.deserialize(serialized_data)
    assert compare_trees(original_root, deserialized_root)

def test_right_skewed_tree(codec):
    """Test a right-skewed tree."""
    original_root = build_tree([1, None, 2, None, 3, None, 4])
    serialized_data = codec.serialize(original_root)
    deserialized_root = codec.deserialize(serialized_data)
    assert compare_trees(original_root, deserialized_root)

def test_negative_values(codec):
    """Test a tree with negative node values."""
    original_root = build_tree([-10, -5, -15, None, -7, None, -20])
    serialized_data = codec.serialize(original_root)
    deserialized_root = codec.deserialize(serialized_data)
    assert compare_trees(original_root, deserialized_root)

def test_zero_values(codec):
    """Test a tree containing zero values."""
    original_root = build_tree([0, 0, 0, None, 0])
    serialized_data = codec.serialize(original_root)
    deserialized_root = codec.deserialize(serialized_data)
    assert compare_trees(original_root, deserialized_root)

def test_min_max_values(codec):
    """Test a tree with values at the constraints."""
    original_root = build_tree([0, -1000, 1000])
    serialized_data = codec.serialize(original_root)
    deserialized_root = codec.deserialize(serialized_data)
    assert compare_trees(original_root, deserialized_root)

def test_complex_tree(codec):
    """Test a more complex, unbalanced tree structure."""
    original_root = build_tree([5, 3, 8, 1, 4, 7, 9, None, 2, None, None, 6])
    serialized_data = codec.serialize(original_root)
    deserialized_root = codec.deserialize(serialized_data)
    assert compare_trees(original_root, deserialized_root)

def test_serialization_format(codec):
    """Verify the specific serialization format for a known tree."""
    # Tree: [1, 2, 3, None, None, 4, 5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    expected_serialization = "1,2,None,None,3,4,None,None,5,None,None"
    assert codec.serialize(root) == expected_serialization

def test_deserialization_from_known_string(codec):
    """Verify deserialization from a known valid string."""
    data = "1,2,None,None,3,4,None,None,5,None,None"
    
    # Expected tree structure for the data string
    expected_root = TreeNode(1)
    expected_root.left = TreeNode(2)
    expected_root.right = TreeNode(3)
    expected_root.right.left = TreeNode(4)
    expected_root.right.right = TreeNode(5)
    
    deserialized_root = codec.deserialize(data)
    assert compare_trees(expected_root, deserialized_root)
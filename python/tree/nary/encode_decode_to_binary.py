
# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/description/
"""
Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-nary tree structure.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See following example).

For example, you may encode the following 3-ary tree to a binary tree in this way:



Input: root = [1,null,3,2,4,null,5,6]
Note that the above is just an example which might or might not work. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
"""
# Definition for a Nary Node.
from collections import deque
from typing import List, Optional
import pytest

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # BFS/DFS encoder is also compatible with DFS/BFS decoder
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None
        binary_root = TreeNode(root.val)
        queue = deque()
        queue.append((binary_root, root))
        while queue:
            binary_parent, curr = queue.popleft()
            prev_binary_node = None
            head_binary_node = None
            for child in curr.children:
                # use the right binary subtree to store sibblings
                new_binary_node = TreeNode(child.val)
                if prev_binary_node:
                    prev_binary_node.right = new_binary_node
                else:
                    head_binary_node = new_binary_node
                prev_binary_node = new_binary_node
                queue.append((new_binary_node, child))

            # the left binary tree will store children
            binary_parent.left = head_binary_node
        return binary_root

    # we can also use the DFS decode the decode the binary tree
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None
        node = Node(data.val, [])
        queue = deque()
        queue.append((data, node))
        while queue:
            binary_node, nary_node = queue.popleft()
            binary_curr = binary_node.left  # first child
            # first all sibblings on the right side of the first child
            while binary_curr:
                child_nary_node = Node(binary_curr.val, [])
                nary_node.children.append(child_nary_node)
                queue.append((binary_curr, child_nary_node))
                binary_curr = binary_curr.right
        return node

class CodecDFS:

    def encode(self, root):
        if not root:
            return None

        binary_root = TreeNode(root.val)
        if len(root.children) > 0:
            firstChild = root.children[0]
            binary_root.left = self.encode(firstChild)

        # the parent for the rest of the children
        binary_curr = binary_root.left

        # encode the rest of the children
        for i in range(1, len(root.children)):
            binary_curr.right = self.encode(root.children[i])
            binary_curr = binary_curr.right

        return binary_root

    # we can also use the BFS decode the decode the binary tree
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        # from the binary tree, use the right path to get sibblings
        # the leaf path of a node will be its children
        if not data:
            return None
        parent = Node(data.val, [])
        binary_node = data.left  # 1st child
        while binary_node:
            parent.children.append(self.decode(binary_node))
            binary_node = binary_node.right
        return parent
    
# === TEST CASES ===

# Helper function to build N-ary tree (manual construction is clearer for complex cases)
def build_n_ary_tree_manual(structure):
    """Builds N-ary tree from a nested structure for clarity."""
    if not structure:
        return None
    val = structure[0]
    children_structures = structure[1] if len(structure) > 1 else []
    node = Node(val, [])
    for child_structure in children_structures:
        node.children.append(build_n_ary_tree_manual(child_structure))
    return node

# Helper function to compare two N-ary trees
def compare_n_ary_trees(node1: Optional[Node], node2: Optional[Node]) -> bool:
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.val != node2.val:
        return False
    if len(node1.children) != len(node2.children):
        return False
    
    # Recursively compare children
    for i in range(len(node1.children)):
        if not compare_n_ary_trees(node1.children[i], node2.children[i]):
            return False
            
    return True

@pytest.fixture(params=[Codec, CodecDFS],
               ids=["BFS_Codec", "DFS_Codec"])
def codec_instance(request):
    """Fixture to provide instances of both Codec classes."""
    return request.param()

def test_example1(codec_instance):
    """Test Example 1 from the problem description."""
    # Tree: [1,null,3,2,4,null,5,6]
    # Manual structure: [1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]
    original_root = build_n_ary_tree_manual([1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]])
    
    encoded_tree = codec_instance.encode(original_root)
    decoded_root = codec_instance.decode(encoded_tree)
    
    assert compare_n_ary_trees(original_root, decoded_root)

def test_example2(codec_instance):
    """Test Example 2 from the problem description."""
    # Tree: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    # Manual structure is very complex, building step-by-step
    root = Node(1, [])
    child1 = Node(2, [])
    child2 = Node(3, [])
    child3 = Node(4, [])
    child4 = Node(5, [])
    root.children = [child1, child2, child3, child4]
    
    child2.children = [Node(6, []), Node(7, [])]
    child3.children = [Node(8, [])]
    child4.children = [Node(9, []), Node(10, [])]
    
    child2.children[1].children = [Node(11, [])]  # 7's child is 11
    child3.children[0].children = [Node(12, [])]  # 8's child is 12
    child4.children[0].children = [Node(13, [])]  # 9's child is 13
    
    child2.children[1].children[0].children = [Node(14, [])]  # 11's child is 14
    original_root = root

    encoded_tree = codec_instance.encode(original_root)
    decoded_root = codec_instance.decode(encoded_tree)
    
    assert compare_n_ary_trees(original_root, decoded_root)

def test_example3(codec_instance):
    """Test Example 3 - empty tree."""
    original_root = None
    encoded_tree = codec_instance.encode(original_root)
    decoded_root = codec_instance.decode(encoded_tree)
    assert decoded_root is None
    assert compare_n_ary_trees(original_root, decoded_root)

def test_single_node(codec_instance):
    """Test with a single node tree."""
    original_root = Node(1, [])
    encoded_tree = codec_instance.encode(original_root)
    decoded_root = codec_instance.decode(encoded_tree)
    assert compare_n_ary_trees(original_root, decoded_root)

def test_two_level_tree(codec_instance):
    """Test with a simple two-level tree."""
    # Structure: [1, [[2, []], [3, []], [4, []]]]
    original_root = build_n_ary_tree_manual([1, [[2, []], [3, []], [4, []]]])
    encoded_tree = codec_instance.encode(original_root)
    decoded_root = codec_instance.decode(encoded_tree)
    assert compare_n_ary_trees(original_root, decoded_root)

def test_deep_tree(codec_instance):
    """Test with a deep, linear tree."""
    # Structure: [1, [[2, [[3, [[4, []]]]]]]]
    original_root = build_n_ary_tree_manual([1, [[2, [[3, [[4, []]]]]]]])
    encoded_tree = codec_instance.encode(original_root)
    decoded_root = codec_instance.decode(encoded_tree)
    assert compare_n_ary_trees(original_root, decoded_root)

def test_wide_tree(codec_instance):
    """Test with a wide tree (many children at one level)."""
    # Structure: [1, [[2,[]],[3,[]],[4,[]],[5,[]],[6,[]]]]
    original_root = build_n_ary_tree_manual([1, [[i, []] for i in range(2, 7)]])
    encoded_tree = codec_instance.encode(original_root)
    decoded_root = codec_instance.decode(encoded_tree)
    assert compare_n_ary_trees(original_root, decoded_root)

def test_uneven_tree(codec_instance):
    """Test with an uneven tree (different depths)."""
    # Structure: [1, [[2, [[4,[]],[5,[]]]], [3, []]]]
    original_root = build_n_ary_tree_manual([1, [[2, [[4,[]],[5,[]]]], [3, []]]])
    encoded_tree = codec_instance.encode(original_root)
    decoded_root = codec_instance.decode(encoded_tree)
    assert compare_n_ary_trees(original_root, decoded_root)

def test_node_values(codec_instance):
    """Test with different node values including 0 and max value."""
    # Structure: [0, [[10000, []], [500, []]]]
    original_root = build_n_ary_tree_manual([0, [[10000, []], [500, []]]])
    encoded_tree = codec_instance.encode(original_root)
    decoded_root = codec_instance.decode(encoded_tree)
    assert compare_n_ary_trees(original_root, decoded_root)
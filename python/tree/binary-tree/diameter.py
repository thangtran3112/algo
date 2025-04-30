# https://leetcode.com/problems/diameter-of-binary-tree/description/
"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""
import pytest
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path_with_root(node) -> int:
            nonlocal diameter
            # base case
            if not node:
                return 0
            longest_left_path = longest_path_with_root(node.left)
            longest_right_path = longest_path_with_root(node.right)
            diameter_with_root_node = longest_left_path + longest_right_path + 1
            diameter = max(diameter, diameter_with_root_node)

            return max(longest_left_path + 1, longest_right_path + 1)

        longest_path_with_root(root)
        return diameter - 1

# === TEST CASES ===

# Helper function to build a binary tree from a list (following LeetCode's serialization format)
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
        
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
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

@pytest.fixture
def solution():
    """Provides an instance of the Solution class."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    # Tree structure: 
    #      1
    #    /   \
    #   2     3
    #  / \
    # 4   5
    root = build_tree([1, 2, 3, 4, 5])
    assert solution.diameterOfBinaryTree(root) == 3

def test_example2(solution):
    """Test Example 2 from the problem description."""
    # Tree structure:
    #   1
    #  /
    # 2
    root = build_tree([1, 2])
    assert solution.diameterOfBinaryTree(root) == 1

def test_empty_tree(solution):
    """Test with an empty tree."""
    root = None
    assert solution.diameterOfBinaryTree(root) == -1

def test_single_node(solution):
    """Test with a single node tree."""
    root = TreeNode(1)
    assert solution.diameterOfBinaryTree(root) == 0

def test_straight_line_left(solution):
    """Test with a straight line tree to the left."""
    # Tree structure:
    #   1
    #  /
    # 2
    #/
    #3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert solution.diameterOfBinaryTree(root) == 2

def test_straight_line_right(solution):
    """Test with a straight line tree to the right."""
    # Tree structure:
    # 1
    #  \
    #   2
    #    \
    #     3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert solution.diameterOfBinaryTree(root) == 2

def test_balanced_tree(solution):
    """Test with a perfectly balanced tree."""
    # Tree structure:
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    assert solution.diameterOfBinaryTree(root) == 4

def test_unbalanced_tree(solution):
    """Test with an unbalanced tree."""
    # Tree structure:
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    #     / \   \
    #    7   8   9
    root = build_tree([1, 2, 3, 4, 5, None, 6, None, None, 7, 8, None, 9])
    assert solution.diameterOfBinaryTree(root) == 6

def test_diameter_through_root(solution):
    """Test where the diameter passes through the root."""
    # Tree structure:
    #     1
    #    / \
    #   2   3
    #  /     \
    # 4       5
    #/         \
    #6         7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    assert solution.diameterOfBinaryTree(root) == 6

def test_diameter_not_through_root(solution):
    """Test where the diameter does not pass through the root."""
    # Tree structure:
    #       1
    #      /
    #     2
    #    / \
    #   3   4
    #  /     \
    # 5       6
    #/         \
    #7         8
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.left.left.left.left = TreeNode(7)
    root.left.right.right.right = TreeNode(8)
    assert solution.diameterOfBinaryTree(root) == 6

def test_zigzag_tree(solution):
    """Test with a zigzag tree structure."""
    # Tree structure:
    #     1
    #    /
    #   2
    #    \
    #     3
    #    /
    #   4
    #    \
    #     5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.left.right.left = TreeNode(4)
    root.left.right.left.right = TreeNode(5)
    assert solution.diameterOfBinaryTree(root) == 4

def test_complete_tree(solution):
    """Test with a complete binary tree."""
    # Tree structure:
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7
    #  / \
    # 8   9
    root = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert solution.diameterOfBinaryTree(root) == 5

def test_negative_values(solution):
    """Test with negative values."""
    # Tree structure:
    #      -1
    #     /  \
    #   -2   -3
    #  /  \
    # -4  -5
    root = build_tree([-1, -2, -3, -4, -5])
    assert solution.diameterOfBinaryTree(root) == 3

def test_deep_tree(solution):
    """Test with a very deep tree."""
    # Create a tree with depth 10 (left-leaning)
    root = TreeNode(1)
    current = root
    for i in range(2, 11):
        current.left = TreeNode(i)
        current = current.left
    
    # Add a branch off the middle to create a longer diameter
    root.left.left.left.right = TreeNode(100)
    root.left.left.left.right.right = TreeNode(101)
    root.left.left.left.right.right.right = TreeNode(102)
    
    # Diameter should be from leaf of right branch to bottom leaf: 6 edges
    assert solution.diameterOfBinaryTree(root) == 9
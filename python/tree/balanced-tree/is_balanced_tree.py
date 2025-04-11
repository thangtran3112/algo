# https://leetcode.com/problems/balanced-binary-tree/description/
"""
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def get_depth(self, node):
        if node in self.caches:
            return self.caches[node]
        if not node:
            return 0
        self.caches[node] = max(self.get_depth(node.left), self.get_depth(node.right)) + 1
        return self.caches[node]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if (not root.left) and (not root.right):
            return True
        self.caches = {}
        left_balance = self.isBalanced(root.left)
        if not left_balance:
            # early exit
            return False
        right_balance = self.isBalanced(root.right)
        if not right_balance:
            # early exit
            return False
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        if abs(left_depth - right_depth) <= 1:
            return True
        return False
    
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_empty_tree(solution):
    """Test with an empty tree."""
    root = None
    assert solution.isBalanced(root) == True

def test_single_node(solution):
    """Test with a single node tree."""
    root = TreeNode(1)
    assert solution.isBalanced(root) == True

def test_balanced_simple_tree(solution):
    """Test with a simple balanced tree."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert solution.isBalanced(root) == True

def test_balanced_complex_tree(solution):
    """Test with a complex balanced tree."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert solution.isBalanced(root) == True

def test_unbalanced_left_heavy_tree(solution):
    """Test with an unbalanced left-heavy tree."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    assert solution.isBalanced(root) == False

def test_unbalanced_right_heavy_tree(solution):
    """Test with an unbalanced right-heavy tree."""
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    assert solution.isBalanced(root) == False

def test_balanced_tree_with_unbalanced_subtree(solution):
    """Test with a tree that has an unbalanced subtree."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.left.left.left.left = TreeNode(7)
    assert solution.isBalanced(root) == False

def test_balanced_left_deeper(solution):
    """Test with a balanced tree where left is one level deeper."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    assert solution.isBalanced(root) == True

def test_balanced_right_deeper(solution):
    """Test with a balanced tree where right is one level deeper."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    assert solution.isBalanced(root) == True

def test_just_unbalanced(solution):
    """Test with a tree that is just unbalanced (difference = 2)."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right = TreeNode(5)
    assert solution.isBalanced(root) == False

def test_deep_balanced_tree(solution):
    """Test with a deeper but still balanced tree."""
    # Create a perfect binary tree of height 4
    root = TreeNode(1)
    
    # Level 2
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    # Level 3
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    # Level 4
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)
    
    assert solution.isBalanced(root) == True
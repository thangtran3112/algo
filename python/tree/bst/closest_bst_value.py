# https://leetcode.com/problems/closest-binary-search-tree-value/description/
"""
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

 

Example 1:


Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
Example 2:

Input: root = [1], target = 4.428571
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 109
-109 <= target <= 109
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root.val == target:
            return root.val
        if root.val < target:
            if root.right:
                closest_right = self.closestValue(root.right, target)
                # prefer smaller number with <=
                if abs(root.val - target) <= abs(closest_right - target):
                    return root.val
                else:
                    return closest_right
            else:
                # no right sub-tree, root.val is the result
                return root.val
        else:
            # pruning the right path, consisder the left path
            if root.left:
                closest_left = self.closestValue(root.left, target)
                # prefer smaller number with <=
                if abs(closest_left - target) <= abs(root.val - target):
                    return closest_left
                else:
                    return root.val
            else:
                # no left sub-tree, root.val is the result
                return root.val
            
# === TEST CASES ===
import pytest  # noqa: E402

# Helper function to build a BST from a list (level-order insertion, not ideal for BST but works for examples)
# A better approach for BST creation is needed for more complex trees
def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        if not root.left:
            root.left = TreeNode(val)
        else:
            insert_into_bst(root.left, val)
    else: # val >= root.val
        if not root.right:
            root.right = TreeNode(val)
        else:
            insert_into_bst(root.right, val)
    return root

def build_bst_from_list(values):
    if not values:
        return None
    root = None
    for val in values:
        if val is not None: # Handle potential Nones if using level-order list
             root = insert_into_bst(root, val)
    return root


@pytest.fixture
def solution():
    """Provides an instance of the Solution class."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    # root = [4,2,5,1,3]
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(5)
    target = 3.714286
    assert solution.closestValue(root, target) == 4

def test_example2(solution):
    """Test Example 2 from the problem description."""
    root = TreeNode(1)
    target = 4.428571
    assert solution.closestValue(root, target) == 1

def test_exact_match(solution):
    """Test when the target exactly matches a node value."""
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(5)
    target = 3.0
    assert solution.closestValue(root, target) == 3

def test_tie_smaller_value(solution):
    """Test tie-breaking: target is equidistant, choose smaller value."""
    # root = [2, 1, 3] target = 2.5 -> |1-2.5|=1.5, |2-2.5|=0.5, |3-2.5|=0.5. Tie between 2 and 3. Choose 2.
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    target = 2.5
    assert solution.closestValue(root, target) == 2

    # root = [5, 3, 7] target = 6.0 -> |5-6|=1, |7-6|=1. Tie between 5 and 7. Choose 5.
    root = TreeNode(5, TreeNode(3), TreeNode(7))
    target = 6.0
    assert solution.closestValue(root, target) == 5

def test_tie_larger_value_closer(solution):
    """Test tie-breaking: target is closer to larger value, but smaller value is also close."""
    # root = [4, 2, 5] target = 3.6 -> |2-3.6|=1.6, |3-3.6|=0.6, |4-3.6|=0.4, |5-3.6|=1.4
    # Closest is 4.
    root = TreeNode(4)
    root.left = TreeNode(2, None, TreeNode(3)) # Added 3
    root.right = TreeNode(5)
    target = 3.6
    assert solution.closestValue(root, target) == 4

def test_target_smaller_than_all(solution):
    """Test when the target is smaller than all node values."""
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(5)
    target = 0.5
    assert solution.closestValue(root, target) == 1

def test_target_larger_than_all(solution):
    """Test when the target is larger than all node values."""
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(5)
    target = 6.0
    assert solution.closestValue(root, target) == 5

def test_single_node_tree(solution):
    """Test with a single node tree."""
    root = TreeNode(10)
    target = 12.0
    assert solution.closestValue(root, target) == 10
    target = 8.0
    assert solution.closestValue(root, target) == 10

def test_left_skewed_tree(solution):
    """Test with a left-skewed tree."""
    root = TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1))))
    target = 2.1
    assert solution.closestValue(root, target) == 2
    target = 0.5
    assert solution.closestValue(root, target) == 1

def test_right_skewed_tree(solution):
    """Test with a right-skewed tree."""
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    target = 3.9
    assert solution.closestValue(root, target) == 4
    target = 1.1
    assert solution.closestValue(root, target) == 1

def test_negative_target(solution):
    """Test with a negative target (Node values are >= 0)."""
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(5)
    target = -1.0
    assert solution.closestValue(root, target) == 1

def test_large_values(solution):
    """Test with large values."""
    root = TreeNode(1000)
    root.left = TreeNode(500)
    root.right = TreeNode(1500)
    target = 1200.5
    # |1000-1200.5|=200.5, |1500-1200.5|=299.5
    assert solution.closestValue(root, target) == 1000

    target = 1250.0 # Tie between 1000 and 1500
    # |1000-1250|=250, |1500-1250|=250. Choose smaller 1000.
    assert solution.closestValue(root, target) == 1000

def test_complex_tree(solution):
    """Test with a more complex BST."""
    #       8
    #      / \
    #     3   10
    #    / \    \
    #   1   6    14
    #      / \   /
    #     4   7 13
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(14)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right.left = TreeNode(13)

    target = 5.0 # Closest is 4 or 6. |4-5|=1, |6-5|=1. Choose 4.
    assert solution.closestValue(root, target) == 4

    target = 11.5 # Closest is 10 or 13. |10-11.5|=1.5, |13-11.5|=1.5. Choose 10.
    assert solution.closestValue(root, target) == 10

    target = 13.6 # Closest is 13 or 14. |13-13.6|=0.6, |14-13.6|=0.4. Choose 14.
    assert solution.closestValue(root, target) == 14

    target = 0.0 # Closest is 1.
    assert solution.closestValue(root, target) == 1
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class SolutionIterative:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while curr:
            if curr.val == val:
                return curr
            if curr.val < val:
                # search right subtree
                curr = curr.right
            else:
                # search left subtree
                curr = curr.left

        return None

class SolutionRecursive:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        if val > root.val:
            return self.searchBST(root.right, val)
        return None
    
import pytest

@pytest.fixture
def iterative_solution():
    return SolutionIterative()

@pytest.fixture
def recursive_solution():
    return SolutionRecursive()

@pytest.fixture
def example_tree():
    """Create the example tree from the problem statement: [4,2,7,1,3]"""
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    return root

def test_example_1_iterative(iterative_solution, example_tree):
    """Test the first example from the problem statement with iterative solution."""
    result = iterative_solution.searchBST(example_tree, 2)
    assert result.val == 2
    assert result.left.val == 1
    assert result.right.val == 3

def test_example_1_recursive(recursive_solution, example_tree):
    """Test the first example from the problem statement with recursive solution."""
    result = recursive_solution.searchBST(example_tree, 2)
    assert result.val == 2
    assert result.left.val == 1
    assert result.right.val == 3

def test_example_2_iterative(iterative_solution, example_tree):
    """Test the second example from the problem statement with iterative solution."""
    result = iterative_solution.searchBST(example_tree, 5)
    assert result is None

def test_example_2_recursive(recursive_solution, example_tree):
    """Test the second example from the problem statement with recursive solution."""
    result = recursive_solution.searchBST(example_tree, 5)
    assert result is None

def test_root_value_iterative(iterative_solution, example_tree):
    """Test searching for the root value with iterative solution."""
    result = iterative_solution.searchBST(example_tree, 4)
    assert result is example_tree
    assert result.val == 4

def test_root_value_recursive(recursive_solution, example_tree):
    """Test searching for the root value with recursive solution."""
    result = recursive_solution.searchBST(example_tree, 4)
    assert result is example_tree
    assert result.val == 4

def test_leaf_node_iterative(iterative_solution, example_tree):
    """Test searching for a leaf node with iterative solution."""
    result = iterative_solution.searchBST(example_tree, 1)
    assert result.val == 1
    assert result.left is None
    assert result.right is None

def test_leaf_node_recursive(recursive_solution, example_tree):
    """Test searching for a leaf node with recursive solution."""
    result = recursive_solution.searchBST(example_tree, 1)
    assert result.val == 1
    assert result.left is None
    assert result.right is None

def test_right_subtree_iterative(iterative_solution, example_tree):
    """Test searching for a node in the right subtree with iterative solution."""
    result = iterative_solution.searchBST(example_tree, 7)
    assert result.val == 7

def test_right_subtree_recursive(recursive_solution, example_tree):
    """Test searching for a node in the right subtree with recursive solution."""
    result = recursive_solution.searchBST(example_tree, 7)
    assert result.val == 7

def test_empty_tree_iterative(iterative_solution):
    """Test searching in an empty tree with iterative solution."""
    result = iterative_solution.searchBST(None, 1)
    assert result is None

def test_empty_tree_recursive(recursive_solution):
    """Test searching in an empty tree with recursive solution."""
    result = recursive_solution.searchBST(None, 1)
    assert result is None

def test_single_node_found_iterative(iterative_solution):
    """Test searching in a single node tree with a value that exists with iterative solution."""
    root = TreeNode(1)
    result = iterative_solution.searchBST(root, 1)
    assert result is root
    assert result.val == 1

def test_single_node_found_recursive(recursive_solution):
    """Test searching in a single node tree with a value that exists with recursive solution."""
    root = TreeNode(1)
    result = recursive_solution.searchBST(root, 1)
    assert result is root
    assert result.val == 1

def test_single_node_not_found_iterative(iterative_solution):
    """Test searching in a single node tree with a value that does not exist with iterative solution."""
    root = TreeNode(1)
    result = iterative_solution.searchBST(root, 2)
    assert result is None

def test_single_node_not_found_recursive(recursive_solution):
    """Test searching in a single node tree with a value that does not exist with recursive solution."""
    root = TreeNode(1)
    result = recursive_solution.searchBST(root, 2)
    assert result is None

def test_larger_tree_iterative(iterative_solution):
    """Test with a larger tree with iterative solution."""
    # Create a larger BST
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(17)
    
    result = iterative_solution.searchBST(root, 13)
    assert result.val == 13

def test_larger_tree_recursive(recursive_solution):
    """Test with a larger tree with recursive solution."""
    # Create a larger BST
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(17)
    
    result = recursive_solution.searchBST(root, 13)
    assert result.val == 13

def test_boundary_values_iterative(iterative_solution):
    """Test with boundary values from the constraints with iterative solution."""
    # Create a tree with min and max values from constraints
    root = TreeNode(10**7)
    root.left = TreeNode(1)
    
    result = iterative_solution.searchBST(root, 1)
    assert result.val == 1
    
    result = iterative_solution.searchBST(root, 10**7)
    assert result.val == 10**7

def test_boundary_values_recursive(recursive_solution):
    """Test with boundary values from the constraints with recursive solution."""
    # Create a tree with min and max values from constraints
    root = TreeNode(10**7)
    root.left = TreeNode(1)
    
    result = recursive_solution.searchBST(root, 1)
    assert result.val == 1
    
    result = recursive_solution.searchBST(root, 10**7)
    assert result.val == 10**7
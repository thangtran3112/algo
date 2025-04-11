# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
                continue
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
                continue
            # common ancestor cannot be on left or right subtrees
            return curr

class SolutionRecursive:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val < p.val and root.val < q.val:
            # discard the left subtree
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            # discard the right subtree
            return self.lowestCommonAncestor(root.left, p, q)
        # since both left subtree and right subtree cannot be a common ancestor.
        # there is no other option, except this root node, can be the common ancestor.
        return root

class SolutionRecursiveNoBST:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q are presented on both left subtree and right subtree
        if left is not None and right is not None:
            return root
        # either left or right will be the lowest ancestor
        return left if left is not None else right

# Unit tests
import pytest

@pytest.fixture
def iterative_solution():
    return Solution()

@pytest.fixture
def recursive_solution():
    return SolutionRecursive()

@pytest.fixture
def general_solution():
    return SolutionRecursiveNoBST()

@pytest.fixture
def example_tree():
    """Create the example tree from the problem statement: [6,2,8,0,4,7,9,null,null,3,5]"""
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    return root

def test_example_1_iterative(iterative_solution, example_tree):
    """Test the first example from the problem statement with iterative solution."""
    p = example_tree.left  # Node with value 2
    q = example_tree.right  # Node with value 8
    result = iterative_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 6

def test_example_1_recursive(recursive_solution, example_tree):
    """Test the first example from the problem statement with recursive solution."""
    p = example_tree.left  # Node with value 2
    q = example_tree.right  # Node with value 8
    result = recursive_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 6

def test_example_1_general(general_solution, example_tree):
    """Test the first example from the problem statement with general solution."""
    p = example_tree.left  # Node with value 2
    q = example_tree.right  # Node with value 8
    result = general_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 6

def test_example_2_iterative(iterative_solution, example_tree):
    """Test the second example from the problem statement with iterative solution."""
    p = example_tree.left  # Node with value 2
    q = example_tree.left.right  # Node with value 4
    result = iterative_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 2

def test_example_2_recursive(recursive_solution, example_tree):
    """Test the second example from the problem statement with recursive solution."""
    p = example_tree.left  # Node with value 2
    q = example_tree.left.right  # Node with value 4
    result = recursive_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 2

def test_example_2_general(general_solution, example_tree):
    """Test the second example from the problem statement with general solution."""
    p = example_tree.left  # Node with value 2
    q = example_tree.left.right  # Node with value 4
    result = general_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 2

def test_example_3_iterative():
    """Test the third example from the problem statement with iterative solution."""
    root = TreeNode(2)
    root.left = TreeNode(1)
    
    solution = Solution()
    p = root  # Node with value 2
    q = root.left  # Node with value 1
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 2

def test_example_3_recursive():
    """Test the third example from the problem statement with recursive solution."""
    root = TreeNode(2)
    root.left = TreeNode(1)
    
    solution = SolutionRecursive()
    p = root  # Node with value 2
    q = root.left  # Node with value 1
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 2

def test_example_3_general():
    """Test the third example from the problem statement with general solution."""
    root = TreeNode(2)
    root.left = TreeNode(1)
    
    solution = SolutionRecursiveNoBST()
    p = root  # Node with value 2
    q = root.left  # Node with value 1
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 2

def test_nodes_in_same_subtree_iterative(iterative_solution, example_tree):
    """Test with both nodes in the same subtree with iterative solution."""
    p = example_tree.left.right.left  # Node with value 3
    q = example_tree.left.right.right  # Node with value 5
    result = iterative_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 4

def test_nodes_in_same_subtree_recursive(recursive_solution, example_tree):
    """Test with both nodes in the same subtree with recursive solution."""
    p = example_tree.left.right.left  # Node with value 3
    q = example_tree.left.right.right  # Node with value 5
    result = recursive_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 4

def test_nodes_in_same_subtree_general(general_solution, example_tree):
    """Test with both nodes in the same subtree with general solution."""
    p = example_tree.left.right.left  # Node with value 3
    q = example_tree.left.right.right  # Node with value 5
    result = general_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 4

def test_one_node_is_ancestor_iterative(iterative_solution, example_tree):
    """Test when one node is an ancestor of the other with iterative solution."""
    p = example_tree.left  # Node with value 2
    q = example_tree.left.right.left  # Node with value 3
    result = iterative_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 2

def test_one_node_is_ancestor_recursive(recursive_solution, example_tree):
    """Test when one node is an ancestor of the other with recursive solution."""
    p = example_tree.left  # Node with value 2
    q = example_tree.left.right.left  # Node with value 3
    result = recursive_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 2

def test_one_node_is_ancestor_general(general_solution, example_tree):
    """Test when one node is an ancestor of the other with general solution."""
    p = example_tree.left  # Node with value 2
    q = example_tree.left.right.left  # Node with value 3
    result = general_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 2

def test_root_is_lca_iterative(iterative_solution, example_tree):
    """Test when root is the LCA with iterative solution."""
    p = example_tree.left.left  # Node with value 0
    q = example_tree.right.right  # Node with value 9
    result = iterative_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 6

def test_root_is_lca_recursive(recursive_solution, example_tree):
    """Test when root is the LCA with recursive solution."""
    p = example_tree.left.left  # Node with value 0
    q = example_tree.right.right  # Node with value 9
    result = recursive_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 6

def test_root_is_lca_general(general_solution, example_tree):
    """Test when root is the LCA with general solution."""
    p = example_tree.left.left  # Node with value 0
    q = example_tree.right.right  # Node with value 9
    result = general_solution.lowestCommonAncestor(example_tree, p, q)
    assert result.val == 6

def test_boundary_values():
    """Test with boundary values from the constraints."""
    # Create a tree with boundary values
    root = TreeNode(0)
    root.left = TreeNode(-10**9)
    root.right = TreeNode(10**9)
    
    solution_iterative = Solution()
    solution_recursive = SolutionRecursive()
    solution_general = SolutionRecursiveNoBST()
    
    p = root.left  # Node with value -10^9
    q = root.right  # Node with value 10^9
    
    result_iterative = solution_iterative.lowestCommonAncestor(root, p, q)
    assert result_iterative.val == 0
    
    result_recursive = solution_recursive.lowestCommonAncestor(root, p, q)
    assert result_recursive.val == 0
    
    result_general = solution_general.lowestCommonAncestor(root, p, q)
    assert result_general.val == 0
    

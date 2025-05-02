# https://leetcode.com/problems/inorder-successor-in-bst/description/
"""
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
All Nodes will have unique values.
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
1. When p.val >= node.val that implies we can safely discard the left subtree since all the nodes there including the current node have values less than p
2. When we found the first root, where root.val > p.val, the successor will be within this subtree. Try going left as much as possible to find the successor
"""
class Solution:
    #            4
    #          /    \
    #        3      8
    #       /     /   \
    #      1     5    10
    #                 /
    #                9
    # Example:
    # 1st round: root = 4, root value < p=8, discard left tree of 4
    # 2nd round: root = 8, root value >= p=8, going right
    # 3rd round: root = 10, P < root value, now keep going left
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        while root:
            if p.val >= root.val:
                # entire left tree can be discard
                root = root.right
            else:
                # all nodes of this left path, will have root.val > p.val
                # keep moving left to find the successor
                successor = root
                root = root.left

        return successor

class SolutionEarlyExit:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        found = [False]
        result = []

        def inorder(node: TreeNode):
            if node.left:
                inorder(node.left)
            if found[0] is True:
                result.append(node)
                found[0] = False
                # early exit
                return
            if node == p:
                found[0] = True
            if node.right:
                inorder(node.right)

        inorder(root)
        return result[0] if len(result) > 0 else None

# Build the inorder array, and look for successor
class SolutionNotOptimize:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        result = []

        def inorder(node: TreeNode):
            if node.left:
                inorder(node.left)
            result.append(node)

            if node.right:
                inorder(node.right)

        inorder(root)

        for i in range(0, len(result)-1):
            if result[i] == p:
                return result[i+1]
        return None

# TEST CASES    
import pytest  # noqa: E402

@pytest.fixture
def optimized_solution():
    return Solution()

@pytest.fixture
def early_exit_solution():
    return SolutionEarlyExit()

@pytest.fixture
def unoptimized_solution():
    return SolutionNotOptimize()

def test_example_1_optimized(optimized_solution):
    """Test the first example from the problem statement with optimized solution."""
    # Create tree [2,1,3]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    p = root.left  # Node with value 1
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == 2

def test_example_1_early_exit(early_exit_solution):
    """Test the first example from the problem statement with early exit solution."""
    # Create tree [2,1,3]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    p = root.left  # Node with value 1
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor.val == 2

def test_example_1_unoptimized(unoptimized_solution):
    """Test the first example from the problem statement with unoptimized solution."""
    # Create tree [2,1,3]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    p = root.left  # Node with value 1
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor.val == 2

def test_example_2_optimized(optimized_solution):
    """Test the second example from the problem statement with optimized solution."""
    # Create tree [5,3,6,2,4,null,null,1]
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    
    p = root.right  # Node with value 6
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor is None

def test_example_2_early_exit(early_exit_solution):
    """Test the second example from the problem statement with early exit solution."""
    # Create tree [5,3,6,2,4,null,null,1]
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    
    p = root.right  # Node with value 6
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor is None

def test_example_2_unoptimized(unoptimized_solution):
    """Test the second example from the problem statement with unoptimized solution."""
    # Create tree [5,3,6,2,4,null,null,1]
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    
    p = root.right  # Node with value 6
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor is None

def test_single_node_optimized(optimized_solution):
    """Test with a single node tree with optimized solution."""
    root = TreeNode(1)
    p = root
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor is None

def test_single_node_early_exit(early_exit_solution):
    """Test with a single node tree with early exit solution."""
    root = TreeNode(1)
    p = root
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor is None

def test_single_node_unoptimized(unoptimized_solution):
    """Test with a single node tree with unoptimized solution."""
    root = TreeNode(1)
    p = root
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor is None

def test_linear_left_tree_optimized(optimized_solution):
    """Test with a linear left-skewed tree with optimized solution."""
    # Create tree [3,2,null,1]
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    
    # Test successor of 1
    p = root.left.left
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == 2

    # Test successor of 2
    p = root.left
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == 3

def test_linear_left_tree_early_exit(early_exit_solution):
    """Test with a linear left-skewed tree with early exit solution."""
    # Create tree [3,2,null,1]
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    
    # Test successor of 1
    p = root.left.left
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor.val == 2

    # Test successor of 2
    p = root.left
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor.val == 3

def test_linear_left_tree_unoptimized(unoptimized_solution):
    """Test with a linear left-skewed tree with unoptimized solution."""
    # Create tree [3,2,null,1]
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    
    # Test successor of 1
    p = root.left.left
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor.val == 2

    # Test successor of 2
    p = root.left
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor.val == 3

def test_linear_right_tree_optimized(optimized_solution):
    """Test with a linear right-skewed tree with optimized solution."""
    # Create tree [1,null,2,null,3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    
    # Test successor of 1
    p = root
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == 2

    # Test successor of 2
    p = root.right
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == 3

def test_linear_right_tree_early_exit(early_exit_solution):
    """Test with a linear right-skewed tree with early exit solution."""
    # Create tree [1,null,2,null,3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    
    # Test successor of 1
    p = root
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor.val == 2

    # Test successor of 2
    p = root.right
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor.val == 3

def test_linear_right_tree_unoptimized(unoptimized_solution):
    """Test with a linear right-skewed tree with unoptimized solution."""
    # Create tree [1,null,2,null,3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    
    # Test successor of 1
    p = root
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor.val == 2

    # Test successor of 2
    p = root.right
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor.val == 3

def test_complex_tree_optimized(optimized_solution):
    """Test with a more complex tree structure with optimized solution."""
    # Create tree [10,5,15,3,7,null,20]
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)
    
    # Test successor of 3
    p = root.left.left
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == 5

    # Test successor of 5
    p = root.left
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == 7

    # Test successor of 7
    p = root.left.right
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == 10

    # Test successor of 10
    p = root
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == 15

    # Test successor of 15
    p = root.right
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == 20

def test_complex_tree_early_exit(early_exit_solution):
    """Test with a more complex tree structure with early exit solution."""
    # Create tree [10,5,15,3,7,null,20]
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)
    
    # Test successor of 3
    p = root.left.left
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor.val == 5

    # Test successor of 5
    p = root.left
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor.val == 7

    # Test successor of 7
    p = root.left.right
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor.val == 10

    # Test successor of 10
    p = root
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor.val == 15

    # Test successor of 15
    p = root.right
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor.val == 20

def test_complex_tree_unoptimized(unoptimized_solution):
    """Test with a more complex tree structure with unoptimized solution."""
    # Create tree [10,5,15,3,7,null,20]
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)
    
    # Test successor of 3
    p = root.left.left
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor.val == 5

    # Test successor of 5
    p = root.left
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor.val == 7

    # Test successor of 7
    p = root.left.right
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor.val == 10

    # Test successor of 10
    p = root
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor.val == 15

    # Test successor of 15
    p = root.right
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor.val == 20

def test_negative_values_optimized(optimized_solution):
    """Test with negative values in the tree with optimized solution."""
    # Create tree [-10,-20,0,-30,-15]
    root = TreeNode(-10)
    root.left = TreeNode(-20)
    root.right = TreeNode(0)
    root.left.left = TreeNode(-30)
    root.left.right = TreeNode(-15)
    
    # Test successor of -30
    p = root.left.left
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == -20

    # Test successor of -20
    p = root.left
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == -15

def test_negative_values_early_exit(early_exit_solution):
    """Test with negative values in the tree with early exit solution."""
    # Create tree [-10,-20,0,-30,-15]
    root = TreeNode(-10)
    root.left = TreeNode(-20)
    root.right = TreeNode(0)
    root.left.left = TreeNode(-30)
    root.left.right = TreeNode(-15)
    
    # Test successor of -30
    p = root.left.left
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor.val == -20

    # Test successor of -20
    p = root.left
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor.val == -15

def test_negative_values_unoptimized(unoptimized_solution):
    """Test with negative values in the tree with unoptimized solution."""
    # Create tree [-10,-20,0,-30,-15]
    root = TreeNode(-10)
    root.left = TreeNode(-20)
    root.right = TreeNode(0)
    root.left.left = TreeNode(-30)
    root.left.right = TreeNode(-15)
    
    # Test successor of -30
    p = root.left.left
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor.val == -20

    # Test successor of -20
    p = root.left
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor.val == -15

def test_boundary_values_optimized(optimized_solution):
    """Test with boundary values from the constraints with optimized solution."""
    # Create tree with boundary values
    root = TreeNode(0)
    root.left = TreeNode(-100000)
    root.right = TreeNode(100000)
    
    p = root.left
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == 0

def test_boundary_values_early_exit(early_exit_solution):
    """Test with boundary values from the constraints with early exit solution."""
    # Create tree with boundary values
    root = TreeNode(0)
    root.left = TreeNode(-100000)
    root.right = TreeNode(100000)
    
    p = root.left
    successor = early_exit_solution.inorderSuccessor(root, p)
    assert successor.val == 0

def test_boundary_values_unoptimized(unoptimized_solution):
    """Test with boundary values from the constraints with unoptimized solution."""
    # Create tree with boundary values
    root = TreeNode(0)
    root.left = TreeNode(-100000)
    root.right = TreeNode(100000)
    
    p = root.left
    successor = unoptimized_solution.inorderSuccessor(root, p)
    assert successor.val == 0

def test_deep_tree_optimized(optimized_solution):
    """Test with a deeper tree structure with optimized solution."""
    # Create a deeper tree
    root = TreeNode(8)
    root.left = TreeNode(4)
    root.right = TreeNode(12)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    root.left.left.left = TreeNode(1)
    root.left.left.right = TreeNode(3)
    root.left.right.left = TreeNode(5)
    root.left.right.right = TreeNode(7)
    
    # Test successor of 3
    p = root.left.left.right  # Node with value 3
    successor = optimized_solution.inorderSuccessor(root, p)
    assert successor.val == 4
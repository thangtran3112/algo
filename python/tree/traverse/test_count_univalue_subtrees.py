import pytest
from count_univalue_subtrees import Solution, TreeNode

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    # Construct the tree [5,1,5,5,5,null,5]
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(5)
    
    assert solution.countUnivalSubtrees(root) == 4

def test_example_2(solution):
    """Test the second example - empty tree."""
    root = None
    assert solution.countUnivalSubtrees(root) == 0

def test_example_3(solution):
    """Test the third example - all nodes have the same value."""
    # Construct the tree [5,5,5,5,5,null,5]
    root = TreeNode(5)
    root.left = TreeNode(5)
    root.right = TreeNode(5)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(5)
    
    assert solution.countUnivalSubtrees(root) == 6

def test_single_node(solution):
    """Test a tree with a single node."""
    root = TreeNode(1)
    assert solution.countUnivalSubtrees(root) == 1

def test_two_nodes_same_value(solution):
    """Test a tree with two nodes having the same value."""
    root = TreeNode(1)
    root.left = TreeNode(1)
    assert solution.countUnivalSubtrees(root) == 2

def test_two_nodes_different_values(solution):
    """Test a tree with two nodes having different values."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    assert solution.countUnivalSubtrees(root) == 1

def test_three_nodes_same_value(solution):
    """Test a tree with three nodes having the same value."""
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    assert solution.countUnivalSubtrees(root) == 3

def test_three_nodes_different_values(solution):
    """Test a tree with three nodes having different values."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert solution.countUnivalSubtrees(root) == 2

def test_complex_tree(solution):
    """Test a more complex tree structure."""
    # Construct a more complex tree
    root = TreeNode(5)
    root.left = TreeNode(5)
    root.right = TreeNode(5)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    
    assert solution.countUnivalSubtrees(root) == 4

def test_negative_values(solution):
    """Test with negative values in the tree."""
    root = TreeNode(-5)
    root.left = TreeNode(-5)
    root.right = TreeNode(-5)
    
    assert solution.countUnivalSubtrees(root) == 3

def test_mixed_positive_negative(solution):
    """Test with a mix of positive and negative values."""
    root = TreeNode(0)
    root.left = TreeNode(-1)
    root.right = TreeNode(1)
    
    assert solution.countUnivalSubtrees(root) == 2

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    root = TreeNode(1000)
    root.left = TreeNode(1000)
    root.right = TreeNode(-1000)
    
    assert solution.countUnivalSubtrees(root) == 2

def test_deep_tree(solution):
    """Test with a deep tree structure."""
    # Create a deep tree where each node has only a left child
    root = TreeNode(1)
    current = root
    for i in range(2, 6):
        current.left = TreeNode(i)
        current = current.left
    
    assert solution.countUnivalSubtrees(root) == 1

def test_wide_tree(solution):
    """Test with a wide tree structure."""
    # Create a wide tree with all leaf nodes
    root = TreeNode(1)
    for i in range(5):
        if i % 2 == 0:
            node = TreeNode(1)  # Same value as root
        else:
            node = TreeNode(2)  # Different value
        
        if i < 2:
            root.left = node
            root.left = node
        else:
            root.right = node
            root.right = node
    
    # The tree will have root plus the last left and right nodes
    assert solution.countUnivalSubtrees(root) == 2
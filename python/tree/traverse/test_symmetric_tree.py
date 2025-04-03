import pytest
from symmetric_tree import Solution, SolutionTwoQueue, TreeNode

@pytest.fixture(params=[Solution, SolutionTwoQueue])
def solution(request):
    """Fixture that provides both solution implementations."""
    return request.param()

def test_example_1(solution):
    """Test the first example from the problem statement - symmetric tree."""
    # Construct tree: [1,2,2,3,4,4,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    
    assert solution.isSymmetric(root) is True

def test_example_2(solution):
    """Test the second example from the problem statement - asymmetric tree."""
    # Construct tree: [1,2,2,null,3,null,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    
    assert solution.isSymmetric(root) is False

def test_empty_tree(solution):
    """Test with an empty tree."""
    assert solution.isSymmetric(None) is True

def test_single_node(solution):
    """Test with a single node tree."""
    root = TreeNode(1)
    assert solution.isSymmetric(root) is True

def test_two_nodes_symmetric(solution):
    """Test with two nodes having the same value."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    assert solution.isSymmetric(root) is True

def test_two_nodes_asymmetric(solution):
    """Test with two nodes having different values."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert solution.isSymmetric(root) is False

def test_symmetric_different_values(solution):
    """Test a symmetric tree with different values at different levels."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(5)
    root.left.left.right = TreeNode(6)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)
    root.right.left.left = TreeNode(8)
    root.right.left.right = TreeNode(7)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(5)
    
    assert solution.isSymmetric(root) is True

def test_assymetric_structure(solution):
    """Test an asymmetric tree structure."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)  # This node makes it asymmetric
    
    assert solution.isSymmetric(root) is False

def test_assymetric_values(solution):
    """Test a tree with symmetric structure but asymmetric values."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)  # Different value makes it asymmetric
    root.right.right = TreeNode(3)
    
    assert solution.isSymmetric(root) is False

def test_negative_values(solution):
    """Test with negative values in a symmetric tree."""
    root = TreeNode(0)
    root.left = TreeNode(-10)
    root.right = TreeNode(-10)
    root.left.left = TreeNode(-20)
    root.right.right = TreeNode(-20)
    
    assert solution.isSymmetric(root) is True

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    root = TreeNode(0)
    root.left = TreeNode(-100)
    root.right = TreeNode(-100)
    root.left.left = TreeNode(100)
    root.right.right = TreeNode(100)
    
    assert solution.isSymmetric(root) is True

def test_deep_symmetric_tree(solution):
    """Test a deep symmetric tree."""
    # Create a deep symmetric tree
    root = TreeNode(1)
    
    # Level 1
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    
    # Level 2
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    
    # Level 3
    root.left.left.left = TreeNode(5)
    root.left.left.right = TreeNode(6)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)
    root.right.left.left = TreeNode(8)
    root.right.left.right = TreeNode(7)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(5)
    
    assert solution.isSymmetric(root) is True

def test_almost_symmetric_tree(solution):
    """Test a tree that is almost symmetric but has one different value."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)  # This should be 3 to be symmetric
    
    assert solution.isSymmetric(root) is False

def test_symmetric_structure_different_values(solution):
    """Test a tree with symmetric structure but completely different values."""
    root = TreeNode(1)
    
    # Level 1 - symmetric structure, different values
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    # Level 2 - symmetric structure, different values
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    assert solution.isSymmetric(root) is False

def test_partially_complete_tree(solution):
    """Test a partially complete tree that is symmetric."""
    root = TreeNode(1)
    
    # Level 1
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    
    # Level 2 - only some children
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    
    assert solution.isSymmetric(root) is True
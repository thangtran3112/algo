import pytest
from bst_inorder_successor import Solution, SolutionEarlyExit, SolutionNotOptimize, TreeNode
from typing import Optional

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
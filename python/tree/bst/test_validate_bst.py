import pytest
from validate_bst import Solution, SolutionRecursive, TreeNode

@pytest.fixture
def iterative_solution():
    return Solution()

@pytest.fixture
def recursive_solution():
    return SolutionRecursive()

def test_example_1_iterative(iterative_solution):
    """Test the first example from the problem statement with iterative solution."""
    # Construct tree [2,1,3]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    assert iterative_solution.isValidBST(root) == True

def test_example_1_recursive(recursive_solution):
    """Test the first example from the problem statement with recursive solution."""
    # Construct tree [2,1,3]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    assert recursive_solution.isValidBST(root) == True

def test_example_2_iterative(iterative_solution):
    """Test the second example from the problem statement with iterative solution."""
    # Construct tree [5,1,4,null,null,3,6]
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    
    assert iterative_solution.isValidBST(root) == False

def test_example_2_recursive(recursive_solution):
    """Test the second example from the problem statement with recursive solution."""
    # Construct tree [5,1,4,null,null,3,6]
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    
    assert recursive_solution.isValidBST(root) == False

def test_single_node_iterative(iterative_solution):
    """Test a tree with a single node with iterative solution."""
    root = TreeNode(1)
    assert iterative_solution.isValidBST(root) == True

def test_single_node_recursive(recursive_solution):
    """Test a tree with a single node with recursive solution."""
    root = TreeNode(1)
    assert recursive_solution.isValidBST(root) == True

def test_two_nodes_valid_iterative(iterative_solution):
    """Test a valid BST with two nodes with iterative solution."""
    root = TreeNode(2)
    root.left = TreeNode(1)
    assert iterative_solution.isValidBST(root) == True

def test_two_nodes_valid_recursive(recursive_solution):
    """Test a valid BST with two nodes with recursive solution."""
    root = TreeNode(2)
    root.left = TreeNode(1)
    assert recursive_solution.isValidBST(root) == True

def test_two_nodes_invalid_iterative(iterative_solution):
    """Test an invalid BST with two nodes with iterative solution."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    assert iterative_solution.isValidBST(root) == False

def test_two_nodes_invalid_recursive(recursive_solution):
    """Test an invalid BST with two nodes with recursive solution."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    assert recursive_solution.isValidBST(root) == False

def test_duplicate_values_iterative(iterative_solution):
    """Test BST validation with duplicate values with iterative solution."""
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    assert iterative_solution.isValidBST(root) == False

def test_duplicate_values_recursive(recursive_solution):
    """Test BST validation with duplicate values with recursive solution."""
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    assert recursive_solution.isValidBST(root) == False

def test_three_nodes_valid_iterative(iterative_solution):
    """Test a valid three-node BST with iterative solution."""
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert iterative_solution.isValidBST(root) == True

def test_three_nodes_valid_recursive(recursive_solution):
    """Test a valid three-node BST with recursive solution."""
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert recursive_solution.isValidBST(root) == True

def test_complex_valid_iterative(iterative_solution):
    """Test a more complex valid BST with iterative solution."""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(17)
    assert iterative_solution.isValidBST(root) == True

def test_complex_valid_recursive(recursive_solution):
    """Test a more complex valid BST with recursive solution."""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(17)
    assert recursive_solution.isValidBST(root) == True

def test_complex_invalid_iterative(iterative_solution):
    """Test a more complex invalid BST with iterative solution."""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(8)  # This should be greater than 10 to be valid
    root.right.right = TreeNode(17)
    assert iterative_solution.isValidBST(root) == False

def test_complex_invalid_recursive(recursive_solution):
    """Test a more complex invalid BST with recursive solution."""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(8)  # This should be greater than 10 to be valid
    root.right.right = TreeNode(17)
    assert recursive_solution.isValidBST(root) == False

def test_negative_values_valid_iterative(iterative_solution):
    """Test a valid BST with negative values with iterative solution."""
    root = TreeNode(0)
    root.left = TreeNode(-5)
    root.right = TreeNode(5)
    assert iterative_solution.isValidBST(root) == True

def test_negative_values_valid_recursive(recursive_solution):
    """Test a valid BST with negative values with recursive solution."""
    root = TreeNode(0)
    root.left = TreeNode(-5)
    root.right = TreeNode(5)
    assert recursive_solution.isValidBST(root) == True

def test_boundary_values_iterative(iterative_solution):
    """Test with boundary values from the constraints with iterative solution."""
    root = TreeNode(0)
    root.left = TreeNode(-2**31)
    root.right = TreeNode(2**31 - 1)
    assert iterative_solution.isValidBST(root) == True

def test_boundary_values_recursive(recursive_solution):
    """Test with boundary values from the constraints with recursive solution."""
    root = TreeNode(0)
    root.left = TreeNode(-2**31)
    root.right = TreeNode(2**31 - 1)
    assert recursive_solution.isValidBST(root) == True

def test_subtree_invalid_iterative(iterative_solution):
    """Test where a subtree violates BST property with iterative solution."""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(17)
    root.right.right.left = TreeNode(16)
    root.right.right.right = TreeNode(4)  # Invalid: 4 < 17
    assert iterative_solution.isValidBST(root) == False

def test_subtree_invalid_recursive(recursive_solution):
    """Test where a subtree violates BST property with recursive solution."""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(17)
    root.right.right.left = TreeNode(16)
    root.right.right.right = TreeNode(4)  # Invalid: 4 < 17
    assert recursive_solution.isValidBST(root) == False
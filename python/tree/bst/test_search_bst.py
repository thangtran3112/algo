import pytest
from search_bst import TreeNode, SolutionIterative, SolutionRecursive

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
import pytest
from insert_bst import TreeNode, Solution, SolutionRecursive

@pytest.fixture
def iterative_solution():
    return Solution()

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
    result = iterative_solution.insertIntoBST(example_tree, 5)
    
    # Verify structure remains correct
    assert result.val == 4
    assert result.left.val == 2
    assert result.right.val == 7
    assert result.left.left.val == 1
    assert result.left.right.val == 3
    
    # Verify insertion
    assert result.right.left.val == 5

def test_example_1_recursive(recursive_solution, example_tree):
    """Test the first example from the problem statement with recursive solution."""
    result = recursive_solution.insertIntoBST(example_tree, 5)
    
    # Verify structure remains correct
    assert result.val == 4
    assert result.left.val == 2
    assert result.right.val == 7
    assert result.left.left.val == 1
    assert result.left.right.val == 3
    
    # Verify insertion
    assert result.right.left.val == 5

def test_example_2_iterative(iterative_solution):
    """Test the second example from the problem statement with iterative solution."""
    # Construct tree [40,20,60,10,30,50,70]
    root = TreeNode(40)
    root.left = TreeNode(20)
    root.right = TreeNode(60)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(30)
    root.right.left = TreeNode(50)
    root.right.right = TreeNode(70)
    
    result = iterative_solution.insertIntoBST(root, 25)
    
    # Verify insertion
    assert result.left.right.left.val == 25

def test_example_2_recursive(recursive_solution):
    """Test the second example from the problem statement with recursive solution."""
    # Construct tree [40,20,60,10,30,50,70]
    root = TreeNode(40)
    root.left = TreeNode(20)
    root.right = TreeNode(60)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(30)
    root.right.left = TreeNode(50)
    root.right.right = TreeNode(70)
    
    result = recursive_solution.insertIntoBST(root, 25)
    
    # Verify insertion
    assert result.left.right.left.val == 25

def test_empty_tree_iterative(iterative_solution):
    """Test insertion into an empty tree with iterative solution."""
    root = None
    val = 5
    
    result = iterative_solution.insertIntoBST(root, val)
    assert result.val == val
    assert result.left is None
    assert result.right is None

def test_empty_tree_recursive(recursive_solution):
    """Test insertion into an empty tree with recursive solution."""
    root = None
    val = 5
    
    result = recursive_solution.insertIntoBST(root, val)
    assert result.val == val
    assert result.left is None
    assert result.right is None

def test_insert_smallest_iterative(iterative_solution, example_tree):
    """Test inserting the smallest value with iterative solution."""
    result = iterative_solution.insertIntoBST(example_tree, 0)
    
    # Verify insertion at leftmost position
    assert result.left.left.left.val == 0

def test_insert_smallest_recursive(recursive_solution, example_tree):
    """Test inserting the smallest value with recursive solution."""
    result = recursive_solution.insertIntoBST(example_tree, 0)
    
    # Verify insertion at leftmost position
    assert result.left.left.left.val == 0

def test_insert_largest_iterative(iterative_solution, example_tree):
    """Test inserting the largest value with iterative solution."""
    result = iterative_solution.insertIntoBST(example_tree, 10)
    
    # Verify insertion at rightmost position
    assert result.right.right.val == 10

def test_insert_largest_recursive(recursive_solution, example_tree):
    """Test inserting the largest value with recursive solution."""
    result = recursive_solution.insertIntoBST(example_tree, 10)
    
    # Verify insertion at rightmost position
    assert result.right.right.val == 10

def test_single_node_tree_iterative(iterative_solution):
    """Test insertion into a single node tree with iterative solution."""
    root = TreeNode(5)
    
    # Insert smaller value
    result = iterative_solution.insertIntoBST(root, 3)
    assert result.val == 5
    assert result.left.val == 3
    
    # Insert larger value
    result = iterative_solution.insertIntoBST(result, 7)
    assert result.val == 5
    assert result.left.val == 3
    assert result.right.val == 7

def test_single_node_tree_recursive(recursive_solution):
    """Test insertion into a single node tree with recursive solution."""
    root = TreeNode(5)
    
    # Insert smaller value
    result = recursive_solution.insertIntoBST(root, 3)
    assert result.val == 5
    assert result.left.val == 3
    
    # Insert larger value
    result = recursive_solution.insertIntoBST(result, 7)
    assert result.val == 5
    assert result.left.val == 3
    assert result.right.val == 7

def test_negative_values_iterative(iterative_solution):
    """Test with negative values in the tree with iterative solution."""
    root = TreeNode(0)
    root.left = TreeNode(-5)
    root.right = TreeNode(5)
    
    result = iterative_solution.insertIntoBST(root, -2)
    
    # Verify insertion
    assert result.left.right.val == -2

def test_negative_values_recursive(recursive_solution):
    """Test with negative values in the tree with recursive solution."""
    root = TreeNode(0)
    root.left = TreeNode(-5)
    root.right = TreeNode(5)
    
    result = recursive_solution.insertIntoBST(root, -2)
    
    # Verify insertion
    assert result.left.right.val == -2

def test_multiple_insertions_iterative(iterative_solution):
    """Test multiple insertions with iterative solution."""
    root = TreeNode(10)
    values = [5, 15, 3, 7, 12, 18]
    
    for val in values:
        root = iterative_solution.insertIntoBST(root, val)
    
    # Verify final structure
    assert root.val == 10
    assert root.left.val == 5
    assert root.right.val == 15
    assert root.left.left.val == 3
    assert root.left.right.val == 7
    assert root.right.left.val == 12
    assert root.right.right.val == 18

def test_multiple_insertions_recursive(recursive_solution):
    """Test multiple insertions with recursive solution."""
    root = TreeNode(10)
    values = [5, 15, 3, 7, 12, 18]
    
    for val in values:
        root = recursive_solution.insertIntoBST(root, val)
    
    # Verify final structure
    assert root.val == 10
    assert root.left.val == 5
    assert root.right.val == 15
    assert root.left.left.val == 3
    assert root.left.right.val == 7
    assert root.right.left.val == 12
    assert root.right.right.val == 18

def test_boundary_values_iterative(iterative_solution):
    """Test with boundary values from the constraints with iterative solution."""
    root = TreeNode(0)
    min_val = -10**8
    max_val = 10**8
    
    result = iterative_solution.insertIntoBST(root, min_val)
    result = iterative_solution.insertIntoBST(result, max_val)
    
    # Verify insertion
    assert result.left.val == min_val
    assert result.right.val == max_val

def test_boundary_values_recursive(recursive_solution):
    """Test with boundary values from the constraints with recursive solution."""
    root = TreeNode(0)
    min_val = -10**8
    max_val = 10**8
    
    result = recursive_solution.insertIntoBST(root, min_val)
    result = recursive_solution.insertIntoBST(result, max_val)
    
    # Verify insertion
    assert result.left.val == min_val
    assert result.right.val == max_val
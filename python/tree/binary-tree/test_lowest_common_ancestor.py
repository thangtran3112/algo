import pytest
from lowest_common_ancestor import TreeNode, SolutionRecursive, SolutionTreeFlatten

@pytest.fixture
def recursive_solution():
    return SolutionRecursive()

@pytest.fixture
def flatten_solution():
    return SolutionTreeFlatten()

def test_example_1_recursive(recursive_solution):
    """Test the first example from the problem with recursive solution."""
    # Build tree [3,5,1,6,2,0,8,null,null,7,4]
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    p = root.left  # Node 5
    q = root.right  # Node 1
    
    lca = recursive_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 3

def test_example_1_flatten(flatten_solution):
    """Test the first example from the problem with flatten solution."""
    # Build tree [3,5,1,6,2,0,8,null,null,7,4]
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    p = root.left  # Node 5
    q = root.right  # Node 1
    
    lca = flatten_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 3

def test_example_2_recursive(recursive_solution):
    """Test the second example from the problem with recursive solution."""
    # Build tree [3,5,1,6,2,0,8,null,null,7,4]
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    p = root.left  # Node 5
    q = root.left.right.right  # Node 4
    
    lca = recursive_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 5

def test_example_2_flatten(flatten_solution):
    """Test the second example from the problem with flatten solution."""
    # Build tree [3,5,1,6,2,0,8,null,null,7,4]
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    p = root.left  # Node 5
    q = root.left.right.right  # Node 4
    
    lca = flatten_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 5

def test_example_3_recursive(recursive_solution):
    """Test the third example from the problem with recursive solution."""
    # Build tree [1,2]
    root = TreeNode(1)
    root.left = TreeNode(2)
    
    p = root  # Node 1
    q = root.left  # Node 2
    
    lca = recursive_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 1

def test_example_3_flatten(flatten_solution):
    """Test the third example from the problem with flatten solution."""
    # Build tree [1,2]
    root = TreeNode(1)
    root.left = TreeNode(2)
    
    p = root  # Node 1
    q = root.left  # Node 2
    
    lca = flatten_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 1

def test_both_left_subtree_recursive(recursive_solution):
    """Test when both nodes are in the left subtree with recursive solution."""
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    
    p = root.left.left  # Node 6
    q = root.left.right  # Node 2
    
    lca = recursive_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 5

def test_both_left_subtree_flatten(flatten_solution):
    """Test when both nodes are in the left subtree with flatten solution."""
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    
    p = root.left.left  # Node 6
    q = root.left.right  # Node 2
    
    lca = flatten_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 5

def test_both_right_subtree_recursive(recursive_solution):
    """Test when both nodes are in the right subtree with recursive solution."""
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    
    p = root.right.left  # Node 0
    q = root.right.right  # Node 8
    
    lca = recursive_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 1

def test_both_right_subtree_flatten(flatten_solution):
    """Test when both nodes are in the right subtree with flatten solution."""
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    
    p = root.right.left  # Node 0
    q = root.right.right  # Node 8
    
    lca = flatten_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 1

def test_root_is_p_recursive(recursive_solution):
    """Test when root is one of the nodes (p) with recursive solution."""
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    
    p = root  # Node 3
    q = root.right  # Node 1
    
    lca = recursive_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 3

def test_root_is_p_flatten(flatten_solution):
    """Test when root is one of the nodes (p) with flatten solution."""
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    
    p = root  # Node 3
    q = root.right  # Node 1
    
    lca = flatten_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 3

def test_deep_tree_recursive(recursive_solution):
    """Test with a deeper tree with recursive solution."""
    # Create a deep tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    
    p = root.left.left.right  # Node 9
    q = root.left.right.left  # Node 10
    
    lca = recursive_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 2

def test_deep_tree_flatten(flatten_solution):
    """Test with a deeper tree with flatten solution."""
    # Create a deep tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    
    p = root.left.left.right  # Node 9
    q = root.left.right.left  # Node 10
    
    lca = flatten_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 2

def test_negative_values_recursive(recursive_solution):
    """Test with negative values in the tree with recursive solution."""
    root = TreeNode(-1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(-4)
    root.left.right = TreeNode(-5)
    
    p = root.left.left  # Node -4
    q = root.right  # Node -3
    
    lca = recursive_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == -1

def test_negative_values_flatten(flatten_solution):
    """Test with negative values in the tree with flatten solution."""
    root = TreeNode(-1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(-4)
    root.left.right = TreeNode(-5)
    
    p = root.left.left  # Node -4
    q = root.right  # Node -3
    
    lca = flatten_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == -1

def test_boundary_values_recursive(recursive_solution):
    """Test with boundary values from the constraints with recursive solution."""
    root = TreeNode(10**9)
    root.left = TreeNode(-(10**9))
    root.right = TreeNode(0)
    
    p = root.left  # Node -10^9
    q = root.right  # Node 0
    
    lca = recursive_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 10**9

def test_boundary_values_flatten(flatten_solution):
    """Test with boundary values from the constraints with flatten solution."""
    root = TreeNode(10**9)
    root.left = TreeNode(-(10**9))
    root.right = TreeNode(0)
    
    p = root.left  # Node -10^9
    q = root.right  # Node 0
    
    lca = flatten_solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 10**9
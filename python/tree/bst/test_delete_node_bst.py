import pytest
from delete_node_bst import Solution, TreeNode

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    # Construct tree [5,3,6,2,4,null,7]
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    
    result = solution.deleteNode(root, 3)
    
    # Check that the structure matches one of the valid answers
    assert result.val == 5
    assert result.right.val == 6
    assert result.right.right.val == 7
    
    # Either [5,4,6,2,null,null,7] or [5,2,6,null,4,null,7]
    if result.left.val == 4:
        assert result.left.left.val == 2
        assert result.left.right is None
    else:
        assert result.left.val == 2
        assert result.left.right.val == 4
        assert result.left.left is None

def test_example_2(solution):
    """Test the second example from the problem statement."""
    # Construct tree [5,3,6,2,4,null,7]
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    
    result = solution.deleteNode(root, 0)
    
    # Tree should remain unchanged
    assert result.val == 5
    assert result.left.val == 3
    assert result.right.val == 6
    assert result.left.left.val == 2
    assert result.left.right.val == 4
    assert result.right.right.val == 7

def test_example_3(solution):
    """Test the third example from the problem statement."""
    root = None
    result = solution.deleteNode(root, 0)
    assert result is None

def test_delete_root_no_children(solution):
    """Test deleting the root node with no children."""
    root = TreeNode(1)
    result = solution.deleteNode(root, 1)
    assert result is None

def test_delete_root_one_child_left(solution):
    """Test deleting the root node with only a left child."""
    root = TreeNode(2)
    root.left = TreeNode(1)
    
    result = solution.deleteNode(root, 2)
    assert result.val == 1
    assert result.left is None
    assert result.right is None

def test_delete_root_one_child_right(solution):
    """Test deleting the root node with only a right child."""
    root = TreeNode(1)
    root.right = TreeNode(2)
    
    result = solution.deleteNode(root, 1)
    assert result.val == 2
    assert result.left is None
    assert result.right is None

def test_delete_root_two_children(solution):
    """Test deleting the root node with two children."""
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    result = solution.deleteNode(root, 2)
    
    # The successor (3) should replace the root
    assert result.val == 3
    assert result.left.val == 1
    assert result.right is None

def test_delete_leaf_node(solution):
    """Test deleting a leaf node."""
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    
    result = solution.deleteNode(root, 3)
    assert result.val == 5
    assert result.left is None
    assert result.right.val == 7

def test_delete_node_with_left_child(solution):
    """Test deleting a node with only a left child."""
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    
    result = solution.deleteNode(root, 3)
    assert result.val == 5
    assert result.left.val == 1
    assert result.right is None

def test_delete_node_with_right_child(solution):
    """Test deleting a node with only a right child."""
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.right = TreeNode(4)
    
    result = solution.deleteNode(root, 3)
    assert result.val == 5
    assert result.left.val == 4
    assert result.right is None

def test_delete_node_with_two_children(solution):
    """Test deleting a node with two children."""
    # Construct a more complex tree
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.left.left.left = TreeNode(1)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(8)
    
    result = solution.deleteNode(root, 5)
    
    # The successor (6) should replace the deleted node
    assert result.val == 10
    assert result.left.val == 6  # Successor of 5
    assert result.left.left.val == 3
    assert result.left.right.val == 7
    assert result.left.right.right.val == 8
    # Make sure the successor was removed from its original position
    assert result.left.right.left is None

def test_delete_nonexistent_node(solution):
    """Test deleting a node that doesn't exist in the tree."""
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    
    result = solution.deleteNode(root, 10)
    
    # Tree should remain unchanged
    assert result.val == 5
    assert result.left.val == 3
    assert result.right.val == 7

def test_negative_values(solution):
    """Test with negative values in the tree."""
    root = TreeNode(0)
    root.left = TreeNode(-5)
    root.right = TreeNode(5)
    
    result = solution.deleteNode(root, -5)
    assert result.val == 0
    assert result.left is None
    assert result.right.val == 5

def test_complex_structure(solution):
    """Test with a more complex tree structure."""
    #        50
    #       /  \
    #     30    70
    #    / \   /  \
    #  20  40 60  80
    #             /
    #            75
    root = TreeNode(50)
    root.left = TreeNode(30)
    root.right = TreeNode(70)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(40)
    root.right.left = TreeNode(60)
    root.right.right = TreeNode(80)
    root.right.right.left = TreeNode(75)
    
    # Delete a node with two children and a successor with no left child
    result = solution.deleteNode(root, 70)
    
    assert result.val == 50
    assert result.right.val == 75  # Successor of 70
    assert result.right.left.val == 60
    assert result.right.right.val == 80
    assert result.right.right.left is None  # Successor was moved

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    root = TreeNode(0)
    root.left = TreeNode(-100000)
    root.right = TreeNode(100000)
    
    result = solution.deleteNode(root, -100000)
    assert result.val == 0
    assert result.left is None
    assert result.right.val == 100000

def test_delete_all_nodes_sequentially(solution):
    """Test deleting all nodes in the tree sequentially."""
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    
    # Delete all nodes one by one
    result = solution.deleteNode(root, 1)
    assert result.val == 3
    assert result.left.val == 2
    assert result.left.left is None
    
    result = solution.deleteNode(result, 2)
    assert result.val == 3
    assert result.left is None
    
    result = solution.deleteNode(result, 4)
    assert result.val == 3
    assert result.right is None
    
    result = solution.deleteNode(result, 3)
    assert result is None
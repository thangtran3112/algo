import pytest
from bst_iterator import BSTIterator, BSTIteratorRecursive, TreeNode

@pytest.fixture
def example_tree():
    """Create the example tree from the problem statement: [7,3,15,null,null,9,20]"""
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    return root

def test_example_iterative(example_tree):
    """Test the example from the problem statement with iterative solution."""
    iterator = BSTIterator(example_tree)
    
    assert iterator.next() == 3
    assert iterator.next() == 7
    assert iterator.hasNext() == True
    assert iterator.next() == 9
    assert iterator.hasNext() == True
    assert iterator.next() == 15
    assert iterator.hasNext() == True
    assert iterator.next() == 20
    assert iterator.hasNext() == False

def test_example_recursive(example_tree):
    """Test the example from the problem statement with recursive solution."""
    iterator = BSTIteratorRecursive(example_tree)
    
    assert iterator.next() == 3
    assert iterator.next() == 7
    assert iterator.hasNext() == True
    assert iterator.next() == 9
    assert iterator.hasNext() == True
    assert iterator.next() == 15
    assert iterator.hasNext() == True
    assert iterator.next() == 20
    assert iterator.hasNext() == False

def test_single_node_iterative():
    """Test with a single node tree with iterative solution."""
    root = TreeNode(1)
    iterator = BSTIterator(root)
    
    assert iterator.hasNext() == True
    assert iterator.next() == 1
    assert iterator.hasNext() == False

def test_single_node_recursive():
    """Test with a single node tree with recursive solution."""
    root = TreeNode(1)
    iterator = BSTIteratorRecursive(root)
    
    assert iterator.hasNext() == True
    assert iterator.next() == 1
    assert iterator.hasNext() == False

def test_linear_tree_left_iterative():
    """Test with a left-skewed tree with iterative solution."""
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(2)
    root.left.left.left.left = TreeNode(1)
    
    iterator = BSTIterator(root)
    
    assert iterator.next() == 1
    assert iterator.next() == 2
    assert iterator.next() == 3
    assert iterator.next() == 4
    assert iterator.next() == 5
    assert iterator.hasNext() == False

def test_linear_tree_left_recursive():
    """Test with a left-skewed tree with recursive solution."""
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(2)
    root.left.left.left.left = TreeNode(1)
    
    iterator = BSTIteratorRecursive(root)
    
    assert iterator.next() == 1
    assert iterator.next() == 2
    assert iterator.next() == 3
    assert iterator.next() == 4
    assert iterator.next() == 5
    assert iterator.hasNext() == False

def test_linear_tree_right_iterative():
    """Test with a right-skewed tree with iterative solution."""
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    root.right.right.right.right = TreeNode(5)
    
    iterator = BSTIterator(root)
    
    assert iterator.next() == 1
    assert iterator.next() == 2
    assert iterator.next() == 3
    assert iterator.next() == 4
    assert iterator.next() == 5
    assert iterator.hasNext() == False

def test_linear_tree_right_recursive():
    """Test with a right-skewed tree with recursive solution."""
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    root.right.right.right.right = TreeNode(5)
    
    iterator = BSTIteratorRecursive(root)
    
    assert iterator.next() == 1
    assert iterator.next() == 2
    assert iterator.next() == 3
    assert iterator.next() == 4
    assert iterator.next() == 5
    assert iterator.hasNext() == False

def test_balanced_tree_iterative():
    """Test with a balanced binary search tree with iterative solution."""
    # Create a balanced BST with values [1,2,3,4,5,6,7]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    
    iterator = BSTIterator(root)
    
    for i in range(1, 8):
        assert iterator.next() == i
    
    assert iterator.hasNext() == False

def test_balanced_tree_recursive():
    """Test with a balanced binary search tree with recursive solution."""
    # Create a balanced BST with values [1,2,3,4,5,6,7]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    
    iterator = BSTIteratorRecursive(root)
    
    for i in range(1, 8):
        assert iterator.next() == i
    
    assert iterator.hasNext() == False

def test_boundary_values_iterative():
    """Test with boundary values from the constraints with iterative solution."""
    # Create a tree with min and max values from constraints
    root = TreeNode(5)
    root.left = TreeNode(0)
    root.right = TreeNode(1000000)
    
    iterator = BSTIterator(root)
    
    assert iterator.next() == 0
    assert iterator.next() == 5
    assert iterator.next() == 1000000
    assert iterator.hasNext() == False

def test_boundary_values_recursive():
    """Test with boundary values from the constraints with recursive solution."""
    # Create a tree with min and max values from constraints
    root = TreeNode(5)
    root.left = TreeNode(0)
    root.right = TreeNode(1000000)
    
    iterator = BSTIteratorRecursive(root)
    
    assert iterator.next() == 0
    assert iterator.next() == 5
    assert iterator.next() == 1000000
    assert iterator.hasNext() == False

def test_interspersed_hasNext_iterative(example_tree):
    """Test with interspersed hasNext calls with iterative solution."""
    iterator = BSTIterator(example_tree)
    
    assert iterator.hasNext() == True
    assert iterator.next() == 3
    assert iterator.hasNext() == True
    assert iterator.hasNext() == True  # Multiple hasNext calls
    assert iterator.next() == 7
    assert iterator.hasNext() == True
    assert iterator.next() == 9
    assert iterator.next() == 15
    assert iterator.hasNext() == True
    assert iterator.next() == 20
    assert iterator.hasNext() == False
    assert iterator.hasNext() == False  # Multiple hasNext calls

def test_interspersed_hasNext_recursive(example_tree):
    """Test with interspersed hasNext calls with recursive solution."""
    iterator = BSTIteratorRecursive(example_tree)
    
    assert iterator.hasNext() == True
    assert iterator.next() == 3
    assert iterator.hasNext() == True
    assert iterator.hasNext() == True  # Multiple hasNext calls
    assert iterator.next() == 7
    assert iterator.hasNext() == True
    assert iterator.next() == 9
    assert iterator.next() == 15
    assert iterator.hasNext() == True
    assert iterator.next() == 20
    assert iterator.hasNext() == False
    assert iterator.hasNext() == False  # Multiple hasNext calls

def test_many_nodes_iterative():
    """Test with a larger tree to verify performance with iterative solution."""
    # Create a larger balanced BST
    values = list(range(0, 101))
    
    def build_balanced_bst(values, start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        node = TreeNode(values[mid])
        
        node.left = build_balanced_bst(values, start, mid - 1)
        node.right = build_balanced_bst(values, mid + 1, end)
        
        return node
    
    root = build_balanced_bst(values, 0, len(values) - 1)
    iterator = BSTIterator(root)
    
    for expected_val in values:
        assert iterator.hasNext() == True
        assert iterator.next() == expected_val
    
    assert iterator.hasNext() == False

def test_many_nodes_recursive():
    """Test with a larger tree to verify performance with recursive solution."""
    # Create a larger balanced BST
    values = list(range(0, 101))
    
    def build_balanced_bst(values, start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        node = TreeNode(values[mid])
        
        node.left = build_balanced_bst(values, start, mid - 1)
        node.right = build_balanced_bst(values, mid + 1, end)
        
        return node
    
    root = build_balanced_bst(values, 0, len(values) - 1)
    iterator = BSTIteratorRecursive(root)
    
    for expected_val in values:
        assert iterator.hasNext() == True
        assert iterator.next() == expected_val
    
    assert iterator.hasNext() == False
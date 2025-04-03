import pytest
from postorder_and_inorder import Solution, TreeNode

@pytest.fixture
def solution():
    return Solution()

# Helper function to verify a tree in level order (for assertion)
def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append(None)
        
        # Remove trailing None values
        while level and level[-1] is None:
            level.pop()
            
        result.extend(level)
    
    return result

def test_example_1(solution):
    # Example 1 from the problem statement
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    
    root = solution.buildTree(inorder, postorder)
    
    # Verify the tree structure
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left.val == 15
    assert root.right.right.val == 7

def test_example_2(solution):
    # Example 2 from the problem statement
    inorder = [-1]
    postorder = [-1]
    
    root = solution.buildTree(inorder, postorder)
    
    # Verify the tree structure
    assert root.val == -1
    assert root.left is None
    assert root.right is None

def test_empty_arrays(solution):
    # Empty arrays should return None
    inorder = []
    postorder = []
    
    root = solution.buildTree(inorder, postorder)
    
    assert root is None

def test_left_skewed_tree(solution):
    # Test a left-skewed tree
    inorder = [4, 3, 2, 1]
    postorder = [4, 3, 2, 1]
    
    root = solution.buildTree(inorder, postorder)
    
    # Verify the tree structure
    assert root.val == 1
    assert root.left.val == 2
    assert root.right is None
    assert root.left.left.val == 3
    assert root.left.left.left.val == 4

def test_right_skewed_tree(solution):
    # Test a right-skewed tree
    inorder = [1, 2, 3, 4]
    postorder = [4, 3, 2, 1]
    
    root = solution.buildTree(inorder, postorder)
    
    # Verify the tree structure
    assert root.val == 1
    assert root.right.val == 2
    assert root.left is None
    assert root.right.right.val == 3
    assert root.right.right.right.val == 4

def test_balanced_tree(solution):
    # Test a balanced tree
    inorder = [4, 2, 5, 1, 6, 3, 7]
    postorder = [4, 5, 2, 6, 7, 3, 1]
    
    root = solution.buildTree(inorder, postorder)
    
    # Verify the tree structure
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.left.left.val == 4
    assert root.left.right.val == 5
    assert root.right.left.val == 6
    assert root.right.right.val == 7

def test_negative_values(solution):
    # Test with negative values
    inorder = [-10, -5, -3, -1, 0]
    postorder = [-10, -5, -3, 0, -1]
    
    root = solution.buildTree(inorder, postorder)
    
    # Verify the tree structure
    assert root.val == -1
    assert root.left.val == -3
    assert root.right.val == 0
    assert root.left.left.val == -5
    assert root.left.left.left.val == -10

def test_max_constraint_values(solution):
    # Test with values at the edge of constraints (-3000 to 3000)
    inorder = [-3000, -1000, 0, 1000, 3000]
    postorder = [-3000, -1000, 1000, 3000, 0]
    
    root = solution.buildTree(inorder, postorder)
    
    # Verify the tree structure
    assert root.val == 0
    assert root.left.val == -1000
    assert root.right.val == 3000
    assert root.left.left.val == -3000
    assert root.right.left.val == 1000

def test_larger_tree(solution):
    # Test with a larger tree
    inorder = [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]
    postorder = [8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1]
    
    root = solution.buildTree(inorder, postorder)
    
    # Verify using level order traversal
    level_order = level_order_traversal(root)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    # Check if all expected nodes are in the tree
    for val in expected:
        assert val in level_order

def test_complete_binary_tree(solution):
    # Test with a complete binary tree
    inorder = [4, 2, 5, 1, 6, 3, 7]
    postorder = [4, 5, 2, 6, 7, 3, 1]
    
    root = solution.buildTree(inorder, postorder)
    
    # Verify using level order traversal
    level_order = level_order_traversal(root)
    expected = [1, 2, 3, 4, 5, 6, 7]
    
    # Check if all expected nodes are in the tree and in the right positions
    assert level_order == expected
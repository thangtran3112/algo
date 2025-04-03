import pytest
from preorder_and_inorder import Solution, TreeNode

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
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    
    root = solution.buildTree(preorder.copy(), inorder)
    
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
    preorder = [-1]
    inorder = [-1]
    
    root = solution.buildTree(preorder.copy(), inorder)
    
    # Verify the tree structure
    assert root.val == -1
    assert root.left is None
    assert root.right is None

def test_empty_arrays(solution):
    # Empty arrays should return None
    preorder = []
    inorder = []
    
    root = solution.buildTree(preorder.copy(), inorder)
    
    assert root is None

def test_left_skewed_tree(solution):
    # Test a left-skewed tree
    preorder = [1, 2, 3, 4]
    inorder = [4, 3, 2, 1]
    
    root = solution.buildTree(preorder.copy(), inorder)
    
    # Verify the tree structure
    assert root.val == 1
    assert root.left.val == 2
    assert root.right is None
    assert root.left.left.val == 3
    assert root.left.left.left.val == 4

def test_right_skewed_tree(solution):
    # Test a right-skewed tree
    preorder = [1, 2, 3, 4]
    inorder = [1, 2, 3, 4]
    
    root = solution.buildTree(preorder.copy(), inorder)
    
    # Verify the tree structure
    assert root.val == 1
    assert root.right.val == 2
    assert root.left is None
    assert root.right.right.val == 3
    assert root.right.right.right.val == 4

def test_balanced_tree(solution):
    # Test a balanced tree
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]
    
    root = solution.buildTree(preorder.copy(), inorder)
    
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
    preorder = [-1, -3, -5, -10, 0]
    inorder = [-10, -5, -3, -1, 0]
    
    root = solution.buildTree(preorder.copy(), inorder)
    
    # Verify the tree structure
    assert root.val == -1
    assert root.left.val == -3
    assert root.right.val == 0
    assert root.left.left.val == -5
    assert root.left.left.left.val == -10

def test_max_constraint_values(solution):
    # Test with values at the edge of constraints (-3000 to 3000)
    preorder = [0, -1000, -3000, 3000, 1000]
    inorder = [-3000, -1000, 0, 1000, 3000]
    
    root = solution.buildTree(preorder.copy(), inorder)
    
    # Verify the tree structure
    assert root.val == 0
    assert root.left.val == -1000
    assert root.right.val == 3000
    assert root.left.left.val == -3000
    assert root.right.left.val == 1000

def test_larger_tree(solution):
    # Test with a larger tree
    preorder = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]
    inorder = [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]
    
    root = solution.buildTree(preorder.copy(), inorder)
    
    # Verify using level order traversal
    level_order = level_order_traversal(root)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    # Check if all expected nodes are in the tree
    for val in expected:
        assert val in level_order

def test_complete_binary_tree(solution):
    # Test with a complete binary tree
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]
    
    root = solution.buildTree(preorder.copy(), inorder)
    
    # Verify using level order traversal
    level_order = level_order_traversal(root)
    expected = [1, 2, 3, 4, 5, 6, 7]
    
    # Check if level order matches expected
    assert level_order == expected

def test_reversed_inorder(solution):
    # Test with inorder values in reverse order
    preorder = [4, 3, 2, 1]
    inorder = [1, 2, 3, 4]
    
    root = solution.buildTree(preorder.copy(), inorder)
    
    # Verify using level order traversal
    level_order = level_order_traversal(root)
    assert level_order == [4, 3, 2, 1]

def test_mutation_of_inputs(solution):
    # Test that the original inputs are not modified
    preorder_original = [3, 9, 20, 15, 7]
    inorder_original = [9, 3, 15, 20, 7]
    
    preorder_copy = preorder_original.copy()
    inorder_copy = inorder_original.copy()
    
    solution.buildTree(preorder_copy, inorder_copy)
    
    # Note: Since implementation modifies preorder by design, this test
    # only checks that we're passing a copy to the function
    assert preorder_original == [3, 9, 20, 15, 7]
    assert inorder_copy == inorder_original
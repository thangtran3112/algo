# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])

        def buildTree(left: int, right: int):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = buildTree(left, mid - 1)
            node.right = buildTree(mid + 1, right)
            return node

        return buildTree(0, len(nums) -1 )
    
# Testing area

    
import pytest

@pytest.fixture
def solution():
    return Solution()

def is_height_balanced(root):
    """Helper function to check if a tree is height-balanced."""
    def height(node):
        if not node:
            return 0
        left_height = height(node.left)
        if left_height == -1:
            return -1  # Not balanced
        right_height = height(node.right)
        if right_height == -1:
            return -1  # Not balanced
        
        # Check if the subtree is balanced
        if abs(left_height - right_height) > 1:
            return -1  # Not balanced
        
        return max(left_height, right_height) + 1
    
    return height(root) != -1

def is_valid_bst(root):
    """Helper function to check if a tree is a valid BST."""
    def is_valid(node, min_val=float('-inf'), max_val=float('inf')):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (is_valid(node.left, min_val, node.val) and 
                is_valid(node.right, node.val, max_val))
    
    return is_valid(root)

def traverse_inorder(root):
    """Helper function to get inorder traversal of the tree."""
    result = []
    
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    
    inorder(root)
    return result

def test_example_1(solution):
    """Test the first example from the problem statement."""
    nums = [-10, -3, 0, 5, 9]
    result = solution.sortedArrayToBST(nums)
    
    # Check that the tree is height-balanced
    assert is_height_balanced(result)
    
    # Check that it's a valid BST
    assert is_valid_bst(result)
    
    # Check that inorder traversal gives the original sorted array
    assert traverse_inorder(result) == nums

def test_example_2(solution):
    """Test the second example from the problem statement."""
    nums = [1, 3]
    result = solution.sortedArrayToBST(nums)
    
    # Check that the tree is height-balanced
    assert is_height_balanced(result)
    
    # Check that it's a valid BST
    assert is_valid_bst(result)
    
    # Check that inorder traversal gives the original sorted array
    assert traverse_inorder(result) == nums

def test_single_element(solution):
    """Test with a single element array."""
    nums = [0]
    result = solution.sortedArrayToBST(nums)
    
    assert result.val == 0
    assert result.left is None
    assert result.right is None
    assert traverse_inorder(result) == nums

def test_three_elements(solution):
    """Test with a three-element array."""
    nums = [1, 2, 3]
    result = solution.sortedArrayToBST(nums)
    
    # For a three-element array, the middle element (2) should be the root
    assert result.val == 2
    assert result.left.val == 1
    assert result.right.val == 3
    
    # Check that the tree is height-balanced
    assert is_height_balanced(result)
    
    # Check that inorder traversal gives the original sorted array
    assert traverse_inorder(result) == nums

def test_larger_array(solution):
    """Test with a larger array."""
    nums = list(range(-10, 11))  # [-10, -9, ..., 9, 10]
    result = solution.sortedArrayToBST(nums)
    
    # Check that the tree is height-balanced
    assert is_height_balanced(result)
    
    # Check that it's a valid BST
    assert is_valid_bst(result)
    
    # Check that inorder traversal gives the original sorted array
    assert traverse_inorder(result) == nums

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    nums = [-10**4, 0, 10**4]
    result = solution.sortedArrayToBST(nums)
    
    # Check that the tree is height-balanced
    assert is_height_balanced(result)
    
    # Check that it's a valid BST
    assert is_valid_bst(result)
    
    # Check that inorder traversal gives the original sorted array
    assert traverse_inorder(result) == nums

def test_max_length_array(solution):
    """Test with an array of maximum allowed length."""
    # Create an array of length 10^4 (maximum allowed by constraints)
    nums = list(range(-5000, 5000))
    result = solution.sortedArrayToBST(nums)
    
    # Check that the tree is height-balanced
    assert is_height_balanced(result)
    
    # Check that it's a valid BST
    assert is_valid_bst(result)
    
    # Check that inorder traversal gives the original sorted array
    assert traverse_inorder(result) == nums
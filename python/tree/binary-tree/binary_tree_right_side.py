# https://leetcode.com/problems/binary-tree-right-side-view/description/
"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # Using BFS layer traversal from the right side 
        # If a level already have a node, next node in the same level
        # will not be added
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            isLevelFilled = False
            for _ in range(len(queue)):
                elem = queue.popleft()
                if not isLevelFilled:
                    result.append(elem.val)
                    isLevelFilled = True
                if elem.right:
                    queue.append(elem.right)
                if elem.left:
                    queue.append(elem.left)
        return result

class SolutionDFS:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # Using DFS to always go right first. if there is not right, go left
        # keep track of the level which has been filled
        occupied_level = -1
        result = []

        def dfs(node, level: int):
            if not node:
                return
            nonlocal occupied_level
            if level > occupied_level:
                # able to add to result
                result.append(node.val)
                occupied_level = level
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return result
    
# === TEST CASES ===
import pytest  # noqa: E402

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Helper function to build a binary tree from a list of values."""
    if not values or values[0] is None:
        return None
        
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
            
    return root

@pytest.fixture(params=[Solution, SolutionDFS],
               ids=["BFS", "DFS"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    root = build_tree([1, 2, 3, None, 5, None, 4])
    expected = [1, 3, 4]
    assert solution_instance.rightSideView(root) == expected

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    # Input: root = [1,2,3,4,null,null,null,5]
    root = build_tree([1, 2, 3, 4, None, None, None, 5])
    expected = [1, 3, 4, 5]
    assert solution_instance.rightSideView(root) == expected

def test_example3(solution_instance):
    """Test Example 3 from the problem description."""
    root = build_tree([1, None, 3])
    expected = [1, 3]
    assert solution_instance.rightSideView(root) == expected

def test_example4(solution_instance):
    """Test Example 4 from the problem description."""
    root = build_tree([])
    expected = []
    assert solution_instance.rightSideView(root) == expected

def test_single_node(solution_instance):
    """Test with a single node tree."""
    root = build_tree([1])
    expected = [1]
    assert solution_instance.rightSideView(root) == expected

def test_left_heavy_tree(solution_instance):
    """Test with a left-heavy tree."""
    root = build_tree([1, 2, None, 3, None, 4, None, 5])
    expected = [1, 2, 3, 4, 5]
    assert solution_instance.rightSideView(root) == expected

def test_right_heavy_tree(solution_instance):
    """Test with a right-heavy tree."""
    root = build_tree([1, None, 2, None, 3, None, 4, None, 5])
    expected = [1, 2, 3, 4, 5]
    assert solution_instance.rightSideView(root) == expected

def test_full_binary_tree(solution_instance):
    """Test with a full binary tree."""
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    expected = [1, 3, 7]
    assert solution_instance.rightSideView(root) == expected

def test_zigzag_tree(solution_instance):
    """Test with a zigzag-shaped tree."""
    root = build_tree([1, 2, None, None, 3, 4, None, None, 5])
    expected = [1, 2, 3, 4, 5]
    assert solution_instance.rightSideView(root) == expected

def test_complete_binary_tree(solution_instance):
    """Test with a complete binary tree."""
    root = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    expected = [1, 3, 7, 15]
    assert solution_instance.rightSideView(root) == expected

def test_negative_values(solution_instance):
    """Test with negative values."""
    root = build_tree([-1, -2, -3, -4, -5])
    expected = [-1, -3, -5]
    assert solution_instance.rightSideView(root) == expected

def test_max_constraints(solution_instance):
    """Test with values at the constraint boundaries."""
    root = build_tree([100, -100, 0])
    expected = [100, 0]
    assert solution_instance.rightSideView(root) == expected

def test_unbalanced_tree(solution_instance):
    """Test with an unbalanced tree."""
    # Create a tree with varying depths on left and right
    root = build_tree([1, 2, 3, 4, 5, None, 6, None, None, 7, 8])
    expected = [1, 3, 6, 8]
    assert solution_instance.rightSideView(root) == expected

def test_deep_tree(solution_instance):
    """Test with a deep tree."""
    # Create a tree with greater depth on one side
    values = [1]
    current = 2
    for _ in range(10):  # Create a tree with depth > 10
        values.extend([current, None])
        current += 1
    
    root = build_tree(values)
    expected = list(range(1, len(values) // 2 + 2))
    assert solution_instance.rightSideView(root) == expected


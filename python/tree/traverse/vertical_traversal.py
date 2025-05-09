# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # { index: [node1, node2, ...]} where index is the horizontal position
        graph = defaultdict(list)

        queue = deque()
        min_column = 0
        max_column = 0
        queue.append([root, 0])

        while queue:
            for _ in range(len(queue)):
                curr, index = queue.popleft()
                min_column = min(min_column, index)
                max_column = max(max_column, index)
                graph[index].append(curr.val)
                if curr.left:
                    queue.append([curr.left, index - 1])
                if curr.right:
                    queue.append([curr.right, index + 1])
        # we do not need to sort the key any more, we just 
        # need to check for key within [min_collumn, max_collumn]
        # sorted_keys = sorted(graph.keys())
        return [graph[x] for x in range(min_column, max_column + 1)]
    
# === TEST CASES ===
import pytest  # noqa: E402

# Helper function to build a binary tree from a list (following LeetCode's serialization format)
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
        
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
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

@pytest.fixture
def solution():
    """Provides an instance of the Solution class."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    root = build_tree([3, 9, 20, None, None, 15, 7])
    expected = [[9], [3, 15], [20], [7]]
    assert solution.verticalOrder(root) == expected

def test_example2(solution):
    """Test Example 2 from the problem description."""
    root = build_tree([3, 9, 8, 4, 0, 1, 7])
    expected = [[4], [9], [3, 0, 1], [8], [7]]
    assert solution.verticalOrder(root) == expected

def test_empty_tree(solution):
    """Test with an empty tree."""
    root = None
    expected = []
    assert solution.verticalOrder(root) == expected

def test_single_node(solution):
    """Test with a single node tree."""
    root = TreeNode(1)
    expected = [[1]]
    assert solution.verticalOrder(root) == expected

def test_left_skewed_tree(solution):
    """Test with a left-skewed tree."""
    root = build_tree([1, 2, None, 3, None, 4, None])
    expected = [[4], [3], [2], [1]]
    assert solution.verticalOrder(root) == expected

def test_right_skewed_tree(solution):
    """Test with a right-skewed tree."""
    root = build_tree([1, None, 2, None, 3, None, 4])
    expected = [[1], [2], [3], [4]]
    assert solution.verticalOrder(root) == expected

def test_same_row_column_order(solution):
    """Test the left-to-right order for nodes in the same row and column."""
    # Tree:
    #     1
    #    / \
    #   2   3
    #  / \ / \
    # 4  5 6  7
    # Node 5 and 6 are in the same column (0) and same row (depth 2)
    # BFS ensures 5 is processed before 6
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    expected = [[4], [2], [1, 5, 6], [3], [7]]
    assert solution.verticalOrder(root) == expected

def test_negative_values(solution):
    """Test with negative values."""
    root = build_tree([-1, -2, -3, None, None, -4, -5])
    expected = [[-2], [-1, -4], [-3], [-5]]
    assert solution.verticalOrder(root) == expected

def test_wider_tree(solution):
    """Test a tree that spreads wider horizontally."""
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.right.right.right = TreeNode(6)
    expected = [[5], [3], [1], [0], [2], [4], [6]]
    assert solution.verticalOrder(root) == expected
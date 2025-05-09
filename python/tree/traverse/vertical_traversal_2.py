# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/
# related: https://leetcode.com/problems/binary-tree-vertical-order-traversal/
"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
Example 2:


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
Example 3:


Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
"""

# Time O(n * log(n/k))
# Assuming we have k columns, each column parition have (n/k) values
# Each partition needs sorting, with (n/k).log(n/k) time complexity
# With k partitions (k columns). Time = k * (n/k) * log(n/k) = O(n * log(n/k))
from collections import defaultdict, deque
import heapq
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionBFSPartitionSort:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        graph = defaultdict(list)
        min_column = max_column = 0

        queue = deque()
        queue.append((root, 0, 0))  # row = 0, col = 0
        # Layer traversal
        while queue:
            for _ in range(len(queue)):
                node, row, col = queue.popleft()
                graph[col].append((row, node.val))
                min_column = min(min_column, col)
                max_column = max(max_column, col)

                if node.left:
                    queue.append((node.left, row + 1, col - 1))
                if node.right:
                    queue.append((node.right, row + 1, col + 1))
        # graph: { 0: [(row1, val1), (row2, val2), ...], -1 :[(row3, val3), ...] }
        # graph is grouped by column as index. It is already arranged from top to bottom
        # Except for nodes, which are in duplicate (row, col), it is arranged from left->right
        # However, we want to sort those duplicate nodes by value, not by left -> right positions

        ans = []
        for col in range(min_column, max_column + 1):
            # default (row, val): sort by row first. And then sort by val
            graph[col].sort() # same as  sort(key=lambda x: (x[0], x[1]))
            vals = [val for _row, val in graph[col]]
            ans.append(vals)
        return ans
    
# Time O(n * log(n/k))
class SolutionDFSHeapPartition:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        graph = defaultdict(list)
        min_column = max_column = 0

        def dfs(node, row, col):
            if not node:
                return
            nonlocal min_column, max_column
            min_column = min(min_column, col)
            max_column = max(max_column, col)
            # min heap with row sorting, and secondary sort key is node.val
            heapq.heappush(graph[col], (row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        ans = []
        for col in range(min_column, max_column + 1):
            curr_list = []
            while graph[col]:
                # extract data using heap property. heap element (row, val),
                # will sort by row and secondary col
                _row, val = heapq.heappop(graph[col])
                curr_list.append(val)
            ans.append(curr_list)
        return ans
    
import pytest  # noqa: E402

@pytest.fixture(params=[SolutionBFSPartitionSort, SolutionDFSHeapPartition], 
                ids=["BFS_Partition_Sort", "DFS_Heap_Partition"])
def solution(request):
    return request.param()

def create_tree(values):
    """Helper function to create a binary tree from a list of values (level-order traversal)."""
    if not values:
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

def test_example1(solution):
    """Test case from Example 1 in the problem description."""
    root = create_tree([3, 9, 20, None, None, 15, 7])
    result = solution.verticalTraversal(root)
    expected = [[9], [3, 15], [20], [7]]
    assert result == expected

def test_example2(solution):
    """Test case from Example 2 in the problem description."""
    root = create_tree([1, 2, 3, 4, 5, 6, 7])
    result = solution.verticalTraversal(root)
    expected = [[4], [2], [1, 5, 6], [3], [7]]
    assert result == expected

def test_example3(solution):
    """Test case from Example 3 in the problem description."""
    root = create_tree([1, 2, 3, 4, 6, 5, 7])
    result = solution.verticalTraversal(root)
    expected = [[4], [2], [1, 5, 6], [3], [7]]
    assert result == expected

def test_empty_tree(solution):
    """Test with an empty tree."""
    root = None
    result = solution.verticalTraversal(root)
    expected = []
    assert result == expected

def test_single_node(solution):
    """Test with a single node tree."""
    root = TreeNode(1)
    result = solution.verticalTraversal(root)
    expected = [[1]]
    assert result == expected

def test_left_skewed_tree(solution):
    """Test with a left-skewed tree."""
    root = create_tree([1, 2, None, 3, None, 4])
    result = solution.verticalTraversal(root)
    expected = [[4], [3], [2], [1]]
    assert result == expected

def test_right_skewed_tree(solution):
    """Test with a right-skewed tree."""
    root = create_tree([1, None, 2, None, 3, None, 4])
    result = solution.verticalTraversal(root)
    expected = [[1], [2], [3], [4]]
    assert result == expected

def test_complete_binary_tree(solution):
    """Test with a complete binary tree."""
    root = create_tree([1, 2, 3, 4, 5, 6, 7])
    result = solution.verticalTraversal(root)
    expected = [[4], [2], [1, 5, 6], [3], [7]]
    assert result == expected

def test_nodes_with_same_position_sorted_by_value(solution):
    """Test that nodes in the same position (row, col) are sorted by value."""
    # Create a tree where multiple nodes have the same position
    #      1
    #    /   \
    #   3     2
    #  / \   / \
    # 4   5 6   7
    root = create_tree([1, 3, 2, 4, 5, 6, 7])
    result = solution.verticalTraversal(root)
    expected = [[4], [3], [1, 5, 6], [2], [7]]
    assert result == expected

def test_complex_tree_with_duplicate_values(solution):
    """Test with a more complex tree that has duplicate values."""
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7
    #  / \
    # 8   9
    root = create_tree([1, 2, 3, 4, 5, 6, 7, 8, 9])
    result = solution.verticalTraversal(root)
    expected = [[8], [4], [2, 9], [1, 5, 6], [3], [7]]
    assert result == expected

def test_tree_with_duplicate_values_at_same_position(solution):
    """Test tree where multiple nodes have same position and same value."""
    # Create a custom tree where nodes have same position and value
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)  # Same value as left child
    
    result = solution.verticalTraversal(root)
    expected = [[4], [2], [1, 4], [3]]
    assert result == expected
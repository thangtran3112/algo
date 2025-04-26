# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
"""
from collections import deque
from typing import List, Optional
import pytest

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            path = []
            for _ in range(len(queue)):
                node = queue.popleft()
                path.append(node.val)
                queue.extend(node.children)
            result.append(path)

        return result
    
# === TEST CASES ===

@pytest.fixture
def solution():
    """Fixture to provide a Solution instance."""
    return Solution()

def build_n_ary_tree(values: List[Optional[int]]) -> Optional[Node]:
    """
    Helper function to build an N-ary tree from a list representation.
    This is a simplified builder for testing purposes. Manual building is often clearer.
    """
    if not values or values[0] is None:
        return None

    root = Node(values[0], [])
    queue = deque([(root, 1)])  # Store (node, index_of_first_child_in_values)

    while queue:
        parent, child_start_index = queue.popleft()
        
        # Find children for the current parent
        i = child_start_index
        children_nodes = []
        while i < len(values):
            if values[i] is None:
                # Null marks the end of children for this parent
                i += 1
                break
            
            child = Node(values[i], [])
            children_nodes.append(child)
            queue.append((child, i + 1)) # Child's children start after this child
            i += 1
        
        if children_nodes:
             parent.children = children_nodes
        
        # This builder is simplified and might not handle all LeetCode format nuances.

    return root

def test_example1(solution):
    """Test Example 1 from the problem description."""
    # Tree: [1,null,3,2,4,null,5,6]
    root = Node(1, [])
    child1 = Node(3, [])
    child2 = Node(2, [])
    child3 = Node(4, [])
    root.children = [child1, child2, child3]
    
    grandchild1 = Node(5, [])
    grandchild2 = Node(6, [])
    child1.children = [grandchild1, grandchild2]
    
    expected = [[1], [3, 2, 4], [5, 6]]
    assert solution.levelOrder(root) == expected

def test_example2(solution):
    """Test Example 2 from the problem description."""
    # Complex tree from example 2
    root = Node(1, [])
    child1 = Node(2, [])
    child2 = Node(3, [])
    child3 = Node(4, [])
    child4 = Node(5, [])
    root.children = [child1, child2, child3, child4]
    
    child2.children = [Node(6, []), Node(7, [])]
    child3.children = [Node(8, [])]
    child4.children = [Node(9, []), Node(10, [])]
    
    child2.children[1].children = [Node(11, [])]  # 7's child is 11
    child3.children[0].children = [Node(12, [])]  # 8's child is 12
    child4.children[0].children = [Node(13, [])]  # 9's child is 13
    
    child2.children[1].children[0].children = [Node(14, [])]  # 11's child is 14
    
    expected = [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]]
    assert solution.levelOrder(root) == expected

def test_empty_tree(solution):
    """Test with empty tree."""
    root = None
    assert solution.levelOrder(root) == []

def test_single_node(solution):
    """Test with a single node tree."""
    root = Node(1, [])
    expected = [[1]]
    assert solution.levelOrder(root) == expected

def test_node_without_children(solution):
    """Test with a node that has an empty children list."""
    root = Node(1, [])
    assert solution.levelOrder(root) == [[1]]

def test_node_with_empty_children_list(solution):
    """Test with a node that has children property as empty list."""
    root = Node(1, [])
    assert solution.levelOrder(root) == [[1]]

def test_two_level_tree(solution):
    """Test with a two-level tree."""
    root = Node(1, [])
    root.children = [Node(2, []), Node(3, []), Node(4, [])]
    expected = [[1], [2, 3, 4]]
    assert solution.levelOrder(root) == expected

def test_max_value_nodes(solution):
    """Test with nodes having maximum allowed value (10^4)."""
    root = Node(10000, [])
    child1 = Node(10000, [])
    child2 = Node(10000, [])
    root.children = [child1, child2]
    expected = [[10000], [10000, 10000]]
    assert solution.levelOrder(root) == expected

def test_deep_tree(solution):
    """Test with a deep tree approaching the height constraint."""
    current = Node(1, [])
    root = current
    
    # Create a deep path
    for i in range(2, 101):  # 100 levels deep
        child = Node(i, [])
        current.children = [child]
        current = child
    
    # Expected result is [[1], [2], [3], ..., [100]]
    expected = [[i] for i in range(1, 101)]
    assert solution.levelOrder(root) == expected

def test_wide_tree(solution):
    """Test with a wide tree (many children at one level)."""
    root = Node(1, [])
    # Add 100 children to root
    root.children = [Node(i, []) for i in range(2, 102)]
    
    expected = [[1], list(range(2, 102))]
    assert solution.levelOrder(root) == expected

def test_uneven_tree(solution):
    """Test with an uneven tree (different depths)."""
    root = Node(1, [])
    
    # First child has deep structure
    child1 = Node(2, [])
    child3 = Node(3, [])
    root.children = [child1, child3]
    
    # Create a deep path under child1
    current = child1
    for i in range(4, 10):
        child = Node(i, [])
        current.children = [child]
        current = child
    
    expected = [[1], [2, 3], [4], [5], [6], [7], [8], [9]]
    assert solution.levelOrder(root) == expected
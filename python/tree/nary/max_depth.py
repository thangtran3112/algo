# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5
 

Constraints:

The total number of nodes is in the range [0, 104].
The depth of the n-ary tree is less than or equal to 1000.
"""
from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
        
class SolutionDFS:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        max_depth = 0
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))
        return max_depth + 1

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        level = 0
        queue = deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                queue.extend(node.children)
            level += 1
        return level
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[SolutionDFS, Solution],
               ids=["DFS", "BFS"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def build_n_ary_tree(values: List[Optional[int]]) -> Optional[Node]:
    """
    Helper function to build an N-ary tree from a list representation.
    Simplified builder, manual construction is clearer for complex cases.
    """
    if not values or values[0] is None:
        return None

    root = Node(values[0], [])
    queue = deque([(root, 1)])  # (node, index_of_first_child_in_values)

    while queue:
        parent, child_start_index = queue.popleft()
        
        i = child_start_index
        children_nodes = []
        while i < len(values):
            if values[i] is None:
                i += 1
                break
            
            child = Node(values[i], [])
            children_nodes.append(child)
            queue.append((child, i + 1))
            i += 1
        
        if children_nodes:
             parent.children = children_nodes
             
    return root

def test_example1(solution_instance):
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
    
    expected = 3
    assert solution_instance.maxDepth(root) == expected

def test_example2(solution_instance):
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
    
    expected = 5
    assert solution_instance.maxDepth(root) == expected

def test_empty_tree(solution_instance):
    """Test with empty tree."""
    root = None
    assert solution_instance.maxDepth(root) == 0

def test_single_node(solution_instance):
    """Test with a single node tree."""
    root = Node(1, [])
    expected = 1
    assert solution_instance.maxDepth(root) == expected

def test_node_without_children(solution_instance):
    """Test with a node that has an empty children list."""
    root = Node(1, [])
    assert solution_instance.maxDepth(root) == 1

def test_node_with_empty_children_list(solution_instance):
    """Test with a node that has children property as empty list."""
    root = Node(1, [])
    assert solution_instance.maxDepth(root) == 1

def test_two_level_tree(solution_instance):
    """Test with a two-level tree."""
    root = Node(1, [])
    root.children = [Node(2, []), Node(3, []), Node(4, [])]
    expected = 2
    assert solution_instance.maxDepth(root) == expected

def test_deep_tree(solution_instance):
    """Test with a deep tree approaching the height constraint."""
    depth = 500 # Test a reasonably deep tree
    current = Node(depth, [])
    root = current
    
    # Create a deep path backwards
    for i in range(depth - 1, 0, -1):
        parent = Node(i, [current])
        current = parent
    root = current # The root is now node 1
    
    expected = depth
    assert solution_instance.maxDepth(root) == expected

def test_wide_tree(solution_instance):
    """Test with a wide tree (many children at one level)."""
    root = Node(1, [])
    # Add 100 children to root
    root.children = [Node(i, []) for i in range(2, 102)]
    
    expected = 2 # Root + one level of children
    assert solution_instance.maxDepth(root) == expected

def test_uneven_tree(solution_instance):
    """Test with an uneven tree (different depths)."""
    root = Node(1, [])
    
    # First child has deep structure
    child1 = Node(2, [])
    child3 = Node(3, []) # Shorter branch
    root.children = [child1, child3]
    
    # Create a deep path under child1
    current = child1
    depth_under_child1 = 8 # Total depth will be 1 (root) + 1 (child1) + 8 = 10
    for i in range(4, 4 + depth_under_child1):
        child = Node(i, [])
        current.children = [child]
        current = child
    
    assert solution_instance.maxDepth(root) == 10

def test_max_nodes(solution_instance):
    """Test with a large number of nodes (wide tree)."""
    # Create a tree with root and 10000 children (total 10001 nodes)
    root = Node(1, [])
    num_children = 5000 # Keep test reasonable
    root.children = [Node(i, []) for i in range(2, 2 + num_children)]
    
    expected = 2
    assert solution_instance.maxDepth(root) == expected
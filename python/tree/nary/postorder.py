# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

Example 1:


Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
"""

from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
        
class SolutionRecursive:
    def postorder(self, root: 'Node') -> List[int]:
        output = []

        def traverse(node):
            if not node:
                return
            for child in node.children:
                traverse(child)
            output.append(node.val)

        traverse(root)
        return output

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []
        stack = [root]
        if not root:
            return []
        while stack:
            node = stack.pop()
            output.append(node.val)
            for child in node.children:
                stack.append(child)

        output.reverse()
        return output
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[SolutionRecursive, Solution],
               ids=["Recursive", "Iterative"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def build_n_ary_tree(values: List[Optional[int]]) -> Optional[Node]:
    """
    Helper function to build an N-ary tree from a list representation.
    This is a simplified builder for testing purposes.
    """
    if not values or values[0] is None:
        return None

    root = Node(values[0], [])
    queue = [(root, 1)]  # Store (node, index_of_first_child_in_values)

    while queue:
        parent, child_start_index = queue.pop(0)
        
        # Find children for the current parent
        i = child_start_index
        while i < len(values):
            if values[i] is None:
                # Null marks the end of children for this parent
                i += 1
                break
            
            child = Node(values[i], [])
            parent.children.append(child)
            queue.append((child, i + 1)) # Child's children start after this child
            i += 1
        
        # Adjust child_start_index for the next node at the same level
        # This part is tricky with the LeetCode format, manual building is often clearer
        # For simplicity, this builder might not perfectly replicate LeetCode's complex format
        # but works for basic structures.

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
    
    expected = [5, 6, 3, 2, 4, 1]
    assert solution_instance.postorder(root) == expected

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
    
    expected = [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
    assert solution_instance.postorder(root) == expected

def test_empty_tree(solution_instance):
    """Test with empty tree."""
    root = None
    assert solution_instance.postorder(root) == []

def test_single_node(solution_instance):
    """Test with a single node tree."""
    root = Node(1, [])
    expected = [1]
    assert solution_instance.postorder(root) == expected

def test_node_without_children(solution_instance):
    """Test with a node that has an empty children list."""
    root = Node(1, [])
    assert solution_instance.postorder(root) == [1]

def test_node_with_empty_children_list(solution_instance):
    """Test with a node that has children property as empty list."""
    root = Node(1, [])
    assert solution_instance.postorder(root) == [1]

def test_two_level_tree(solution_instance):
    """Test with a two-level tree."""
    root = Node(1, [])
    root.children = [Node(2, []), Node(3, []), Node(4, [])]
    expected = [2, 3, 4, 1]
    assert solution_instance.postorder(root) == expected

def test_max_value_nodes(solution_instance):
    """Test with nodes having maximum allowed value (10^4)."""
    root = Node(10000, [])
    child1 = Node(10000, [])
    child2 = Node(10000, [])
    root.children = [child1, child2]
    expected = [10000, 10000, 10000]
    assert solution_instance.postorder(root) == expected

def test_deep_tree(solution_instance):
    """Test with a deep tree approaching the height constraint."""
    current = Node(100, []) # Start from 100
    root = current
    
    # Create a deep path backwards
    for i in range(99, 0, -1): # 100 levels deep
        parent = Node(i, [current])
        current = parent
    root = current # The root is now node 1
    
    # Expected result is [100, 99, ..., 2, 1]
    expected = list(range(100, 0, -1))
    assert solution_instance.postorder(root) == expected

def test_wide_tree(solution_instance):
    """Test with a wide tree (many children at one level)."""
    root = Node(1, [])
    # Add 100 children to root
    root.children = [Node(i, []) for i in range(2, 102)]
    
    expected = list(range(2, 102)) + [1]
    assert solution_instance.postorder(root) == expected

def test_uneven_tree(solution_instance):
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
    
    expected = [9, 8, 7, 6, 5, 4, 2, 3, 1]
    assert solution_instance.postorder(root) == expected
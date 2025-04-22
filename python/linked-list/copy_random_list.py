# https://leetcode.com/problems/copy-list-with-random-pointer/editorial/
"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # keeping a Hashmap of [copied_node, original_node]
        copy_map = {}
        inverted_map = {}
        if not head:
            return None
        
        prev = Node(-1)
        sentinel = prev
        while head:
            prev.next = Node(head.val)
            prev = prev.next
            copy_map[prev] = head
            inverted_map[head] = prev
            head = head.next
        
        # recreating random pointer
        cur = sentinel.next
        while cur:
            original = copy_map[cur]
            original_random = original.random
            # because original_random could be None, and will not be in inverted_map
            if original_random is not None:
                cur.random = inverted_map[original_random]
            cur = cur.next

        return sentinel.next
    
# === TEST CASES ===
import pytest  # noqa: E402

# Helper functions for creating and comparing linked lists with random pointers
def create_linked_list(values_and_random_indices):
    """
    Create a linked list with random pointers from a list of [val, random_index] pairs.
    """
    if not values_and_random_indices:
        return None
    
    # Create nodes without setting random pointers
    nodes = []
    for val, _ in values_and_random_indices:
        nodes.append(Node(val))
    
    # Connect next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Set random pointers
    for i, (_, random_index) in enumerate(values_and_random_indices):
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    
    return nodes[0]

def compare_linked_lists(list1, list2):
    """
    Compare two linked lists with random pointers.
    Returns True if they have the same structure and values, False otherwise.
    Also ensures that the copied list nodes are distinct from the original.
    """
    if list1 is None and list2 is None:
        return True
    
    if list1 is None or list2 is None:
        return False
    
    # Maps to track corresponding nodes in both lists
    original_to_copy = {}
    copy_to_original = {}
    
    node1, node2 = list1, list2
    
    # First pass: check values and next pointers
    while node1 and node2:
        if node1.val != node2.val:
            return False
        
        # Ensure nodes are distinct objects
        if node1 is node2:
            return False
        
        original_to_copy[node1] = node2
        copy_to_original[node2] = node1
        
        node1 = node1.next
        node2 = node2.next
    
    # Check if both lists ended at the same time
    if node1 is not None or node2 is not None:
        return False
    
    # Second pass: check random pointers
    node1, node2 = list1, list2
    while node1 and node2:
        # If original node's random is None, copied node's random should also be None
        if node1.random is None and node2.random is not None:
            return False
        if node1.random is not None and node2.random is None:
            return False
            
        # If original node's random points to a node, copied node's random should point
        # to the corresponding node in the copied list
        if node1.random is not None:
            if original_to_copy[node1.random] is not node2.random:
                return False
        
        node1 = node1.next
        node2 = node2.next
    
    return True

# Test cases
@pytest.fixture
def solution():
    """Fixture to provide a solution instance."""
    return Solution()

def test_empty_list(solution):
    """Test with an empty list."""
    head = None
    result = solution.copyRandomList(head)
    assert result is None

def test_example1(solution):
    """Test Example 1 from the problem description."""
    # [[7,null],[13,0],[11,4],[10,2],[1,0]]
    values_and_random_indices = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head = create_linked_list(values_and_random_indices)
    result = solution.copyRandomList(head)
    assert compare_linked_lists(head, result)
    
    # Ensure that the lists are distinct (deep copy)
    assert head is not result
    
    # Check random pointers
    original_node = head
    copied_node = result
    for _ in range(5):  # Traverse all 5 nodes
        if original_node.random is not None:
            # Nodes should be distinct but have same values
            assert original_node.random is not copied_node.random
            assert original_node.random.val == copied_node.random.val
        else:
            assert copied_node.random is None
        original_node = original_node.next
        copied_node = copied_node.next

def test_example2(solution):
    """Test Example 2 from the problem description."""
    # [[1,1],[2,1]]
    values_and_random_indices = [[1, 1], [2, 1]]
    head = create_linked_list(values_and_random_indices)
    result = solution.copyRandomList(head)
    assert compare_linked_lists(head, result)

def test_example3(solution):
    """Test Example 3 from the problem description."""
    # [[3,null],[3,0],[3,null]]
    values_and_random_indices = [[3, None], [3, 0], [3, None]]
    head = create_linked_list(values_and_random_indices)
    result = solution.copyRandomList(head)
    assert compare_linked_lists(head, result)

def test_self_reference(solution):
    """Test nodes that have random pointers pointing to themselves."""
    # Create a list where each node's random pointer points to itself
    values_and_random_indices = [[1, 0], [2, 1], [3, 2]]
    head = create_linked_list(values_and_random_indices)
    result = solution.copyRandomList(head)
    assert compare_linked_lists(head, result)

def test_circular_reference(solution):
    """Test with circular random pointers."""
    # Create a list with circular random pointers
    values_and_random_indices = [[1, 2], [2, 0], [3, 1]]
    head = create_linked_list(values_and_random_indices)
    result = solution.copyRandomList(head)
    assert compare_linked_lists(head, result)

def test_single_node(solution):
    """Test with a single node with random pointing to itself."""
    values_and_random_indices = [[1, 0]]
    head = create_linked_list(values_and_random_indices)
    result = solution.copyRandomList(head)
    assert compare_linked_lists(head, result)
    assert result.random is result  # Random pointer should point to itself

def test_single_node_null_random(solution):
    """Test with a single node with null random pointer."""
    values_and_random_indices = [[1, None]]
    head = create_linked_list(values_and_random_indices)
    result = solution.copyRandomList(head)
    assert compare_linked_lists(head, result)
    assert result.random is None  # Random pointer should be None

def test_all_random_null(solution):
    """Test with all random pointers being null."""
    values_and_random_indices = [[1, None], [2, None], [3, None], [4, None]]
    head = create_linked_list(values_and_random_indices)
    result = solution.copyRandomList(head)
    assert compare_linked_lists(head, result)
    
    # Verify all random pointers are null
    cur = result
    while cur:
        assert cur.random is None
        cur = cur.next

def test_long_list(solution):
    """Test with a longer list."""
    # Create a longer list of 10 nodes
    values_and_random_indices = [[i, (i+1) % 10 if i < 9 else None] for i in range(10)]
    head = create_linked_list(values_and_random_indices)
    result = solution.copyRandomList(head)
    assert compare_linked_lists(head, result)
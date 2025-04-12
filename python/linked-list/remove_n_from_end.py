# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        # using 2 pointers, fast and slow
        fast = head
        # sentinel -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None, n = 2, removedNode = 5
        for _ in range(n - 1):
            if fast:
                fast = fast.next

        # if fast is None, the list does not have enough Nth elements
        if not fast:
            return None

        # fast = 2
        slow = ListNode(-1)  # sentinel node
        slow.next = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        # fast = tail = 6, slow = 4

        # remove slow.next = 5
        if slow.next == head:
            # remove head case
            head = head.next
        else:
            # not removing head
            slow.next = slow.next.next
        return head
    
import pytest

def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Helper function to convert a linked list to a list for easier testing."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

@pytest.fixture
def solution():
    return Solution()

def test_remove_second_node_from_end(solution):
    """Test removing the second node from the end of the list."""
    head = create_linked_list([1, 2, 3, 4, 5])
    result = solution.removeNthFromEnd(head, 2)
    assert linked_list_to_list(result) == [1, 2, 3, 5]

def test_remove_head_when_single_node(solution):
    """Test removing the head when the list has only one node."""
    head = create_linked_list([1])
    result = solution.removeNthFromEnd(head, 1)
    assert result is None

def test_remove_last_node(solution):
    """Test removing the last node of the list."""
    head = create_linked_list([1, 2])
    result = solution.removeNthFromEnd(head, 1)
    assert linked_list_to_list(result) == [1]

def test_remove_head_from_multiple_nodes(solution):
    """Test removing the head when the list has multiple nodes."""
    head = create_linked_list([1, 2, 3, 4])
    result = solution.removeNthFromEnd(head, 4)
    assert linked_list_to_list(result) == [2, 3, 4]

def test_remove_middle_node(solution):
    """Test removing a middle node from the list."""
    head = create_linked_list([1, 2, 3, 4, 5])
    result = solution.removeNthFromEnd(head, 3)
    assert linked_list_to_list(result) == [1, 2, 4, 5]

def test_empty_list(solution):
    """Test with an empty list."""
    result = solution.removeNthFromEnd(None, 1)
    assert result is None

def test_n_exceeds_list_length(solution):
    """Test when n exceeds the list length."""
    head = create_linked_list([1, 2, 3])
    result = solution.removeNthFromEnd(head, 4)
    assert result is None

def test_remove_last_node_from_long_list(solution):
    """Test removing the last node from a longer list."""
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = solution.removeNthFromEnd(head, 1)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_remove_first_node_from_long_list(solution):
    """Test removing the first node from a longer list."""
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = solution.removeNthFromEnd(head, 10)
    assert linked_list_to_list(result) == [2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_nodes_with_duplicate_values(solution):
    """Test removing a node when there are duplicate values in the list."""
    head = create_linked_list([1, 2, 2, 3, 2])
    result = solution.removeNthFromEnd(head, 2)
    assert linked_list_to_list(result) == [1, 2, 2, 2]

def test_boundary_values(solution):
    """Test with boundary values according to the constraints."""
    # Create a list with maximum allowed node values (100)
    head = create_linked_list([100, 0, 100])
    result = solution.removeNthFromEnd(head, 2)
    assert linked_list_to_list(result) == [100, 100]

def test_consecutive_removals(solution):
    """Test removing multiple nodes consecutively."""
    head = create_linked_list([1, 2, 3, 4, 5])
    # First removal
    result1 = solution.removeNthFromEnd(head, 2)  # Remove 4
    assert linked_list_to_list(result1) == [1, 2, 3, 5]
    # Second removal
    result2 = solution.removeNthFromEnd(result1, 1)  # Remove 5
    assert linked_list_to_list(result2) == [1, 2, 3]
    # Third removal
    result3 = solution.removeNthFromEnd(result2, 3)  # Remove 1
    assert linked_list_to_list(result3) == [2, 3]

def test_all_same_values(solution):
    """Test with a list where all nodes have the same value."""
    head = create_linked_list([42, 42, 42, 42, 42])
    result = solution.removeNthFromEnd(head, 3)
    assert linked_list_to_list(result) == [42, 42, 42, 42]

def test_two_nodes_remove_second(solution):
    """Test removing the second node in a two-node list."""
    head = create_linked_list([1, 2])
    result = solution.removeNthFromEnd(head, 2)
    assert linked_list_to_list(result) == [2]

def test_edge_case_n_equals_list_length(solution):
    """Test when n equals the list length (should remove head)."""
    head = create_linked_list([1, 2, 3, 4, 5])
    result = solution.removeNthFromEnd(head, 5)
    assert linked_list_to_list(result) == [2, 3, 4, 5]

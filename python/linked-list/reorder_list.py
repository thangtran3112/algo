# https://leetcode.com/problems/reorder-list/description/
"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev = None
        curr = slow
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        # prev will become the new head of the reversed list

        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first = head
        second = prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

# === TEST CASES ===
import pytest  # noqa: E402


# Helper functions for creating and comparing linked lists
def create_linked_list(values):
    """Create a linked list from a list of values."""
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    """Convert a linked list to a list for easier comparison."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

@pytest.fixture
def solution():
    """Fixture to provide a solution instance."""
    return Solution()

def test_empty_list(solution):
    """Test with an empty list."""
    head = None
    solution.reorderList(head)
    assert head is None

def test_single_node(solution):
    """Test with a single node list."""
    head = create_linked_list([1])
    solution.reorderList(head)
    assert linked_list_to_list(head) == [1]

def test_two_nodes(solution):
    """Test with a two node list."""
    head = create_linked_list([1, 2])
    solution.reorderList(head)
    assert linked_list_to_list(head) == [1, 2]

def test_example1(solution):
    """Test Example 1 from the problem description."""
    head = create_linked_list([1, 2, 3, 4])
    solution.reorderList(head)
    assert linked_list_to_list(head) == [1, 4, 2, 3]

def test_example2(solution):
    """Test Example 2 from the problem description."""
    head = create_linked_list([1, 2, 3, 4, 5])
    solution.reorderList(head)
    assert linked_list_to_list(head) == [1, 5, 2, 4, 3]

def test_longer_list_even_length(solution):
    """Test with a longer list of even length."""
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    solution.reorderList(head)
    assert linked_list_to_list(head) == [1, 6, 2, 5, 3, 4]

def test_longer_list_odd_length(solution):
    """Test with a longer list of odd length."""
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    solution.reorderList(head)
    assert linked_list_to_list(head) == [1, 7, 2, 6, 3, 5, 4]

def test_all_same_values(solution):
    """Test with all nodes having the same value."""
    head = create_linked_list([5, 5, 5, 5])
    solution.reorderList(head)
    # Structure should change even if values are the same
    assert linked_list_to_list(head) == [5, 5, 5, 5]
    
    # We can't easily test the exact reordering since all values are the same,
    # but we can verify the function doesn't crash

def test_large_list(solution):
    """Test with a larger list."""
    values = list(range(1, 101))  # 1 to 100
    head = create_linked_list(values)
    solution.reorderList(head)
    
    # Expected reordering: 1, 100, 2, 99, 3, 98, ...
    expected = []
    for i in range(1, 51):
        expected.append(i)
        expected.append(101 - i)
    
    assert linked_list_to_list(head) == expected
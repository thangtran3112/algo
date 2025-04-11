# https://leetcode.com/problems/odd-even-linked-list/description/
"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        * Break down the list into 2 lists
        * OddList, keep head the same
        * EvenList, keep track of head, as even_head = head.next
        * Using slow and fast pointers, to break down the original list
        * For example: [2,1,3,5,6,4,7] will be broken down into 2 lists:
        * head: [2,3,6,7] and even_head: [1,5,4]
        * Connecting the tail of oddList to head of evenList
        """
        if not head or not head.next:
            return head
        even_head = head.next

        slow = head
        fast = head.next
        # [2,1,3,5,6,4,7]
        while slow and fast:
            # 1st loop: 2 -> (3,5,6,4,7), and 1 -> (3,5,6,4,7), slow = 2, fast = 1
            slow.next = fast.next
            #  1st loop: slow = 3, fast = 1
            slow = slow.next
            if fast.next:
                #  1st loop: fast=1 -> (5,6,4,7), slow= 3 -> (5,6,4,7)
                fast.next = slow.next
            #  1st loop: fast= 5 -> (6,4,7), slow = 3 -> (5,6,4,7)
            fast = fast.next

        # find the end of odd list
        curr = head
        while curr.next:
            curr = curr.next
        # connecting the tail of oddList with the head of even list
        curr.next = even_head

        return head

# TEST CASES

import pytest

@pytest.fixture
def solution():
    return Solution()

# Helper function to convert list to linked list
def list_to_linked_list(nums):
    dummy = ListNode(0)
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Helper function to convert linked list to list
def linked_list_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

def test_empty_list(solution):
    """Test with an empty list."""
    head = None
    result = solution.oddEvenList(head)
    assert result is None

def test_single_node(solution):
    """Test with a single node."""
    head = ListNode(1)
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [1]

def test_two_nodes(solution):
    """Test with two nodes."""
    head = list_to_linked_list([1, 2])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [1, 2]

def test_odd_number_of_nodes(solution):
    """Test with odd number of nodes."""
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [1, 3, 5, 2, 4]

def test_even_number_of_nodes(solution):
    """Test with even number of nodes."""
    head = list_to_linked_list([1, 2, 3, 4, 5, 6])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [1, 3, 5, 2, 4, 6]

def test_example_from_problem(solution):
    """Test with the example from the problem statement."""
    head = list_to_linked_list([2, 1, 3, 5, 6, 4, 7])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [2, 3, 6, 7, 1, 5, 4]

def test_repeated_values(solution):
    """Test with repeated values."""
    head = list_to_linked_list([1, 1, 1, 1, 1])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [1, 1, 1, 1, 1]

def test_negative_values(solution):
    """Test with negative values."""
    head = list_to_linked_list([-1, -2, -3, -4, -5])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [-1, -3, -5, -2, -4]

def test_large_list(solution):
    """Test with a larger list."""
    values = list(range(1, 21))  # 1 to 20
    head = list_to_linked_list(values)
    result = solution.oddEvenList(head)
    expected = [i for i in range(1, 21, 2)] + [i for i in range(2, 21, 2)]
    assert linked_list_to_list(result) == expected

def test_alternating_positive_negative(solution):
    """Test with alternating positive and negative values."""
    head = list_to_linked_list([1, -1, 2, -2, 3, -3])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [1, 2, 3, -1, -2, -3]

def test_ascending_values(solution):
    """Test with ascending values."""
    head = list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [1, 3, 5, 7, 2, 4, 6, 8]

def test_descending_values(solution):
    """Test with descending values."""
    head = list_to_linked_list([8, 7, 6, 5, 4, 3, 2, 1])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [8, 6, 4, 2, 7, 5, 3, 1]

def test_boundary_values(solution):
    """Test with boundary values from constraints."""
    head = list_to_linked_list([10**6, -(10**6), 10**6, -(10**6)])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [10**6, 10**6, -(10**6), -(10**6)]

def test_three_nodes(solution):
    """Test with exactly three nodes."""
    head = list_to_linked_list([1, 2, 3])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [1, 3, 2]
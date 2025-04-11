# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast:
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

# TEST CASES
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    # Create linked list [3,2,0,-4] with a cycle at position 1
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    # Create cycle: -4 -> 2
    head.next.next.next.next = head.next
    
    assert solution.hasCycle(head) == True

def test_example_2(solution):
    """Test the second example from the problem statement."""
    # Create linked list [1,2] with a cycle at position 0
    head = ListNode(1)
    head.next = ListNode(2)
    # Create cycle: 2 -> 1
    head.next.next = head
    
    assert solution.hasCycle(head) == True

def test_example_3(solution):
    """Test the third example from the problem statement."""
    # Create linked list [1] with no cycle
    head = ListNode(1)
    
    assert solution.hasCycle(head) == False

def test_empty_list(solution):
    """Test with an empty list."""
    head = None
    
    assert solution.hasCycle(head) == False

def test_long_list_no_cycle(solution):
    """Test with a longer list with no cycle."""
    # Create linked list [1,2,3,4,5]
    head = ListNode(1)
    current = head
    for i in range(2, 6):
        current.next = ListNode(i)
        current = current.next
    
    assert solution.hasCycle(head) == False

def test_long_list_with_cycle(solution):
    """Test with a longer list with a cycle."""
    # Create linked list [1,2,3,4,5] with a cycle 5 -> 3
    head = ListNode(1)
    current = head
    cycle_point = None
    
    for i in range(2, 6):
        current.next = ListNode(i)
        current = current.next
        if i == 3:
            cycle_point = current
    
    # Create cycle
    current.next = cycle_point
    
    assert solution.hasCycle(head) == True

def test_self_cycle(solution):
    """Test with a node pointing to itself."""
    head = ListNode(1)
    head.next = head
    
    assert solution.hasCycle(head) == True

def test_two_node_no_cycle(solution):
    """Test with two nodes and no cycle."""
    head = ListNode(1)
    head.next = ListNode(2)
    
    assert solution.hasCycle(head) == False

def test_cycle_at_end(solution):
    """Test with a cycle at the end of the list."""
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next.next.next
    
    assert solution.hasCycle(head) == True

def test_large_list(solution):
    """Test with a large list to verify performance."""
    head = ListNode(0)
    current = head
    
    # Create a list with 10000 nodes (maximum from constraints)
    for i in range(1, 10000):
        current.next = ListNode(i)
        current = current.next
    
    # No cycle
    assert solution.hasCycle(head) == False
    
    # Add cycle at the end
    current.next = head
    assert solution.hasCycle(head) == True

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    # Create a list with the min and max values
    head = ListNode(-10**5)
    head.next = ListNode(10**5)
    
    # No cycle
    assert solution.hasCycle(head) == False
    
    # Add cycle
    head.next.next = head
    assert solution.hasCycle(head) == True
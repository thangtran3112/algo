# https://leetcode.com/problems/linked-list-cycle-ii/description/
"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                break

        # The beginning list may be empty, or has a single node
        if not fast or not fast.next:
            return None

        # move slow from head, until it meets fast.
        # the meeting point is the start of the cycle
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

# TEST CASES
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    # Create linked list [3,2,0,-4] with a cycle at position 1
    head = ListNode(3)
    cycle_start = ListNode(2)
    head.next = cycle_start
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    # Create cycle: -4 -> 2
    head.next.next.next.next = cycle_start
    
    result = solution.detectCycle(head)
    assert result == cycle_start
    assert result.val == 2

def test_example_2(solution):
    """Test the second example from the problem statement."""
    # Create linked list [1,2] with a cycle at position 0
    head = ListNode(1)
    head.next = ListNode(2)
    # Create cycle: 2 -> 1
    head.next.next = head
    
    result = solution.detectCycle(head)
    assert result == head
    assert result.val == 1

def test_example_3(solution):
    """Test the third example from the problem statement."""
    # Create linked list [1] with no cycle
    head = ListNode(1)
    
    result = solution.detectCycle(head)
    assert result is None

def test_empty_list(solution):
    """Test with an empty list."""
    head = None
    
    result = solution.detectCycle(head)
    assert result is None

def test_single_node_no_cycle(solution):
    """Test with a single node and no cycle."""
    head = ListNode(1)
    
    result = solution.detectCycle(head)
    assert result is None

def test_single_node_with_self_cycle(solution):
    """Test with a single node pointing to itself."""
    head = ListNode(1)
    head.next = head
    
    result = solution.detectCycle(head)
    assert result == head
    assert result.val == 1

def test_long_list_no_cycle(solution):
    """Test with a longer list with no cycle."""
    # Create linked list [1,2,3,4,5]
    head = ListNode(1)
    current = head
    for i in range(2, 6):
        current.next = ListNode(i)
        current = current.next
    
    result = solution.detectCycle(head)
    assert result is None

def test_long_list_with_cycle_at_beginning(solution):
    """Test with a longer list with a cycle at the beginning."""
    # Create linked list [1,2,3,4,5] with a cycle 5 -> 1
    head = ListNode(1)
    current = head
    for i in range(2, 6):
        current.next = ListNode(i)
        current = current.next
    
    # Create cycle
    current.next = head
    
    result = solution.detectCycle(head)
    assert result == head
    assert result.val == 1

def test_long_list_with_cycle_in_middle(solution):
    """Test with a longer list with a cycle in the middle."""
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
    
    result = solution.detectCycle(head)
    assert result == cycle_point
    assert result.val == 3

def test_cycle_between_two_nodes(solution):
    """Test with a cycle between two nodes."""
    head = ListNode(1)
    node2 = ListNode(2)
    head.next = node2
    node2.next = head
    
    result = solution.detectCycle(head)
    assert result == head
    assert result.val == 1

def test_cycle_at_last_node(solution):
    """Test with a cycle at the last node."""
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    last_node = ListNode(4)
    head.next.next.next = last_node
    last_node.next = last_node  # Self-cycle
    
    result = solution.detectCycle(head)
    assert result == last_node
    assert result.val == 4

def test_large_list(solution):
    """Test with a large list to verify performance."""
    head = ListNode(0)
    current = head
    cycle_start = None
    
    # Create a list with 9999 nodes (close to the max from constraints)
    for i in range(1, 10000):
        current.next = ListNode(i)
        current = current.next
        # Mark a node in the middle as the cycle start
        if i == 5000:
            cycle_start = current
    
    # Create cycle at the end back to the middle
    current.next = cycle_start
    
    result = solution.detectCycle(head)
    assert result == cycle_start
    assert result.val == 5000

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    # Create a small list with the min and max values
    head = ListNode(-10**5)
    cycle_start = ListNode(0)
    head.next = cycle_start
    head.next.next = ListNode(10**5)
    
    # Add cycle
    head.next.next.next = cycle_start
    
    result = solution.detectCycle(head)
    assert result == cycle_start
    assert result.val == 0
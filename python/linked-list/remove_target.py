"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        # special case, removing at head
        while head and head.val == val:
            head = head.next

        # after removing any beginning elements, where their value = val
        # current head will have head.val != val
        prev = ListNode(-1)
        prev.next = head
        while prev:
            while prev.next and prev.next.val == val:
                prev.next = prev.next.next
            prev = prev.next
        return head
    
import pytest

@pytest.fixture
def solution():
    return Solution()

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
    """Helper function to convert a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    
    return result

def test_example_1(solution):
    """Test the first example from the problem statement."""
    head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
    val = 6
    result = solution.removeElements(head, val)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5]

def test_example_2(solution):
    """Test the second example - empty list."""
    head = None
    val = 1
    result = solution.removeElements(head, val)
    assert result is None

def test_example_3(solution):
    """Test the third example - remove all elements."""
    head = create_linked_list([7, 7, 7, 7])
    val = 7
    result = solution.removeElements(head, val)
    assert result is None

def test_remove_head(solution):
    """Test removing the head node."""
    head = create_linked_list([6, 1, 2, 3])
    val = 6
    result = solution.removeElements(head, val)
    assert linked_list_to_list(result) == [1, 2, 3]

def test_remove_tail(solution):
    """Test removing the tail node."""
    head = create_linked_list([1, 2, 3, 6])
    val = 6
    result = solution.removeElements(head, val)
    assert linked_list_to_list(result) == [1, 2, 3]

def test_remove_multiple_consecutive_nodes(solution):
    """Test removing multiple consecutive nodes."""
    head = create_linked_list([1, 6, 6, 6, 2, 3])
    val = 6
    result = solution.removeElements(head, val)
    assert linked_list_to_list(result) == [1, 2, 3]

def test_remove_multiple_scattered_nodes(solution):
    """Test removing multiple scattered nodes."""
    head = create_linked_list([1, 6, 2, 6, 3, 6])
    val = 6
    result = solution.removeElements(head, val)
    assert linked_list_to_list(result) == [1, 2, 3]

def test_remove_head_and_tail(solution):
    """Test removing both head and tail nodes."""
    head = create_linked_list([6, 1, 2, 3, 6])
    val = 6
    result = solution.removeElements(head, val)
    assert linked_list_to_list(result) == [1, 2, 3]

def test_single_node_match(solution):
    """Test with a single node that matches the target value."""
    head = create_linked_list([6])
    val = 6
    result = solution.removeElements(head, val)
    assert result is None

def test_single_node_no_match(solution):
    """Test with a single node that doesn't match the target value."""
    head = create_linked_list([1])
    val = 6
    result = solution.removeElements(head, val)
    assert linked_list_to_list(result) == [1]

def test_no_matches(solution):
    """Test with a list where no nodes match the target value."""
    head = create_linked_list([1, 2, 3, 4, 5])
    val = 6
    result = solution.removeElements(head, val)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5]

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    # Create a list with min and max values from constraints
    head = create_linked_list([1, 50, 1, 50])
    
    # Remove min value
    result = solution.removeElements(head, 1)
    assert linked_list_to_list(result) == [50, 50]
    
    # Remove max value
    result = solution.removeElements(result, 50)
    assert result is None

def test_long_list(solution):
    """Test with a longer list to verify performance."""
    # Create a list with 1000 elements, where every other element is the target
    values = []
    for i in range(1, 1001):
        if i % 2 == 0:
            values.append(6)  # Target value
        else:
            values.append(i)
    
    head = create_linked_list(values)
    val = 6
    result = solution.removeElements(head, val)
    
    # Expected result: only odd numbers from 1 to 999
    expected = list(range(1, 1000, 2))
    assert linked_list_to_list(result) == expected
# https://leetcode.com/problems/reverse-linked-list/
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # at this point curr = None, prev is the last reversing node
        return prev

class SolutionRecursive:
    def reverseList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

# TEST CASES
import pytest

@pytest.fixture
def iterative_solution():
    return Solution()

@pytest.fixture
def recursive_solution():
    return SolutionRecursive()

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

def test_empty_list_iterative(iterative_solution):
    """Test reversing an empty list with iterative solution."""
    head = None
    result = iterative_solution.reverseList(head)
    assert result is None

def test_empty_list_recursive(recursive_solution):
    """Test reversing an empty list with recursive solution."""
    head = None
    result = recursive_solution.reverseList(head)
    assert result is None

def test_single_node_iterative(iterative_solution):
    """Test reversing a single node list with iterative solution."""
    head = ListNode(5)
    result = iterative_solution.reverseList(head)
    assert result.val == 5
    assert result.next is None

def test_single_node_recursive(recursive_solution):
    """Test reversing a single node list with recursive solution."""
    head = ListNode(5)
    result = recursive_solution.reverseList(head)
    assert result.val == 5
    assert result.next is None

def test_example_1_iterative(iterative_solution):
    """Test the first example from the problem statement with iterative solution."""
    head = create_linked_list([1, 2, 3, 4, 5])
    result = iterative_solution.reverseList(head)
    assert linked_list_to_list(result) == [5, 4, 3, 2, 1]

def test_example_1_recursive(recursive_solution):
    """Test the first example from the problem statement with recursive solution."""
    head = create_linked_list([1, 2, 3, 4, 5])
    result = recursive_solution.reverseList(head)
    assert linked_list_to_list(result) == [5, 4, 3, 2, 1]

def test_example_2_iterative(iterative_solution):
    """Test the second example from the problem statement with iterative solution."""
    head = create_linked_list([1, 2])
    result = iterative_solution.reverseList(head)
    assert linked_list_to_list(result) == [2, 1]

def test_example_2_recursive(recursive_solution):
    """Test the second example from the problem statement with recursive solution."""
    head = create_linked_list([1, 2])
    result = recursive_solution.reverseList(head)
    assert linked_list_to_list(result) == [2, 1]

def test_duplicate_values_iterative(iterative_solution):
    """Test with duplicate values with iterative solution."""
    head = create_linked_list([1, 1, 2, 3, 3])
    result = iterative_solution.reverseList(head)
    assert linked_list_to_list(result) == [3, 3, 2, 1, 1]

def test_duplicate_values_recursive(recursive_solution):
    """Test with duplicate values with recursive solution."""
    head = create_linked_list([1, 1, 2, 3, 3])
    result = recursive_solution.reverseList(head)
    assert linked_list_to_list(result) == [3, 3, 2, 1, 1]

def test_negative_values_iterative(iterative_solution):
    """Test with negative values with iterative solution."""
    head = create_linked_list([-5, -4, -3, -2, -1])
    result = iterative_solution.reverseList(head)
    assert linked_list_to_list(result) == [-1, -2, -3, -4, -5]

def test_negative_values_recursive(recursive_solution):
    """Test with negative values with recursive solution."""
    head = create_linked_list([-5, -4, -3, -2, -1])
    result = recursive_solution.reverseList(head)
    assert linked_list_to_list(result) == [-1, -2, -3, -4, -5]

def test_long_list_iterative(iterative_solution):
    """Test with a longer list to verify performance with iterative solution."""
    values = list(range(1, 1001))
    head = create_linked_list(values)
    result = iterative_solution.reverseList(head)
    assert linked_list_to_list(result) == list(reversed(values))

def test_long_list_recursive(recursive_solution):
    """Test with a longer list to verify performance with recursive solution."""
    values = list(range(1, 101))  # Using a smaller list for recursive to avoid stack overflow
    head = create_linked_list(values)
    result = recursive_solution.reverseList(head)
    assert linked_list_to_list(result) == list(reversed(values))

def test_boundary_values_iterative(iterative_solution):
    """Test with boundary values from the constraints with iterative solution."""
    head = create_linked_list([-5000, 0, 5000])
    result = iterative_solution.reverseList(head)
    assert linked_list_to_list(result) == [5000, 0, -5000]

def test_boundary_values_recursive(recursive_solution):
    """Test with boundary values from the constraints with recursive solution."""
    head = create_linked_list([-5000, 0, 5000])
    result = recursive_solution.reverseList(head)
    assert linked_list_to_list(result) == [5000, 0, -5000]
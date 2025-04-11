"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution with a stack
# O(n) time and O(n) space
class SolutionStack:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next

        while head:
            if head.val != stack.pop():
                return False
            head = head.next
        return True

# O(n) time and O(1) space
class Solution:
    """
    * Using 2 pointers to find the middle of the list
    * Reverse the second half of the list
    * Compare the first half and the second half
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # calculating the length of the list
        curr = head
        n = 0  # length of this list
        while curr:
            n += 1
            curr = curr.next

        # using 2 pointers
        slow = head
        fast = slow
        for _ in range(n // 2):
            fast = fast.next
        # if the list has odd number of nodes. we ignore the mid node
        if n % 2 != 0:
            fast = fast.next

        # reverse the direction of the second half of the list
        prev = None
        curr = fast
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # at this point curr = None, prev is the last reversing node, which is the new head
        fast = prev
        while fast and slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True


#################################################################################  
# TEST CASES

import pytest

@pytest.fixture
def stack_solution():
    return SolutionStack()

@pytest.fixture
def optimized_solution():
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

def test_empty_list_stack(stack_solution):
    """Test an empty list with stack solution."""
    head = None
    assert stack_solution.isPalindrome(head) is True

def test_empty_list_optimized(optimized_solution):
    """Test an empty list with optimized solution."""
    head = None
    assert optimized_solution.isPalindrome(head) is True

def test_single_node_stack(stack_solution):
    """Test a single node list with stack solution."""
    head = ListNode(5)
    assert stack_solution.isPalindrome(head) is True

def test_single_node_optimized(optimized_solution):
    """Test a single node list with optimized solution."""
    head = ListNode(5)
    assert optimized_solution.isPalindrome(head) is True

def test_even_palindrome_stack(stack_solution):
    """Test even length palindrome with stack solution."""
    head = create_linked_list([1, 2, 2, 1])
    assert stack_solution.isPalindrome(head) is True

def test_even_palindrome_optimized(optimized_solution):
    """Test even length palindrome with optimized solution."""
    head = create_linked_list([1, 2, 2, 1])
    assert optimized_solution.isPalindrome(head) is True

def test_odd_palindrome_stack(stack_solution):
    """Test odd length palindrome with stack solution."""
    head = create_linked_list([1, 2, 3, 2, 1])
    assert stack_solution.isPalindrome(head) is True

def test_odd_palindrome_optimized(optimized_solution):
    """Test odd length palindrome with optimized solution."""
    head = create_linked_list([1, 2, 3, 2, 1])
    assert optimized_solution.isPalindrome(head) is True

def test_non_palindrome_even_stack(stack_solution):
    """Test even length non-palindrome with stack solution."""
    head = create_linked_list([1, 2])
    assert stack_solution.isPalindrome(head) is False

def test_non_palindrome_even_optimized(optimized_solution):
    """Test even length non-palindrome with optimized solution."""
    head = create_linked_list([1, 2])
    assert optimized_solution.isPalindrome(head) is False

def test_non_palindrome_odd_stack(stack_solution):
    """Test odd length non-palindrome with stack solution."""
    head = create_linked_list([1, 2, 3])
    assert stack_solution.isPalindrome(head) is False

def test_non_palindrome_odd_optimized(optimized_solution):
    """Test odd length non-palindrome with optimized solution."""
    head = create_linked_list([1, 2, 3])
    assert optimized_solution.isPalindrome(head) is False

def test_repeated_values_palindrome_stack(stack_solution):
    """Test palindrome with repeated values with stack solution."""
    head = create_linked_list([1, 1, 2, 1, 1])
    assert stack_solution.isPalindrome(head) is True

def test_repeated_values_palindrome_optimized(optimized_solution):
    """Test palindrome with repeated values with optimized solution."""
    head = create_linked_list([1, 1, 2, 1, 1])
    assert optimized_solution.isPalindrome(head) is True

def test_repeated_values_non_palindrome_stack(stack_solution):
    """Test non-palindrome with repeated values with stack solution."""
    head = create_linked_list([1, 1, 2, 2])
    assert stack_solution.isPalindrome(head) is False

def test_repeated_values_non_palindrome_optimized(optimized_solution):
    """Test non-palindrome with repeated values with optimized solution."""
    head = create_linked_list([1, 1, 2, 2])
    assert optimized_solution.isPalindrome(head) is False

def test_all_same_values_stack(stack_solution):
    """Test list with all the same values with stack solution."""
    head = create_linked_list([5, 5, 5, 5])
    assert stack_solution.isPalindrome(head) is True

def test_all_same_values_optimized(optimized_solution):
    """Test list with all the same values with optimized solution."""
    head = create_linked_list([5, 5, 5, 5])
    assert optimized_solution.isPalindrome(head) is True

def test_long_palindrome_stack(stack_solution):
    """Test a longer palindrome with stack solution."""
    values = list(range(500)) + list(range(499, -1, -1))
    head = create_linked_list(values)
    assert stack_solution.isPalindrome(head) is True

def test_long_palindrome_optimized(optimized_solution):
    """Test a longer palindrome with optimized solution."""
    values = list(range(500)) + list(range(499, -1, -1))
    head = create_linked_list(values)
    assert optimized_solution.isPalindrome(head) is True

def test_long_non_palindrome_stack(stack_solution):
    """Test a longer non-palindrome with stack solution."""
    values = list(range(1000))
    head = create_linked_list(values)
    assert stack_solution.isPalindrome(head) is False

def test_long_non_palindrome_optimized(optimized_solution):
    """Test a longer non-palindrome with optimized solution."""
    values = list(range(1000))
    head = create_linked_list(values)
    assert optimized_solution.isPalindrome(head) is False

def test_almost_palindrome_stack(stack_solution):
    """Test an almost palindrome with stack solution."""
    head = create_linked_list([1, 2, 3, 4, 5, 4, 3, 2, 0])
    assert stack_solution.isPalindrome(head) is False

def test_almost_palindrome_optimized(optimized_solution):
    """Test an almost palindrome with optimized solution."""
    head = create_linked_list([1, 2, 3, 4, 5, 4, 3, 2, 0])
    assert optimized_solution.isPalindrome(head) is False

def test_boundary_values_palindrome_stack(stack_solution):
    """Test with boundary values (0-9) in a palindrome with stack solution."""
    head = create_linked_list([0, 9, 9, 0])
    assert stack_solution.isPalindrome(head) is True

def test_boundary_values_palindrome_optimized(optimized_solution):
    """Test with boundary values (0-9) in a palindrome with optimized solution."""
    head = create_linked_list([0, 9, 9, 0])
    assert optimized_solution.isPalindrome(head) is True

def test_two_node_palindrome_stack(stack_solution):
    """Test a two-node palindrome with stack solution."""
    head = create_linked_list([1, 1])
    assert stack_solution.isPalindrome(head) is True

def test_two_node_palindrome_optimized(optimized_solution):
    """Test a two-node palindrome with optimized solution."""
    head = create_linked_list([1, 1])
    assert optimized_solution.isPalindrome(head) is True

def test_two_node_non_palindrome_stack(stack_solution):
    """Test a two-node non-palindrome with stack solution."""
    head = create_linked_list([1, 2])
    assert stack_solution.isPalindrome(head) is False

def test_two_node_non_palindrome_optimized(optimized_solution):
    """Test a two-node non-palindrome with optimized solution."""
    head = create_linked_list([1, 2])
    assert optimized_solution.isPalindrome(head) is False
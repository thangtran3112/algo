# https://leetcode.com/problems/intersection-of-two-linked-lists/
from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
    connecting the tail to headB, It becomes a cycle
    The problem become detecting the start of cycle, with head=headA
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # find the tail of listA and listB
        # if the tails are different, listA and listB do not intersect
        def find_tail(node: ListNode):
            while node:
                if node.next is None:
                    return node
                node = node.next
            return None

        tailA = find_tail(headA)
        tailB = find_tail(headB)
        if tailA != tailB:
            # no intersection
            return None

        # there is an intersection point
        # connect tail to headB, to create a cycle
        tailA.next = headB

        # start from headA, find the start of the cycle of tortoise-hare technique
        slow = headA
        fast = headA

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # bring slow back to headA
                slow = headA
                break

        # this is guarantee to be cycle, we do not need to check for special cases
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # remove the artificial next pointer from tail
        tailA.next = None
        return slow
    
# Solution with either hashmap or using prev pointer
class SolutionHashmap:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == headB:
            return headA
        prev_map = defaultdict(set)
        sentinelB = ListNode(0)
        sentinelA = ListNode(0)
        sentinelA.next = headA
        sentinelB.next = headB

        # put a pseudo head to start checking from head
        curr = sentinelA

        while curr.next:
            prev_map[curr.next].add(curr)
            curr = curr.next
        curr = sentinelB
        result = None
        while curr.next:
            if len(prev_map[curr.next]) != 0:
                # this is the intersection point 
                # since there is already a prev pointer from curr.next to a node in listA 
                result = curr.next
                break
            curr = curr.next

        return result

# TEST CASES
import pytest

@pytest.fixture
def solution():
    return Solution()

@pytest.fixture
def hashmap_solution():
    return SolutionHashmap()

def test_example_1(solution, hashmap_solution):
    """Test the first example from the problem statement."""
    # Create linked list A: 4->1->8->4->5
    headA = ListNode(4)
    headA.next = ListNode(1)
    common = ListNode(8)
    headA.next.next = common
    common.next = ListNode(4)
    common.next.next = ListNode(5)
    
    # Create linked list B: 5->6->1->8->4->5
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = common  # Intersection at node with value 8
    
    # Test the cycle detection solution
    result = solution.getIntersectionNode(headA, headB)
    assert result == common
    assert result.val == 8
    
    # Test the hashmap solution
    result = hashmap_solution.getIntersectionNode(headA, headB)
    assert result == common
    assert result.val == 8

def test_example_2(solution, hashmap_solution):
    """Test the second example from the problem statement."""
    # Create linked list A: 1->9->1->2->4
    headA = ListNode(1)
    headA.next = ListNode(9)
    headA.next.next = ListNode(1)
    common = ListNode(2)
    headA.next.next.next = common
    common.next = ListNode(4)
    
    # Create linked list B: 3->2->4
    headB = ListNode(3)
    headB.next = common  # Intersection at node with value 2
    
    # Test the cycle detection solution
    result = solution.getIntersectionNode(headA, headB)
    assert result == common
    assert result.val == 2
    
    # Test the hashmap solution
    result = hashmap_solution.getIntersectionNode(headA, headB)
    assert result == common
    assert result.val == 2

def test_example_3(solution, hashmap_solution):
    """Test the third example from the problem statement with no intersection."""
    # Create linked list A: 2->6->4
    headA = ListNode(2)
    headA.next = ListNode(6)
    headA.next.next = ListNode(4)
    
    # Create linked list B: 1->5
    headB = ListNode(1)
    headB.next = ListNode(5)
    
    # Test both solutions
    result = solution.getIntersectionNode(headA, headB)
    assert result is None
    
    result = hashmap_solution.getIntersectionNode(headA, headB)
    assert result is None

def test_same_lists(solution, hashmap_solution):
    """Test with the same list as both inputs."""
    # Create list: 1->2->3
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    
    # Test both solutions
    result = solution.getIntersectionNode(head, head)
    assert result == head
    assert result.val == 1
    
    result = hashmap_solution.getIntersectionNode(head, head)
    assert result == head
    assert result.val == 1

def test_intersection_at_first_node(solution, hashmap_solution):
    """Test with intersection at the first node."""
    # Both lists are the same: 1->2->3
    common = ListNode(1)
    common.next = ListNode(2)
    common.next.next = ListNode(3)
    
    # Test both solutions
    result = solution.getIntersectionNode(common, common)
    assert result == common
    assert result.val == 1
    
    result = hashmap_solution.getIntersectionNode(common, common)
    assert result == common
    assert result.val == 1

def test_one_empty_list(solution, hashmap_solution):
    """Test with one empty list."""
    head = ListNode(1)
    head.next = ListNode(2)
    
    # Test both solutions
    result = solution.getIntersectionNode(head, None)
    assert result is None
    
    result = solution.getIntersectionNode(None, head)
    assert result is None
    
    result = hashmap_solution.getIntersectionNode(head, None)
    assert result is None
    
    result = hashmap_solution.getIntersectionNode(None, head)
    assert result is None

def test_single_node_lists_with_intersection(solution, hashmap_solution):
    """Test with single node lists that intersect."""
    common = ListNode(5)
    
    # Test both solutions
    result = solution.getIntersectionNode(common, common)
    assert result == common
    assert result.val == 5
    
    result = hashmap_solution.getIntersectionNode(common, common)
    assert result == common
    assert result.val == 5

def test_single_node_lists_without_intersection(solution, hashmap_solution):
    """Test with single node lists that do not intersect."""
    headA = ListNode(1)
    headB = ListNode(2)
    
    # Test both solutions
    result = solution.getIntersectionNode(headA, headB)
    assert result is None
    
    result = hashmap_solution.getIntersectionNode(headA, headB)
    assert result is None

def test_intersection_at_last_node(solution, hashmap_solution):
    """Test with intersection at the last node."""
    # Create linked list A: 1->2->3
    headA = ListNode(1)
    headA.next = ListNode(2)
    common = ListNode(3)
    headA.next.next = common
    
    # Create linked list B: 4->5->3
    headB = ListNode(4)
    headB.next = ListNode(5)
    headB.next.next = common
    
    # Test both solutions
    result = solution.getIntersectionNode(headA, headB)
    assert result == common
    assert result.val == 3
    
    result = hashmap_solution.getIntersectionNode(headA, headB)
    assert result == common
    assert result.val == 3

def test_long_lists(solution, hashmap_solution):
    """Test with longer lists to verify algorithm's efficiency."""
    # Create a common portion: 100->101->...->199
    common_start = ListNode(100)
    current = common_start
    for i in range(101, 200):
        current.next = ListNode(i)
        current = current.next
    
    # Create list A: 0->1->...->99->common
    headA = ListNode(0)
    current = headA
    for i in range(1, 100):
        current.next = ListNode(i)
        current = current.next
    current.next = common_start
    
    # Create list B: -100->-99->...->-1->common
    headB = ListNode(-100)
    current = headB
    for i in range(-99, 0):
        current.next = ListNode(i)
        current = current.next
    current.next = common_start
    
    # Test both solutions
    result = solution.getIntersectionNode(headA, headB)
    assert result == common_start
    assert result.val == 100
    
    result = hashmap_solution.getIntersectionNode(headA, headB)
    assert result == common_start
    assert result.val == 100

def test_boundary_values(solution, hashmap_solution):
    """Test with boundary values from the constraints."""
    # Create a common node with min/max values
    common = ListNode(-10**4)  # Min value
    common.next = ListNode(10**4)  # Max value
    
    # List A: -10^4 -> 10^4
    headA = common
    
    # List B: 0 -> -10^4 -> 10^4
    headB = ListNode(0)
    headB.next = common
    
    # Test both solutions
    result = solution.getIntersectionNode(headA, headB)
    assert result == common
    assert result.val == -10**4
    
    result = hashmap_solution.getIntersectionNode(headA, headB)
    assert result == common
    assert result.val == -10**4
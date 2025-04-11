# https://leetcode.com/problems/design-linked-list/description/
"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

# Doubly linked list
class MyLinkedList(object):
    def __init__(self):
        self.size = 0
        # sentinel nodes as pseudo-head and pseudo-tail
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        
        # choose the fastest way: from head or from tail
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        pred, succ = self.head, self.head.next
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
    
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        succ, pred = self.tail, self.tail.prev
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        Notes: addAtIndex will start from [1,..,size], it will not be [0,..,size-1]
        """
        # If index is greater than the length, 
        # the node will not be inserted.
        if index > self.size:
            return
        
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0 # sentinent index
        
        # go to index from head or tail, depends of which one is nearer
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        # Insertion itself
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        Index is within [0,..,size-1]
        """
        # If the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        # Find the pred and succ of the node to be deleted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev

        # delete pred.next
        self.size -= 1
        pred.next = succ
        succ.prev = pred

# TESTING SECTION
import pytest

@pytest.fixture
def empty_list():
    return MyLinkedList()

def test_example_from_description():
    """Test the example provided in the problem description."""
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)  # linked list becomes 1->2->3
    assert myLinkedList.get(1) == 2
    myLinkedList.deleteAtIndex(1)  # now the linked list is 1->3
    assert myLinkedList.get(1) == 3

def test_empty_list_operations(empty_list):
    """Test operations on an empty list."""
    assert empty_list.get(0) == -1  # Get from empty list should return -1
    empty_list.deleteAtIndex(0)  # Should not crash on empty list
    assert empty_list.size == 0  # Size should remain 0

def test_add_at_head(empty_list):
    """Test adding elements at the head."""
    empty_list.addAtHead(1)
    assert empty_list.get(0) == 1
    empty_list.addAtHead(2)
    assert empty_list.get(0) == 2
    assert empty_list.get(1) == 1
    assert empty_list.size == 2

def test_add_at_tail(empty_list):
    """Test adding elements at the tail."""
    empty_list.addAtTail(1)
    assert empty_list.get(0) == 1
    empty_list.addAtTail(2)
    assert empty_list.get(0) == 1
    assert empty_list.get(1) == 2
    assert empty_list.size == 2

def test_add_at_index(empty_list):
    """Test adding elements at specific indices."""
    # Add to empty list at index 0
    empty_list.addAtIndex(0, 1)
    assert empty_list.get(0) == 1
    
    # Add at the beginning
    empty_list.addAtIndex(0, 2)
    assert empty_list.get(0) == 2
    assert empty_list.get(1) == 1
    
    # Add in the middle
    empty_list.addAtIndex(1, 3)
    assert empty_list.get(0) == 2
    assert empty_list.get(1) == 3
    assert empty_list.get(2) == 1
    
    # Add at the end
    empty_list.addAtIndex(3, 4)
    assert empty_list.get(3) == 4
    
    # Add beyond the end (should be ignored)
    empty_list.addAtIndex(5, 5)
    assert empty_list.size == 4
    assert empty_list.get(4) == -1
    
    # Add at negative index (should be treated as index 0)
    empty_list.addAtIndex(-1, 0)
    assert empty_list.get(0) == 0
    assert empty_list.size == 5

def test_delete_at_index(empty_list):
    """Test deleting elements at specific indices."""
    # Setup list: 1->2->3->4
    empty_list.addAtHead(1)
    empty_list.addAtTail(2)
    empty_list.addAtTail(3)
    empty_list.addAtTail(4)
    
    # Delete from the beginning
    empty_list.deleteAtIndex(0)
    assert empty_list.get(0) == 2
    assert empty_list.size == 3
    
    # Delete from the middle
    empty_list.deleteAtIndex(1)
    assert empty_list.get(0) == 2
    assert empty_list.get(1) == 4
    assert empty_list.size == 2
    
    # Delete from the end
    empty_list.deleteAtIndex(1)
    assert empty_list.get(0) == 2
    assert empty_list.get(1) == -1
    assert empty_list.size == 1
    
    # Delete invalid index (should be ignored)
    empty_list.deleteAtIndex(5)
    assert empty_list.size == 1
    
    # Delete negative index (should be ignored)
    empty_list.deleteAtIndex(-1)
    assert empty_list.size == 1
    
    # Delete the last element
    empty_list.deleteAtIndex(0)
    assert empty_list.size == 0
    assert empty_list.get(0) == -1

def test_get_operation():
    """Test get operation with various scenarios."""
    myList = MyLinkedList()
    
    # Get from empty list
    assert myList.get(0) == -1
    assert myList.get(5) == -1
    assert myList.get(-1) == -1
    
    # Add elements and get
    myList.addAtHead(1)
    assert myList.get(0) == 1
    assert myList.get(1) == -1
    
    myList.addAtTail(2)
    assert myList.get(0) == 1
    assert myList.get(1) == 2
    assert myList.get(2) == -1

def test_combined_operations():
    """Test a sequence of mixed operations."""
    myList = MyLinkedList()
    
    myList.addAtHead(7)  # 7
    myList.addAtHead(2)  # 2->7
    myList.addAtHead(1)  # 1->2->7
    myList.addAtIndex(3, 0)  # 1->2->7->0
    myList.deleteAtIndex(2)  # 1->2->0
    myList.addAtHead(6)  # 6->1->2->0
    
    assert myList.get(0) == 6
    assert myList.get(1) == 1
    assert myList.get(2) == 2
    assert myList.get(3) == 0

def test_edge_case_large_list():
    """Test operations on a larger list."""
    myList = MyLinkedList()
    
    # Add 100 elements
    for i in range(100):
        myList.addAtTail(i)
    
    assert myList.size == 100
    assert myList.get(0) == 0
    assert myList.get(50) == 50
    assert myList.get(99) == 99
    
    # Delete elements from various positions
    myList.deleteAtIndex(0)  # Delete first
    assert myList.get(0) == 1
    
    myList.deleteAtIndex(48)  # Delete middle (was 49)
    assert myList.get(48) == 50
    
    myList.deleteAtIndex(97)  # Delete last (was 99)
    assert myList.get(97) == -1
    assert myList.size == 97

def test_boundary_values():
    """Test with boundary values from the constraints."""
    myList = MyLinkedList()
    
    # Max values from constraints
    myList.addAtHead(1000)
    assert myList.get(0) == 1000
    
    # Add at maximum valid index
    myList.addAtIndex(1, 999)
    assert myList.get(1) == 999
    
    # Try to get invalid indices
    assert myList.get(1000) == -1
    assert myList.get(-1) == -1

def test_alternate_traversal_paths():
    """Test the functionality that chooses optimal traversal from head or tail."""
    myList = MyLinkedList()
    
    # Add enough elements to test both traversal paths
    for i in range(10):
        myList.addAtTail(i)
    
    # These should traverse from head
    assert myList.get(0) == 0
    assert myList.get(4) == 4
    
    # These should traverse from tail
    assert myList.get(9) == 9
    assert myList.get(6) == 6
    
    # Modify elements that would be accessed from different directions
    myList.deleteAtIndex(2)  # Traverse from head
    assert myList.get(2) == 3
    
    myList.deleteAtIndex(7)  # Traverse from tail
    assert myList.get(7) == 9

def test_list_structure_integrity():
    """Test that the list structure remains intact after operations."""
    myList = MyLinkedList()
    
    # Build list: 1->2->3->4->5
    for i in range(1, 6):
        myList.addAtTail(i)
    
    # Modify the middle
    myList.deleteAtIndex(2)  # 1->2->4->5
    myList.addAtIndex(2, 3)  # 1->2->3->4->5
    
    # Check the entire list
    for i in range(5):
        assert myList.get(i) == i + 1
    
    # Rebuild the list in reverse: 5->4->3->2->1
    myList = MyLinkedList()
    for i in range(5, 0, -1):
        myList.addAtHead(i)
    
    # Check the entire list
    for i in range(5):
        assert myList.get(i) == i + 1


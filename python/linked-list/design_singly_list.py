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
# Singly linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = Node(0)  # pseudo-head, sentinel node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        index goes from [0,..,size-1]
        * get(0) will give the first element, not including the sentinel node
        """
        if index < 0 or index >= self.size:
            return -1
        prev = self.head
        # sentinel->1->2->3->4. index = 2, delete node 3
        for _ in range(index + 1):
            # need to loop 3 times from sentinel,
            # thus we use range(index + 1), when index = 2, we have range(3) or (0,1,2)
            prev = prev.next
        return prev.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        index goes from 0,1,2,..,size.
        * In which addAtIndex(0, val) mean add to head
        * addAtIndex(size, val) will be addAtTail()
        """
        if index > self.size:
            return

        if index < 0:
            index = 0

        self.size += 1

        # find the predecessor of the node to be added 
        pred = self.head

        # 1->2->3->4, index=2, new value = 5, we have 1->2->5->3->4
        for _ in range(index):
            # _ is in (0, 1), as index = 2
            pred = pred.next
            # pred comes to 2, since we have a psedo sentinel head node

        # break down 2->3 connection, and insert 5. the result will be 2->5->3
        new_node = Node(val)
        new_node.next = pred.next
        pred.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        index goes from 0,1,2,..,size-1
        """
        if index < 0 or index >= self.size:
            return
        self.size -= 1

        # pseudo_head->1->2->3->4, index=2, delete node=3
        prev = self.head
        for _ in range(index):
            # when index = 2, _ will be in (0,1). Loop will run 2 times
            prev = prev.next
        # after the loop, prev will be at node 2
        # delete prev.next 
        prev.next = prev.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

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
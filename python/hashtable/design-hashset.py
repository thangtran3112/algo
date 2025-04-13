# https://leetcode.com/problems/design-hashset/description/
"""
    Design a HashSet without using any built-in hash table libraries.

    Implement MyHashSet class:

    void add(key) Inserts the value key into the HashSet.
    bool contains(key) Returns whether the value key exists in the HashSet or not.
    void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
    

    Example 1:

    Input
    ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
    [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    Output
    [null, null, null, true, false, null, true, null, false]

    Explanation
    MyHashSet myHashSet = new MyHashSet();
    myHashSet.add(1);      // set = [1]
    myHashSet.add(2);      // set = [1, 2]
    myHashSet.contains(1); // return True
    myHashSet.contains(3); // return False, (not found)
    myHashSet.add(2);      // set = [1, 2]
    myHashSet.contains(2); // return True
    myHashSet.remove(2);   // set = [1]
    myHashSet.contains(2); // return False, (already removed)
    

    Constraints:

    0 <= key <= 106
    At most 104 calls will be made to add, remove, and contains.
"""
from typing import Optional


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# https://leetcode.com/problems/delete-node-in-a-bst/description/
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or val == root.val:
            return root
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)

    def insertIntoBST(self, root: Optional[TreeNode], val) -> TreeNode:
        # empty branch, add leave
        if not root: 
            return TreeNode(val)
        if val == root.val:
            # element is already in the set, do nothing
            return root
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    # only successor of a node with both left and right Children.
    # go right, and go all the way left
    def successor(self, root) -> int:
        root = root.right
        while root.left:
            root = root.left
        return root.val

    # delete node with value = key, from a given "root" node
    def deleteNode(self, root, key) -> TreeNode:
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # root is the node to be deleted, root.val == key here
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            # having both left and child nodes from here. swapping with successor
            succ_val = self.successor(root)
            # cloning
            root.val = succ_val
            # recursively deleting successor (a leaf node) after cloning
            root.right = self.deleteNode(root.right, succ_val)

        # allow callers to connect/reconnect to this node
        return root

class Bucket:
    def __init__(self):
        self.tree = BinarySearchTree()

    def insert(self, value):
        self.tree.root = self.tree.insertIntoBST(self.tree.root, value)

    def delete(self, value):
        self.tree.root = self.tree.deleteNode(self.tree.root, value)

    def exists(self, value):
        return (self.tree.searchBST(self.tree.root, value) is not None)

# For each key, _hash function will give a Bucket
# Within each bucket, data is arranged as a BinarySearchTree
# O(log(N/K)), with K: keyRange
class MyHashSetByBST:

    def __init__(self):
        self.keyRange = 1000
        self.bucketArray = [Bucket() for _ in range(self.keyRange)]
    
    def _hash(self, key) -> int:
        return key % self.keyRange

    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key: int) -> None:
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key: int) -> bool:
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)

class MyHashSetByArray:
    def __init__(self):
        self.n = 10000
        self.arr = [[] for _ in range(self.n)]

    def add(self, key: int) -> None:
        i = key % self.n
        if key not in self.arr[i]:
            self.arr[i].append(key)

    def remove(self, key: int) -> None:
        i = key % self.n
        if key in self.arr[i]:
            self.arr[i].remove(key)

    def contains(self, key: int) -> bool:
        i = key % self.n
        return key in self.arr[i]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

import pytest  # noqa: E402

@pytest.fixture(params=[MyHashSetByBST, MyHashSetByArray])
def hashset(request):
    """Fixture that provides both hashset implementations."""
    return request.param()

def test_example_1(hashset):
    """Test the first example from the problem statement."""
    # myHashSet = new MyHashSet();
    # myHashSet.add(1);      // set = [1]
    # myHashSet.add(2);      // set = [1, 2]
    # myHashSet.contains(1); // return True
    # myHashSet.contains(3); // return False, (not found)
    # myHashSet.add(2);      // set = [1, 2]
    # myHashSet.contains(2); // return True
    # myHashSet.remove(2);   // set = [1]
    # myHashSet.contains(2); // return False, (already removed)
    
    hashset.add(1)
    hashset.add(2)
    assert hashset.contains(1) is True
    assert hashset.contains(3) is False
    hashset.add(2)  # Add duplicate
    assert hashset.contains(2) is True
    hashset.remove(2)
    assert hashset.contains(2) is False

def test_empty_hashset(hashset):
    """Test operations on an empty hashset."""
    assert hashset.contains(1) is False
    hashset.remove(1)  # Should do nothing
    assert hashset.contains(1) is False

def test_add_and_remove(hashset):
    """Test adding and removing multiple elements."""
    # Add elements
    for i in range(10):
        hashset.add(i)
        assert hashset.contains(i) is True
    
    # Remove elements
    for i in range(0, 10, 2):  # Remove even numbers
        hashset.remove(i)
        assert hashset.contains(i) is False
    
    # Check remaining elements
    for i in range(10):
        if i % 2 == 0:  # Even numbers were removed
            assert hashset.contains(i) is False
        else:  # Odd numbers should still be there
            assert hashset.contains(i) is True

def test_add_duplicates(hashset):
    """Test adding duplicate elements."""
    hashset.add(5)
    assert hashset.contains(5) is True
    
    # Add the same element multiple times
    for _ in range(5):
        hashset.add(5)
    
    # Should still contain only one instance
    assert hashset.contains(5) is True
    
    # Remove once should remove all instances
    hashset.remove(5)
    assert hashset.contains(5) is False

def test_remove_nonexistent(hashset):
    """Test removing elements that don't exist."""
    # Remove from empty set
    hashset.remove(10)
    assert hashset.contains(10) is False
    
    # Add some elements
    hashset.add(1)
    hashset.add(2)
    
    # Remove a non-existent element
    hashset.remove(3)
    assert hashset.contains(1) is True
    assert hashset.contains(2) is True
    assert hashset.contains(3) is False

def test_boundary_values(hashset):
    """Test with boundary values from the constraints."""
    # Minimum value: 0
    hashset.add(0)
    assert hashset.contains(0) is True
    
    # Maximum value: 10^6
    max_value = 10**6
    hashset.add(max_value)
    assert hashset.contains(max_value) is True
    
    # Remove boundary values
    hashset.remove(0)
    hashset.remove(max_value)
    assert hashset.contains(0) is False
    assert hashset.contains(max_value) is False

def test_collision_handling(hashset):
    """Test handling of hash collisions."""
    # These values should cause collisions in most implementations
    # For MyHashSetByArray with n=10000, these will collide
    hashset.add(10000)
    hashset.add(20000)
    hashset.add(30000)
    
    assert hashset.contains(10000) is True
    assert hashset.contains(20000) is True
    assert hashset.contains(30000) is True
    
    # Remove one of the colliding values
    hashset.remove(20000)
    
    assert hashset.contains(10000) is True
    assert hashset.contains(20000) is False
    assert hashset.contains(30000) is True

def test_many_operations(hashset):
    """Test many operations to approach the constraint limit."""
    # Add a larger number of elements
    elements = 1000  # Less than 10^4 calls constraint
    
    # Add elements
    for i in range(elements):
        hashset.add(i)
    
    # Check if all were added
    for i in range(elements):
        assert hashset.contains(i) is True
    
    # Remove half the elements
    for i in range(0, elements, 2):
        hashset.remove(i)
    
    # Check remaining elements
    for i in range(elements):
        if i % 2 == 0:
            assert hashset.contains(i) is False
        else:
            assert hashset.contains(i) is True

def test_mixed_operations(hashset):
    """Test a mix of add, remove, and contains operations."""
    operations = [
        ('add', 5), ('add', 10), ('add', 15),
        ('contains', 5, True), ('contains', 20, False),
        ('remove', 10), ('contains', 10, False),
        ('add', 20), ('add', 5),  # Adding 5 again
        ('contains', 5, True), ('contains', 20, True),
        ('remove', 5), ('contains', 5, False)
    ]
    
    for operation in operations:
        if operation[0] == 'add':
            hashset.add(operation[1])
        elif operation[0] == 'remove':
            hashset.remove(operation[1])
        elif operation[0] == 'contains':
            assert hashset.contains(operation[1]) is operation[2]

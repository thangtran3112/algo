from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        # move the key to the end, so it is the most recently used cache
        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.dic and len(self.dic) == self.capacity:
            # evict the head key
            self.dic.popitem(False)  # False = FIFO, True = LIFO
        self.dic[key] = value
        self.dic.move_to_end(key)

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCacheWithDoublyLinkedList:

    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        # Remove all links to node, node will be garbage collected
        node.prev.next = node.next
        node.next.prev = node.prev

    # Least recently used node will be at head.next
    def add_right_before_tail(self, node):
        # Add a new node, most recently used node will be at tail.prev
        # Connect previous tail to new node
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end

        # Connecting node to tail, node.next=tail, tail.prev = node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key not in self.dic:
            return -1
        
        node = self.dic[key]

        # Remove then add node back, so it becomes the most recently used
        self.remove(node)
        self.add_right_before_tail(node)
        return node.val
        

    def put(self, key, value):
        if key in self.dic.keys():
            # Remove existing value at key
            old_node = self.dic[key]
            # Remove old node from the dic. We do not overwrite this node value directly
            # But we will add new node, so value will be most recently used
            self.remove(old_node)

        # Add the new node, to tail.prev, so it is the most recently used
        node = Node(key, value)
        self.dic[key] = node
        self.add_right_before_tail(node)

        # If over capacity, remove head.next
        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key] 


# === TEST CASES ===
import pytest

@pytest.fixture(params=[LRUCache, LRUCacheWithDoublyLinkedList],
               ids=["OrderedDict", "DoublyLinkedList"])
def cache_instance(request):
    """Fixture to provide instances of both LRU Cache implementations."""
    return lambda capacity: request.param(capacity)

def test_simple_operations(cache_instance):
    """Test basic get and put operations."""
    lru = cache_instance(2)
    
    # Put operations
    lru.put(1, 1)
    lru.put(2, 2)
    
    # Get operations
    assert lru.get(1) == 1
    assert lru.get(2) == 2
    assert lru.get(3) == -1  # Non-existent key

def test_example_from_problem(cache_instance):
    """Test the example from the problem description."""
    lru = cache_instance(2)
    
    lru.put(1, 1)           # cache is {1=1}
    lru.put(2, 2)           # cache is {1=1, 2=2}
    assert lru.get(1) == 1  # return 1
    
    lru.put(3, 3)           # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert lru.get(2) == -1 # returns -1 (not found)
    
    lru.put(4, 4)           # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    assert lru.get(1) == -1 # return -1 (not found)
    assert lru.get(3) == 3  # return 3
    assert lru.get(4) == 4  # return 4

def test_eviction_policy(cache_instance):
    """Test the LRU eviction policy."""
    lru = cache_instance(2)
    
    lru.put(1, 1)
    lru.put(2, 2)
    
    # Access key 1, making key 2 the LRU
    lru.get(1)
    
    # Add new key, should evict key 2
    lru.put(3, 3)
    
    assert lru.get(1) == 1  # Key 1 should still be present
    assert lru.get(2) == -1 # Key 2 should be evicted
    assert lru.get(3) == 3  # Key 3 should be present

def test_update_existing_key(cache_instance):
    """Test updating an existing key."""
    lru = cache_instance(2)
    
    lru.put(1, 1)
    lru.put(2, 2)
    
    # Update key 1
    lru.put(1, 10)
    
    assert lru.get(1) == 10 # Key 1 should have the updated value
    assert lru.get(2) == 2  # Key 2 should still be present

def test_update_makes_key_most_recent(cache_instance):
    """Test that updating a key makes it the most recently used."""
    lru = cache_instance(2)
    
    lru.put(1, 1)
    lru.put(2, 2)
    
    # Update key 1, making it the most recently used
    lru.put(1, 10)
    
    # Add new key, should evict key 2 (the LRU)
    lru.put(3, 3)
    
    assert lru.get(1) == 10 # Key 1 should still be present
    assert lru.get(2) == -1 # Key 2 should be evicted
    assert lru.get(3) == 3  # Key 3 should be present

def test_get_makes_key_most_recent(cache_instance):
    """Test that getting a key makes it the most recently used."""
    lru = cache_instance(2)
    
    lru.put(1, 1)
    lru.put(2, 2)
    
    # Access key 1, making it the most recently used
    lru.get(1)
    
    # Add new key, should evict key 2 (the LRU)
    lru.put(3, 3)
    
    assert lru.get(1) == 1  # Key 1 should still be present
    assert lru.get(2) == -1 # Key 2 should be evicted
    assert lru.get(3) == 3  # Key 3 should be present

def test_capacity_one(cache_instance):
    """Test with capacity of 1."""
    lru = cache_instance(1)
    
    lru.put(1, 1)
    assert lru.get(1) == 1
    
    lru.put(2, 2)
    assert lru.get(1) == -1 # Key 1 should be evicted
    assert lru.get(2) == 2
    
    lru.put(3, 3)
    assert lru.get(2) == -1 # Key 2 should be evicted
    assert lru.get(3) == 3

def test_repeated_access_pattern(cache_instance):
    """Test with a specific access pattern that tests LRU behavior."""
    lru = cache_instance(3)
    
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    
    # Access keys in this order: 3, 1, 2, 3, 1, 3
    lru.get(3)  # LRU order: 1, 2, 3
    lru.get(1)  # LRU order: 2, 3, 1
    lru.get(2)  # LRU order: 3, 1, 2
    lru.get(3)  # LRU order: 1, 2, 3
    lru.get(1)  # LRU order: 2, 3, 1
    lru.get(3)  # LRU order: 2, 1, 3
    
    # Add new key, should evict key 2 (the LRU)
    lru.put(4, 4)  # LRU order: 1, 3, 4
    
    assert lru.get(1) == 1
    assert lru.get(2) == -1 # Key 2 should be evicted
    assert lru.get(3) == 3
    assert lru.get(4) == 4

def test_very_large_operations(cache_instance):
    """Test with a large number of operations."""
    lru = cache_instance(5)
    
    # Perform 1000 operations
    for i in range(1000):
        lru.put(i, i)
        
        # Every 100 operations, check the most recent 5 keys
        if i % 100 == 99:
            for j in range(i-4, i+1):
                assert lru.get(j) == j
            
            # Older keys should be evicted
            assert lru.get(i-5) == -1

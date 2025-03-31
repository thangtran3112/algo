import pytest
from circular_queue import MyCircularQueue

def test_init():
    # Test initialization with different sizes
    queue = MyCircularQueue(3)
    assert queue.isEmpty() is True
    assert queue.isFull() is False

def test_enqueue_dequeue_basic():
    queue = MyCircularQueue(3)
    
    # Add elements and check properties
    assert queue.enQueue(1) is True
    assert queue.isEmpty() is False
    assert queue.isFull() is False
    assert queue.Front() == 1
    assert queue.Rear() == 1
    
    assert queue.enQueue(2) is True
    assert queue.Front() == 1
    assert queue.Rear() == 2
    
    assert queue.enQueue(3) is True
    assert queue.isFull() is True
    assert queue.Front() == 1
    assert queue.Rear() == 3
    
    # Queue is full now
    assert queue.enQueue(4) is False
    
    # Remove elements
    assert queue.deQueue() is True  # Remove 1
    assert queue.Front() == 2
    assert queue.Rear() == 3
    assert queue.isFull() is False

def test_circular_behavior():
    queue = MyCircularQueue(3)
    
    # Fill the queue
    assert queue.enQueue(1) is True
    assert queue.enQueue(2) is True
    assert queue.enQueue(3) is True
    
    # Remove from front
    assert queue.deQueue() is True  # Remove 1
    
    # Add to rear (circular behavior)
    assert queue.enQueue(4) is True
    assert queue.Front() == 2
    assert queue.Rear() == 4
    
    # Continue cycling
    assert queue.deQueue() is True  # Remove 2
    assert queue.deQueue() is True  # Remove 3
    assert queue.Front() == 4
    assert queue.Rear() == 4
    
    assert queue.deQueue() is True  # Remove 4
    assert queue.isEmpty() is True

def test_empty_queue_operations():
    queue = MyCircularQueue(3)
    
    # Operations on empty queue
    assert queue.isEmpty() is True
    assert queue.isFull() is False
    assert queue.Front() == -1
    assert queue.Rear() == -1
    assert queue.deQueue() is False

def test_queue_cycling():
    queue = MyCircularQueue(5)
    
    # Fill and empty multiple times to test cycling
    for i in range(1, 6):
        assert queue.enQueue(i) is True
    
    assert queue.isFull() is True
    
    # Remove all
    for _ in range(5):
        assert queue.deQueue() is True
    
    assert queue.isEmpty() is True
    
    # Fill again (should work even after emptying)
    for i in range(6, 11):
        assert queue.enQueue(i) is True
    
    assert queue.Front() == 6
    assert queue.Rear() == 10

def test_edge_case_size_1():
    queue = MyCircularQueue(1)
    
    assert queue.isEmpty() is True
    assert queue.isFull() is False
    
    assert queue.enQueue(42) is True
    assert queue.isEmpty() is False
    assert queue.isFull() is True
    assert queue.Front() == 42
    assert queue.Rear() == 42
    
    assert queue.enQueue(43) is False  # Full, can't add
    assert queue.deQueue() is True
    assert queue.isEmpty() is True
    assert queue.Front() == -1
    assert queue.Rear() == -1

def test_complex_sequence():
    queue = MyCircularQueue(4)
    
    # Complex sequence of operations
    assert queue.enQueue(1) is True
    assert queue.enQueue(2) is True
    assert queue.deQueue() is True
    assert queue.enQueue(3) is True
    assert queue.deQueue() is True
    assert queue.enQueue(4) is True
    assert queue.enQueue(5) is True
    assert queue.Front() == 3
    assert queue.Rear() == 5
    
    assert queue.deQueue() is True
    assert queue.deQueue() is True
    assert queue.enQueue(6) is True
    assert queue.enQueue(7) is True
    assert queue.enQueue(8) is True
    assert queue.isFull() is True
    assert queue.Front() == 5
    assert queue.Rear() == 8

def test_large_capacity():
    queue = MyCircularQueue(1000)
    
    # Test with large capacity
    for i in range(1000):
        assert queue.enQueue(i) is True
    
    assert queue.isFull() is True
    assert queue.Front() == 0
    assert queue.Rear() == 999
    
    # Remove half
    for _ in range(500):
        assert queue.deQueue() is True
    
    assert queue.isFull() is False
    assert queue.Front() == 500
    assert queue.Rear() == 999
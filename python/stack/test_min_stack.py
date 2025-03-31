import pytest
from min_stack import MinStack

def test_example_from_problem():
    """Test the example provided in the problem statement."""
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2

def test_empty_stack_initialization():
    """Test that a new stack is properly initialized."""
    minStack = MinStack()
    assert len(minStack.stack) == 0

def test_push_and_top():
    """Test push and top operations."""
    minStack = MinStack()
    minStack.push(5)
    assert minStack.top() == 5
    minStack.push(10)
    assert minStack.top() == 10

def test_push_and_pop():
    """Test push and pop operations."""
    minStack = MinStack()
    minStack.push(5)
    minStack.push(10)
    minStack.push(15)
    minStack.pop()
    assert minStack.top() == 10
    minStack.pop()
    assert minStack.top() == 5

def test_get_min_basic():
    """Test getMin returns the minimum value."""
    minStack = MinStack()
    minStack.push(5)
    assert minStack.getMin() == 5
    minStack.push(3)
    assert minStack.getMin() == 3
    minStack.push(7)
    assert minStack.getMin() == 3

def test_get_min_after_pop():
    """Test getMin returns correct min after popping."""
    minStack = MinStack()
    minStack.push(5)
    minStack.push(3)
    minStack.push(7)
    minStack.pop()  # Remove 7
    assert minStack.getMin() == 3
    minStack.pop()  # Remove 3
    assert minStack.getMin() == 5

def test_multiple_equal_mins():
    """Test handling multiple occurrences of the minimum value."""
    minStack = MinStack()
    minStack.push(1)
    minStack.push(1)
    minStack.push(1)
    assert minStack.getMin() == 1
    minStack.pop()
    assert minStack.getMin() == 1
    minStack.pop()
    assert minStack.getMin() == 1

def test_negative_values():
    """Test with negative values."""
    minStack = MinStack()
    minStack.push(-5)
    minStack.push(-10)
    minStack.push(-3)
    assert minStack.getMin() == -10
    minStack.pop()  # Remove -3
    assert minStack.getMin() == -10
    minStack.pop()  # Remove -10
    assert minStack.getMin() == -5

def test_min_changes_after_operations():
    """Test min changes correctly after various operations."""
    minStack = MinStack()
    minStack.push(10)
    minStack.push(5)
    minStack.push(15)
    assert minStack.getMin() == 5
    minStack.pop()  # Remove 15
    assert minStack.getMin() == 5
    minStack.pop()  # Remove 5
    assert minStack.getMin() == 10

def test_boundary_values():
    """Test with boundary values from constraints."""
    minStack = MinStack()
    max_val = 2**31 - 1
    min_val = -2**31
    
    minStack.push(max_val)
    assert minStack.getMin() == max_val
    minStack.push(min_val)
    assert minStack.getMin() == min_val

def test_large_number_of_operations():
    """Test a large number of operations (within constraints)."""
    minStack = MinStack()
    # Just testing a reasonable number that won't slow down tests too much
    num_operations = 1000
    
    for i in range(num_operations):
        minStack.push(i)
        assert minStack.top() == i
        assert minStack.getMin() == 0
    
    for i in range(num_operations-1, -1, -1):
        assert minStack.top() == i
        minStack.pop()

def test_complex_sequence():
    """Test a complex sequence of operations."""
    minStack = MinStack()
    
    # Push values in decreasing then increasing order
    minStack.push(9)
    minStack.push(7)
    minStack.push(5)
    minStack.push(3)
    minStack.push(1)
    minStack.push(2)
    minStack.push(4)
    minStack.push(6)
    minStack.push(8)
    minStack.push(10)
    
    # Check current state
    assert minStack.top() == 10
    assert minStack.getMin() == 1
    
    # Remove some values
    minStack.pop()  # Remove 10
    minStack.pop()  # Remove 8
    minStack.pop()  # Remove 6
    
    # Check state
    assert minStack.top() == 4
    assert minStack.getMin() == 1
    
    # Remove the min
    minStack.pop()  # Remove 4
    minStack.pop()  # Remove 2
    minStack.pop()  # Remove 1
    
    # Check new min
    assert minStack.getMin() == 3
    
    # Empty the stack
    minStack.pop()  # Remove 3
    minStack.pop()  # Remove 5
    minStack.pop()  # Remove 7
    minStack.pop()  # Remove 9
    
    # Push new values
    minStack.push(5)
    assert minStack.getMin() == 5
    assert minStack.top() == 5
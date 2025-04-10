import pytest
from k_largest_elements import KthLargest, KthLargestSortedArray

@pytest.fixture
def heap_implementation():
    return KthLargest

@pytest.fixture
def sorted_array_implementation():
    return KthLargestSortedArray

def test_example_1_heap(heap_implementation):
    """Test the first example from the problem statement with heap implementation."""
    kthLargest = heap_implementation(3, [4, 5, 8, 2])
    assert kthLargest.add(3) == 4
    assert kthLargest.add(5) == 5
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 8
    assert kthLargest.add(4) == 8

def test_example_1_sorted_array(sorted_array_implementation):
    """Test the first example from the problem statement with sorted array implementation."""
    kthLargest = sorted_array_implementation(3, [4, 5, 8, 2])
    assert kthLargest.add(3) == 4
    assert kthLargest.add(5) == 5
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 8
    assert kthLargest.add(4) == 8

def test_example_2_heap(heap_implementation):
    """Test the second example from the problem statement with heap implementation."""
    kthLargest = heap_implementation(4, [7, 7, 7, 7, 8, 3])
    assert kthLargest.add(2) == 7
    assert kthLargest.add(10) == 7
    assert kthLargest.add(9) == 7
    assert kthLargest.add(9) == 8

def test_example_2_sorted_array(sorted_array_implementation):
    """Test the second example from the problem statement with sorted array implementation."""
    kthLargest = sorted_array_implementation(4, [7, 7, 7, 7, 8, 3])
    assert kthLargest.add(2) == 7
    assert kthLargest.add(10) == 7
    assert kthLargest.add(9) == 7
    assert kthLargest.add(9) == 8

def test_empty_initial_array_heap(heap_implementation):
    """Test with an empty initial array with heap implementation."""
    kthLargest = heap_implementation(1, [])
    assert kthLargest.add(3) == 3
    assert kthLargest.add(5) == 5
    assert kthLargest.add(1) == 5

def test_empty_initial_array_sorted_array(sorted_array_implementation):
    """Test with an empty initial array with sorted array implementation."""
    kthLargest = sorted_array_implementation(1, [])
    assert kthLargest.add(3) == 3
    assert kthLargest.add(5) == 5
    assert kthLargest.add(1) == 5

def test_k_equals_1_heap(heap_implementation):
    """Test with k=1 (only interested in maximum element) with heap implementation."""
    kthLargest = heap_implementation(1, [4, 5, 8, 2])
    assert kthLargest.add(3) == 8
    assert kthLargest.add(10) == 10
    assert kthLargest.add(9) == 10

def test_k_equals_1_sorted_array(sorted_array_implementation):
    """Test with k=1 (only interested in maximum element) with sorted array implementation."""
    kthLargest = sorted_array_implementation(1, [4, 5, 8, 2])
    assert kthLargest.add(3) == 8
    assert kthLargest.add(10) == 10
    assert kthLargest.add(9) == 10

def test_negative_values_heap(heap_implementation):
    """Test with negative values in the array with heap implementation."""
    kthLargest = heap_implementation(2, [-4, -5, -8, -2])
    assert kthLargest.add(-3) == -3
    assert kthLargest.add(-1) == -2
    assert kthLargest.add(-10) == -2

def test_negative_values_sorted_array(sorted_array_implementation):
    """Test with negative values in the array with sorted array implementation."""
    kthLargest = sorted_array_implementation(2, [-4, -5, -8, -2])
    assert kthLargest.add(-3) == -3
    assert kthLargest.add(-1) == -2
    assert kthLargest.add(-10) == -2

def test_duplicate_values_heap(heap_implementation):
    """Test with duplicate values in the array with heap implementation."""
    kthLargest = heap_implementation(3, [5, 5, 5, 5])
    assert kthLargest.add(5) == 5
    assert kthLargest.add(6) == 5
    assert kthLargest.add(7) == 5  # Changed from 6 to 5

def test_duplicate_values_sorted_array(sorted_array_implementation):
    """Test with duplicate values in the array with sorted array implementation."""
    kthLargest = sorted_array_implementation(3, [5, 5, 5, 5])
    assert kthLargest.add(5) == 5
    assert kthLargest.add(6) == 5
    assert kthLargest.add(7) == 5  # Changed from 6 to 5

def test_boundary_values_heap(heap_implementation):
    """Test with boundary values from the constraints with heap implementation."""
    kthLargest = heap_implementation(2, [-10**4, 10**4])
    assert kthLargest.add(0) == 0
    assert kthLargest.add(10**4) == 10**4
    assert kthLargest.add(-10**4) == 10**4

def test_boundary_values_sorted_array(sorted_array_implementation):
    """Test with boundary values from the constraints with sorted array implementation."""
    kthLargest = sorted_array_implementation(2, [-10**4, 10**4])
    assert kthLargest.add(0) == 0
    assert kthLargest.add(10**4) == 10**4
    assert kthLargest.add(-10**4) == 10**4

def test_large_array_heap(heap_implementation):
    """Test with a larger array to verify efficiency with heap implementation."""
    nums = list(range(-100, 101))  # Array of size 201
    kthLargest = heap_implementation(5, nums)
    assert kthLargest.add(101) == 97  # Changed from 96 to 97
    assert kthLargest.add(102) == 98
    assert kthLargest.add(103) == 99

def test_large_array_sorted_array(sorted_array_implementation):
    """Test with a larger array to verify efficiency with sorted array implementation."""
    nums = list(range(-100, 101))  # Array of size 201
    kthLargest = sorted_array_implementation(5, nums)
    assert kthLargest.add(101) == 97  # Changed from 96 to 97
    assert kthLargest.add(102) == 98
    assert kthLargest.add(103) == 99

def test_k_equals_initial_length_plus_one_heap(heap_implementation):
    """Test with k equal to initial array length plus one with heap implementation."""
    kthLargest = heap_implementation(5, [1, 2, 3, 4])
    assert kthLargest.add(5) == 1
    assert kthLargest.add(6) == 2
    assert kthLargest.add(7) == 3

def test_k_equals_initial_length_plus_one_sorted_array(sorted_array_implementation):
    """Test with k equal to initial array length plus one with sorted array implementation."""
    kthLargest = sorted_array_implementation(5, [1, 2, 3, 4])
    assert kthLargest.add(5) == 1
    assert kthLargest.add(6) == 2
    assert kthLargest.add(7) == 3

def test_many_additions_heap(heap_implementation):
    """Test with many additions to verify performance with heap implementation."""
    kthLargest = heap_implementation(3, [4, 5, 8, 2])
    results = []
    for i in range(100):
        results.append(kthLargest.add(i))
    assert results[-3:] == [95, 96, 97]  # Changed from [97, 98, 99] to [95, 96, 97]

def test_many_additions_sorted_array(sorted_array_implementation):
    """Test with many additions to verify performance with sorted array implementation."""
    kthLargest = sorted_array_implementation(3, [4, 5, 8, 2])
    results = []
    for i in range(100):
        results.append(kthLargest.add(i))
    assert results[-3:] == [95, 96, 97]
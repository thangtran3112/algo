import pytest
from intersecton_arrays_2 import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 2
    assert result.count(2) == 2

def test_example_2(solution):
    """Test the second example from the problem statement."""
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 2
    assert 4 in result
    assert 9 in result

def test_no_intersection(solution):
    """Test when there is no intersection between arrays."""
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 0
    assert result == []

def test_identical_arrays(solution):
    """Test when both arrays are identical."""
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 3
    assert sorted(result) == [1, 2, 3]

def test_empty_array(solution):
    """Test when one array is empty."""
    nums1 = []
    nums2 = [1, 2, 3]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 0
    assert result == []

    nums1 = [1, 2, 3]
    nums2 = []
    result = solution.intersect(nums1, nums2)
    assert len(result) == 0
    assert result == []

def test_both_empty_arrays(solution):
    """Test when both arrays are empty."""
    nums1 = []
    nums2 = []
    result = solution.intersect(nums1, nums2)
    assert len(result) == 0
    assert result == []

def test_multiple_duplicates(solution):
    """Test with multiple duplicates in both arrays."""
    nums1 = [1, 1, 2, 2, 3, 3]
    nums2 = [1, 1, 1, 2, 2, 3, 3, 3]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 6
    assert result.count(1) == 2
    assert result.count(2) == 2
    assert result.count(3) == 2

def test_single_element_arrays(solution):
    """Test with single element arrays."""
    nums1 = [5]
    nums2 = [5]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 1
    assert result == [5]

def test_single_element_no_intersection(solution):
    """Test with single element arrays with no intersection."""
    nums1 = [5]
    nums2 = [10]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 0
    assert result == []

def test_frequency_matters(solution):
    """Test that element frequency is respected."""
    nums1 = [1, 1, 1, 2]
    nums2 = [1, 1]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 2
    assert result.count(1) == 2

def test_large_arrays(solution):
    """Test with large arrays to verify efficiency."""
    nums1 = [i for i in range(1000) for _ in range(3)]  # Each number appears 3 times
    nums2 = [i for i in range(500, 1500) for _ in range(2)]  # Each number appears 2 times
    result = solution.intersect(nums1, nums2)
    assert len(result) == 500 * 2  # 500 numbers overlap, each appears twice
    
    # Check a sample of the results to verify frequencies
    counts = {}
    for num in result:
        counts[num] = counts.get(num, 0) + 1
    
    for i in range(500, 1000):
        assert counts.get(i, 0) == 2


def test_different_order(solution):
    """Test that the order doesn't matter for the intersection."""
    nums1 = [1, 2, 3, 4]
    nums2 = [4, 3, 2, 1]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 4
    assert sorted(result) == [1, 2, 3, 4]

def test_one_element_subset(solution):
    """Test when one array is a subset of the other with different frequencies."""
    nums1 = [1, 2, 3, 4, 5, 1, 2]
    nums2 = [2, 1, 2]
    result = solution.intersect(nums1, nums2)
    assert len(result) == 3
    assert result.count(1) == 1
    assert result.count(2) == 2
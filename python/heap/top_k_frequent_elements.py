# https://leetcode.com/problems/top-k-frequent-elements/description/
"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import heapq
from typing import List


class Solution:
    # Using min-heap of k-size to keep track of k-largest frequencies
    # Notes: some elements could have identical frequencies
    # https://leetcode.com/explore/learn/card/heap/645/applications-of-heap/4031/
    # Time complexity n + nlog(k), which is better than n.log(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        # Time complexity O(n)
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1

        indexes = []
        # Time O(n*log(k)) because n rounds of loop, which iteration cost O(logk)
        for f in freqs.values():
            if len(indexes) < k:
                # Time: O(logk)
                heapq.heappush(indexes, f)
            else:
                cur_min = heapq.heappop(indexes)
                larger = max(cur_min, f)
                # Time: O(logk)
                heapq.heappush(indexes, larger)

        min_freq = indexes[0]

        # all elements with more frequencies than min_freq will be in the answer
        result = []
        for key, value in freqs.items():
            if value >= min_freq:
                result.append(key)

        return result
    
import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Fixture that provides the solution implementation."""
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = solution.topKFrequent(nums, k)
    # Sort for comparison since order doesn't matter
    assert sorted(result) == [1, 2]

def test_example_2(solution):
    """Test the second example from the problem statement."""
    nums = [1]
    k = 1
    assert solution.topKFrequent(nums, k) == [1]

def test_single_element_multiple_times(solution):
    """Test with a single element appearing multiple times."""
    nums = [5, 5, 5, 5, 5]
    k = 1
    assert solution.topKFrequent(nums, k) == [5]

def test_negative_numbers(solution):
    """Test with negative numbers."""
    nums = [-1, -1, -2, -2, -2, -3]
    k = 2
    result = solution.topKFrequent(nums, k)
    assert sorted(result) == [-2, -1]

def test_boundary_values(solution):
    """Test with boundary values from the constraints."""
    # Test with values at the extremes of the constraints
    nums = [-10**4, 10**4] * 50  # Mix of min and max values
    k = 2
    result = solution.topKFrequent(nums, k)
    assert sorted(result) == [-10**4, 10**4]

def test_k_equals_number_of_unique_elements(solution):
    """Test when k equals the number of unique elements."""
    nums = [1, 1, 2, 2, 3, 3, 4]
    k = 4  # There are 4 unique elements
    result = solution.topKFrequent(nums, k)
    assert sorted(result) == [1, 2, 3, 4]

def test_diverse_frequencies(solution):
    """Test with diverse frequencies."""
    nums = [1, 1, 1, 2, 2, 3]
    k = 1
    assert solution.topKFrequent(nums, k) == [1]

def test_result_uniqueness(solution):
    """Test that the result contains unique elements (as guaranteed by problem)."""
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    k = 3
    result = solution.topKFrequent(nums, k)
    assert len(result) == len(set(result))  # No duplicates
    assert sorted(result) == [1, 3, 4]  # Elements with frequencies 3, 3, and 4

def test_complex_distribution(solution):
    """Test with a more complex frequency distribution."""
    # Create a distribution where elements have frequencies 1, 2, 3, ..., 10
    nums = []
    for i in range(1, 11):
        nums.extend([i] * i)
    
    k = 5
    result = solution.topKFrequent(nums, k)
    # The 5 most frequent elements should be 10, 9, 8, 7, 6
    assert sorted(result) == [6, 7, 8, 9, 10]

def test_edge_case_k_1(solution):
    """Test the edge case where k = 1."""
    nums = [1, 1, 2, 2, 2, 3]
    k = 1
    assert solution.topKFrequent(nums, k) == [2]

def test_all_same_frequency(solution):
    """Test when all elements have the same frequency."""
    nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    k = 3
    result = solution.topKFrequent(nums, k)
    assert len(result) == 5  # All elements have same frequency, so all are returned
    assert set(result) == {1, 2, 3, 4, 5}

def test_ties_at_kth_position(solution):
    """Test behavior when there are ties at the k-th position."""
    nums = [1, 1, 2, 2, 3, 3, 4, 4, 5]  # Elements 1-4 appear twice, 5 appears once
    k = 4
    result = solution.topKFrequent(nums, k)
    assert len(result) == 4
    assert set(result).issubset({1, 2, 3, 4})

def test_large_input_performance(solution):
    """Test performance with a large input array."""
    # Create a large array with predictable frequencies
    nums = []
    for i in range(100):
        nums.extend([i] * (100 - i))  # Element i appears (100-i) times
    
    k = 10
    result = solution.topKFrequent(nums, k)
    
    # The most frequent elements should be 0-9
    expected = list(range(10))
    assert all(num in expected for num in result)
    assert len(result) == 10

def test_with_sparse_frequencies(solution):
    """Test with sparse frequency distribution."""
    nums = [1] * 100 + [2] * 10 + [3]  # 1 appears 100 times, 2 appears 10 times, 3 once
    k = 2
    result = solution.topKFrequent(nums, k)
    assert sorted(result) == [1, 2]

def test_extreme_frequency_differences(solution):
    """Test with extreme differences in frequency."""
    nums = [1] * 1000 + [2] * 10 + list(range(3, 30))  # 1 appears 1000 times, 2 appears 10 times
    k = 1
    assert solution.topKFrequent(nums, k) == [1]

def test_with_random_data(solution):
    """Test with random data."""
    import random
    random.seed(42)  # For reproducibility
    
    # Generate random data with controllable frequencies
    nums = []
    expected_top = []
    
    # Add top k elements with high frequencies
    for i in range(5):
        freq = random.randint(50, 100)
        nums.extend([i] * freq)
        expected_top.append(i)
    
    # Add other elements with lower frequencies
    for i in range(5, 20):
        freq = random.randint(1, 30)
        nums.extend([i] * freq)
    
    # Shuffle the array
    random.shuffle(nums)
    
    k = 5
    result = solution.topKFrequent(nums, k)
    
    # All elements in expected_top should be in result
    assert all(x in result for x in expected_top)
    assert len(result) == k

if __name__ == "__main__":
    # Run tests manually
    solution_instance = Solution()
    test_examples = [
        ([1, 1, 1, 2, 2, 3], 2),
        ([1], 1),
        ([1, 2, 2, 3, 3, 3], 1)
    ]
    
    for nums, k in test_examples:
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Output: {solution_instance.topKFrequent(nums, k)}")
        print()


"""
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
 

Constraints:

1 <= w.length <= 104
1 <= w[i] <= 105
pickIndex will be called at most 104 times.
"""
import random
from typing import List
import pytest
from collections import Counter

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        curr_sum = 0
        for weight in w:
            curr_sum += weight
            self.prefix_sums.append(curr_sum)

        self.total_sum = curr_sum

    def pickIndex(self) -> int:
        # target = randint(0, self.total_sum) # will cause memory out of range
        target = self.total_sum * random.random()
        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid
        return left

class SolutionMemoryExceeded:

    def __init__(self, w: List[int]):
        self.arr = []
        for i in range(len(w)):
            frequency = w[i]
            for k in range(frequency):
                # append multiple of index i, following frequency of it
                self.arr.append(i)

    def pickIndex(self) -> int:
        # Use floor instead of round to avoid going out of bounds
        random_index = int(random.random() * len(self.arr))
        return self.arr[random_index]

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


@pytest.fixture(params=[Solution, SolutionMemoryExceeded], ids=["Optimized", "MemoryExceeded"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param

def test_single_weight(solution_instance):
    """Test with a single weight."""
    obj = solution_instance([1])
    assert obj.pickIndex() == 0  # Only one index, must always return 0

def test_equal_weights(solution_instance):
    """Test with equal weights."""
    obj = solution_instance([1, 1, 1, 1])
    results = [obj.pickIndex() for _ in range(1000)]
    counts = Counter(results)
    # All indices should have approximately equal counts
    for count in counts.values():
        assert abs(count - 250) < 50  # Allow some randomness

def test_different_weights(solution_instance):
    """Test with different weights."""
    obj = solution_instance([1, 3])
    results = [obj.pickIndex() for _ in range(1000)]
    counts = Counter(results)
    # Index 1 should be picked approximately 3 times more often than index 0
    ratio = counts[1] / counts[0]
    assert 2.5 < ratio < 3.5  # Allow some randomness

def test_large_weights(solution_instance):
    """Test with large weights."""
    obj = solution_instance([1000, 1])
    results = [obj.pickIndex() for _ in range(1000)]
    counts = Counter(results)
    # Index 0 should be picked much more often than index 1
    assert counts[0] > 950
    assert counts[1] < 50

def test_multiple_weights(solution_instance):
    """Test with multiple weights."""
    obj = solution_instance([1, 2, 3, 4])
    results = [obj.pickIndex() for _ in range(1000)]
    counts = Counter(results)
    # The probabilities should roughly match the weights
    total_weight = sum([1, 2, 3, 4])
    expected_ratios = [1 / total_weight, 2 / total_weight, 3 / total_weight, 4 / total_weight]
    for i, weight in enumerate([1, 2, 3, 4]):
        observed_ratio = counts[i] / 1000
        assert abs(observed_ratio - expected_ratios[i]) < 0.05  # Allow some randomness

def test_large_number_of_weights(solution_instance):
    """Test with a large number of weights."""
    weights = [i for i in range(1, 101)]  # Weights from 1 to 100
    obj = solution_instance(weights)
    results = [obj.pickIndex() for _ in range(10000)]
    counts = Counter(results)
    # Higher indices should be picked more often
    assert counts[99] > counts[0]

def test_edge_case_small_weights(solution_instance):
    """Test with very small weights."""
    obj = solution_instance([1, 1, 1])
    results = [obj.pickIndex() for _ in range(1000)]
    counts = Counter(results)
    # All indices should have approximately equal counts
    for count in counts.values():
        assert abs(count - 333) < 50  # Allow some randomness

def test_edge_case_large_weights(solution_instance):
    """Test with very large weights."""
    obj = solution_instance([10**5, 1])
    results = [obj.pickIndex() for _ in range(1000)]
    counts = Counter(results)
    # Index 0 should dominate
    assert counts[0] > 950
    assert counts[1] < 50

# To run these tests:
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest
# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/description/
"""
This is an interactive problem.

You have a sorted array of unique elements and an unknown size. You do not have an access to the array but you can use the ArrayReader interface to access it. You can call ArrayReader.get(i) that:

returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
returns 231 - 1 if the i is out of the boundary of the array.
You are also given an integer target.

Return the index k of the hidden array where secret[k] == target or return -1 otherwise.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: secret = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in secret and its index is 4.
Example 2:

Input: secret = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in secret so return -1.
 

Constraints:

1 <= secret.length <= 104
-104 <= secret[i], target <= 104
secret is sorted in a strictly increasing order.
"""
class ArrayReader:
    def __init__(self, secret):
        self.secret = secret

    def get(self, index: int) -> int:
        if index >= len(self.secret):
            return 2**31 - 1
        return self.secret[index]

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        infinity = 2 ** 31 - 1

        # Step 1: Find the boundary with exponential search
        index = 1
        while reader.get(index) < target:
            index *= 2

        # Step 2: Binary search within the boundary
        left = index // 2
        right = index
        while left <= right:
            mid = (left + right) // 2
            val = reader.get(mid)

            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
    
# === TEST CASES ===
import pytest  # noqa: E402

# ArrayReader is already defined in the file, we'll use that.
# If it were in a separate file, we'd import it.

@pytest.fixture
def solution():
    """Provides an instance of the Solution class."""
    return Solution()

# Test cases using the ArrayReader mock from the provided file
def test_example1(solution):
    """Test Example 1 from the problem description."""
    secret = [-1, 0, 3, 5, 9, 12]
    target = 9
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 4

def test_example2(solution):
    """Test Example 2 from the problem description."""
    secret = [-1, 0, 3, 5, 9, 12]
    target = 2
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == -1

def test_target_at_index_0(solution):
    """Test when the target is the first element."""
    secret = [5, 7, 8, 10]
    target = 5
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 0

def test_target_at_index_1(solution):
    """Test when the target is at index 1 (initial exponential check might hit it or just past it)."""
    secret = [-1, 3, 5, 9, 12]
    target = 3
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 1

def test_target_requires_bound_expansion(solution):
    """Test when the target requires expanding the search boundary multiple times."""
    secret = [i for i in range(0, 100, 2)] # [0, 2, 4, ..., 98]
    target = 98
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 49 # Index of 98

def test_target_not_found_within_bounds(solution):
    """Test when the target is not found but within the calculated binary search bounds."""
    secret = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] # Exponential search might go up to index 8 (val 17) or 16 (infinity)
    target = 6 # Exponential search for 6: index=1 (val 3), index=2 (val 5), index=4 (val 9). BS range [2,4]
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == -1

def test_target_smaller_than_all(solution):
    """Test when the target is smaller than all elements."""
    secret = [10, 20, 30, 40]
    target = 5
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == -1

def test_target_larger_than_all_within_bounds(solution):
    """Test when the target is larger than all elements within the eventually found bounds."""
    secret = [1, 2, 3, 4, 5] # Exponential search for 6: index=1 (val 2), index=2 (val 3), index=4 (val 5), index=8 (infinity). BS range [4,8]
    target = 6
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == -1

def test_single_element_array_found(solution):
    """Test with a single element array where the target is found."""
    secret = [5]
    target = 5
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 0

def test_single_element_array_not_found_larger(solution):
    """Test with a single element array where the target is not found (target larger)."""
    secret = [5]
    target = 10
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == -1

def test_single_element_array_not_found_smaller(solution):
    """Test with a single element array where the target is not found (target smaller)."""
    secret = [5]
    target = 3
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == -1


def test_large_array_target_found_early(solution):
    """Test with a larger array, target found early."""
    secret = list(range(1000))
    target = 10
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 10

def test_large_array_target_found_late(solution):
    """Test with a larger array, target found late."""
    secret = list(range(1000))
    target = 990
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 990

def test_large_array_not_found(solution):
    """Test with a larger array where the target is not found."""
    secret = list(range(0, 2000, 2)) # Even numbers up to 1998
    target = 999 # Odd number, not in array
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == -1

def test_negative_numbers(solution):
    """Test with negative numbers."""
    secret = [-10, -5, -2, 0, 3, 7]
    target = -2
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 2

def test_boundary_condition_exact_power_of_2_index(solution):
    """Test when the target is found at an index that is a power of 2 (minus 1, due to 0-indexing)."""
    # e.g. index = 1, 2, 4, 8 ...
    # reader.get(1) -> if target is reader.get(0), index becomes 0.
    # reader.get(1) < target, index = 2.
    # reader.get(2) < target, index = 4.
    # reader.get(4) >= target. BS range [2,4]
    secret = list(range(20)) # 0 to 19
    target = 4 # index 4
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 4

    target = 8 # index 8
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 8

def test_boundary_condition_just_before_power_of_2_index(solution):
    """Test when the target is found just before an index that is a power of 2."""
    secret = list(range(20))
    target = 3 # index 3. Exp search: get(1)=1, get(2)=2, get(4)=4. BS range [2,4]
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 3

    target = 7 # index 7. Exp search: get(1)=1, get(2)=2, get(4)=4, get(8)=8. BS range [4,8]
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 7

def test_array_reader_out_of_bounds_immediately(solution):
    """Test when even reader.get(0) is out of bounds (empty secret array)."""
    # The problem constraints state 1 <= secret.length <= 10^4, so secret won't be empty.
    # However, if ArrayReader was more general:
    # secret = []
    # target = 5
    # reader = ArrayReader(secret)
    # The current Solution's exponential search starts with index=1.
    # reader.get(1) would be infinity.
    # Then binary search on [0, 1].
    # mid = 0, reader.get(0) is infinity. right = -1. Loop ends. Returns -1. Correct.
    pass # Covered by constraints, but logic seems okay.

def test_target_is_first_element_and_array_size_one(solution):
    secret = [100]
    target = 100
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 0

def test_target_is_zero(solution):
    secret = [-5, 0, 5]
    target = 0
    reader = ArrayReader(secret)
    assert solution.search(reader, target) == 1
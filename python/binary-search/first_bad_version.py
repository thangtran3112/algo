# https://leetcode.com/problems/first-bad-version/description/
"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Binary search
class Solution:
    def firstBadVersion(self, n: int, isBadVersion) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            res = isBadVersion(mid)

            if res is True:
                # the first bad version will be within [left, mid] inclusively
                # trying to find right, until we have the first right, which is bad version
                right = mid
            else:
                # the first bad version will be within [mid + 1, right]
                left = mid + 1

        # in case that the bad version could be the next to right
        return right if isBadVersion(right) else right - 1

import pytest  # noqa: E402

@pytest.fixture
def solution():
    return Solution()

def create_is_bad_version(bad_version):
    """Create an isBadVersion function with the specified first bad version."""
    def isBadVersion(version):
        return version >= bad_version
    return isBadVersion

def test_example_1(solution):
    """Test the first example from the problem statement."""
    n = 5
    bad = 4
    isBadVersion = create_is_bad_version(bad)
    assert solution.firstBadVersion(n, isBadVersion) == 4

def test_example_2(solution):
    """Test the second example from the problem statement."""
    n = 1
    bad = 1
    isBadVersion = create_is_bad_version(bad)
    assert solution.firstBadVersion(n, isBadVersion) == 1

def test_all_bad_versions(solution):
    """Test when all versions are bad."""
    n = 10
    bad = 1
    isBadVersion = create_is_bad_version(bad)
    assert solution.firstBadVersion(n, isBadVersion) == 1

def test_bad_version_in_middle(solution):
    """Test when the bad version is somewhere in the middle."""
    n = 100
    bad = 50
    isBadVersion = create_is_bad_version(bad)
    assert solution.firstBadVersion(n, isBadVersion) == 50

def test_large_number_of_versions(solution):
    """Test with a large number of versions."""
    n = 10**6
    bad = 500000
    isBadVersion = create_is_bad_version(bad)
    assert solution.firstBadVersion(n, isBadVersion) == 500000

def test_last_version_is_bad(solution):
    """Test when only the last version is bad."""
    n = 100
    bad = 100
    isBadVersion = create_is_bad_version(bad)
    assert solution.firstBadVersion(n, isBadVersion) == 100

def test_second_version_is_bad(solution):
    """Test when the second version is the first bad one."""
    n = 100
    bad = 2
    isBadVersion = create_is_bad_version(bad)
    assert solution.firstBadVersion(n, isBadVersion) == 2

def test_boundary_case_maximum_n(solution):
    """Test with n close to the maximum constraint."""
    n = 2**31 - 1
    bad = 2**31 - 100
    isBadVersion = create_is_bad_version(bad)
    assert solution.firstBadVersion(n, isBadVersion) == 2**31 - 100

def test_sequential_search_edge_cases(solution):
    """Test sequential search edge cases where binary search might have edge cases."""
    # Testing cases where binary search might have edge conditions
    test_cases = [
        (2, 1),    # First version is bad
        (2, 2),    # Last version is bad
        (3, 2),    # Middle version is bad
    ]
    
    for n, bad in test_cases:
        isBadVersion = create_is_bad_version(bad)
        assert solution.firstBadVersion(n, isBadVersion) == bad
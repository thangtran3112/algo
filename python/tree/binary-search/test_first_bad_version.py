import pytest
from first_bad_version import Solution

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
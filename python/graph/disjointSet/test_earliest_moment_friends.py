import pytest
from earliest_moment_friends import Solution

# pytest -v .\python\graph\disjointSet\test_earliest_moment_friends.py
class TestEarliestMomentFriends:
    def test_example_1(self):
        """Test with example 1 from the problem statement"""
        solution = Solution()
        logs = [
            [20190101, 0, 1],
            [20190104, 3, 4],
            [20190107, 2, 3],
            [20190211, 1, 5],
            [20190224, 2, 4],
            [20190301, 0, 3],
            [20190312, 1, 2],
            [20190322, 4, 5]
        ]
        n = 6
        assert solution.earliestAcq(logs, n) == 20190301

    def test_example_2(self):
        """Test with example 2 from the problem statement"""
        solution = Solution()
        logs = [
            [0, 2, 0],
            [1, 0, 1],
            [3, 0, 3],
            [4, 1, 2],
            [7, 3, 1]
        ]
        n = 4
        assert solution.earliestAcq(logs, n) == 3

    def test_already_connected_group(self):
        """Test with logs where some people are already connected"""
        solution = Solution()
        logs = [
            [10, 0, 1],  # Connect 0-1
            [20, 1, 2],  # Connect 1-2 (and by extension, 0-1-2 all connected)
            [30, 0, 2]   # 0 and 2 are already connected indirectly
        ]
        n = 3
        # Everyone becomes friends at timestamp 20, when 1 and 2 become friends
        # (0 was already friends with 1 from the first log)
        assert solution.earliestAcq(logs, n) == 20

    def test_unsorted_logs(self):
        """Test with logs that are not sorted by timestamp"""
        solution = Solution()
        logs = [
            [30, 0, 2],
            [20, 1, 2],
            [10, 0, 1]
        ]
        n = 3
        # Despite being unsorted, the algorithm should sort them and correctly identify 20
        assert solution.earliestAcq(logs, n) == 20

    def test_not_enough_connections(self):
        """Test when there aren't enough connections to connect everyone"""
        solution = Solution()
        logs = [
            [10, 0, 1],
            [20, 2, 3]
        ]
        n = 4
        # We have two separate groups: [0,1] and [2,3], but no connection between them
        assert solution.earliestAcq(logs, n) == -1

    def test_single_connection_needed(self):
        """Test when only one connection is needed"""
        solution = Solution()
        logs = [
            [5, 0, 1]
        ]
        n = 2
        assert solution.earliestAcq(logs, n) == 5

    def test_minimum_connections_needed(self):
        """Test with the minimum number of connections needed (n-1)"""
        solution = Solution()
        logs = [
            [1, 0, 1],
            [2, 1, 2],
            [3, 2, 3],
            [4, 3, 4]
        ]
        n = 5
        # The last connection at timestamp 4 makes everyone friends
        assert solution.earliestAcq(logs, n) == 4

    def test_redundant_connections(self):
        """Test with redundant connections that don't change the result"""
        solution = Solution()
        logs = [
            [1, 0, 1],
            [2, 1, 2],
            [3, 0, 2],  # Redundant, as 0-1-2 already forms a connected group
            [4, 2, 3]
        ]
        n = 4
        assert solution.earliestAcq(logs, n) == 4

    def test_large_group(self):
        """Test with a larger number of people"""
        solution = Solution()
        # Create a star-shaped connection pattern where person 0 connects to everyone else
        logs = [[i, 0, i] for i in range(1, 10)]
        n = 10
        # The timestamp of the last connection (9) is when everyone becomes friends
        assert solution.earliestAcq(logs, n) == 9

    def test_complex_connection_pattern(self):
        """Test with a more complex connection pattern"""
        solution = Solution()
        logs = [
            [10, 0, 1],  # Group: [0,1], [2], [3], [4]
            [20, 2, 3],  # Group: [0,1], [2,3], [4]
            [30, 1, 4],  # Group: [0,1,4], [2,3]
            [40, 1, 2]   # Group: [0,1,2,3,4] - everyone connected
        ]
        n = 5
        assert solution.earliestAcq(logs, n) == 40

    def test_immediate_friendship(self):
        """Test when everyone becomes friends at the earliest possible timestamp"""
        solution = Solution()
        # In a group of 3, we need exactly 2 connections
        logs = [
            [5, 0, 1],
            [5, 1, 2]  # Same timestamp as the first connection
        ]
        n = 3
        # Everyone becomes friends at timestamp 5
        assert solution.earliestAcq(logs, n) == 5
    
    def test_cyclic_connections(self):
        """Test with cyclic connection pattern"""
        solution = Solution()
        logs = [
            [1, 0, 1],
            [2, 1, 2],
            [3, 2, 3],
            [4, 3, 0]  # Creates a cycle 0-1-2-3-0
        ]
        n = 4
        # Everyone becomes friends at timestamp 3, when 2-3 connection is made
        # (This creates path 0-1-2-3)
        assert solution.earliestAcq(logs, n) == 3
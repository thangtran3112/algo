import pytest
from count_provinces import SolutionWithUnionFind


# pytest -v python/graph/test_count_provinces.py
class TestSolutionWithUnionFind:
    def test_example1(self):
        """Test with first example from problem statement"""
        solution = SolutionWithUnionFind()
        isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        assert solution.findCircleNum(isConnected) == 2

    def test_example2(self):
        """Test with second example from problem statement"""
        solution = SolutionWithUnionFind()
        isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        assert solution.findCircleNum(isConnected) == 3

    def test_single_city(self):
        """Test with a single city"""
        solution = SolutionWithUnionFind()
        isConnected = [[1]]
        assert solution.findCircleNum(isConnected) == 1

    def test_all_connected(self):
        """Test when all cities are connected"""
        solution = SolutionWithUnionFind()
        isConnected = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        assert solution.findCircleNum(isConnected) == 1

    def test_none_connected(self):
        """Test when no cities are connected (except to themselves)"""
        solution = SolutionWithUnionFind()
        isConnected = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        assert solution.findCircleNum(isConnected) == 4

    def test_non_transitive_connections(self):
        """Test with connections that are not immediately transitive"""
        solution = SolutionWithUnionFind()
        isConnected = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
        assert solution.findCircleNum(isConnected) == 2

    def test_complex_connection_pattern(self):
        """Test with a more complex connection pattern"""
        solution = SolutionWithUnionFind()
        isConnected = [
            [1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
        ]
        # Cities 0,3,4 form one province and 1,2 form another
        assert solution.findCircleNum(isConnected) == 2

    def test_indirect_connections(self):
        """Test indirect connections through intermediary cities"""
        solution = SolutionWithUnionFind()
        isConnected = [
            [1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1],
        ]
        # All cities are connected through intermediaries
        assert solution.findCircleNum(isConnected) == 1

    def test_larger_graph(self):
        """Test with a larger graph"""
        solution = SolutionWithUnionFind()
        # 10 cities with 3 provinces
        isConnected = [
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        ]
        assert solution.findCircleNum(isConnected) == 3

    def test_asymmetric_connections(self):
        """Test with asymmetric connection matrix (should handle properly)"""
        solution = SolutionWithUnionFind()
        # This is technically invalid input since the matrix should be symmetric,
        # but testing how the solution handles it
        isConnected = [
            [1, 1, 0],
            [0, 1, 0],  # Note: [1,0] is 0 but [0,1] is 1
            [0, 0, 1],
        ]
        # The solution should use the upper triangle, so it should see
        # a connection between 0 and 1, making it 2 provinces
        assert solution.findCircleNum(isConnected) == 2

    def test_disconnected_diagonal(self):
        """Test with disconnected diagonal (invalid but checking handling)"""
        solution = SolutionWithUnionFind()
        # This is technically invalid input (diagonal should be all 1s)
        isConnected = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
        # Even with invalid diagonal, the solution should find connections
        assert solution.findCircleNum(isConnected) == 2

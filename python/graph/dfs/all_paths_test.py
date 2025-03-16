import pytest
from all_paths import Solution, SolutionWithStack

# Define a fixture that parameterizes over both solution implementations
@pytest.fixture(params=[
    Solution(),
    SolutionWithStack()
])
def solver(request):
    return request.param

class TestAllPathsSourceTarget:
    def test_example_1(self, solver):
        """Test with example 1 from the problem statement"""
        graph = [[1, 2], [3], [3], []]
        expected = [[0, 1, 3], [0, 2, 3]]
        result = solver.allPathsSourceTarget(graph)
        
        # Sort both expected and result for consistent comparison
        expected.sort()
        result.sort()
        assert result == expected

    def test_example_2(self, solver):
        """Test with example 2 from the problem statement"""
        graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
        expected = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
        result = solver.allPathsSourceTarget(graph)
        
        # Sort both expected and result for consistent comparison
        expected.sort()
        result.sort()
        assert result == expected

    def test_single_path(self, solver):
        """Test with a graph containing only one path"""
        graph = [[1], [2], [3], []]
        expected = [[0, 1, 2, 3]]
        result = solver.allPathsSourceTarget(graph)
        assert result == expected

    def test_no_path(self, solver):
        """Test with a graph where there's no path from source to target"""
        graph = [[1], [2], [], []]  # No path to node 3
        expected = []
        result = solver.allPathsSourceTarget(graph)
        assert result == expected

    def test_multiple_direct_paths(self, solver):
        """Test with a graph where all paths are direct from source to destination"""
        graph = [[1, 2, 3], [], [], []]
        expected = [[0, 3]]
        result = solver.allPathsSourceTarget(graph)
        assert result == expected

    def test_branching_paths(self, solver):
        """Test with a graph that has multiple branching paths"""
        graph = [[1, 2], [3, 4], [3, 4], [5], [5], []]
        expected = [
            [0, 1, 3, 5],
            [0, 1, 4, 5],
            [0, 2, 3, 5],
            [0, 2, 4, 5]
        ]
        result = solver.allPathsSourceTarget(graph)
        
        # Sort both expected and result for consistent comparison
        expected.sort()
        result.sort()
        assert result == expected

    def test_complex_dag(self, solver):
        """Test with a more complex DAG with many possible paths"""
        graph = [[1, 2, 3], [4, 5], [4, 5], [4, 5], [6], [6], []]
        expected = [
            [0, 1, 4, 6],
            [0, 1, 5, 6],
            [0, 2, 4, 6],
            [0, 2, 5, 6],
            [0, 3, 4, 6],
            [0, 3, 5, 6]
        ]
        result = solver.allPathsSourceTarget(graph)
        
        # Sort both expected and result for consistent comparison
        expected.sort()
        result.sort()
        assert result == expected

    def test_minimal_graph(self, solver):
        """Test with a minimal graph of just 2 nodes"""
        graph = [[1], []]
        expected = [[0, 1]]
        result = solver.allPathsSourceTarget(graph)
        assert result == expected

    def test_diamond_shape(self, solver):
        """Test with a diamond-shaped graph"""
        # Diamond shape: 0 -> 1 -> 3
        #             \-> 2 -/
        graph = [[1, 2], [3], [3], []]
        expected = [[0, 1, 3], [0, 2, 3]]
        result = solver.allPathsSourceTarget(graph)
        
        # Sort both expected and result for consistent comparison
        expected.sort()
        result.sort()
        assert result == expected

    def test_multiple_paths_same_length(self, solver):
        """Test with multiple paths of the same length"""
        graph = [[1, 2, 3], [4], [4], [4], []]
        expected = [[0, 1, 4], [0, 2, 4], [0, 3, 4]]
        result = solver.allPathsSourceTarget(graph)
        
        # Sort both expected and result for consistent comparison
        expected.sort()
        result.sort()
        assert result == expected

    def test_dense_graph(self, solver):
        """Test with a dense graph where almost every node connects to every other node"""
        # Each node connects to all nodes with higher indices
        graph = [
            [1, 2, 3, 4],  # Node 0 connects to 1,2,3,4
            [2, 3, 4],     # Node 1 connects to 2,3,4
            [3, 4],        # Node 2 connects to 3,4
            [4],           # Node 3 connects to 4
            []             # Node 4 has no outgoing edges
        ]
        expected = [
            [0, 1, 2, 3, 4],
            [0, 1, 2, 4],
            [0, 1, 3, 4],
            [0, 1, 4],
            [0, 2, 3, 4],
            [0, 2, 4],
            [0, 3, 4],
            [0, 4]
        ]
        result = solver.allPathsSourceTarget(graph)
        
        # Sort both expected and result for consistent comparison
        expected.sort()
        result.sort()
        assert result == expected
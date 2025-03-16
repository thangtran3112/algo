import pytest

from path_exist import Solution
from path_exist import SolutionWithStack

# Define all solution implementations to test
# pytest python/graph/dfs/path_exist_test.py -v
@pytest.fixture(params=[
    Solution(),
    SolutionWithStack()
])
def solver(request):
    return request.param

# Test cases that will run for both solution implementations
class TestPathExist:
    def test_example_1(self, solver):
        n = 3
        edges = [[0, 1], [1, 2], [2, 0]]
        source = 0
        destination = 2
        assert solver.validPath(n, edges, source, destination) is True

    def test_example_2(self, solver):
        n = 6
        edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
        source = 0
        destination = 5
        assert solver.validPath(n, edges, source, destination) is False

    def test_single_node(self, solver):
        n = 1
        edges = []
        source = 0
        destination = 0
        assert solver.validPath(n, edges, source, destination) is True

    def test_no_edges(self, solver):
        n = 4
        edges = []
        source = 0
        destination = 3
        assert solver.validPath(n, edges, source, destination) is False

    def test_direct_connection(self, solver):
        n = 2
        edges = [[0, 1]]
        source = 0
        destination = 1
        assert solver.validPath(n, edges, source, destination) is True

    def test_disconnected_graph(self, solver):
        n = 5
        edges = [[0, 1], [2, 3]]
        source = 0
        destination = 3
        assert solver.validPath(n, edges, source, destination) is False

    def test_cycle_graph(self, solver):
        n = 4
        edges = [[0, 1], [1, 2], [2, 3], [3, 0]]
        source = 0
        destination = 2
        assert solver.validPath(n, edges, source, destination) is True

    def test_multiple_paths(self, solver):
        n = 5
        edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
        source = 0
        destination = 4
        assert solver.validPath(n, edges, source, destination) is True

    def test_bidirectional_path(self, solver):
        n = 3
        edges = [[0, 1], [1, 2]]
        source = 2
        destination = 0
        assert solver.validPath(n, edges, source, destination) is True

    def test_source_equals_destination(self, solver):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        source = 2
        destination = 2
        assert solver.validPath(n, edges, source, destination) is True

    def test_large_graph(self, solver):
        n = 50
        # Create a chain from 0 to 49
        edges = [[i, i+1] for i in range(49)]
        source = 0
        destination = 49
        assert solver.validPath(n, edges, source, destination) is True

    def test_complex_graph(self, solver):
        n = 8
        edges = [
            [0, 1], [1, 2], [2, 3], [3, 4],
            [4, 5], [5, 6], [6, 7], [0, 7],
            [1, 7], [2, 6], [3, 5]
        ]
        source = 0
        destination = 7
        assert solver.validPath(n, edges, source, destination) is True

    def test_isolated_nodes(self, solver):
        n = 5
        edges = [[1, 2], [2, 3]]  # Nodes 0 and 4 are isolated
        source = 0
        destination = 4
        assert solver.validPath(n, edges, source, destination) is False
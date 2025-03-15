import pytest

from path_exist import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    assert solution.validPath(n, edges, source, destination) is True

def test_example_2(solution):
    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    destination = 5
    assert solution.validPath(n, edges, source, destination) is False

def test_single_node(solution):
    n = 1
    edges = []
    source = 0
    destination = 0
    assert solution.validPath(n, edges, source, destination) is True

def test_no_edges(solution):
    n = 4
    edges = []
    source = 0
    destination = 3
    assert solution.validPath(n, edges, source, destination) is False

def test_direct_connection(solution):
    n = 2
    edges = [[0,1]]
    source = 0
    destination = 1
    assert solution.validPath(n, edges, source, destination) is True

def test_disconnected_graph(solution):
    n = 5
    edges = [[0,1],[2,3]]
    source = 0
    destination = 3
    assert solution.validPath(n, edges, source, destination) is False

def test_cycle_graph(solution):
    n = 4
    edges = [[0,1],[1,2],[2,3],[3,0]]
    source = 0
    destination = 2
    assert solution.validPath(n, edges, source, destination) is True

def test_multiple_paths(solution):
    n = 5
    edges = [[0,1],[0,2],[1,3],[2,3],[3,4]]
    source = 0
    destination = 4
    assert solution.validPath(n, edges, source, destination) is True

def test_no_path_due_to_direction(solution):
    n = 3
    edges = [[0,1],[1,2]]
    source = 2
    destination = 0
    assert solution.validPath(n, edges, source, destination) is True
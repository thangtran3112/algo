import pytest
from network_time_delay import SolutionBellmanFord

@pytest.fixture
def solution():
    return SolutionBellmanFord()

def test_example_1(solution):
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    assert solution.networkDelayTime(times, n, k) == 2

def test_example_2(solution):
    times = [[1, 2, 1]]
    n = 2
    k = 1
    assert solution.networkDelayTime(times, n, k) == 1

def test_example_3(solution):
    times = [[1, 2, 1]]
    n = 2
    k = 2
    assert solution.networkDelayTime(times, n, k) == -1

def test_disconnected_graph(solution):
    times = [[1, 2, 1], [2, 3, 2]]
    n = 4
    k = 1
    assert solution.networkDelayTime(times, n, k) == -1  # Node 4 is unreachable

def test_large_weights(solution):
    times = [[1, 2, 100], [2, 3, 100], [3, 4, 100]]
    n = 4
    k = 1
    assert solution.networkDelayTime(times, n, k) == 300

def test_single_node(solution):
    times = []
    n = 1
    k = 1
    assert solution.networkDelayTime(times, n, k) == 0

def test_two_nodes_direct_connection(solution):
    times = [[1, 2, 5]]
    n = 2
    k = 1
    assert solution.networkDelayTime(times, n, k) == 5

def test_two_nodes_no_connection(solution):
    times = []
    n = 2
    k = 1
    assert solution.networkDelayTime(times, n, k) == -1

def test_cycle_in_graph(solution):
    times = [[1, 2, 1], [2, 3, 1], [3, 1, 1]]
    n = 3
    k = 1
    assert solution.networkDelayTime(times, n, k) == 2

def test_large_graph(solution):
    times = [[i, i + 1, 1] for i in range(1, 100)]
    n = 100
    k = 1
    assert solution.networkDelayTime(times, n, k) == 99

def test_multiple_paths(solution):
    times = [[1, 2, 1], [1, 3, 4], [2, 3, 2]]
    n = 3
    k = 1
    assert solution.networkDelayTime(times, n, k) == 3  # Shortest path is 1 -> 2 -> 3

def test_unreachable_node(solution):
    times = [[1, 2, 1], [2, 3, 2]]
    n = 4
    k = 1
    assert solution.networkDelayTime(times, n, k) == -1  # Node 4 is unreachable

def test_large_weights_with_unreachable_node(solution):
    times = [[1, 2, 100], [2, 3, 100]]
    n = 4
    k = 1
    assert solution.networkDelayTime(times, n, k) == -1  # Node 4 is unreachable

def test_multiple_edges_between_nodes(solution):
    times = [[1, 2, 1], [1, 2, 2], [2, 3, 1]]
    n = 3
    k = 1
    assert solution.networkDelayTime(times, n, k) == 2  # Shortest path is 1 -> 2 -> 3

def test_large_dense_graph(solution):
    # Fully connected graph with 100 nodes and random weights
    n = 100
    k = 1
    times = [[i, j, (i + j) % 100 + 1] for i in range(1, n + 1) for j in range(1, n + 1) if i != j]
    assert solution.networkDelayTime(times, n, k) > 0  # Ensure it runs without errors

def test_large_sparse_graph(solution):
    # Sparse graph with 1000 nodes and only 999 edges forming a line
    n = 100
    k = 1
    times = [[i, i + 1, 1] for i in range(1, n)]
    assert solution.networkDelayTime(times, n, k) == 99  # Linear connection from 1 to 1000

def test_large_graph_with_unreachable_nodes(solution):
    # Graph with 1000 nodes but only 500 connected
    n = 100
    k = 1
    times = [[i, i + 1, 1] for i in range(1, 50)]
    assert solution.networkDelayTime(times, n, k) == -1  # Nodes 501 to 1000 are unreachable

def test_large_graph_with_random_weights(solution):
    # Graph with 100 nodes and random weights
    import random
    n = 100
    k = 1
    random.seed(42)
    times = [[i, i + 1, random.randint(1, 100)] for i in range(1, n)]
    assert solution.networkDelayTime(times, n, k) > 0  # Ensure it runs without errors

def test_large_graph_with_multiple_paths(solution):
    # Graph with 100 nodes and multiple paths between nodes
    n = 100
    k = 1
    times = [[i, i + 1, 1] for i in range(1, n)] + [[1, i, i] for i in range(2, n + 1)]
    assert solution.networkDelayTime(times, n, k) == 99  # Shortest path is linear
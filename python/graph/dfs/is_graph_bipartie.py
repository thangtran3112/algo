# https://leetcode.com/problems/is-graph-bipartite/description/
"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

 

Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

Constraints:

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
"""
from collections import deque
from typing import List


class SolutionBFS:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        NOT_SEEN = -1
        RED = 0
        BLUE = 1
        n = len(graph)
        colors = [NOT_SEEN] * n

        # BFS through the graph
        # if a node is never seen, marks it with the same color as the start node
        # if meeting a node of different color, return False
        for start_node in range(n):
            # if node was never met before from previous neighbors, we are processing it

            # if a node is already met from other nodes, the whole previous cluster has
            # already be evaluated. We can ignore it
            if colors[start_node] != -1:
                continue

            # Case: a new node never visited before from neighbors
            # from all previous clusters. traversing from this node to mark its whole cluster
            # Since it is a new disjoint set, we can color the node with whatever color
            colors[start_node] = RED
            queue = deque([start_node])
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if colors[neighbor] == NOT_SEEN:
                        colors[neighbor] = RED if colors[curr] == BLUE else BLUE
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[curr]:
                        return False

        return True
    
class SolutionDFS:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        NOT_SEEN = -1
        RED = 0
        BLUE = 1
        n = len(graph)
        colors = [NOT_SEEN] * n

        def dfs(start_node: int, expected_color: int):
            if colors[start_node] == NOT_SEEN:
                colors[start_node] = expected_color
            elif colors[start_node] != expected_color:
                return False

            next_color = RED if expected_color == BLUE else BLUE
            for neighbor in graph[start_node]:
                if colors[neighbor] == NOT_SEEN:
                    if not dfs(neighbor, next_color):
                        return False
                elif colors[neighbor] == colors[start_node]:
                    return False
            return True

        for i in range(n):
            if colors[i] == NOT_SEEN:
                if not dfs(i, NOT_SEEN):
                    return False
        return True

# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[SolutionBFS, SolutionDFS],
               ids=["BFS", "DFS"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description (not bipartite)."""
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    assert solution_instance.isBipartite(graph) is False

def test_example2(solution_instance):
    """Test Example 2 from the problem description (bipartite)."""
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    assert solution_instance.isBipartite(graph) is True

def test_disconnected_bipartite(solution_instance):
    """Test a disconnected graph where all components are bipartite."""
    graph = [[1], [0], [3], [2]]  # Two separate edges: 0-1 and 2-3
    assert solution_instance.isBipartite(graph) is True

def test_disconnected_non_bipartite(solution_instance):
    """Test a disconnected graph where one component is not bipartite."""
    graph = [[1, 2], [0, 2], [0, 1], [4], [3]]  # Triangle 0-1-2 and edge 3-4
    assert solution_instance.isBipartite(graph) is False

def test_single_node(solution_instance):
    """Test a graph with a single node."""
    graph = [[]]
    assert solution_instance.isBipartite(graph) is True

def test_two_nodes_connected(solution_instance):
    """Test a graph with two connected nodes."""
    graph = [[1], [0]]
    assert solution_instance.isBipartite(graph) is True

def test_two_nodes_disconnected(solution_instance):
    """Test a graph with two disconnected nodes."""
    graph = [[], []]
    assert solution_instance.isBipartite(graph) is True

def test_triangle(solution_instance):
    """Test a simple triangle graph (not bipartite)."""
    graph = [[1, 2], [0, 2], [0, 1]]
    assert solution_instance.isBipartite(graph) is False

def test_square(solution_instance):
    """Test a simple square graph (bipartite)."""
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    assert solution_instance.isBipartite(graph) is True

def test_pentagon(solution_instance):
    """Test a simple pentagon graph (not bipartite)."""
    graph = [[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]]
    assert solution_instance.isBipartite(graph) is False

def test_hexagon(solution_instance):
    """Test a simple hexagon graph (bipartite)."""
    graph = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [0, 4]]
    assert solution_instance.isBipartite(graph) is True

def test_line_graph(solution_instance):
    """Test a line graph (bipartite)."""
    graph = [[1], [0, 2], [1, 3], [2, 4], [3]]
    assert solution_instance.isBipartite(graph) is True

def test_star_graph(solution_instance):
    """Test a star graph (bipartite)."""
    graph = [[1, 2, 3], [0], [0], [0]]  # Node 0 connected to 1, 2, 3
    assert solution_instance.isBipartite(graph) is True

def test_complex_bipartite(solution_instance):
    """Test a more complex bipartite graph."""
    graph = [[3], [2, 4], [1], [0, 4], [1, 3]]
    assert solution_instance.isBipartite(graph) is True

def test_complex_non_bipartite(solution_instance):
    """Test a more complex non-bipartite graph."""
    graph = [[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]]
    assert solution_instance.isBipartite(graph) is True

def test_graph_with_isolated_nodes(solution_instance):
    """Test a graph with isolated nodes."""
    graph = [[1], [0], [], [4], [3]] # Edge 0-1, isolated 2, edge 3-4
    assert solution_instance.isBipartite(graph) is True

def test_larger_graph_bipartite(solution_instance):
    """Test a larger bipartite graph."""
    # A grid-like structure
    graph = [
        [1, 4], [0, 2, 5], [1, 3, 6], [2, 7],
        [0, 5], [1, 4, 6], [2, 5, 7], [3, 6]
    ]
    assert solution_instance.isBipartite(graph) is True

def test_larger_graph_non_bipartite(solution_instance):
    """Test a larger non-bipartite graph."""
    # Add an edge to the grid to create an odd cycle (e.g., 0-5)
    graph = [
        [1, 4, 5], [0, 2, 5], [1, 3, 6], [2, 7],
        [0, 5], [1, 4, 6, 0], [2, 5, 7], [3, 6]
    ]
    assert solution_instance.isBipartite(graph) is False
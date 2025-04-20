"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, return the path as a list of integer node, which create the highest possibility

If there is no path from start to end, return [].

Constraints:

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
"""

from collections import defaultdict
from heapq import heappop, heappush
from typing import List

class SolutionDijkstraReturnPath:
    def maxProbabilityPath(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> List[int]:
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        visited = set()
        heap = [(-1.0, start_node)]  # (negative_probability, node) simulate max heap
        parent = {start_node: None}  # to reconstruct path
        probabilities = [0] * n 
        probabilities[start_node] = 1
        
        while heap:
            prob, node = heappop(heap)
            prob = -prob  # convert back to positive
            visited.add(node)

            if node == end_node:
                # reconstruct the path from end_node to start_node
                path = []
                while node is not None:
                    path.append(node)
                    node = parent[node]
                return path[::-1]  # reverse to get path from start to end

            for nei, edge_prob in graph[node]:
                if nei not in visited:
                    new_prob = prob * edge_prob
                    heappush(heap, (-new_prob, nei))

                    # record parent only once to ensure shortest path
                    # use probabilities to keep track of cost, update parent only for better prob
                    if nei not in parent or new_prob > probabilities[nei]:  
                        parent[nei] = node
                        probabilities[nei] = new_prob

        return []  # return empty list if no path exists

# Reversed BellmanFord algorithm to find the maximum paths    
class SolutionBellmanFord:
    def maxProbabilityPath(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> List[int]:
        prev_cost = [0] * n  # 0 is the lowest possiblity
        prev_cost[start_node] = 1
        parent = [None] * n

        # BellmanFord shortest path will have at-most n - 1 edges
        for _ in range(n - 1):
            next_cost = prev_cost.copy()
            updated = False

            # Note: the connection between u and v are bidirectional
            # When evaluating an edge, we must evaluate both next_cost_u and next_cost_v
            for i in range(len(succProb)):
                u, v = edges[i]
                new_cost_u = prev_cost[v] * succProb[i]
                new_cost_v = prev_cost[u] * succProb[i]
                if new_cost_u > next_cost[u]:
                    updated = True
                    next_cost[u] = new_cost_u
                    parent[u] = v
                if new_cost_v > next_cost[v]:
                    updated = True
                    next_cost[v] = new_cost_v
                    parent[v] = u
            
            if not updated:
                break
            prev_cost = next_cost  # carry forward updated costs

        
        max_prob = prev_cost[end_node]
        # no path is found
        if max_prob == 0:
            return []
        # Reconstructing path from end_node to start_node, then reverse
        path = []
        node = end_node
        while node is not None:
            path.append(node)
            node = parent[node]

        return path[::-1]
    

# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[SolutionDijkstraReturnPath, SolutionBellmanFord], 
                ids=["DijkstraPath", "BellmanFordPath"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test a simple path with high probability edges."""
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start_node = 0
    end_node = 2
    # Two paths: 0->2 (p=0.2) or 0->1->2 (p=0.5*0.5=0.25)
    expected = [0, 1, 2]  # Path with probability 0.25
    assert solution_instance.maxProbabilityPath(n, edges, succProb, start_node, end_node) == expected

def test_example2(solution_instance):
    """Test a path where direct is better than indirect."""
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.3, 0.5, 0.7]
    start_node = 0
    end_node = 2
    # Two paths: 0->2 (p=0.7) or 0->1->2 (p=0.3*0.5=0.15)
    # Higher probability path: 0->2
    expected = [0, 2]
    assert solution_instance.maxProbabilityPath(n, edges, succProb, start_node, end_node) == expected

def test_no_path(solution_instance):
    """Test when no path exists between start and end nodes."""
    n = 4
    edges = [[0, 1], [2, 3]]
    succProb = [0.5, 0.5]
    start_node = 0
    end_node = 3
    expected = []  # No path from 0 to 3
    assert solution_instance.maxProbabilityPath(n, edges, succProb, start_node, end_node) == expected

def test_single_edge(solution_instance):
    """Test with a single edge between start and end."""
    n = 2
    edges = [[0, 1]]
    succProb = [0.9]
    start_node = 0
    end_node = 1
    expected = [0, 1]
    assert solution_instance.maxProbabilityPath(n, edges, succProb, start_node, end_node) == expected

def test_longer_path(solution_instance):
    """Test with a longer path where intermediate probabilities matter."""
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]
    succProb = [0.9, 0.9, 0.9, 0.9, 0.5]
    start_node = 0
    end_node = 4
    # Two paths: 0->4 (p=0.5) or 0->1->2->3->4 (p=0.9*0.9*0.9*0.9=0.6561)
    # Higher probability path: 0->1->2->3->4
    expected = [0, 1, 2, 3, 4]
    assert solution_instance.maxProbabilityPath(n, edges, succProb, start_node, end_node) == expected

def test_complex_graph(solution_instance):
    """Test with a more complex graph with multiple paths."""
    n = 6
    edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4], [3, 5], [4, 5]]
    succProb = [0.8, 0.7, 0.9, 0.5, 0.6, 0.7, 0.8]
    start_node = 0
    end_node = 5
    # Multiple paths:
    # 0->1->3->5: 0.8 * 0.9 * 0.7 = 0.504
    # 0->2->3->5: 0.7 * 0.5 * 0.7 = 0.245
    # 0->2->4->5: 0.7 * 0.6 * 0.8 = 0.336
    # Highest probability path: 0->1->3->5
    expected = [0, 1, 3, 5]
    assert solution_instance.maxProbabilityPath(n, edges, succProb, start_node, end_node) == expected

def test_equal_probability_paths(solution_instance):
    """Test with multiple paths having the same probability."""
    n = 4
    edges = [[0, 1], [1, 3], [0, 2], [2, 3]]
    succProb = [0.5, 0.5, 0.5, 0.5]
    start_node = 0
    end_node = 3
    # Two paths with equal probability: 
    # 0->1->3: 0.5 * 0.5 = 0.25
    # 0->2->3: 0.5 * 0.5 = 0.25
    # The path returned depends on the algorithm implementation
    result = solution_instance.maxProbabilityPath(n, edges, succProb, start_node, end_node)
    assert (result == [0, 1, 3] or result == [0, 2, 3])
    # Check that the path length is correct
    assert len(result) == 3

def test_perfect_probability(solution_instance):
    """Test with perfect probability edges (probability = 1.0)."""
    n = 4
    edges = [[0, 1], [1, 2], [2, 3]]
    succProb = [1.0, 1.0, 1.0]
    start_node = 0
    end_node = 3
    expected = [0, 1, 2, 3]
    assert solution_instance.maxProbabilityPath(n, edges, succProb, start_node, end_node) == expected

def test_zero_probability(solution_instance):
    """Test with some zero probability edges."""
    n = 4
    edges = [[0, 1], [1, 3], [0, 2], [2, 3]]
    succProb = [0.5, 0.0, 0.5, 0.5]
    start_node = 0
    end_node = 3
    # 0->1->3: 0.5 * 0.0 = 0.0
    # 0->2->3: 0.5 * 0.5 = 0.25
    # Higher probability path: 0->2->3
    expected = [0, 2, 3]
    assert solution_instance.maxProbabilityPath(n, edges, succProb, start_node, end_node) == expected

def test_start_end_adjacent(solution_instance):
    """Test when start and end nodes are adjacent."""
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]
    succProb = [0.1, 0.1, 0.1, 0.1, 0.9]
    start_node = 0
    end_node = 4
    # Direct edge with high probability
    expected = [0, 4]
    assert solution_instance.maxProbabilityPath(n, edges, succProb, start_node, end_node) == expected
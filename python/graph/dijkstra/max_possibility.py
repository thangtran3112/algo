"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

Example 1:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
Example 2:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:



Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
 

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

"""
    * keep a max-heap of current maximum path to each node. Initially heap = [(-1, start)]
    * keep a visited set to keep track of evaluated node
    * for each evaluated node, update the cost if incoming probability is higher
"""
class SolutionDijkstra:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (u, v), cost in zip(edges, succProb):
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        visited = set()
        # the heap element (k, nei) will keep track of the maximum probabily
        # for reaching nei from start_node
        heap = [(-1, start_node)]  # using negative simulation for max heap

        while heap:
            cost, node = heappop(heap)
            cost = -cost
            visited.add(node)
            if node == end_node:
                # found the end_node with maximum of product between possibilities
                return cost
            for nei, nei_cost in graph[node]:
                if nei not in visited:
                    negative_cost = -(cost * nei_cost)
                    heappush(heap, (negative_cost, nei))

        return 0

class SolutionBellmanFord:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        prev_costs = [0] * n
        prev_costs[start_node] = 1

        # run to maximum n - 1 times. Optional: detect negative weight cycle
        for _ in range(n - 1):
            next_costs = prev_costs[:]

            has_update = False
            # Notes: a probablity between i and j is bidirectional.
            # When we evaluate an undirected edge, we need to evaluate both vertices
            for i in range(len(succProb)):
                u, v = edges[i]
                weight = succProb[i]
                new_cost_v = prev_costs[u] * weight
                new_cost_u = prev_costs[v] * weight
                if weight != 0:
                    if new_cost_v > next_costs[v]:
                        next_costs[v] = new_cost_v
                        has_update = True
                    if new_cost_u > next_costs[u]:
                        next_costs[u] = new_cost_u
                        has_update = True

            if not has_update:
                break
            else:
                prev_costs = next_costs

        return prev_costs[end_node] if prev_costs[end_node] != 0 else 0
    
# === TEST CASES ===
import pytest  # noqa: E402

# Do not modify the existing solutions

@pytest.fixture(params=[SolutionDijkstra, SolutionBellmanFord], 
               ids=["Dijkstra", "BellmanFord"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start = 0
    end = 2
    # Two paths: 0->2 (p=0.2) or 0->1->2 (p=0.5*0.5=0.25)
    expected = 0.25
    result = solution_instance.maxProbability(n, edges, succProb, start, end)
    assert abs(result - expected) < 1e-5

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.3]
    start = 0
    end = 2
    # Two paths: 0->2 (p=0.3) or 0->1->2 (p=0.5*0.5=0.25)
    expected = 0.3
    result = solution_instance.maxProbability(n, edges, succProb, start, end)
    assert abs(result - expected) < 1e-5

def test_example3_no_path(solution_instance):
    """Test Example 3 from the problem description with no path."""
    n = 3
    edges = [[0, 1]]
    succProb = [0.5]
    start = 0
    end = 2
    # No path from 0 to 2
    expected = 0.0
    result = solution_instance.maxProbability(n, edges, succProb, start, end)
    assert abs(result - expected) < 1e-5

def test_longer_path_better(solution_instance):
    """Test when a longer path has higher probability."""
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]
    succProb = [0.9, 0.9, 0.9, 0.9, 0.5]
    start = 0
    end = 4
    # Two paths: 0->4 (p=0.5) or 0->1->2->3->4 (p=0.9*0.9*0.9*0.9=0.6561)
    expected = 0.6561
    result = solution_instance.maxProbability(n, edges, succProb, start, end)
    assert abs(result - expected) < 1e-5

def test_direct_path_better(solution_instance):
    """Test when a direct path has higher probability."""
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]
    succProb = [0.1, 0.1, 0.1, 0.1, 0.8]
    start = 0
    end = 4
    # Two paths: 0->4 (p=0.8) or 0->1->2->3->4 (p=0.1*0.1*0.1*0.1=0.0001)
    expected = 0.8
    result = solution_instance.maxProbability(n, edges, succProb, start, end)
    assert abs(result - expected) < 1e-5

def test_complex_network(solution_instance):
    """Test with a more complex network of paths."""
    n = 6
    edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4], [3, 5], [4, 5]]
    succProb = [0.8, 0.7, 0.9, 0.5, 0.6, 0.7, 0.8]
    start = 0
    end = 5
    # Multiple paths:
    # 0->1->3->5: 0.8 * 0.9 * 0.7 = 0.504
    # 0->2->3->5: 0.7 * 0.5 * 0.7 = 0.245
    # 0->2->4->5: 0.7 * 0.6 * 0.8 = 0.336
    expected = 0.504
    result = solution_instance.maxProbability(n, edges, succProb, start, end)
    assert abs(result - expected) < 1e-5

def test_single_edge(solution_instance):
    """Test with a single edge between start and end."""
    n = 2
    edges = [[0, 1]]
    succProb = [0.9]
    start = 0
    end = 1
    expected = 0.9
    result = solution_instance.maxProbability(n, edges, succProb, start, end)
    assert abs(result - expected) < 1e-5

def test_perfect_probability(solution_instance):
    """Test with perfect probability edges (probability = 1.0)."""
    n = 4
    edges = [[0, 1], [1, 2], [2, 3]]
    succProb = [1.0, 1.0, 1.0]
    start = 0
    end = 3
    expected = 1.0
    result = solution_instance.maxProbability(n, edges, succProb, start, end)
    assert abs(result - expected) < 1e-5

def test_zero_probability_edge(solution_instance):
    """Test with some zero probability edges."""
    n = 4
    edges = [[0, 1], [1, 3], [0, 2], [2, 3]]
    succProb = [0.5, 0.0, 0.5, 0.5]
    start = 0
    end = 3
    # 0->1->3: 0.5 * 0.0 = 0.0
    # 0->2->3: 0.5 * 0.5 = 0.25
    expected = 0.25
    result = solution_instance.maxProbability(n, edges, succProb, start, end)
    assert abs(result - expected) < 1e-5

def test_multiple_equal_paths(solution_instance):
    """Test with multiple paths having the same probability."""
    n = 4
    edges = [[0, 1], [1, 3], [0, 2], [2, 3]]
    succProb = [0.5, 0.5, 0.5, 0.5]
    start = 0
    end = 3
    # Two paths with equal probability: 
    # 0->1->3: 0.5 * 0.5 = 0.25
    # 0->2->3: 0.5 * 0.5 = 0.25
    expected = 0.25
    result = solution_instance.maxProbability(n, edges, succProb, start, end)
    assert abs(result - expected) < 1e-5

def test_disconnected_components(solution_instance):
    """Test with disconnected components in the graph."""
    n = 5
    edges = [[0, 1], [2, 3]]
    succProb = [0.9, 0.8]
    start = 0
    end = 4
    # No path from 0 to 4
    expected = 0.0
    result = solution_instance.maxProbability(n, edges, succProb, start, end)
    assert abs(result - expected) < 1e-5

def test_very_small_probabilities(solution_instance):
    """Test with very small probability values."""
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]
    succProb = [0.01, 0.01, 0.01, 0.01, 0.0001]
    start = 0
    end = 4
    # Two paths: 
    # 0->4 (p=0.0001) 
    # 0->1->2->3->4 (p=0.01^4=1e-8)
    expected = 0.0001
    result = solution_instance.maxProbability(n, edges, succProb, start, end)
    assert abs(result - expected) < 1e-5
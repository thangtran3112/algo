# https://leetcode.com/problems/evaluate-division/?envType=problem-list-v2&envId=shortest-path
"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""
from collections import defaultdict
from heapq import heappop, heappush
from typing import List
import pytest

# DFS solution
class SolutionDFSBacktrack:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            u, v = equations[i]
            cost = values[i]
            graph[u].append((v, cost))
            graph[v].append((u, 1 / cost))

        visited = set()

        # dfs with backtrack for finding path between cur and target
        def dfs(cur, target, cost):
            if cur not in graph or target not in graph:
                return -1
            if (cur == target):
                return cost
            visited.add(cur)
            for nei, nei_cost in graph[cur]:
                if nei not in visited:
                    total_cost = dfs(nei, target, cost * nei_cost)
                    if total_cost != -1:
                        visited.remove(cur)
                        return total_cost
            visited.remove(cur)
            return -1

        return [dfs(src, dst, 1) for src, dst in queries]

# Dijistra solution with max-heap
class SolutionReversedDijkstra:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        # zip will append multiple array elements: → [ (["a", "b"], 2.0), (["b", "c"], 3.0) ]
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        # find the shortest path between src and dst. 2D Dijistra
        def reversed_dijkstra(src, dst):
            if src not in graph or dst not in graph:
                return -1
            visited = set()
            # initially, cost from src to src will be 1
            heap = [(-1.0, src)]  # using max-heap by negative simulation

            while heap:
                cost, node = heappop(heap)
                cost = -cost  # revert back to positive
                if node == dst:
                    return cost
                visited.add(node)
                for nei, weight in graph[node]:
                    if nei not in visited:
                        # for the sake of max-heap, we convert positive back to negative
                        negative_cost = -(cost * weight)
                        heappush(heap, (negative_cost, nei))

            # cannot find the path
            return -1

        return [reversed_dijkstra(a, b) for a, b in queries]

# === TEST CASES ===

@pytest.fixture(params=[SolutionDFSBacktrack, SolutionReversedDijkstra], 
               ids=["DFS_Backtrack", "Reversed_Dijkstra"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
    result = solution_instance.calcEquation(equations, values, queries)
    
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        if e == -1:
            assert r == -1
        else:
            assert abs(r - e) < 1e-5

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    expected = [3.75000, 0.40000, 5.00000, 0.20000]
    result = solution_instance.calcEquation(equations, values, queries)
    
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5

def test_example3(solution_instance):
    """Test Example 3 from the problem description."""
    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    expected = [0.50000, 2.00000, -1.00000, -1.00000]
    result = solution_instance.calcEquation(equations, values, queries)
    
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        if e == -1:
            assert r == -1
        else:
            assert abs(r - e) < 1e-5

def test_single_variable(solution_instance):
    """Test case with a single variable equations like a/a = 1."""
    equations = [["a", "a"]]
    values = [1.0]
    queries = [["a", "a"], ["b", "b"]]
    expected = [1.00000, -1.00000]
    result = solution_instance.calcEquation(equations, values, queries)
    
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        if e == -1:
            assert r == -1
        else:
            assert abs(r - e) < 1e-5

def test_chain_of_equations(solution_instance):
    """Test a chain of equations where the answer requires traversing multiple edges."""
    equations = [["a", "b"], ["b", "c"], ["c", "d"], ["d", "e"]]
    values = [2.0, 3.0, 4.0, 5.0]
    queries = [["a", "e"], ["e", "a"], ["b", "e"], ["a", "c"]]
    expected = [120.00000, 1/120.00000, 60.00000, 6.00000]
    result = solution_instance.calcEquation(equations, values, queries)
    
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5

def test_disconnected_graph(solution_instance):
    """Test with a disconnected graph (multiple separate components)."""
    equations = [["a", "b"], ["c", "d"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]
    expected = [-1.00000, -1.00000, 0.50000, 1/3.00000]
    result = solution_instance.calcEquation(equations, values, queries)
    
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        if e == -1:
            assert r == -1
        else:
            assert abs(r - e) < 1e-5

def test_circular_dependencies(solution_instance):
    """Test with circular dependencies in the graph."""
    equations = [["a", "b"], ["b", "c"], ["c", "a"]]
    values = [2.0, 3.0, 1/6.0]
    queries = [["a", "a"], ["b", "b"], ["c", "c"], ["a", "b"], ["a", "c"]]
    expected = [1.00000, 1.00000, 1.00000, 2.00000, 6.00000]
    result = solution_instance.calcEquation(equations, values, queries)
    
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5

def test_same_equation_different_values(solution_instance):
    """Test where the same equation is given multiple times with different values."""
    equations = [["a", "b"], ["a", "b"]]
    values = [2.0, 2.0]  # Consistent values
    queries = [["a", "b"], ["b", "a"]]
    expected = [2.00000, 0.50000]
    result = solution_instance.calcEquation(equations, values, queries)
    
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5

def test_precision_handling(solution_instance):
    """Test handling of floating-point precision."""
    equations = [["a", "b"], ["b", "c"]]
    values = [1.0/3.0, 3.0]
    queries = [["a", "c"], ["c", "a"]]
    expected = [1.00000, 1.00000]
    result = solution_instance.calcEquation(equations, values, queries)
    
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5

def test_boundary_values(solution_instance):
    """Test with values at the boundaries of the constraints."""
    equations = [["a", "b"]]
    values = [20.0]  # Upper bound of constraint
    queries = [["a", "b"], ["b", "a"]]
    expected = [20.00000, 0.05000]
    result = solution_instance.calcEquation(equations, values, queries)
    
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5

def test_empty_query(solution_instance):
    """Test with an empty query list."""
    equations = [["a", "b"]]
    values = [2.0]
    queries = []
    expected = []
    result = solution_instance.calcEquation(equations, values, queries)
    
    assert result == expected

def test_multiple_paths(solution_instance):
    """Test when there are multiple paths between nodes."""
    equations = [["a", "b"], ["b", "c"], ["a", "c"]]
    values = [2.0, 3.0, 6.0]  # Consistent (a/c = a/b * b/c = 2*3 = 6)
    queries = [["a", "c"], ["b", "a"]]
    expected = [6.00000, 0.50000]
    result = solution_instance.calcEquation(equations, values, queries)
    
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5




# https://leetcode.com/problems/connecting-cities-with-minimum-cost/description/
"""
There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1,

The cost is the sum of the connections' costs used.

 

Example 1:


Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:


Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: There is no way to connect all cities even if all edges are used.
 

Constraints:

1 <= n <= 104
1 <= connections.length <= 104
connections[i].length == 3
1 <= xi, yi <= n
xi != yi
0 <= costi <= 105
"""
from typing import List
import pytest


class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, node: int) -> int:
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            # already connected
            return False
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = self.root[root_x]
            self.rank[root_x] += 1
        return True

# Solution class implementing Kruskal's algorithm
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # Kruskal algorithm, sorting connections
        connections.sort(key=lambda x: x[2])

        edges_used = 0
        mst_cost = 0
        uf = UnionFind(n + 1)  # city starting from 1, buffering the union with [0,..,n]
        for x, y, cost in connections:
            if uf.union(x, y):
                mst_cost += cost
                edges_used += 1
                # Kruskal algorithm stops when n - 1 edges are used, where n = vertices
                if edges_used == n - 1:
                    break

        return mst_cost if edges_used == n - 1 else -1

# === TEST CASES ===

@pytest.fixture
def solution():
    """Fixture to provide a Solution instance."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    n = 3
    connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    expected = 6  # Min cost to connect all cities (using edges [2,3,1] and [1,2,5])
    assert solution.minimumCost(n, connections) == expected

def test_example2(solution):
    """Test Example 2 from the problem description."""
    n = 4
    connections = [[1, 2, 3], [3, 4, 4]]
    expected = -1  # Impossible to connect all cities
    assert solution.minimumCost(n, connections) == expected

def test_single_city(solution):
    """Test case with a single city."""
    n = 1
    connections = []
    expected = 0  # No connections needed for a single city
    assert solution.minimumCost(n, connections) == expected

def test_two_cities_connected(solution):
    """Test case with two cities and a connection."""
    n = 2
    connections = [[1, 2, 5]]
    expected = 5  # Only one possible connection
    assert solution.minimumCost(n, connections) == expected

def test_two_cities_not_connected(solution):
    """Test case with two cities but no connection."""
    n = 2
    connections = []
    expected = -1  # No way to connect cities
    assert solution.minimumCost(n, connections) == expected

def test_multiple_connections_same_cities(solution):
    """Test case with multiple connections between the same cities."""
    n = 3
    connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1], [1, 2, 3], [1, 3, 2]]
    expected = 3  # Should choose connections [2,3,1] and [1,3,2]
    assert solution.minimumCost(n, connections) == expected

def test_multiple_components_cannot_connect(solution):
    """Test case with multiple disconnected components."""
    n = 5
    connections = [[1, 2, 3], [3, 4, 4], [1, 3, 1]]
    expected = -1  # Cannot connect all cities (city 5 is isolated)
    assert solution.minimumCost(n, connections) == expected

def test_cycle_in_graph(solution):
    """Test case with a cycle in the graph."""
    n = 4
    connections = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 1, 4]]
    expected = 6  # Minimum spanning tree excludes the most expensive edge
    assert solution.minimumCost(n, connections) == expected

def test_larger_example(solution):
    """Test a larger example with more cities and connections."""
    n = 6
    connections = [
        [1, 2, 1], [2, 3, 2], [3, 4, 3],
        [4, 5, 4], [5, 6, 5], [1, 6, 7],
        [2, 4, 10], [3, 6, 8], [1, 3, 9]
    ]
    expected = 15  # MST uses connections with costs 1,2,3,4,5
    assert solution.minimumCost(n, connections) == expected

def test_duplicate_connections(solution):
    """Test case with duplicate connections (same cities, different costs)."""
    n = 3
    connections = [[1, 2, 5], [1, 2, 3], [2, 3, 4], [2, 3, 1]]
    expected = 4  # Should choose connections [1,2,3] and [2,3,1]
    assert solution.minimumCost(n, connections) == expected

def test_union_find_standalone():
    """Test the UnionFind data structure independently."""
    uf = UnionFind(5)
    
    # Initially, each element is in its own set
    for i in range(5):
        assert uf.find(i) == i
    
    # Union operations
    assert uf.union(1, 2) == True  # 1 and 2 are now connected
    assert uf.find(1) == uf.find(2)
    
    assert uf.union(3, 4) == True  # 3 and 4 are now connected
    assert uf.find(3) == uf.find(4)
    
    assert uf.union(1, 3) == True  # Connect the two components
    assert uf.find(1) == uf.find(3)
    
    # Attempt to connect already connected elements
    assert uf.union(2, 4) == False
    
    # All elements 1,2,3,4 are in the same component
    root = uf.find(1)
    for i in range(1, 5):
        assert uf.find(i) == root
    
    # Element 0 is still in its own component
    assert uf.find(0) != root
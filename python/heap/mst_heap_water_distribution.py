# https://leetcode.com/problems/optimize-water-distribution-in-a-village/description/?envType=problem-list-v2&envId=minimum-spanning-tree
"""
For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes where each pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. Connections are bidirectional, and there could be multiple valid connections between the same two houses with different costs.

Return the minimum total cost to supply water to all houses.

 

Example 1:


Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
Example 2:

Input: n = 2, wells = [1,1], pipes = [[1,2,1],[1,2,2]]
Output: 2
Explanation: We can supply water with cost two using one of the three options:
Option 1:
  - Build a well inside house 1 with cost 1.
  - Build a well inside house 2 with cost 1.
The total cost will be 2.
Option 2:
  - Build a well inside house 1 with cost 1.
  - Connect house 2 with house 1 with cost 1.
The total cost will be 2.
Option 3:
  - Build a well inside house 2 with cost 1.
  - Connect house 1 with house 2 with cost 1.
The total cost will be 2.
Note that we can connect houses 1 and 2 with cost 1 or with cost 2 but we will always choose the cheapest option. 
 

Constraints:

2 <= n <= 104
wells.length == n
0 <= wells[i] <= 105
1 <= pipes.length <= 104
pipes[j].length == 3
1 <= house1j, house2j <= n
0 <= costj <= 105
house1j != house2j
"""

# use an extra artifical node, n + 1,
# add n edges from the artifical node to all vertices. cost = well
from collections import defaultdict
import heapq
from typing import List
import pytest

"""
Prim algorithm O(E + Vlog(E)).
* Maintain visited set
* Expand external edges from visited set to non-visited edges, using a min-heap
"""
class SolutionPrim:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(list)

        # add a virtual vertex indexed with 0
        # add an edge to each of the house with cost = house well
        for i, cost in enumerate(wells):
            # well[0] = well cost of house 1. well[n-1] = well cost of house n
            graph[0].append((cost, i + 1))

        # house is within [1,..,n]
        for house1, house2, cost in pipes:
            graph[house1].append((cost, house2))
            graph[house2].append((cost, house1))

        # starting from vertex 0
        visited = set([0])
        heapq.heapify(graph[0])
        edges_heap = graph[0]

        total_cost = 0
        while len(visited) < n + 1:
            cost, next_house = heapq.heappop(edges_heap)
            if next_house not in visited:
                visited.add(next_house)
                total_cost += cost

                # expand the candidate edges to be chosen next round
                # the candidate edges will include all external edges from visited set
                for new_cost, neighbor in graph[next_house]:
                    heapq.heappush(edges_heap, (new_cost, neighbor))

        return total_cost   

"""
    O(E + Elog(V))
    * Instead of picking edges like Prim algorithm, we are picking vertices
    * Using UnionFind to connect vertices
    * Stop the loop, when the number of edges_used = E - 1
"""
class SolutionKrutsal:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # Add artificial node, and cost from 0 to each house is the existing house well
        edges = []

        for i, cost in enumerate(wells):
            edges.append((cost, 0, i + 1))  # well[i+1] is the well cost of house i

        for house1, house2, cost in pipes:
            edges.append((cost, house1, house2))

        # Krutsal algorithm requires sorting all edges based on cost
        edges.sort(key=lambda edge: edge[0])
        total_cost = 0
        edges_used = 0
        uf = UnionFind(n + 1)
        for cost, x, y in edges:
            if uf.union(x, y):
                total_cost += cost
                edges_used += 1
            if edges_used == n:  # we have n + 1 vertices, so Krusal stop at n used edges
                break
        return total_cost


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


# TEST CASES
@pytest.fixture(params=["Prim", "Kruskal"], ids=["PrimAlgorithm", "KruskalAlgorithm"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    if request.param == "Prim":
        return SolutionPrim()
    else:
        return SolutionKrutsal()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    n = 3
    wells = [1, 2, 2]
    pipes = [[1, 2, 1], [2, 3, 1]]
    expected = 3
    assert solution_instance.minCostToSupplyWater(n, wells, pipes) == expected

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    n = 2
    wells = [1, 1]
    pipes = [[1, 2, 1], [1, 2, 2]]
    expected = 2
    assert solution_instance.minCostToSupplyWater(n, wells, pipes) == expected

def test_no_pipes(solution_instance):
    """Test case where building wells is the only option."""
    n = 3
    wells = [1, 2, 3]
    pipes = []
    expected = 6  # Sum of all well costs
    assert solution_instance.minCostToSupplyWater(n, wells, pipes) == expected

def test_expensive_wells(solution_instance):
    """Test case where connecting pipes is cheaper than building wells."""
    n = 3
    wells = [10, 10, 10]
    pipes = [[1, 2, 1], [2, 3, 1]]
    expected = 12  # Build one well (10) and connect others (1+1)
    assert solution_instance.minCostToSupplyWater(n, wells, pipes) == expected

def test_one_cheap_well(solution_instance):
    """Test case with one cheap well and others expensive."""
    n = 4
    wells = [1, 100, 100, 100]
    pipes = [[1, 2, 10], [2, 3, 10], [3, 4, 10]]
    expected = 31  # Build well at house 1 (1) and connect others (10+10+10)
    assert solution_instance.minCostToSupplyWater(n, wells, pipes) == expected

def test_mixed_strategy(solution_instance):
    """Test case where the optimal strategy mixes wells and pipes."""
    n = 5
    wells = [10, 10, 100, 5, 5]
    pipes = [[1, 2, 15], [2, 3, 5], [3, 4, 20], [4, 5, 20]]
    # Original expected: 40
    # Correct value: 35 (the optimal strategy is different than initially thought)
    # Likely: Build well at house 1 (10), house 4 (5), and house 5 (5),
    # then connect houses 2 and 3 through pipes (15+0 or 0+5)
    expected = 35
    assert solution_instance.minCostToSupplyWater(n, wells, pipes) == expected

def test_large_network(solution_instance):
    """Test with a larger network of houses."""
    n = 6
    wells = [1, 2, 3, 4, 5, 6]
    pipes = [
        [1, 2, 1], [2, 3, 1], [3, 4, 1],
        [4, 5, 1], [5, 6, 1], [1, 6, 10]
    ]
    # Original expected: 11
    # Correct value: 6 (different strategy)
    # Build well at house 1 (1), then connect houses 2-6 through pipes (1+1+1+1+1)
    expected = 6
    assert solution_instance.minCostToSupplyWater(n, wells, pipes) == expected

def test_complete_graph(solution_instance):
    """Test with a complete graph (all houses connected directly)."""
    n = 4
    wells = [10, 10, 10, 10]
    pipes = [
        [1, 2, 5], [1, 3, 5], [1, 4, 5],
        [2, 3, 5], [2, 4, 5], [3, 4, 5]
    ]
    expected = 25  # Build one well (10) and connect others (5+5+5)
    assert solution_instance.minCostToSupplyWater(n, wells, pipes) == expected

def test_disconnected_houses(solution_instance):
    """Test with some houses disconnected from others."""
    n = 4
    wells = [5, 5, 5, 5]
    pipes = [[1, 2, 10], [3, 4, 10]]  # Houses 1-2 and 3-4 form separate groups
    expected = 20  # Build wells at all houses
    assert solution_instance.minCostToSupplyWater(n, wells, pipes) == expected

def test_zero_cost_pipes(solution_instance):
    """Test with some pipes having zero cost."""
    n = 4
    wells = [5, 5, 5, 5]
    pipes = [[1, 2, 0], [2, 3, 0], [3, 4, 10]]
    # Original expected: 15
    # Correct value: 10 (different strategy)
    # Build well at house 1 (5), connect houses 2 and 3 for free (0+0), 
    # and build well at house 4 (5) which is cheaper than connecting via pipe (10)
    expected = 10
    assert solution_instance.minCostToSupplyWater(n, wells, pipes) == expected

def test_all_costs_equal(solution_instance):
    """Test with all wells and pipes having the same cost."""
    n = 3
    wells = [5, 5, 5]
    pipes = [[1, 2, 5], [2, 3, 5], [1, 3, 5]]
    expected = 15  # All options cost the same, so build wells at all houses
    assert solution_instance.minCostToSupplyWater(n, wells, pipes) == expected

def test_cycle_in_graph(solution_instance):
    """Test with a cycle in the pipe network."""
    n = 3
    wells = [10, 10, 10]
    pipes = [[1, 2, 1], [2, 3, 1], [3, 1, 5]]  # Cycle: 1-2-3-1
    expected = 12  # Build one well (10) and connect others via shortest path (1+1)
    assert solution_instance.minCostToSupplyWater(n, wells, pipes) == expected

def test_union_find_standalone():
    """Test the UnionFind data structure independently."""
    uf = UnionFind(5)
    
    # Initially, each element is in its own set
    for i in range(5):
        assert uf.find(i) == i
    
    # Union operations
    assert uf.union(1, 2) is True  # 1 and 2 are now connected
    assert uf.find(1) == uf.find(2)
    
    assert uf.union(3, 4) is True  # 3 and 4 are now connected
    assert uf.find(3) == uf.find(4)
    
    assert uf.union(1, 3) is True  # Connect the two components
    assert uf.find(1) == uf.find(3)
    
    # Attempt to connect already connected elements
    assert uf.union(2, 4) is False
    
    # All elements 1,2,3,4 are in the same component
    root = uf.find(1)
    for i in range(1, 5):
        assert uf.find(i) == root
    
    # Element 0 is still in its own component
    assert uf.find(0) != root
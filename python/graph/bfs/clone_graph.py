# https://leetcode.com/problems/clone-graph/description/
"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""
from collections import deque
from typing import Optional
import pytest
from typing import List
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        # if we use normal dfs, it creates multiple clone when a node is revisited.
        # we must use a dictionary to keeptrack of the clone node of each original node
        clone_map: dict['Node', 'Node'] = {}

        def dfs(cur_node) -> Optional['Node']:
            if cur_node in clone_map:
                return clone_map[cur_node]
            clone_node = Node(cur_node.val, [])
            # With this, we avoid infinite recursion, when the cur_node may be revisited
            clone_map[cur_node] = clone_node
            for neighbor in cur_node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            return clone_node

        return dfs(node)
    
class SolutionBFS:
    def cloneGraph(self, node):
        if not node:
            return None
        queue = deque()
        my_map = { node: Node(node.val)} 

        queue.append(node)
        while queue:
            curr = queue.popleft()
            curr_clone = my_map[curr]
            for nei in curr.neighbors:
                if nei not in my_map:
                    # only add a new node if it was never created
                    my_map[nei] = Node(nei.val)
                    queue.append(nei)
                # when a node is visited/revisted, it will be readded to the queue
                curr_clone.neighbors.append(my_map[nei])


        return my_map[node]


# === TEST CASES ===

@pytest.fixture(params=[Solution, SolutionBFS],
               ids=["DFS", "BFS"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
    """
    Helper function to build a graph from an adjacency list.
    Returns the first node (with val=1) or None if the graph is empty.
    """
    if not adj_list:
        return None
        
    # Create all nodes first
    nodes = {i+1: Node(i+1, []) for i in range(len(adj_list))}
    
    # Add neighbors
    for i, neighbors in enumerate(adj_list):
        node_val = i + 1  # 1-indexed
        for neighbor_val in neighbors:
            nodes[node_val].neighbors.append(nodes[neighbor_val])
    
    return nodes[1] if nodes else None

def get_adjacency_list(node: Optional[Node]) -> List[List[int]]:
    """
    Convert a graph back to an adjacency list representation.
    """
    if not node:
        return []
        
    adj_list = []
    visited = {}
    
    def dfs(cur_node):
        if cur_node.val in visited:
            return
        
        # Ensure the list is big enough
        while len(adj_list) < cur_node.val:
            adj_list.append([])
            
        # Add neighbors
        neighbor_vals = []
        for neighbor in cur_node.neighbors:
            neighbor_vals.append(neighbor.val)
            
        adj_list[cur_node.val - 1] = sorted(neighbor_vals)  # Sort for consistent comparison
        visited[cur_node.val] = True
        
        for neighbor in cur_node.neighbors:
            dfs(neighbor)
    
    dfs(node)
    return adj_list

def are_graphs_equal(original: Optional[Node], clone: Optional[Node]) -> bool:
    """
    Check if two graphs are structurally identical.
    Also verifies that they are separate instances.
    """
    if original is None and clone is None:
        return True
    if original is None or clone is None:
        return False
        
    # Get adjacency lists and compare
    original_adj = get_adjacency_list(original)
    clone_adj = get_adjacency_list(clone)
    
    # Check they're the same structure
    if original_adj != clone_adj:
        return False
    
    # Check they're separate instances
    visited_original = {}
    visited_clone = {}
    queue_original = [original]
    queue_clone = [clone]
    
    while queue_original:
        node_original = queue_original.pop(0)
        node_clone = queue_clone.pop(0)
        
        # Check they're different instances
        if node_original is node_clone:
            return False
            
        visited_original[node_original.val] = True
        visited_clone[node_clone.val] = True
        
        for i in range(len(node_original.neighbors)):
            neighbor_original = node_original.neighbors[i]
            neighbor_clone = node_clone.neighbors[i]
            
            if neighbor_original.val not in visited_original:
                queue_original.append(neighbor_original)
                queue_clone.append(neighbor_clone)
    
    return True

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    adj_list = [[2,4],[1,3],[2,4],[1,3]]
    original = build_graph(adj_list)
    clone = solution_instance.cloneGraph(original)
    assert are_graphs_equal(original, clone)

def test_example2(solution_instance):
    """Test Example 2 - single node without neighbors."""
    adj_list = [[]]
    original = build_graph(adj_list)
    clone = solution_instance.cloneGraph(original)
    assert are_graphs_equal(original, clone)

def test_example3(solution_instance):
    """Test Example 3 - empty graph."""
    original = None
    clone = solution_instance.cloneGraph(original)
    assert clone is None

def test_linear_graph(solution_instance):
    """Test with a linear graph."""
    adj_list = [[2], [1, 3], [2, 4], [3]]
    original = build_graph(adj_list)
    clone = solution_instance.cloneGraph(original)
    assert are_graphs_equal(original, clone)

def test_circular_graph(solution_instance):
    """Test with a circular graph."""
    adj_list = [[2, 5], [1, 3], [2, 4], [3, 5], [1, 4]]
    original = build_graph(adj_list)
    clone = solution_instance.cloneGraph(original)
    assert are_graphs_equal(original, clone)

def test_complete_graph(solution_instance):
    """Test with a complete graph where every node connects to all others."""
    n = 5  # 5 nodes
    adj_list = [list(range(1, n+1)) for _ in range(n)]
    for i in range(n):
        # Remove self connection
        adj_list[i].remove(i+1)
    
    original = build_graph(adj_list)
    clone = solution_instance.cloneGraph(original)
    assert are_graphs_equal(original, clone)

def test_star_graph(solution_instance):
    """Test with a star graph - one center node connected to all others."""
    n = 6  # 6 nodes
    adj_list = [[j for j in range(2, n+1)]]  # First node connects to all
    for i in range(1, n):
        adj_list.append([1])  # All other nodes connect only to first
    
    original = build_graph(adj_list)
    clone = solution_instance.cloneGraph(original)
    assert are_graphs_equal(original, clone)

def test_large_graph(solution_instance):
    """Test with a larger graph (near constraint limit of 100 nodes)."""
    n = 50  # 50 nodes
    # Create a large connected graph
    adj_list = []
    for i in range(n):
        neighbors = []
        if i > 0:
            neighbors.append(i)  # Connect to previous
        if i < n-1:
            neighbors.append(i+2)  # Connect to next
        adj_list.append(neighbors)
    
    original = build_graph(adj_list)
    clone = solution_instance.cloneGraph(original)
    assert are_graphs_equal(original, clone)

def test_complex_graph(solution_instance):
    """Test with a more complex graph structure."""
    # Create a graph with some interesting connectivity
    adj_list = [[2, 3, 4], [1, 5, 6], [1, 5, 7], [1, 6, 7], [2, 3, 8], [2, 4, 8], [3, 4, 8], [5, 6, 7]]
    original = build_graph(adj_list)
    clone = solution_instance.cloneGraph(original)
    assert are_graphs_equal(original, clone)
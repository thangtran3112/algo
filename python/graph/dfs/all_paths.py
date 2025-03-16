# https://leetcode.com/problems/all-paths-from-source-to-target/description/
"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
"""
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        visited = [False] * n
        destination = n - 1
        results = []
        path = []

        def dfs_backtrack(node):
            visited[node] = True
            path.append(node)

            if node == destination:
                # clone and copy
                results.append(list(path))
            else:
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        dfs_backtrack(neighbor)

            # backtracking
            visited[node] = False
            path.pop()
            return

        dfs_backtrack(0)

        return results

class SolutionWithStack:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        destination = n - 1
        results = []
        
        # Stack will store tuples of (node, path_so_far)
        stack = [(0, [0])]
        
        while stack:
            node, path = stack.pop()

            if node == destination:
                # Add the complete path to results
                results.append(path)
            else:
                # For each neighbor, add a new path to the stack
                for neighbor in graph[node]:
                    # Create a new path that includes the neighbor
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path))

        return results

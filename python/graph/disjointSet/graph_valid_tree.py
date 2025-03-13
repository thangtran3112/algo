# Link: https://leetcode.com/problems/graph-valid-tree/description/
# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
from typing import List

class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent: List[int] = [i for i in range(size)]
        self.rank: List[int] = [1] * size

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, x: int, y: int) -> bool:
        root_x: int = self.find(x)
        root_y: int = self.find(y)

        if root_x == root_y:
            return False  # x and y are already connected

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

    def isConnected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def count_roots(self) -> int:
        size: int = len(self.parent)
        all_roots: set[int] = {self.find(i) for i in range(size)}  # Collect unique roots
        return len(all_roots)  # Return the number of unique roots
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # union all nodes into disjoint sets, if there is only 1 root (1 set), we have a tree
        # when doing union(x, y) and x,y is already connected (through) then the graph has a cycle
        uf = UnionFind(n) 
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                # edge[0] and edge[1] is already connected through other node
                return False

        # check if there is more than 1 root, the set is not all connected, it is an invalid tree
        return uf.count_roots() == 1
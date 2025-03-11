# This problem can be solved by DFS, BFS or Union-Find. Here we will use Union-Find to solve the problem.
# Link: https://leetcode.com/problems/number-of-provinces/description/
"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
            return
        # ranks are equal now
        self.root[root_y] = root_x
        self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    # count the number of different roots
    def set_count(self):
        # immediate parent of a node, may not be root, we must use find(i) to to find the root.
        # unique_roots = set(self.find(i) for i in range(len(self.root)))
        unique_roots = set()
        for i in range(len(self.root)):
            root_i = self.find(i)
            unique_roots.add(root_i)
        return len(unique_roots)


class SolutionWithUnionFind(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        # After connecting all cities into the disjoint set, count the number of different roots
        return uf.set_count()

# This class will combine the two techniques of path compression and union by rank
# to optimize the union-find operations. The rank array will keep track of the depth of each tree,
# and the path compression will ensure that the trees remain flat after each find operation.


class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        # Path compression: point to the root directly
        # Some ranks may become obsolete so they are not updated
        # We only care about rank of root nodes
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # Time complexity: O(log n) amortized
    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
                return
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
                return
            self.root[root_y] = root_x
            self.rank[root_x] += 1

    # Time complexity: O(log n) amortized
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true

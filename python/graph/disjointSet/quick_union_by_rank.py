class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n  # intially all nodes are also their own roots, rank = 1

    # Time: 0(n) worst case, O(log n) amortized
    def find(self, x) -> int:
        while self.root[x] != x:
            x = self.root[x]
        return x

    def union(self, x, y) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # check the rank of the roots
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
                return
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
                return
            # if ranks are equal, after attaching, new height is increased by exactly 1
            self.root[root_y] = root_x
            self.rank[root_x] += 1

    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)

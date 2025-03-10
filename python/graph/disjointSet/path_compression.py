class SimpleUnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]

    # find the root of x with path compression
    # Time complexity: O(log n) amortized
    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        # point to the root directly
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x
        # Time complexity: O(log n) amortized

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
        # Time complexity: O(log n) amortized

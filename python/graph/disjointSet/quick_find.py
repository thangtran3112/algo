class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]  # initially each element is its own root

    # find the root of x
    # Time complexity: O(1)
    def find(self, x: int) -> int:
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX
        # Time complexity: O(n)

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
        # Time complexity: O(1)

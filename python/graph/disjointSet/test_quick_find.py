from quick_find import UnionFind

# pytest -v .\test_quick_find.py


def test_initialization():
    """Test that initialization creates correct root array"""
    uf = UnionFind(5)
    assert uf.root == [0, 1, 2, 3, 4]


def test_find():
    """Test the find operation returns the correct root"""
    uf = UnionFind(5)
    assert uf.find(0) == 0
    assert uf.find(1) == 1
    assert uf.find(4) == 4


def test_connected_initially():
    """Test that no nodes are initially connected unless they're the same node"""
    uf = UnionFind(5)
    assert uf.connected(0, 0) is True
    assert uf.connected(1, 1) is True
    assert uf.connected(0, 1) is False
    assert uf.connected(1, 2) is False


def test_basic_union():
    """Test basic union operation between two nodes"""
    uf = UnionFind(5)
    uf.union(0, 1)
    assert uf.find(1) == 0
    assert uf.connected(0, 1) is True
    assert uf.connected(1, 0) is True


def test_transitive_union():
    """Test that unions are properly transitive"""
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)

    # All three should now be in the same component with root 0
    assert uf.find(0) == 0
    assert uf.find(1) == 0
    assert uf.find(2) == 0
    assert uf.connected(0, 2) is True


def test_multiple_components():
    """Test handling of multiple separate components"""
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)

    # {0,1,2} should form one component and {3,4} another, with 5 by itself
    assert uf.connected(0, 2) is True
    assert uf.connected(3, 4) is True
    assert uf.connected(0, 3) is False
    assert uf.connected(2, 5) is False
    assert uf.connected(4, 5) is False


def test_repeated_unions():
    """Test that repeated unions don't break anything"""
    uf = UnionFind(4)
    uf.union(0, 1)
    uf.union(0, 1)  # Repeat the same union
    assert uf.connected(0, 1) is True

    uf.union(1, 2)
    uf.union(0, 2)  # Redundant since 0-1-2 are already connected
    assert uf.connected(0, 2) is True


def test_component_merger():
    """Test merging of two existing components"""
    uf = UnionFind(6)
    # Create component {0,1,2}
    uf.union(0, 1)
    uf.union(1, 2)

    # Create component {3,4,5}
    uf.union(3, 4)
    uf.union(4, 5)

    # Verify components are separate
    assert uf.connected(0, 3) is False

    # Merge the components
    uf.union(2, 3)

    # Verify all nodes are now connected
    assert uf.connected(0, 5) is True
    assert uf.find(5) == uf.find(0)


def test_large_set():
    """Test with a larger set to ensure performance isn't an issue"""
    size = 100
    uf = UnionFind(size)

    # Connect all even numbers
    for i in range(0, size - 2, 2):
        uf.union(i, i + 2)

    # Connect all odd numbers
    for i in range(1, size - 2, 2):
        uf.union(i, i + 2)

    # Verify connectivity within parity groups
    for i in range(0, size - 4, 2):
        assert uf.connected(i, i + 4) is True

    for i in range(1, size - 4, 2):
        assert uf.connected(i, i + 4) is True

    # Verify separation between parity groups
    for i in range(0, size, 2):
        for j in range(1, size, 2):
            assert uf.connected(i, j) is False

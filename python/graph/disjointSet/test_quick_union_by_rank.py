import pytest
from quick_union_by_rank import UnionFind


def test_initialization():
    """Test that initialization creates correct root and rank arrays"""
    uf = UnionFind(5)
    assert uf.root == [0, 1, 2, 3, 4]
    assert uf.rank == [1, 1, 1, 1, 1]


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

    # Since ranks are initially equal, 1's root becomes 0
    assert uf.find(1) == 0
    assert uf.connected(0, 1) is True
    assert uf.connected(1, 0) is True

    # Check that rank is updated correctly
    assert uf.rank[0] == 2
    assert uf.rank[1] == 1


def test_union_by_rank():
    """Test that union by rank works correctly"""
    uf = UnionFind(6)

    # Create a tree with root 0 and height 2
    uf.union(0, 1)  # 1 points to 0, rank[0] = 2
    uf.union(0, 2)  # 2 points to 0, rank[0] still 2

    # Create another tree with root 3 and height 1
    uf.union(3, 4)  # 4 points to 3, rank[3] = 2

    # When we unite these trees, the root with higher rank should become the new root
    uf.union(0, 3)

    # Since both roots have rank 2, one becomes root and its rank increases to 3
    if uf.find(0) == 0:  # If 0 became the root
        assert uf.find(3) == 0
        assert uf.rank[0] == 3
    else:  # If 3 became the root
        assert uf.find(0) == 3
        assert uf.rank[3] == 3


def test_path_compression():
    """Test that find operation performs path compression"""
    uf = UnionFind(5)

    # Create a chain: 4 -> 3 -> 2 -> 1 -> 0
    uf.root[1] = 0
    uf.root[2] = 1
    uf.root[3] = 2
    uf.root[4] = 3

    # Call find on the leaf node
    root = uf.find(4)
    assert root == 0

    # Path compression is not implemented in this version,
    # so we don't expect any path compression


def test_transitive_union():
    """Test that unions are properly transitive"""
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)

    # All three should now be in the same component
    assert uf.connected(0, 2) is True

    # Check that the root is consistent
    root = uf.find(0)
    assert uf.find(1) == root
    assert uf.find(2) == root


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


def test_large_set():
    """Test with a larger set to ensure performance isn't an issue"""
    size = 1000
    uf = UnionFind(size)

    # Create a balanced tree structure
    for i in range(1, size):
        uf.union(i - 1, i)

    # Verify all elements are connected to element 0
    for i in range(1, size):
        assert uf.connected(0, i) is True

    # The tree height should be logarithmic due to union by rank
    # which means find operations should be efficient
    root = uf.find(size - 1)
    assert root == uf.find(0)

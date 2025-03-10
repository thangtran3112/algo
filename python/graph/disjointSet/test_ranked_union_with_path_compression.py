from ranked_union_with_path_compression import UnionFind


# pytest -v test_ranked_union_with_path_compression.py
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

    # After union, they should be connected and share the same root
    assert uf.connected(0, 1) is True
    assert uf.find(0) == uf.find(1)


def test_rank_based_union():
    """Test that union by rank works correctly"""
    uf = UnionFind(6)

    # Create a tree with root 0 and rank 2
    uf.union(0, 1)  # 1 points to 0, rank[0] = 2
    uf.union(0, 2)  # 2 points to 0, rank[0] still 2

    # Create another tree with root 3 and rank 2
    uf.union(3, 4)  # 4 points to 3, rank[3] = 2

    # Check ranks before merging
    assert uf.rank[0] == 2
    assert uf.rank[3] == 2

    # When we unite these trees with equal ranks, one root's rank should increase
    uf.union(0, 3)

    # Find the final root
    if uf.find(0) == 0:  # If 0 became the root
        assert uf.find(3) == 0
        assert uf.rank[0] == 3
    else:  # If 3 became the root
        assert uf.find(0) == 3
        assert uf.rank[3] == 3


def test_path_compression():
    """Test that path compression works properly"""
    uf = UnionFind(5)

    # Manually create a deep path: 4->3->2->1->0
    uf.root[1] = 0
    uf.root[2] = 1
    uf.root[3] = 2
    uf.root[4] = 3

    # Call find on the leaf node
    root = uf.find(4)
    assert root == 0

    # After path compression, all nodes should point directly to the root
    assert uf.root[1] == 0
    assert uf.root[2] == 0
    assert uf.root[3] == 0
    assert uf.root[4] == 0


def test_transitive_union():
    """Test that unions are properly transitive and paths are compressed"""
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)

    # All three should be connected
    assert uf.connected(0, 2) is True

    # Find the root and verify that path compression occurred
    root = uf.find(0)
    assert uf.find(1) == root
    assert uf.find(2) == root

    # Check direct pointers after compression
    assert uf.root[1] == root
    assert uf.root[2] == root


def test_multiple_components():
    """Test handling of multiple separate components"""
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)

    # Verify two separate components
    assert uf.connected(0, 2) is True
    assert uf.connected(3, 4) is True
    assert uf.connected(0, 3) is False
    assert uf.connected(2, 5) is False

    # Each component should have its own root
    root0 = uf.find(0)
    root3 = uf.find(3)
    assert root0 != root3


def test_component_merger():
    """Test merging of two existing components with path compression and rank"""
    uf = UnionFind(6)
    # Create component {0,1,2}
    uf.union(0, 1)
    uf.union(1, 2)

    # Create component {3,4,5}
    uf.union(3, 4)
    uf.union(4, 5)

    # Get the roots before merging
    root0 = uf.find(0)
    root3 = uf.find(3)

    # Get the ranks before merging
    rank0 = uf.rank[root0]
    rank3 = uf.rank[root3]

    # Merge the components
    uf.union(2, 3)

    # All should now be connected in a single component
    assert uf.connected(0, 5) is True

    # The root should be the one with higher rank, or if equal,
    # one of them with an incremented rank
    final_root = uf.find(0)
    if rank0 > rank3:
        assert final_root == root0
    elif rank0 < rank3:
        assert final_root == root3
    else:
        # If ranks were equal, either could be the new root with increased rank
        if final_root == root0:
            assert uf.rank[root0] == rank0 + 1
        else:
            assert uf.rank[root3] == rank3 + 1


def test_large_set():
    """Test with a larger set to ensure optimizations are effective"""
    size = 1000
    uf = UnionFind(size)

    # Create a chain of elements
    for i in range(1, size):
        uf.union(i - 1, i)

    # Verify all elements are in the same component
    for i in range(1, size):
        assert uf.connected(0, i) is True

    # Check that path compression has flattened the structure
    root = uf.find(0)
    for i in range(size):
        # After calling find on all elements, they should point directly to the root
        assert uf.find(i) == root
        assert uf.root[i] == root


def test_example_from_file():
    """Test the example provided in the file"""
    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)

    assert uf.connected(1, 5) is True
    assert uf.connected(5, 7) is True
    assert uf.connected(4, 9) is False

    uf.union(9, 4)
    assert uf.connected(4, 9) is True

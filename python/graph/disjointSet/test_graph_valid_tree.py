import pytest
from graph_valid_tree import Solution, UnionFind

# pytest -v .\python\graph\disjointSet\test_graph_valid_tree.py
class TestUnionFind:
    def test_initialization(self):
        """Test that UnionFind initializes correctly"""
        uf = UnionFind(5)
        assert uf.parent == [0, 1, 2, 3, 4]
        assert uf.rank == [1, 1, 1, 1, 1]

    def test_find(self):
        """Test the find operation returns the correct parent"""
        uf = UnionFind(5)
        assert uf.find(0) == 0
        assert uf.find(4) == 4

    def test_union_success(self):
        """Test that union connects elements and returns True for new connections"""
        uf = UnionFind(5)
        # First connection should succeed
        assert uf.union(0, 1) is True
        assert uf.isConnected(0, 1) is True

    def test_union_already_connected(self):
        """Test that union returns False when elements are already connected"""
        uf = UnionFind(5)
        # Connect 0 and 1
        assert uf.union(0, 1) is True
        # Connect 1 and 2
        assert uf.union(1, 2) is True
        # Try to connect 0 and 2 (already connected indirectly)
        assert uf.union(0, 2) is False

    def test_is_connected(self):
        """Test isConnected method"""
        uf = UnionFind(5)
        # Initially not connected
        assert uf.isConnected(0, 1) is False
        # After union
        uf.union(0, 1)
        assert uf.isConnected(0, 1) is True

    def test_count_roots_initial(self):
        """Test count_roots with no unions (all separate)"""
        uf = UnionFind(5)
        assert uf.count_roots() == 5

    def test_count_roots_after_unions(self):
        """Test count_roots after some unions"""
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(2, 3)
        # Should have 3 roots: [0, 2, 4]
        assert uf.count_roots() == 3

        # Connect all into one component
        uf.union(0, 2)
        uf.union(0, 4)
        assert uf.count_roots() == 1

    def test_path_compression(self):
        """Test that path compression optimizes the tree structure"""
        uf = UnionFind(5)
        # Create a chain: 0 <- 1 <- 2 <- 3 <- 4
        uf.parent[1] = 0
        uf.parent[2] = 1
        uf.parent[3] = 2
        uf.parent[4] = 3
        
        # Find should compress the path
        root = uf.find(4)
        assert root == 0
        
        # After compression, all should point directly to the root
        assert uf.parent[4] == 0
        assert uf.parent[3] == 0
        assert uf.parent[2] == 0
        assert uf.parent[1] == 0


class TestSolution:
    def test_example1(self):
        """Test with the example from the problem statement"""
        solution = Solution()
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        assert solution.validTree(n, edges) is True

    def test_cycle_detection(self):
        """Test that a graph with a cycle is not a valid tree"""
        solution = Solution()
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]  # Edge [1,3] creates a cycle
        assert solution.validTree(n, edges) is False

    def test_disconnected_graph(self):
        """Test that a disconnected graph is not a valid tree"""
        solution = Solution()
        n = 5
        edges = [[0, 1], [2, 3]]  # Two separate components
        assert solution.validTree(n, edges) is False

    def test_empty_graph(self):
        """Test with an empty graph (no edges)"""
        solution = Solution()
        n = 1
        edges = []
        # A single node with no edges is a valid tree
        assert solution.validTree(n, edges) is True

    def test_multi_node_no_edges(self):
        """Test multiple nodes with no edges"""
        solution = Solution()
        n = 5
        edges = []
        # Multiple nodes with no edges is not a valid tree (disconnected)
        assert solution.validTree(n, edges) is False

    def test_self_loops(self):
        """Test a graph with self loops"""
        solution = Solution()
        n = 3
        edges = [[0, 1], [1, 2], [0, 0]]  # Edge [0,0] is a self-loop
        assert solution.validTree(n, edges) is False

    def test_multiple_edges(self):
        """Test a graph with multiple edges between the same nodes"""
        solution = Solution()
        n = 3
        edges = [[0, 1], [1, 2], [0, 1]]  # Edge [0,1] appears twice
        assert solution.validTree(n, edges) is False

    def test_line_graph(self):
        """Test with a line graph (all nodes connected in a line)"""
        solution = Solution()
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        assert solution.validTree(n, edges) is True

    def test_star_graph(self):
        """Test with a star graph (all nodes connected to a central node)"""
        solution = Solution()
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [0, 4]]
        assert solution.validTree(n, edges) is True

    def test_too_many_edges(self):
        """Test with too many edges for a tree"""
        solution = Solution()
        n = 5
        # A tree with n nodes should have exactly n-1 edges
        edges = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]  # 6 edges for 5 nodes
        assert solution.validTree(n, edges) is False

    def test_correct_edge_count(self):
        """Test that the solution validates edge count"""
        solution = Solution()
        n = 4
        edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]  # 5 edges for 4 nodes
        # This has too many edges for a tree (should have n-1 = 3)
        assert solution.validTree(n, edges) is False

    def test_larger_valid_tree(self):
        """Test with a larger valid tree structure"""
        solution = Solution()
        n = 10
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]
        assert solution.validTree(n, edges) is True

    def test_invalid_node_index(self):
        """Test behavior with invalid node indices (out of range)"""
        solution = Solution()
        n = 3
        edges = [[0, 1], [1, 3]]  # Node 3 is out of range (0-2)
        
        # This should ideally be handled by the implementation
        # If not, we can check if it raises an IndexError
        with pytest.raises(IndexError):
            solution.validTree(n, edges)
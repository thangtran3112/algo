import unittest
from path_compression import SimpleUnionFind


# cd c:\Users\user\Documents\GitHub\algo\python\graph\disjointSet
# python test_path_compression.py
# OR python -m pytest python/graph/disjointSet/test_path_compression.py -v
class TestPathCompression(unittest.TestCase):
    def test_initialization(self):
        """Test that initialization creates correct root array"""
        uf = SimpleUnionFind(5)
        self.assertEqual(uf.root, [0, 1, 2, 3, 4])

        # Test that each element is initially its own root
        for i in range(5):
            self.assertEqual(uf.find(i), i)

    def test_find_no_compression_needed(self):
        """Test the find operation when no compression is needed"""
        uf = SimpleUnionFind(5)
        # Each node is its own root initially
        self.assertEqual(uf.find(0), 0)
        self.assertEqual(uf.find(1), 1)
        self.assertEqual(uf.find(4), 4)

    def test_connected_initially(self):
        """Test that no nodes are initially connected unless they're the same node"""
        uf = SimpleUnionFind(5)
        for i in range(5):
            self.assertTrue(uf.connected(i, i))  # Each node is connected to itself

        # Different nodes should not be connected initially
        self.assertFalse(uf.connected(0, 1))
        self.assertFalse(uf.connected(1, 2))
        self.assertFalse(uf.connected(3, 4))

    def test_basic_union(self):
        """Test basic union operation between two nodes"""
        uf = SimpleUnionFind(5)
        uf.union(0, 1)

        # After union, they should be connected and share the same root
        self.assertTrue(uf.connected(0, 1))
        self.assertEqual(uf.find(0), uf.find(1))

    def test_path_compression(self):
        """Test that path compression works properly"""
        uf = SimpleUnionFind(5)

        # Manually create a deep path 4->3->2->1->0
        uf.root[1] = 0
        uf.root[2] = 1
        uf.root[3] = 2
        uf.root[4] = 3

        # Find should compress the path
        root = uf.find(4)
        self.assertEqual(root, 0)

        # After compression, nodes 1, 2, 3, 4 should directly point to 0
        self.assertEqual(uf.root[1], 0)
        self.assertEqual(uf.root[2], 0)
        self.assertEqual(uf.root[3], 0)
        self.assertEqual(uf.root[4], 0)

    def test_transitive_union(self):
        """Test that unions are properly transitive and paths are compressed"""
        uf = SimpleUnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)

        # All three should be connected
        self.assertTrue(uf.connected(0, 2))

        # Path should be compressed, so 2 should point directly to the root
        root = uf.find(0)
        self.assertEqual(uf.root[2], root)

    def test_multiple_components(self):
        """Test handling of multiple separate components"""
        uf = SimpleUnionFind(6)
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(3, 4)

        # Verify two separate components
        self.assertTrue(uf.connected(0, 2))
        self.assertTrue(uf.connected(3, 4))
        self.assertFalse(uf.connected(0, 3))
        self.assertFalse(uf.connected(2, 5))

        # All elements in component should point to the same root after find
        root0 = uf.find(0)
        self.assertEqual(uf.root[1], root0)
        self.assertEqual(uf.root[2], root0)

        root3 = uf.find(3)
        self.assertEqual(uf.root[4], root3)

    def test_component_merger(self):
        """Test merging of two existing components with path compression"""
        uf = SimpleUnionFind(6)
        # Create component {0,1,2}
        uf.union(0, 1)
        uf.union(1, 2)

        # Create component {3,4,5}
        uf.union(3, 4)
        uf.union(4, 5)

        # Merge the components
        uf.union(2, 3)

        # All should now be connected in a single component
        self.assertTrue(uf.connected(0, 5))

    def test_large_set(self):
        """Test with a larger set to ensure path compression helps efficiency"""
        size = 1000
        uf = SimpleUnionFind(size)

        # Create a chain
        for i in range(1, size):
            uf.union(0, i)

        # Check that all elements are connected to element 0
        for i in range(1, size):
            self.assertTrue(uf.connected(0, i))

        # After all the finds, path compression should have happened
        # All elements should point directly to the root
        root = uf.find(0)
        for i in range(size):
            self.assertEqual(uf.root[i], root)

    def test_repeated_operations(self):
        """Test that repeated operations don't break anything"""
        uf = SimpleUnionFind(5)

        # Perform same union multiple times
        uf.union(0, 1)
        uf.union(0, 1)
        self.assertTrue(uf.connected(0, 1))

        # Add more to the component
        uf.union(1, 2)
        uf.union(0, 2)  # Redundant

        # Check consistency
        self.assertTrue(uf.connected(0, 2))

        # Find operations shouldn't change connectivity
        root = uf.find(0)
        self.assertEqual(uf.find(1), root)
        self.assertEqual(uf.find(2), root)
        self.assertTrue(uf.connected(0, 2))


if __name__ == "__main__":
    unittest.main()

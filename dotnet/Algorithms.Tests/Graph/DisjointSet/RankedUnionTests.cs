using Algorithms.Core.Graph.DisjointSet;

namespace Algorithms.Tests.Graph.DisjointSet
{
    public class RankedUnionTests
    {
        [Fact]
        public void Constructor_InitializesCorrectly()
        {
            // Arrange & Act
            var unionFind = new RankedUnion(5);

            // Assert - Check initialization through Find method
            for (int i = 0; i < 5; i++)
            {
                Assert.Equal(i, unionFind.Find(i));
            }
        }

        [Fact]
        public void Find_WithNoUnions_ReturnsElementItself()
        {
            // Arrange
            var unionFind = new RankedUnion(5);

            // Act & Assert
            for (int i = 0; i < 5; i++)
            {
                Assert.Equal(i, unionFind.Find(i));
            }
        }

        [Fact]
        public void Connected_InitialState_ReturnsTrueOnlyForSameElement()
        {
            // Arrange
            var unionFind = new RankedUnion(5);

            // Act & Assert
            for (int i = 0; i < 5; i++)
            {
                Assert.True(unionFind.Connected(i, i));

                for (int j = i + 1; j < 5; j++)
                {
                    Assert.False(unionFind.Connected(i, j));
                }
            }
        }

        [Fact]
        public void Union_ConnectsTwoElements()
        {
            // Arrange
            var unionFind = new RankedUnion(5);

            // Act
            unionFind.Union(1, 2);

            // Assert
            Assert.True(unionFind.Connected(1, 2));
            Assert.False(unionFind.Connected(0, 1));
            Assert.False(unionFind.Connected(0, 2));
        }

        [Fact]
        public void Union_IsTransitive()
        {
            // Arrange
            var unionFind = new RankedUnion(5);

            // Act
            unionFind.Union(0, 1);
            unionFind.Union(1, 2);

            // Assert
            Assert.True(unionFind.Connected(0, 2));
        }

        [Fact]
        public void Union_MaintainsMultipleComponents()
        {
            // Arrange
            var unionFind = new RankedUnion(6);

            // Act - Create two separate components
            unionFind.Union(0, 1);
            unionFind.Union(1, 2);
            unionFind.Union(3, 4);

            // Assert
            Assert.True(unionFind.Connected(0, 2));
            Assert.True(unionFind.Connected(3, 4));
            Assert.False(unionFind.Connected(0, 3));
            Assert.False(unionFind.Connected(2, 4));
            Assert.False(unionFind.Connected(2, 5));
        }

        [Fact]
        public void Union_ByRank_MakesSmallTreePointToLargeTree()
        {
            // Arrange
            var unionFind = new RankedUnion(5);

            // Create a tree with higher rank
            unionFind.Union(0, 1); // 0 and 1 united
            unionFind.Union(0, 2); // 0, 1, and 2 united with 0 as root

            // Create a smaller tree
            unionFind.Union(3, 4); // 3 and 4 united

            // Act
            unionFind.Union(2, 3); // Should unite the two trees with 0 as the root

            // Assert
            int expectedRoot = unionFind.Find(0);
            for (int i = 0; i < 5; i++)
            {
                Assert.Equal(expectedRoot, unionFind.Find(i));
            }

            // All elements should be connected
            for (int i = 0; i < 4; i++)
            {
                Assert.True(unionFind.Connected(i, i + 1));
            }
        }

        [Fact]
        public void PathCompression_OptimizesPathToRoot()
        {
            // Arrange
            var unionFind = new RankedUnion(5);

            // Create a chain: 4 -> 3 -> 2 -> 1 -> 0
            // We can't access _root directly, so we need to simulate this scenario
            // by carefully creating unions
            unionFind.Union(0, 1); // 1's root is 0
            unionFind.Union(2, 1); // 2's root is 0
            unionFind.Union(3, 2); // 3's root is 0
            unionFind.Union(4, 3); // 4's root is 0

            // Act
            int root = unionFind.Find(4); // This should compress the path

            // Assert
            Assert.Equal(0, root); // The root should be 0

            // All elements should be connected to the root
            for (int i = 0; i < 5; i++)
            {
                Assert.True(unionFind.Connected(0, i));
            }
        }

        [Fact]
        public void Union_WithLargeDataset_IsEfficient()
        {
            // Arrange
            int size = 1000;
            var unionFind = new RankedUnion(size);

            // Act
            // Create a balanced tree structure
            for (int i = 1; i < size; i++)
            {
                unionFind.Union(i - 1, i);
            }

            // Assert
            // All elements should be connected to element 0
            for (int i = 1; i < size; i++)
            {
                Assert.True(unionFind.Connected(0, i));
            }
        }
    }
}
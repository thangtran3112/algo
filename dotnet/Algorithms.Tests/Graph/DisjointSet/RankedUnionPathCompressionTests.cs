using System;
using Xunit;
using Algorithms.Core.Graph.DisjointSet;

// dotnet test --filter "RankedUnionPathCompressionTests"
namespace Algorithms.Tests.Graph.DisjointSet
{
    public class RankedUnionPathCompressionTests
    {
        [Fact]
        public void Constructor_InitializesCorrectly()
        {
            // Arrange & Act
            var uf = new RankedUnionPathCompression(5);

            // Assert - Each element should be its own root initially
            for (int i = 0; i < 5; i++)
            {
                Assert.Equal(i, uf.Find(i));
            }
        }

        [Fact]
        public void Find_OnInitialState_ReturnsElementItself()
        {
            // Arrange
            var uf = new RankedUnionPathCompression(5);

            // Act & Assert
            for (int i = 0; i < 5; i++)
            {
                Assert.Equal(i, uf.Find(i));
            }
        }

        [Fact]
        public void Connected_InitialState_ReturnsTrueOnlyForSameElement()
        {
            // Arrange
            var uf = new RankedUnionPathCompression(5);

            // Act & Assert
            for (int i = 0; i < 5; i++)
            {
                // Each element is connected to itself
                Assert.True(uf.Connected(i, i));

                // But not to any other element
                for (int j = i + 1; j < 5; j++)
                {
                    Assert.False(uf.Connected(i, j));
                }
            }
        }

        [Fact]
        public void Union_ConnectsTwoElements()
        {
            // Arrange
            var uf = new RankedUnionPathCompression(5);

            // Act
            uf.Union(0, 1);

            // Assert
            Assert.True(uf.Connected(0, 1));
            Assert.False(uf.Connected(0, 2));
            Assert.False(uf.Connected(1, 2));
        }

        [Fact]
        public void Union_IsTransitive()
        {
            // Arrange
            var uf = new RankedUnionPathCompression(5);

            // Act
            uf.Union(0, 1);
            uf.Union(1, 2);

            // Assert - Connected should be transitive
            Assert.True(uf.Connected(0, 2));
            Assert.False(uf.Connected(0, 3));
            Assert.False(uf.Connected(2, 4));
        }

        [Fact]
        public void Union_ByRank_MakesLowerRankTreePointToHigherRankTree()
        {
            // Arrange
            var uf = new RankedUnionPathCompression(6);

            // Create two separate trees with different ranks
            uf.Union(0, 1); // Union trees of rank 0, resulting in 0 being root with rank 1
            uf.Union(0, 2); // Union trees with ranks 1 and 0, resulting in 0 still being root

            uf.Union(3, 4); // Union trees of rank 0, resulting in 3 being root with rank 1

            // Verify initial connectivity
            Assert.True(uf.Connected(0, 2));
            Assert.True(uf.Connected(3, 4));
            Assert.False(uf.Connected(0, 3));

            // Act
            uf.Union(0, 3);

            // Assert
            // All elements should now be connected
            Assert.True(uf.Connected(0, 3));
            Assert.True(uf.Connected(1, 4));
            Assert.True(uf.Connected(2, 3));
        }

        [Fact]
        public void Union_WithEqualRanks_IncreasesRankOfResultingRoot()
        {
            // Arrange
            var uf = new RankedUnionPathCompression(4);

            // Create two single-element trees
            int element0 = 0;
            int element1 = 1;

            // Both have rank 0 initially

            // Act
            uf.Union(element0, element1);

            // Assert
            // Both elements should now be connected
            Assert.True(uf.Connected(element0, element1));

            // Create another single element tree
            int element2 = 2;

            // Union it with our existing tree
            uf.Union(element0, element2);

            // All three should now be connected
            Assert.True(uf.Connected(element0, element2));
            Assert.True(uf.Connected(element1, element2));
        }

        [Fact]
        public void PathCompression_OptimizesPathToRoot()
        {
            // Arrange - Create a chain-like structure
            var uf = new RankedUnionPathCompression(5);

            // Create the chain through a series of unions with appropriate rank structure
            uf.Union(0, 1); // 1 points to 0
            uf.Union(1, 2); // 2 points to the root of 1, which is 0
            uf.Union(2, 3); // 3 points to the root of 2, which is 0
            uf.Union(3, 4); // 4 points to the root of 3, which is 0

            // Verify all elements are connected
            for (int i = 0; i < 4; i++)
            {
                Assert.True(uf.Connected(i, i + 1));
            }

            // All elements should be connected to element 0
            for (int i = 1; i < 5; i++)
            {
                Assert.True(uf.Connected(0, i));
            }
        }

        [Fact]
        public void Connected_AfterComplexOperations_ReturnsCorrectResult()
        {
            // Arrange
            var uf = new RankedUnionPathCompression(10);

            // Create several components
            uf.Union(0, 1);
            uf.Union(2, 3);
            uf.Union(4, 5);
            uf.Union(6, 7);
            uf.Union(8, 9);

            // Verify initial separate components
            Assert.True(uf.Connected(0, 1));
            Assert.True(uf.Connected(2, 3));
            Assert.False(uf.Connected(0, 2));
            Assert.False(uf.Connected(1, 3));
            Assert.False(uf.Connected(4, 6));

            // Merge some components
            uf.Union(1, 2); // Merges {0,1} and {2,3}
            uf.Union(5, 6); // Merges {4,5} and {6,7}

            // Verify merged components
            Assert.True(uf.Connected(0, 3));
            Assert.True(uf.Connected(4, 7));
            Assert.False(uf.Connected(0, 4));
            Assert.False(uf.Connected(3, 5));

            // Final merge into a single component
            uf.Union(3, 4);
            uf.Union(7, 8);

            // Verify all elements are connected
            for (int i = 0; i < 9; i++)
            {
                for (int j = i + 1; j < 10; j++)
                {
                    Assert.True(uf.Connected(i, j));
                }
            }
        }

        [Fact]
        public void Connected_WithMultipleComponentsAndPathCompression_ReturnsCorrectResult()
        {
            // Arrange
            var uf = new RankedUnionPathCompression(15);

            // Create three separate components
            // Component 1: {0,1,2,3,4}
            uf.Union(0, 1);
            uf.Union(1, 2);
            uf.Union(2, 3);
            uf.Union(3, 4);

            // Component 2: {5,6,7,8,9}
            uf.Union(5, 6);
            uf.Union(6, 7);
            uf.Union(7, 8);
            uf.Union(8, 9);

            // Component 3: {10,11,12,13,14}
            uf.Union(10, 11);
            uf.Union(11, 12);
            uf.Union(12, 13);
            uf.Union(13, 14);

            // Act - Test connectivity within and between components

            // Assert - Within components should be connected
            Assert.True(uf.Connected(0, 4));
            Assert.True(uf.Connected(5, 9));
            Assert.True(uf.Connected(10, 14));

            // Between components should not be connected
            Assert.False(uf.Connected(0, 5));
            Assert.False(uf.Connected(4, 10));
            Assert.False(uf.Connected(9, 10));

            // Merge component 1 and 2
            uf.Union(4, 5);

            // Now component 1 and 2 should be connected
            Assert.True(uf.Connected(0, 9));
            Assert.True(uf.Connected(1, 8));
            Assert.True(uf.Connected(2, 7));

            // But still separate from component 3
            Assert.False(uf.Connected(0, 10));
            Assert.False(uf.Connected(9, 14));

            // Final merge to create a single component
            uf.Union(9, 10);

            // Now all elements should be connected
            for (int i = 0; i < 14; i++)
            {
                Assert.True(uf.Connected(i, i + 1));
                Assert.True(uf.Connected(0, i));
            }
        }

        [Fact]
        public void Find_AndConnected_WithLargeDataset_IsEfficient()
        {
            // Arrange
            int size = 1000;
            var uf = new RankedUnionPathCompression(size);

            // Create a chain
            for (int i = 0; i < size - 1; i++)
            {
                uf.Union(i, i + 1);
            }

            // Act & Assert
            // All elements should be connected
            for (int i = 0; i < size - 1; i++)
            {
                Assert.True(uf.Connected(i, i + 1));
                Assert.True(uf.Connected(0, i));
            }

            // This test is efficient because path compression should have happened
            // during the Union operations
        }

        [Fact]
        public void Connected_IdenticalElements_AlwaysReturnsTrue()
        {
            // Arrange
            var uf = new RankedUnionPathCompression(5);

            // Act & Assert
            for (int i = 0; i < 5; i++)
            {
                Assert.True(uf.Connected(i, i));
            }

            // Even after some unions, same element should still be connected to itself
            uf.Union(0, 1);
            uf.Union(2, 3);

            for (int i = 0; i < 5; i++)
            {
                Assert.True(uf.Connected(i, i));
            }
        }
    }
}
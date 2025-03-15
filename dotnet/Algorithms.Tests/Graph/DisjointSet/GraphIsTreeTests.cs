using System;
using Xunit;
using Algorithms.Core.Graph.DisjointSet;

// dotnet test --filter "GraphIsTreeTests" 
namespace Algorithms.Tests.Graph.DisjointSet
{
    public class GraphIsTreeTests
    {
        [Fact]
        public void ValidTree_WithValidTree_ReturnsTrue()
        {
            // Arrange
            var graphIsTree = new GraphIsTree();
            int n = 5;
            int[][] edges = new int[][]
            {
                new int[] { 0, 1 },
                new int[] { 0, 2 },
                new int[] { 0, 3 },
                new int[] { 1, 4 }
            };

            // Act
            bool result = graphIsTree.ValidTree(n, edges);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public void ValidTree_WithCycle_ReturnsFalse()
        {
            // Arrange
            var graphIsTree = new GraphIsTree();
            int n = 5;
            int[][] edges = new int[][]
            {
                new int[] { 0, 1 },
                new int[] { 1, 2 },
                new int[] { 2, 3 },
                new int[] { 1, 3 }, // Creates a cycle
                new int[] { 1, 4 }
            };

            // Act
            bool result = graphIsTree.ValidTree(n, edges);

            // Assert
            Assert.False(result);
        }

        [Fact]
        public void ValidTree_WithDisconnectedGraph_ReturnsFalse()
        {
            // Arrange
            var graphIsTree = new GraphIsTree();
            int n = 5;
            int[][] edges = new int[][]
            {
                new int[] { 0, 1 },
                new int[] { 2, 3 }
            };

            // Act
            bool result = graphIsTree.ValidTree(n, edges);

            // Assert
            Assert.False(result);
        }

        [Fact]
        public void ValidTree_SingleNode_ReturnsTrue()
        {
            // Arrange
            var graphIsTree = new GraphIsTree();
            int n = 1;
            int[][] edges = Array.Empty<int[]>();

            // Act
            bool result = graphIsTree.ValidTree(n, edges);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public void ValidTree_TooManyEdges_ReturnsFalse()
        {
            // Arrange
            var graphIsTree = new GraphIsTree();
            int n = 5;
            int[][] edges = new int[][]
            {
                new int[] { 0, 1 },
                new int[] { 0, 2 },
                new int[] { 0, 3 },
                new int[] { 1, 4 },
                new int[] { 2, 3 } // Extra edge
            };

            // Act
            bool result = graphIsTree.ValidTree(n, edges);

            // Assert
            Assert.False(result);
        }

        [Fact]
        public void ValidTree_TooFewEdges_ReturnsFalse()
        {
            // Arrange
            var graphIsTree = new GraphIsTree();
            int n = 5;
            int[][] edges = new int[][]
            {
                new int[] { 0, 1 },
                new int[] { 0, 2 },
                new int[] { 1, 4 }
            }; // Missing one edge

            // Act
            bool result = graphIsTree.ValidTree(n, edges);

            // Assert
            Assert.False(result);
        }

        [Fact]
        public void ValidTree_LineGraph_ReturnsTrue()
        {
            // Arrange
            var graphIsTree = new GraphIsTree();
            int n = 5;
            int[][] edges = new int[][]
            {
                new int[] { 0, 1 },
                new int[] { 1, 2 },
                new int[] { 2, 3 },
                new int[] { 3, 4 }
            };

            // Act
            bool result = graphIsTree.ValidTree(n, edges);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public void ValidTree_StarGraph_ReturnsTrue()
        {
            // Arrange
            var graphIsTree = new GraphIsTree();
            int n = 5;
            int[][] edges = new int[][]
            {
                new int[] { 0, 1 },
                new int[] { 0, 2 },
                new int[] { 0, 3 },
                new int[] { 0, 4 }
            };

            // Act
            bool result = graphIsTree.ValidTree(n, edges);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public void ValidTree_WithSelfLoop_ReturnsFalse()
        {
            // Arrange
            var graphIsTree = new GraphIsTree();
            int n = 3;
            int[][] edges = new int[][]
            {
                new int[] { 0, 1 },
                new int[] { 1, 2 },
                new int[] { 2, 2 } // Self-loop
            };

            // Act
            bool result = graphIsTree.ValidTree(n, edges);

            // Assert
            Assert.False(result);
        }

        [Fact]
        public void ValidTree_WithMultipleEdgesBetweenSameNodes_ReturnsFalse()
        {
            // Arrange
            var graphIsTree = new GraphIsTree();
            int n = 3;
            int[][] edges = new int[][]
            {
                new int[] { 0, 1 },
                new int[] { 0, 1 }, // Duplicate edge
                new int[] { 1, 2 }
            };

            // Act
            bool result = graphIsTree.ValidTree(n, edges);

            // Assert
            Assert.False(result);
        }

        [Fact]
        public void ValidTree_ZeroNodes_ReturnsFalse()
        {
            // Arrange
            var graphIsTree = new GraphIsTree();
            int n = 0;
            int[][] edges = Array.Empty<int[]>();

            // Act
            bool result = graphIsTree.ValidTree(n, edges);

            // Assert
            Assert.False(result);
        }

        [Fact]
        public void ValidTree_LargerValidTree_ReturnsTrue()
        {
            // Arrange
            var graphIsTree = new GraphIsTree();
            int n = 10;
            int[][] edges = new int[][]
            {
                new int[] { 0, 1 },
                new int[] { 1, 2 },
                new int[] { 2, 3 },
                new int[] { 3, 4 },
                new int[] { 4, 5 },
                new int[] { 5, 6 },
                new int[] { 6, 7 },
                new int[] { 7, 8 },
                new int[] { 8, 9 }
            };

            // Act
            bool result = graphIsTree.ValidTree(n, edges);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public void ValidTree_ComplexTree_ReturnsTrue()
        {
            // Arrange
            var graphIsTree = new GraphIsTree();
            int n = 6;
            int[][] edges = new int[][]
            {
                new int[] { 0, 1 },
                new int[] { 0, 2 },
                new int[] { 2, 3 },
                new int[] { 2, 4 },
                new int[] { 4, 5 }
            };

            // Act
            bool result = graphIsTree.ValidTree(n, edges);

            // Assert
            Assert.True(result);
        }
    }
}
using System;
using System.Collections.Generic;
using Xunit;
using Algorithms.Core.Graph.Dfs;

namespace Algorithms.Tests.Graph.Dfs
{
    public class PathExistTest
    {
        [Fact]
        public void ValidPath_Example1_ReturnsTrue()
        {
            // Arrange
            var pathExist = new PathExist();
            int n = 3;
            int[][] edges =
            [
                [0, 1],
                [1, 2],
                [2, 0]
            ];
            int source = 0;
            int destination = 2;

            // Act
            bool result = pathExist.ValidPath(n, edges, source, destination);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public void ValidPath_Example2_ReturnsFalse()
        {
            // Arrange
            var pathExist = new PathExist();
            int n = 6;
            int[][] edges =
            [
                [0, 1],
                [0, 2],
                [3, 5],
                [5, 4],
                [4, 3]
            ];
            int source = 0;
            int destination = 5;

            // Act
            bool result = pathExist.ValidPath(n, edges, source, destination);

            // Assert
            Assert.False(result);
        }

        [Fact]
        public void ValidPath_SourceEqualsDestination_ReturnsTrue()
        {
            // Arrange
            var pathExist = new PathExist();
            int n = 3;
            int[][] edges =
            [
                [0, 1],
                [1, 2]
            ];
            int source = 1;
            int destination = 1;

            // Act
            bool result = pathExist.ValidPath(n, edges, source, destination);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public void ValidPath_SingleEdge_DirectConnection_ReturnsTrue()
        {
            // Arrange
            var pathExist = new PathExist();
            int n = 2;
            int[][] edges =
            [
                [0, 1]
            ];
            int source = 0;
            int destination = 1;

            // Act
            bool result = pathExist.ValidPath(n, edges, source, destination);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public void ValidPath_LongPath_ReturnsTrue()
        {
            // Arrange
            var pathExist = new PathExist();
            int n = 6;
            int[][] edges =
            [
                [0, 1],
                [1, 2],
                [2, 3],
                [3, 4],
                [4, 5]
            ];
            int source = 0;
            int destination = 5;

            // Act
            bool result = pathExist.ValidPath(n, edges, source, destination);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public void ValidPath_DisconnectedGraphs_ReturnsFalse()
        {
            // Arrange
            var pathExist = new PathExist();
            int n = 7;
            int[][] edges =
            [
                [0, 1],
                [1, 2],
                [3, 4],
                [4, 5],
                [5, 6]
            ];
            int source = 0;
            int destination = 6;

            // Act
            bool result = pathExist.ValidPath(n, edges, source, destination);

            // Assert
            Assert.False(result);
        }

        [Fact]
        public void ValidPath_CyclicGraph_ReturnsTrue()
        {
            // Arrange
            var pathExist = new PathExist();
            int n = 4;
            int[][] edges =
            [
                [0, 1],
                [1, 2],
                [2, 3],
                [3, 0]
            ];
            int source = 0;
            int destination = 2;

            // Act
            bool result = pathExist.ValidPath(n, edges, source, destination);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public void ValidPath_ComplexGraph_ReturnsTrue()
        {
            // Arrange
            var pathExist = new PathExist();
            int n = 8;
            int[][] edges =
            [
                [0, 1],
                [1, 2],
                [2, 3],
                [0, 4],
                [4, 5],
                [5, 6],
                [6, 7],
                [2, 7]
            ];
            int source = 0;
            int destination = 7;

            // Act
            bool result = pathExist.ValidPath(n, edges, source, destination);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public void ValidPath_MultiplePathsExist_ReturnsTrue()
        {
            // Arrange
            var pathExist = new PathExist();
            int n = 5;
            int[][] edges =
            [
                [0, 1],
                [1, 2],
                [2, 4],
                [0, 3],
                [3, 4]
            ];
            int source = 0;
            int destination = 4;

            // Act
            bool result = pathExist.ValidPath(n, edges, source, destination);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public void ValidPath_LargeGraph_ReturnsExpectedResult()
        {
            // Arrange
            var pathExist = new PathExist();
            int n = 100;
            var edges = new List<int[]>();
            
            // Create a long chain from 0 to 98
            for (int i = 0; i < 99; i++)
            {
                edges.Add([i, i + 1]);
            }
            
            int source = 0;
            int destination = 99;

            // Act
            bool result = pathExist.ValidPath(n, edges.ToArray(), source, destination);

            // Assert
            Assert.True(result);
        }
    }
}
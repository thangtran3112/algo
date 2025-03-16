using System;
using System.Collections.Generic;
using System.Linq;
using Xunit;
using Algorithms.Core.Graph.Dfs;

namespace Algorithms.Tests.Graph.Dfs
{
    public class AllPathsTest
    {
        [Fact]
        public void AllPathsSourceTarget_Example1_ReturnsCorrectPaths()
        {
            // Arrange
            var allPaths = new AllPaths();
            int[][] graph =
            [
                [1, 2],
                [3],
                [3],
                []
            ];

            // Act
            var result = allPaths.AllPathsSourceTarget(graph);

            // Assert
            // We need to check if all expected paths are present regardless of order
            var expectedPaths = new List<List<int>>
            {
                new List<int> { 0, 1, 3 },
                new List<int> { 0, 2, 3 }
            };
            
            AssertPathsEqual(expectedPaths, result);
        }

        [Fact]
        public void AllPathsSourceTarget_Example2_ReturnsCorrectPaths()
        {
            // Arrange
            var allPaths = new AllPaths();
            int[][] graph =
            [
                [4, 3, 1],
                [3, 2, 4],
                [3],
                [4],
                []
            ];

            // Act
            var result = allPaths.AllPathsSourceTarget(graph);

            // Assert
            var expectedPaths = new List<List<int>>
            {
                new List<int> { 0, 4 },
                new List<int> { 0, 3, 4 },
                new List<int> { 0, 1, 3, 4 },
                new List<int> { 0, 1, 2, 3, 4 },
                new List<int> { 0, 1, 4 }
            };
            
            AssertPathsEqual(expectedPaths, result);
        }

        [Fact]
        public void AllPathsSourceTarget_MinimumSizeGraph_ReturnsCorrectPath()
        {
            // Arrange - Minimum graph size is 2 according to constraints
            var allPaths = new AllPaths();
            int[][] graph =
            [
                [1],
                []
            ];

            // Act
            var result = allPaths.AllPathsSourceTarget(graph);

            // Assert
            var expectedPaths = new List<List<int>>
            {
                new List<int> { 0, 1 }
            };
            
            AssertPathsEqual(expectedPaths, result);
        }

        [Fact]
        public void AllPathsSourceTarget_SinglePath_ReturnsCorrectPath()
        {
            // Arrange
            var allPaths = new AllPaths();
            int[][] graph =
            [
                [1],
                [2],
                [3],
                [4],
                []
            ];

            // Act
            var result = allPaths.AllPathsSourceTarget(graph);

            // Assert
            var expectedPaths = new List<List<int>>
            {
                new List<int> { 0, 1, 2, 3, 4 }
            };
            
            AssertPathsEqual(expectedPaths, result);
        }

        [Fact]
        public void AllPathsSourceTarget_NoPath_ReturnsEmptyList()
        {
            // Arrange - No path from source to target
            var allPaths = new AllPaths();
            int[][] graph =
            [
                [1, 2],
                [],
                [],
                []
            ];

            // Act
            var result = allPaths.AllPathsSourceTarget(graph);

            // Assert
            Assert.Empty(result);
        }

        [Fact]
        public void AllPathsSourceTarget_ComplexGraph_ReturnsAllPaths()
        {
            // Arrange
            var allPaths = new AllPaths();
            int[][] graph =
            [
                [1, 2, 3], // Node 0 connects to 1, 2, and 3
                [4, 5],    // Node 1 connects to 4 and 5
                [4, 5],    // Node 2 connects to 4 and 5
                [4, 5],    // Node 3 connects to 4 and 5
                [6],       // Node 4 connects to 6
                [6],       // Node 5 connects to 6
                []          // Node 6 is the destination
            ];

            // Act
            var result = allPaths.AllPathsSourceTarget(graph);

            // Assert
            var expectedPaths = new List<List<int>>
            {
                new List<int> { 0, 1, 4, 6 },
                new List<int> { 0, 1, 5, 6 },
                new List<int> { 0, 2, 4, 6 },
                new List<int> { 0, 2, 5, 6 },
                new List<int> { 0, 3, 4, 6 },
                new List<int> { 0, 3, 5, 6 }
            };
            
            AssertPathsEqual(expectedPaths, result);
        }

        [Fact]
        public void AllPathsSourceTarget_DirectPaths_ReturnsCorrectPaths()
        {
            // Arrange - Direct paths from source to various nodes including destination
            var allPaths = new AllPaths();
            int[][] graph =
            [
                [1, 2, 3, 4], // Source connects directly to all nodes including destination
                [],
                [],
                [],
                []             // Destination
            ];

            // Act
            var result = allPaths.AllPathsSourceTarget(graph);

            // Assert
            var expectedPaths = new List<List<int>>
            {
                new List<int> { 0, 4 } // Only the direct path to destination is valid
            };
            
            AssertPathsEqual(expectedPaths, result);
        }

        [Fact]
        public void AllPathsSourceTarget_LargeGraph_ReturnsCorrectPaths()
        {
            // Arrange - A larger graph (constrained to n <= 15)
            var allPaths = new AllPaths();
            
            // Create a graph where each node connects to the next node
            // and node 0 also has a direct connection to destination
            int[][] graph = new int[15][];
            for (int i = 0; i < 14; i++)
            {
                graph[i] = [i + 1];
            }
            graph[14] = []; // Destination
            
            // Add a direct connection from source to destination
            graph[0] = [1, 14];

            // Act
            var result = allPaths.AllPathsSourceTarget(graph);

            // Assert
            var expectedPaths = new List<List<int>>
            {
                new List<int> { 0, 14 }, // Direct path
                new List<int> { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 } // Long path
            };
            
            AssertPathsEqual(expectedPaths, result);
        }

        [Fact]
        public void AllPathsSourceTarget_DenseGraph_ReturnsAllPaths()
        {
            // Arrange - A dense graph where many paths are possible
            var allPaths = new AllPaths();
            
            // Create a dense graph where each node i connects to all nodes j where j > i
            int n = 5;
            int[][] graph = new int[n][];
            for (int i = 0; i < n - 1; i++)
            {
                var connections = new List<int>();
                for (int j = i + 1; j < n; j++)
                {
                    connections.Add(j);
                }
                graph[i] = connections.ToArray();
            }
            graph[n - 1] = []; // Destination
            
            // Act
            var result = allPaths.AllPathsSourceTarget(graph);

            // Assert - Should have many different paths
            // For n=5, paths are: [0,4], [0,1,4], [0,2,4], [0,3,4], [0,1,2,4], [0,1,3,4], [0,2,3,4], [0,1,2,3,4]
            Assert.Equal(8, result.Count); // We expect 8 different paths
            
            // Check that all paths start with 0 and end with n-1 (4)
            foreach (var path in result)
            {
                Assert.Equal(0, path[0]);
                Assert.Equal(n - 1, path[path.Count - 1]);
            }
        }

        // Helper method to assert that two collections of paths are equal regardless of order
        private void AssertPathsEqual(IEnumerable<IList<int>> expected, IEnumerable<IList<int>> actual)
        {
            // Convert both to sorted strings for comparison
            var expectedStrings = expected.Select(path => string.Join(",", path)).OrderBy(s => s).ToList();
            var actualStrings = actual.Select(path => string.Join(",", path)).OrderBy(s => s).ToList();
            
            Assert.Equal(expectedStrings.Count, actualStrings.Count);
            for (int i = 0; i < expectedStrings.Count; i++)
            {
                Assert.Equal(expectedStrings[i], actualStrings[i]);
            }
        }
    }
}
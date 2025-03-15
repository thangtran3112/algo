using System;
using Xunit;
using Algorithms.Core.Graph.DisjointSet;

namespace Algorithms.Tests.Graph.DisjointSet
{
    public class EarliestBecomeFriendsTests
    {
        [Fact]
        public void EarliestAcq_Example1_Returns20190301()
        {
            // Arrange
            var earliestBecomeFriends = new EalieastBecomeFriends();
            int[][] logs = new int[][]
            {
                new int[] { 20190101, 0, 1 },
                new int[] { 20190104, 3, 4 },
                new int[] { 20190107, 2, 3 },
                new int[] { 20190211, 1, 5 },
                new int[] { 20190224, 2, 4 },
                new int[] { 20190301, 0, 3 },
                new int[] { 20190312, 1, 2 },
                new int[] { 20190322, 4, 5 }
            };
            int n = 6;

            // Act
            int result = earliestBecomeFriends.EarliestAcq(logs, n);

            // Assert
            Assert.Equal(20190301, result);
        }

        [Fact]
        public void EarliestAcq_Example2_Returns3()
        {
            // Arrange
            var earliestBecomeFriends = new EalieastBecomeFriends();
            int[][] logs = new int[][]
            {
                new int[] { 0, 2, 0 },
                new int[] { 1, 0, 1 },
                new int[] { 3, 0, 3 },
                new int[] { 4, 1, 2 },
                new int[] { 7, 3, 1 }
            };
            int n = 4;

            // Act
            int result = earliestBecomeFriends.EarliestAcq(logs, n);

            // Assert
            Assert.Equal(3, result);
        }

        [Fact]
        public void EarliestAcq_UnsortedLogs_SortsAndReturnsCorrectResult()
        {
            // Arrange - logs are intentionally not sorted by timestamp
            var earliestBecomeFriends = new EalieastBecomeFriends();
            int[][] logs = new int[][]
            {
                new int[] { 30, 0, 2 },
                new int[] { 10, 0, 1 },
                new int[] { 20, 1, 2 }
            };
            int n = 3;

            // Act
            int result = earliestBecomeFriends.EarliestAcq(logs, n);

            // Assert - The method should sort the logs and find the correct timestamp (20)
            Assert.Equal(20, result);
        }

        [Fact]
        public void EarliestAcq_NotEnoughConnections_ReturnsNegativeOne()
        {
            // Arrange - Two separate groups that never connect
            var earliestBecomeFriends = new EalieastBecomeFriends();
            int[][] logs = new int[][]
            {
                new int[] { 10, 0, 1 },
                new int[] { 20, 2, 3 }
            };
            int n = 4;

            // Act
            int result = earliestBecomeFriends.EarliestAcq(logs, n);

            // Assert
            Assert.Equal(-1, result);
        }

        [Fact]
        public void EarliestAcq_EmptyLogs_ReturnsNegativeOne()
        {
            // Arrange
            var earliestBecomeFriends = new EalieastBecomeFriends();
            int[][] logs = Array.Empty<int[]>();
            int n = 3;

            // Act
            int result = earliestBecomeFriends.EarliestAcq(logs, n);

            // Assert
            Assert.Equal(-1, result);
        }

        [Fact]
        public void EarliestAcq_ZeroPeople_ReturnsNegativeOne()
        {
            // Arrange
            var earliestBecomeFriends = new EalieastBecomeFriends();
            int[][] logs = new int[][]
            {
                new int[] { 10, 0, 1 }
            };
            int n = 0;

            // Act
            int result = earliestBecomeFriends.EarliestAcq(logs, n);

            // Assert
            Assert.Equal(-1, result);
        }

        [Fact]
        public void EarliestAcq_AlreadyConnectedFriends_IgnoresRedundantConnections()
        {
            // Arrange - The second log (timestamp 20) is redundant
            var earliestBecomeFriends = new EalieastBecomeFriends();
            int[][] logs = new int[][]
            {
                new int[] { 10, 0, 1 },
                new int[] { 20, 0, 1 }, // Redundant - already friends
                new int[] { 30, 1, 2 }
            };
            int n = 3;

            // Act
            int result = earliestBecomeFriends.EarliestAcq(logs, n);

            // Assert - Everyone becomes friends at timestamp 30
            Assert.Equal(30, result);
        }

        [Fact]
        public void EarliestAcq_MinimumConnectionsNeeded_ReturnsCorrectTimestamp()
        {
            // Arrange - For n people, we need at least n-1 connections
            var earliestBecomeFriends = new EalieastBecomeFriends();
            int[][] logs = new int[][]
            {
                new int[] { 1, 0, 1 },
                new int[] { 2, 1, 2 },
                new int[] { 3, 2, 3 },
                new int[] { 4, 3, 4 }
            };
            int n = 5;

            // Act
            int result = earliestBecomeFriends.EarliestAcq(logs, n);

            // Assert - Everyone becomes friends at timestamp 4
            Assert.Equal(4, result);
        }

        [Fact]
        public void EarliestAcq_ComplexConnectionPattern_ReturnsCorrectTimestamp()
        {
            // Arrange
            var earliestBecomeFriends = new EalieastBecomeFriends();
            int[][] logs = new int[][]
            {
                new int[] { 10, 0, 1 }, // Groups: [0,1], [2], [3], [4]
                new int[] { 20, 2, 3 }, // Groups: [0,1], [2,3], [4]
                new int[] { 30, 1, 4 }, // Groups: [0,1,4], [2,3]
                new int[] { 40, 1, 2 }  // Groups: [0,1,2,3,4] - all connected
            };
            int n = 5;

            // Act
            int result = earliestBecomeFriends.EarliestAcq(logs, n);

            // Assert
            Assert.Equal(40, result);
        }

        [Fact]
        public void EarliestAcq_CyclicConnections_ReturnsCorrectTimestamp()
        {
            // Arrange - Connections form a cycle
            var earliestBecomeFriends = new EalieastBecomeFriends();
            int[][] logs = new int[][]
            {
                new int[] { 1, 0, 1 },
                new int[] { 2, 1, 2 },
                new int[] { 3, 2, 3 },
                new int[] { 4, 3, 0 } // Creates a cycle 0-1-2-3-0
            };
            int n = 4;

            // Act
            int result = earliestBecomeFriends.EarliestAcq(logs, n);

            // Assert - Everyone becomes friends at timestamp 3
            Assert.Equal(3, result);
        }

        [Fact]
        public void EarliestAcq_LargeFriendshipGroup_ReturnsCorrectTimestamp()
        {
            // Arrange - Test with a larger group
            var earliestBecomeFriends = new EalieastBecomeFriends();
            var logs = new List<int[]>();
            
            // Create a star-shaped connection pattern where person 0 connects to everyone else
            for (int i = 1; i < 10; i++)
            {
                logs.Add(new int[] { i, 0, i });
            }
            
            int n = 10;

            // Act
            int result = earliestBecomeFriends.EarliestAcq(logs.ToArray(), n);

            // Assert - Everyone becomes friends at timestamp 9
            Assert.Equal(9, result);
        }

        [Fact]
        public void EarliestAcq_SameTimestamp_ReturnsCorrectTimestamp()
        {
            // Arrange - Multiple friendships formed at the same time
            var earliestBecomeFriends = new EalieastBecomeFriends();
            int[][] logs = new int[][]
            {
                new int[] { 5, 0, 1 },
                new int[] { 5, 1, 2 } // Same timestamp as the first connection
            };
            int n = 3;

            // Act
            int result = earliestBecomeFriends.EarliestAcq(logs, n);

            // Assert - Everyone becomes friends at timestamp 5
            Assert.Equal(5, result);
        }
    }
}
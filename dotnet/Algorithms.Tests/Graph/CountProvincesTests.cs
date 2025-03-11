using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Xunit;
using Algorithms.Core.Graph;

// dotnet test --filter "CountProvincesTests" 
namespace Algorithms.Tests.Graph
{
    public class CountProvincesTests
    {
        [Fact]
        public void FindCircleNum_Example1_Returns2()
        {
            // Arrange
            var countProvinces = new CountProvinces();
            int[][] isConnected = new int[][]
            {
                new int[] { 1, 1, 0 },
                new int[] { 1, 1, 0 },
                new int[] { 0, 0, 1 }
            };

            // Act
            int result = countProvinces.FindCircleNum(isConnected);

            // Assert
            Assert.Equal(2, result);
        }

        [Fact]
        public void FindCircleNum_Example2_Returns3()
        {
            // Arrange
            var countProvinces = new CountProvinces();
            int[][] isConnected = new int[][]
            {
                new int[] { 1, 0, 0 },
                new int[] { 0, 1, 0 },
                new int[] { 0, 0, 1 }
            };

            // Act
            int result = countProvinces.FindCircleNum(isConnected);

            // Assert
            Assert.Equal(3, result);
        }

        [Fact]
        public void FindCircleNum_AllCitiesInOneProvince_Returns1()
        {
            // Arrange
            var countProvinces = new CountProvinces();
            int[][] isConnected = new int[][]
            {
                new int[] { 1, 1, 1 },
                new int[] { 1, 1, 1 },
                new int[] { 1, 1, 1 }
            };

            // Act
            int result = countProvinces.FindCircleNum(isConnected);

            // Assert
            Assert.Equal(1, result);
        }

        [Fact]
        public void FindCircleNum_SingleCity_Returns1()
        {
            // Arrange
            var countProvinces = new CountProvinces();
            int[][] isConnected = new int[][]
            {
                new int[] { 1 }
            };

            // Act
            int result = countProvinces.FindCircleNum(isConnected);

            // Assert
            Assert.Equal(1, result);
        }

        [Fact]
        public void FindCircleNum_ComplexConnections_ReturnsCorrectCount()
        {
            // Arrange
            var countProvinces = new CountProvinces();
            int[][] isConnected = new int[][]
            {
                new int[] { 1, 0, 0, 1, 0 },
                new int[] { 0, 1, 1, 0, 0 },
                new int[] { 0, 1, 1, 0, 0 },
                new int[] { 1, 0, 0, 1, 1 },
                new int[] { 0, 0, 0, 1, 1 }
            };
            // Cities [0,3,4] form one province and [1,2] form another

            // Act
            int result = countProvinces.FindCircleNum(isConnected);

            // Assert
            Assert.Equal(2, result);
        }

        [Fact]
        public void FindCircleNum_IndirectConnections_ReturnsCorrectCount()
        {
            // Arrange
            var countProvinces = new CountProvinces();
            int[][] isConnected = new int[][]
            {
                new int[] { 1, 1, 0, 0, 0 },
                new int[] { 1, 1, 1, 0, 0 },
                new int[] { 0, 1, 1, 1, 0 },
                new int[] { 0, 0, 1, 1, 1 },
                new int[] { 0, 0, 0, 1, 1 }
            };
            // All cities are connected either directly or indirectly

            // Act
            int result = countProvinces.FindCircleNum(isConnected);

            // Assert
            Assert.Equal(1, result);
        }

        [Fact]
        public void FindCircleNum_LargerMatrix_ReturnsCorrectCount()
        {
            // Arrange
            var countProvinces = new CountProvinces();
            int[][] isConnected = new int[10][];
            for (int i = 0; i < 10; i++)
            {
                isConnected[i] = new int[10];
                isConnected[i][i] = 1; // Self-connection
            }

            // Connect cities in groups
            // Group 1: cities 0-2
            isConnected[0][1] = isConnected[1][0] = 1;
            isConnected[1][2] = isConnected[2][1] = 1;

            // Group 2: cities 3-5
            isConnected[3][4] = isConnected[4][3] = 1;
            isConnected[4][5] = isConnected[5][4] = 1;

            // Group 3: cities 6-9
            isConnected[6][7] = isConnected[7][6] = 1;
            isConnected[7][8] = isConnected[8][7] = 1;
            isConnected[8][9] = isConnected[9][8] = 1;

            // Act
            int result = countProvinces.FindCircleNum(isConnected);

            // Assert
            Assert.Equal(3, result);
        }

        [Fact]
        public void FindCircleNum_DiagonalOnesOnly_ReturnsMatrixSize()
        {
            // Arrange
            int size = 5;
            var countProvinces = new CountProvinces();
            int[][] isConnected = new int[size][];

            for (int i = 0; i < size; i++)
            {
                isConnected[i] = new int[size];
                isConnected[i][i] = 1; // Only diagonal entries are 1 (self-connections)
            }

            // Act
            int result = countProvinces.FindCircleNum(isConnected);

            // Assert
            Assert.Equal(size, result); // Each city forms its own province
        }

        [Fact]
        public void FindCircleNum_AsymmetricMatrix_HandlesCorrectly()
        {
            // Arrange
            var countProvinces = new CountProvinces();
            int[][] isConnected = new int[][]
            {
                new int[] { 1, 1, 0 },
                new int[] { 0, 1, 0 }, // Note: [1,0] is 0 but [0,1] is 1
                new int[] { 0, 0, 1 }
            };

            // Act
            int result = countProvinces.FindCircleNum(isConnected);

            // Assert - Should still detect the connection between 0 and 1
            Assert.Equal(2, result);
        }

        [Fact]
        public void FindCircleNum_CircularConnections_Returns1()
        {
            // Arrange
            var countProvinces = new CountProvinces();
            int[][] isConnected = new int[][]
            {
                new int[] { 1, 1, 0, 0 },
                new int[] { 1, 1, 1, 0 },
                new int[] { 0, 1, 1, 1 },
                new int[] { 0, 0, 1, 1 }
            };
            // Cities connected in a circular pattern

            // Act
            int result = countProvinces.FindCircleNum(isConnected);

            // Assert
            Assert.Equal(1, result);
        }
    }
}
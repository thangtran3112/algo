using System.Collections.Generic;
using System.Linq;
using Xunit;
using Algorithms.Core.Graph.Dfs;

namespace Algorithms.Tests.Graph.Dfs
{
    public class CloneGraphDfsTests
    {
        [Fact]
        public void CloneGraph_SingleNodeNoNeighbors_ReturnsCopyWithSameValue()
        {
            // Arrange
            var cloneGraphDfs = new CloneGraphDfs();
            var node = new Node(1);

            // Act
            var result = cloneGraphDfs.CloneGraph(node);

            // Assert
            Assert.NotSame(node, result); // Check it's a different object
            Assert.Equal(1, result.val);
            Assert.Empty(result.neighbors);
        }

        [Fact]
        public void CloneGraph_TwoConnectedNodes_ClonesMaintainingConnections()
        {
            // Arrange
            var cloneGraphDfs = new CloneGraphDfs();
            var node1 = new Node(1);
            var node2 = new Node(2);
            
            node1.neighbors.Add(node2);
            node2.neighbors.Add(node1);

            // Act
            var clonedNode1 = cloneGraphDfs.CloneGraph(node1);

            // Assert
            Assert.NotSame(node1, clonedNode1);
            Assert.Equal(1, clonedNode1.val);
            Assert.Single(clonedNode1.neighbors);
            
            var clonedNode2 = clonedNode1.neighbors[0];
            Assert.NotSame(node2, clonedNode2);
            Assert.Equal(2, clonedNode2.val);
            Assert.Single(clonedNode2.neighbors);
            
            // Check circular reference is maintained
            Assert.Same(clonedNode1, clonedNode2.neighbors[0]);
        }

        [Fact]
        public void CloneGraph_SquareGraph_ClonesMaintainingAllConnections()
        {
            // Arrange - Create a square graph: 1 -- 2
            //                                 |    |
            //                                 4 -- 3
            var cloneGraphDfs = new CloneGraphDfs();
            var node1 = new Node(1);
            var node2 = new Node(2);
            var node3 = new Node(3);
            var node4 = new Node(4);
            
            node1.neighbors.Add(node2);
            node1.neighbors.Add(node4);
            
            node2.neighbors.Add(node1);
            node2.neighbors.Add(node3);
            
            node3.neighbors.Add(node2);
            node3.neighbors.Add(node4);
            
            node4.neighbors.Add(node1);
            node4.neighbors.Add(node3);

            // Act
            var clonedNode1 = cloneGraphDfs.CloneGraph(node1);

            // Assert
            Assert.Equal(1, clonedNode1.val);
            Assert.Equal(2, clonedNode1.neighbors.Count);
            
            // Build map of cloned nodes
            var clonedNodes = new Dictionary<int, Node>();
            CollectNodes(clonedNode1, clonedNodes);
            
            // Check we have 4 nodes
            Assert.Equal(4, clonedNodes.Count);
            
            // Check all nodes are different objects from originals
            Assert.NotSame(node1, clonedNodes[1]);
            Assert.NotSame(node2, clonedNodes[2]);
            Assert.NotSame(node3, clonedNodes[3]);
            Assert.NotSame(node4, clonedNodes[4]);
            
            // Check connections are correct
            Assert.Equal(2, clonedNodes[1].neighbors.Count);
            Assert.Contains(clonedNodes[1].neighbors, n => n.val == 2);
            Assert.Contains(clonedNodes[1].neighbors, n => n.val == 4);
            
            Assert.Equal(2, clonedNodes[2].neighbors.Count);
            Assert.Contains(clonedNodes[2].neighbors, n => n.val == 1);
            Assert.Contains(clonedNodes[2].neighbors, n => n.val == 3);
            
            Assert.Equal(2, clonedNodes[3].neighbors.Count);
            Assert.Contains(clonedNodes[3].neighbors, n => n.val == 2);
            Assert.Contains(clonedNodes[3].neighbors, n => n.val == 4);
            
            Assert.Equal(2, clonedNodes[4].neighbors.Count);
            Assert.Contains(clonedNodes[4].neighbors, n => n.val == 1);
            Assert.Contains(clonedNodes[4].neighbors, n => n.val == 3);
        }

        [Fact]
        public void CloneGraph_ComplexGraph_ClonesMaintainingStructure()
        {
            // Arrange
            var cloneGraphDfs = new CloneGraphDfs();
            
            // Create a more complex graph
            var nodes = new List<Node>();
            for (int i = 1; i <= 5; i++)
            {
                nodes.Add(new Node(i));
            }
            
            // Node 1 connects to 2, 3, 4
            nodes[0].neighbors.Add(nodes[1]); // 1->2
            nodes[0].neighbors.Add(nodes[2]); // 1->3
            nodes[0].neighbors.Add(nodes[3]); // 1->4
            
            // Node 2 connects to 1, 5
            nodes[1].neighbors.Add(nodes[0]); // 2->1
            nodes[1].neighbors.Add(nodes[4]); // 2->5
            
            // Node 3 connects to 1, 4
            nodes[2].neighbors.Add(nodes[0]); // 3->1
            nodes[2].neighbors.Add(nodes[3]); // 3->4
            
            // Node 4 connects to 1, 3, 5
            nodes[3].neighbors.Add(nodes[0]); // 4->1
            nodes[3].neighbors.Add(nodes[2]); // 4->3
            nodes[3].neighbors.Add(nodes[4]); // 4->5
            
            // Node 5 connects to 2, 4
            nodes[4].neighbors.Add(nodes[1]); // 5->2
            nodes[4].neighbors.Add(nodes[3]); // 5->4

            // Act
            var clonedNode1 = cloneGraphDfs.CloneGraph(nodes[0]);

            // Assert
            var clonedNodes = new Dictionary<int, Node>();
            CollectNodes(clonedNode1, clonedNodes);
            
            // Check we have all 5 nodes
            Assert.Equal(5, clonedNodes.Count);
            
            // Check connections
            Assert.Equal(3, clonedNodes[1].neighbors.Count);
            Assert.Contains(clonedNodes[1].neighbors, n => n.val == 2);
            Assert.Contains(clonedNodes[1].neighbors, n => n.val == 3);
            Assert.Contains(clonedNodes[1].neighbors, n => n.val == 4);
            
            Assert.Equal(2, clonedNodes[2].neighbors.Count);
            Assert.Contains(clonedNodes[2].neighbors, n => n.val == 1);
            Assert.Contains(clonedNodes[2].neighbors, n => n.val == 5);
            
            Assert.Equal(2, clonedNodes[3].neighbors.Count);
            Assert.Contains(clonedNodes[3].neighbors, n => n.val == 1);
            Assert.Contains(clonedNodes[3].neighbors, n => n.val == 4);
            
            Assert.Equal(3, clonedNodes[4].neighbors.Count);
            Assert.Contains(clonedNodes[4].neighbors, n => n.val == 1);
            Assert.Contains(clonedNodes[4].neighbors, n => n.val == 3);
            Assert.Contains(clonedNodes[4].neighbors, n => n.val == 5);
            
            Assert.Equal(2, clonedNodes[5].neighbors.Count);
            Assert.Contains(clonedNodes[5].neighbors, n => n.val == 2);
            Assert.Contains(clonedNodes[5].neighbors, n => n.val == 4);
        }

        [Fact]
        public void CloneGraph_DeepCopyTest_OriginalModificationDoesNotAffectClone()
        {
            // Arrange
            var cloneGraphDfs = new CloneGraphDfs();
            var node1 = new Node(1);
            var node2 = new Node(2);
            
            node1.neighbors.Add(node2);
            node2.neighbors.Add(node1);
            
            // Act
            var clonedNode1 = cloneGraphDfs.CloneGraph(node1);
            
            // Modify original graph
            var node3 = new Node(3);
            node1.neighbors.Add(node3);
            node3.neighbors.Add(node1);
            
            // Assert
            Assert.Equal(2, node1.neighbors.Count);  // Original now has 2 neighbors
            Assert.Single(clonedNode1.neighbors);  // Clone still has 1 neighbor
            Assert.Equal(2, clonedNode1.neighbors[0].val);  // And it's node 2
        }
        
        // Helper method to collect all nodes in a graph into a dictionary by value
        private void CollectNodes(Node node, Dictionary<int, Node> visited)
        {
            if (visited.ContainsKey(node.val))
                return;
                
            visited[node.val] = node;
            
            foreach (var neighbor in node.neighbors)
            {
                CollectNodes(neighbor, visited);
            }
        }
    }
}
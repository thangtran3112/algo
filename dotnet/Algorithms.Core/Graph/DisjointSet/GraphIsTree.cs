using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Algorithms.Core.Graph.DisjointSet
{
    public class GraphIsTree
    {
        public bool ValidTree(int n, int[][] edges) {
            if (n == 0 || edges.Length != n - 1) return false; // A tree must have exactly n-1 edges
            if (n == 1 && edges.Length == 0) return true; // A single node with no edges is a tree
            OpttimizedUnionFind uf = new OpttimizedUnionFind(n);

            // Connect and check for cycles
            foreach (var edge in edges)
            {
                if (!uf.Union(edge[0], edge[1]))
                {
                    return false; // Cycle detected
                }
            }

            return uf.CountRoots() == 1; // Check if all nodes are connected
        }

        public GraphIsTree()
        {

        }
    }
}
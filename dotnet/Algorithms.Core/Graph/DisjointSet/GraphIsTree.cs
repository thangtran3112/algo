using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Algorithms.Core.Graph.DisjointSet
{
    public class GraphIsTree
    {
        private class AdvancedUnionFind
        {
            int[] parent;
            int[] rank;
            int size;

            public AdvancedUnionFind(int size)
            {
                this.size = size;
                parent = new int[size];
                rank = new int[size];
                for (int i = 0; i < size; i++)
                {
                    parent[i] = i;
                    rank[i] = 0;
                }
            }

            public int Find(int x)
            {
                if (parent[x] != x)
                {
                    parent[x] = Find(parent[x]); // Path compression
                }
                return parent[x];
            }

            public bool UnionAndCheck(int x, int y)
            {
                int rootX = Find(x);
                int rootY = Find(y);

                if (rootX == rootY) 
                {
                    return false; // Cycle detected
                }
                if (rank[rootX] > rank[rootY]) {
                    parent[rootY] = rootX;
                    return true;
                }
                if (rank[rootX] < rank[rootY]) {
                    parent[rootX] = rootY;
                    return true;
                }   
                parent[rootY] = rootX;
                rank[rootX]++;
                return true;
            }

            public int CountRoots()
            {
                int rootCount = 0;
                // rootCount = parent.Select(x => Find(x)).Distinct().Count(); // This is not good for performance
                for (int i = 0; i < size; i++)
                {
                    if (parent[i] == i)
                    {
                        rootCount++;
                    }
                }
                return rootCount;
            }
        }

        public bool ValidTree(int n, int[][] edges) {
            if (n == 0 || edges.Length != n - 1) return false; // A tree must have exactly n-1 edges
            if (n == 1 && edges.Length == 0) return true; // A single node with no edges is a tree
            AdvancedUnionFind uf = new AdvancedUnionFind(n);

            // Connect and check for cycles
            foreach (var edge in edges)
            {
                if (!uf.UnionAndCheck(edge[0], edge[1]))
                {
                    return false; // Cycle detected
                }
            }

            return uf.CountRoots() == 1; // Check if all nodes are connected
        }
    }
}
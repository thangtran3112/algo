using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Algorithms.Core.Graph.DisjointSet
{
     public class OpttimizedUnionFind
    {
        int[] parent;
        int[] rank;
        int size;

        int rootCount;

        public OpttimizedUnionFind(int size)
        {
            this.size = size;
            parent = new int[size];
            rank = new int[size];
            rootCount = size; // Initialize root count to the number of elements
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

        public bool Union(int x, int y)
        {
            int rootX = Find(x);
            int rootY = Find(y);

            if (rootX == rootY) 
            {
                return false; // already connected
            }
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }

            // whenever there is successful connection, we decrease the root count by 1
            rootCount--;

            return true;
        }

        public int CountRoots()
        {
            return rootCount;
        }

        // this is not optimized, it can be done in O(1) time by keeping track of the 
        // number of roots
        // public int CountRoots()
        // {
        //     int rootCount = 0;
        //     // rootCount = parent.Select(x => Find(x)).Distinct().Count(); // This is not good for performance
        //     for (int i = 0; i < size; i++)
        //     {
        //         if (parent[i] == i)
        //         {
        //             rootCount++;
        //         }
        //     }
        //     return rootCount;
        // }
    }

}
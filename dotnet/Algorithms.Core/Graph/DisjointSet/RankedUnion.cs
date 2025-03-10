using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Algorithms.Core.Graph.DisjointSet
{
    public class RankedUnion
    {
        private int[] _root;
        private int[] _rank;

        public RankedUnion(int size)
        {
            _root = new int[size];
            _rank = new int[size];

            // Initialize each element to be its own root and set rank to 1
            for (int i = 0; i < size; i++)
            {
                _root[i] = i;
                _rank[i] = 1;
            }
        }

        public int Find(int x)
        {
            if (_root[x] != x)
            {
                _root[x] = Find(_root[x]); // Path compression
            }
            return _root[x];
        }

        public void Union(int x, int y)
        {
            int rootX = Find(x);
            int rootY = Find(y);

            if (rootX != rootY)
            {
                if (_rank[rootX] > _rank[rootY])
                {
                    _root[rootY] = rootX;
                    return;
                }
                if (_rank[rootX] < _rank[rootY])
                {
                    _root[rootX] = rootY;
                    return;
                }

                // Ranks are equal if we reach here
                _root[rootY] = rootX;
                _rank[rootX] += 1; // Increase the rank of the new root
            }
        }

        public bool Connected(int x, int y)
        {
            return Find(x) == Find(y);
        }
    }
}
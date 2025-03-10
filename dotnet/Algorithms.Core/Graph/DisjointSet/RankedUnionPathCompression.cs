using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Algorithms.Core.Graph.DisjointSet
{
    public class RankedUnionPathCompression
    {
        private readonly int[] _root;
        private readonly int[] _rank;

        public RankedUnionPathCompression(int size)
        {
            _root = new int[size];
            _rank = new int[size];

            for (int i = 0; i < size; i++)
            {
                _root[i] = i;
                _rank[i] = 0;
            }
        }

        public int Find(int x)
        {
            if (_root[x] != x)
            {
                _root[x] = Find(_root[x]);
            }
            // Some ranks may become obsolete so they are not updated.
            // This is not a problem as long as we only care about the ranks of the roots.
            return _root[x];
        }

        public void Union(int x, int y)
        {
            int rootX = Find(x);
            int rootY = Find(y);

            if (rootX != rootY)
            {
                if (_rank[rootX] < _rank[rootY])
                {
                    _root[rootX] = rootY;
                    return;
                }
                if (_rank[rootX] > _rank[rootY])
                {
                    _root[rootY] = rootX;
                    return;
                }

                // Ranks are equal, so make one root the parent of the other and increment its rank
                _root[rootY] = rootX;
                _rank[rootX]++;
            }
        }

        public bool Connected(int x, int y)
        {
            return Find(x) == Find(y);
        }
    }
}
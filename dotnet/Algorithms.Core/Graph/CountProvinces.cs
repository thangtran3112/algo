using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
/*
Link: https://leetcode.com/problems/number-of-provinces/description/
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3 */
namespace Algorithms.Core.Graph
{
    public class CountProvinces
    {
        private class UnionFind
        {
            int[] _root;
            int[] _rank;

            public UnionFind(int size)
            {
                _root = new int[size];
                _rank = new int[size];

                for (int i = 0; i < size; i++)
                {
                    _root[i] = i;
                    _rank[i] = 1;
                }
            }

            public int Find(int x) => _root[x] == x ? x : (_root[x] = Find(_root[x]));

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

                    _root[rootY] = rootX;
                    _rank[rootX]++;
                }
            }

            public int SetCount()
            {
                // Shorter option:
                // return _root.Select(x, i) => Find(i)).Distinct().Count();
                HashSet<int> set = new HashSet<int>();
                for (int i = 0; i < _root.Length; i++)
                {
                    set.Add(Find(i));
                }
                return set.Count;
            }
        }

        public int FindCircleNum(int[][] isConnected)
        {
            int n = isConnected.Length;
            UnionFind uf = new UnionFind(n);

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (isConnected[i][j] == 1)
                    {
                        uf.Union(i, j);
                    }
                }
            }

            return uf.SetCount();
        }
    }
}
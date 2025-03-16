// https://leetcode.com/problems/all-paths-from-source-to-target/
/***
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
***/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
namespace Algorithms.Core.Graph.Dfs
{
    public class AllPaths
    {
        public IList<IList<int>> AllPathsSourceTarget(int[][] graph) 
        {
            int n = graph.Length;
            IList<IList<int>> result = new List<IList<int>>();
            List<int> path = new List<int>();
            int destination = n - 1;
            HashSet<int> visited = new HashSet<int>();

            void internal_backtrack(int node)
            {
                visited.Add(node);
                path.Add(node);
                if (node == destination)
                {
                    // clone and copy the path to result
                    result.Add(new List<int>(path));
                }
                else
                {
                    foreach (int neighbor in graph[node])
                    {
                        if (!visited.Contains(neighbor))
                        {
                            internal_backtrack(neighbor);
                        }
                    }
                }
                // backtracking
                path.RemoveAt(path.Count - 1);
                visited.Remove(node);
            }
            // start from node 0
            internal_backtrack(0);
            return result;
        }
    }
}
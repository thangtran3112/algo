using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Algorithms.Core.Graph.Dfs
{
    public class Node {
        public int val;
        public IList<Node> neighbors;

        public Node() {
            val = 0;
            neighbors = new List<Node>();
        }

        public Node(int _val) {
            val = _val;
            neighbors = new List<Node>();
        }

        public Node(int _val, List<Node> _neighbors) {
            val = _val;
            neighbors = _neighbors;
        }
    }
    public class CloneGraphDfs
    {
        public Node CloneGraph(Node node) {
            if (node == null) {
                return node;
            }
            Dictionary<Node, Node> cloneMap = new Dictionary<Node, Node>();
            
            Node Dfs(Node cur) {
                if (cloneMap.ContainsKey(cur)) {
                    return cloneMap[cur];
                }
                var cloneNode = new Node(cur.val, new List<Node>());
                cloneMap[cur] = cloneNode;
                foreach (var neighbor in cur.neighbors) {
                    cloneNode.neighbors.Add(Dfs(neighbor));
                }
                return cloneNode;
            }

            return Dfs(node);
        }
    }
}
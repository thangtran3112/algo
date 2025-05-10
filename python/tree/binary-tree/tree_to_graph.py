# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree
"""
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
"""
# Definition for a binary tree node.
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionConvertToGraph:
    # convert the tree to an undirected graph
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_graph(node, parent):
            if node and parent:
                graph[node].append(parent)
                graph[parent].append(node)
            if node.left:
                build_graph(node.left, node)
            if node.right:
                build_graph(node.right, node)
        build_graph(root, None)

        result = []
        seen = set()

        # dfs from target to distance of k
        def dfs(node, distance):
            if not node:
                return
            if distance > k:
                # stop moving forward
                return
            seen.add(node)
            if distance == k:
                result.append(node.val)
                return
            # case: distance < k
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor, distance + 1)

        dfs(target, 0)
        return result
    
class SolutionParentPointer:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Recursively add a parent pointer to each node.
        def add_parent(cur, parent):
            if cur:
                cur.parent = parent
                add_parent(cur.left, cur)
                add_parent(cur.right, cur)

        add_parent(root, None)

        answer = []
        visited = set()

        def dfs(cur, distance):
            if not cur or cur in visited:
                return
            visited.add(cur)
            if distance == 0:
                answer.append(cur.val)
                return
            dfs(cur.parent, distance - 1)
            dfs(cur.left, distance - 1)
            dfs(cur.right, distance - 1)

        dfs(target, k)


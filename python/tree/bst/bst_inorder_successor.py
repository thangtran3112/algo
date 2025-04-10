# https://leetcode.com/problems/inorder-successor-in-bst/description/
"""
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
All Nodes will have unique values.
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
1. When p.val >= node.val that implies we can safely discard the left subtree since all the nodes there including the current node have values less than p
2. When we found the first root, where root.val > p.val, the successor will be within this subtree. Try going left as much as possible to find the successor
"""
class Solution:
    #            4
    #          /    \
    #        3      8
    #       /     /   \
    #      1     5    10
    #                 /
    #                9
    # Example:
    # 1st round: root = 4, root value < p=8, discard left tree of 4
    # 2nd round: root = 8, root value >= p=8, going right
    # 3rd round: root = 10, P < root value, now keep going left
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        while root:
            if p.val >= root.val:
                # entire left tree can be discard
                root = root.right
            else:
                # all nodes of this left path, will have root.val > p.val
                # keep moving left to find the successor
                successor = root
                root = root.left

        return successor

class SolutionEarlyExit:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        found = [False]
        result = []

        def inorder(node: TreeNode):
            if node.left:
                inorder(node.left)
            if found[0] is True:
                result.append(node)
                found[0] = False
                # early exit
                return
            if node == p:
                found[0] = True
            if node.right:
                inorder(node.right)

        inorder(root)
        return result[0] if len(result) > 0 else None

# Build the inorder array, and look for successor
class SolutionNotOptimize:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        result = []

        def inorder(node: TreeNode):
            if node.left:
                inorder(node.left)
            result.append(node)

            if node.right:
                inorder(node.right)

        inorder(root)

        for i in range(0, len(result)-1):
            if result[i] == p:
                return result[i+1]
        return None
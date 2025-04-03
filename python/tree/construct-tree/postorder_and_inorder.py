# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/editorial/

"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # [9, 15, 7,20, 3] -> last element 3 is root
        # index of 3 in inorder is 1. Left subtree-inorder [9], right subtree-inorder [15, 20, 7]
        # left subtree postorder []. right subtree postorder is [9, 15, 7, 20]

        # Build a map of value to index from inorder traversal:
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        def dfs(inorder_left, inorder_right) -> Optional[TreeNode]:
            if inorder_left > inorder_right:
                return None

            # pop and take the last element in postorder as root
            val = postorder.pop()
            root = TreeNode(val)

            index = inorder_map[val]

            # keep building the right subtree first, until the bottom node
            root.right = dfs(index + 1, inorder_right)

            # build the left subtree, after done building all right subtree
            root.left = dfs(inorder_left, index - 1)

            return root

        return dfs(0, len(inorder) - 1)

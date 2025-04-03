# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # reversing preorder array, so we can just pop to get next root at the end
        # [3,9,20,15,7] -> reverse -> [7,15,20,9,3]. Roots will be 3, 9, 20, pop() from the end
        preorder.reverse()

        inorder_map = { value : i for i, value in enumerate(inorder) }

        def dfs(inorder_left: int, inorder_right: int):
            if inorder_left > inorder_right:
                return None
            root_val = preorder.pop()
            index = inorder_map[root_val]
            root = TreeNode(root_val)

            # keep building the left tree first
            root.left = dfs(inorder_left, index - 1)

            # After building all left tree
            root.right = dfs(index + 1, inorder_right)
            return root
        return dfs(0, len(inorder) - 1)

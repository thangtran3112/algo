# https://leetcode.com/problems/count-univalue-subtrees/description/
"""
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

 

Example 1:


Input: root = [5,1,5,5,5,null,5]
Output: 4
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6
 

Constraints:

The number of the node in the tree will be in the range [0, 1000].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(node) -> bool:
            # base case, node is None
            if not node:
                return True

            # base case, leave node
            if not node.left and not node.right:
                result[0] += 1
                return True

            is_left = dfs(node.left)
            is_right = dfs(node.right)
            if is_left and is_right:
                is_uni = False
                # both left and right exist
                if node.left and node.right:
                    is_uni = node.val == node.left.val and node.val == node.right.val
                elif node.left:
                    # only left exist
                    is_uni = node.val == node.left.val
                else:
                    # only right exist
                    is_uni = node.val == node.right.val
                if is_uni:
                    result[0] += 1
                return is_uni

        dfs(root)
        return result[0]

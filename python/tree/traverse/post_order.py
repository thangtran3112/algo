# left -> right -> root
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# left -> right -> root
class SolutionRecursive:
    # left -> right -> root
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return []

        def helper(node: Optional[TreeNode]):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            result.append(node.val)

        helper(root)

        return result

# doing root -> right -> left and then reverse the result
class Solution:
    # left -> right -> root
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []

        stack = [root]
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        result.reverse()
        return result

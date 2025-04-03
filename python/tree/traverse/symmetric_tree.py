# https://leetcode.com/problems/symmetric-tree/description/
"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Level traversal with 2 queues
class SolutionTwoQueue:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q1 = deque()
        q2 = deque()
        q1.append(root)
        q2.append(root)

        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()
            if n1.val != n2.val:
                return False
            if n1.left:
                if not n2.right:
                    return False
                q1.append(n1.left)
                q2.append(n2.right)
            if n1.right:
                if not n2.left:
                    return False
                q1.append(n1.right)
                q2.append(n2.left)

        return True

# Recursive traversing
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(x, y):
            if not x and not y:
                return True
            if (x and not y) or (y and not x):
                return False
            if x.val != y.val:
                return False

            if not isMirror(x.left, y.right):
                return False
            if not isMirror(x.right, y.left):
                return False
            return True
        return isMirror(root, root)



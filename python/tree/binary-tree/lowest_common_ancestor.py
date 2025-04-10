# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionRecursive:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            # since p, and q will never be in the same branch
            return root
        elif left is None and right:
            return right
        elif right is None and left:
            return left
        else:
            return None
        
class SolutionTreeFlatten:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node, val, path):
            if node is None:
                return False
            if node.val == val:
                path.append(node)
                return True
            if find(node.left, val, path) or find(node.right, val, path):
                path.append(node)
                return True
            return False

        # populate all parents of p, and q
        path_p, path_q = [], []
        find(root, p.val, path_p)
        find(root, q.val, path_q)

        # keep going until the ancestors are diverging
        i = len(path_p) - 1
        j = len(path_q) - 1
        while i >= 0 and j >= 0 and path_p[i] == path_q[j]:
            i -= 1
            j -= 1
        return path_p[i + 1]

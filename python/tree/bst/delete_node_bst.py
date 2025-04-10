# https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1025/
"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
1. If the target node has no child, we can simply remove the node.
2. If the target node has one child, we can use its child to replace itself.
3. If the target node has two children, replace the node with its in-order successor or predecessor node and delete that node.
"""
class Solution:
    #        50
    #       /  \
    #     30    70
    #    / \   /  \
    #  20  40 60  80
    #             /
    #            75
    # only find successor when this node has children. This does work for leaf nodes
    def findSuccessor(self, root):
        """
        In a BST, it's the leftmost node in the right subtree.
        For example, node = 70, successor = 75
        """
        curr = root.right
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root, key):
        if not root:
            return None
        if root.val < key:
            # find and delete from right subtree 
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # Node value equals to key
            if not root.left:
                # connect the right tree to previous node. Also means, deleting root
                return root.right
            if not root.right:
                # connect the left tree to previous node.
                return root.left

            # having both left and right children
            successor = self.findSuccessor(root)
            root.val = successor.val
            # delete successor after copying the value of successor
            root.right = self.deleteNode(root.right, successor.val)

        # allow previous node to connect to this node
        return root

# https://leetcode.com/problems/diameter-of-binary-tree/description/
"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path_with_root(node) -> int:
            nonlocal diameter
            # base case
            if not node:
                return 0
            longest_left_path = longest_path_with_root(node.left)
            longest_right_path = longest_path_with_root(node.right)
            diameter_with_root_node = longest_left_path + longest_right_path + 1
            diameter = max(diameter, diameter_with_root_node)

            return max(longest_left_path + 1, longest_right_path + 1)

        longest_path_with_root(root)
        return diameter - 1

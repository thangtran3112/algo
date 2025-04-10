# https://leetcode.com/problems/populating-next-right-pointers-in-each-TreeNode/description/
"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode *next;
}
Populate each next pointer to point to its next right TreeNode. If there is no next right TreeNode, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right TreeNode, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of TreeNodes in the tree is in the range [0, 212 - 1].
-1000 <= TreeNode.val <= 1000
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root:
            return root
        
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                # Connect 2 children of same parent
                head.left.next = head.right

                # Connect 2 TreeNodes with different parents
                if head.next:
                    head.right.next = head.next.left
                
                # progress to next head
                head = head.next
            
            # move to next level
            leftmost = leftmost.left
        return root

class SolutionBFS:
    def connect(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        # using BFS
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            prev = None

            # iterating by layer
            for i in range(size):
                TreeNode = queue.popleft()
                if prev:
                    prev.next = TreeNode
                if TreeNode.left:
                    queue.append(TreeNode.left)
                if TreeNode.right:
                    queue.append(TreeNode.right)
                prev = TreeNode

        return root
                


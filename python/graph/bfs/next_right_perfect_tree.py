"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""
import collections
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return root
        # this is a perfect tree without any cycles so we do not need visited array
        # next node will always be the BFS next node in queue
        queue = collections.deque()
        # keep track of the rank of each node, so if the rank go up, the next node is null
        queue.append([root, 0])
        prev_tuple = None
        while queue:
            cur_tuple = queue.popleft()
            [cur_node, cur_rank] = cur_tuple
            if prev_tuple:
                [prev_node, prev_rank] = prev_tuple
                if prev_rank == cur_rank:
                    # same rank, can connect
                    prev_node.next = cur_node
                else:
                    # next node in queue has different rank
                    prev_node.next = None
            prev_tuple = cur_tuple
            if cur_node.left:
                # there must be right child too, as this is a perfect TreeNode
                queue.append([cur_node.left, cur_rank + 1])
                queue.append([cur_node.right, cur_rank + 1])

        return root
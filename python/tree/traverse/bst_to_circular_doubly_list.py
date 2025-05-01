# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/
"""
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

 

Example 1:



Input: root = [4,2,5,1,3]


Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

Example 2:

Input: root = [2,1,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
All the values of the tree are unique.
"""
from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        # do an inorder traversing, mark node in a HashMap
        dic = {}  # { 1: Node1, 2: Node2 }
        inorder_arr = []  # [1, 2, 3, 4, 5]

        def inorder(node):
            # base case
            if not node:
                return
            # left -> root -> right
            inorder(node.left)
            dic[node.val] = node
            inorder_arr.append(node.val)
            inorder(node.right)

        inorder(root)
        # rebuild the connection between nodes, following the order of inorder_arr
        first_element = dic[inorder_arr[0]]
        n = len(inorder_arr)
        # left = prev, right = next
        for i in range(n - 1):
            curr_val = inorder_arr[i]
            node = dic[curr_val]
            next_val = inorder_arr[i + 1]
            next_node = dic[next_val]
            node.right = next_node
            next_node.left = node

        # connecting first and last elements
        last_element = dic[inorder_arr[n - 1]]
        last_element.right = first_element
        first_element.left = last_element

        return first_element

class SolutionInorderDFS:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        first, last = None, None

        def inorder(node):
            nonlocal first, last
            if not node:
                return

            inorder(node.left)

            if last:
                # Link previous node (last) with current one (node)
                last.right = node
                node.left = last
            else:
                # This is the smallest node (leftmost), becomes head
                first = node

            last = node  # Update last to current

            inorder(node.right)

        inorder(root)
        # Close circular doubly linked list
        first.left = last
        last.right = first

        return first
    
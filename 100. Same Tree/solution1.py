# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        q1 = deque()
        q1.append(p)
        q2 = deque()
        q2.append(q)
        
        while q1 or q2:
            current_node1 = q1.popleft()
            current_node2 = q2.popleft()
            if current_node1 == None and current_node2 == None:
                continue
            elif current_node1 == None or current_node2 == None or current_node1.val != current_node2.val:
                return False
            q1.append(current_node1.left)
            q1.append(current_node1.right)
            q2.append(current_node2.left)
            q2.append(current_node2.right)
            
        return True
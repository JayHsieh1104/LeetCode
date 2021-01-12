"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node: 'Node') -> None:
            nonlocal first_node, last_node
            if node == None:
                return
            
            helper(node.left)
            
            if last_node:
                node.left = last_node
                last_node.right = node
            else:
                first_node = node
            last_node = node
            
            helper(node.right)
        
        
        if root == None:
            return None
            
        first_node, last_node = None, None
        helper(root)
        first_node.left = last_node
        last_node.right = first_node
        
        return first_node
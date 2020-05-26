# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.parentDict = {root: None}
        self.seen = set()
        self.stack = [root]
        
        while p not in self.parentDict or q not in self.parentDict:
            current_node = self.stack.pop()
            if current_node.right != None:
                self.parentDict[current_node.right] = current_node
                self.stack.append(current_node.right)
            if current_node.left != None:
                self.parentDict[current_node.left] = current_node
                self.stack.append(current_node.left)
            
        while p:
            self.seen.add(p)
            p = self.parentDict[p]
            
        
        while q not in self.seen:
            q = self.parentDict[q]
        
        return q
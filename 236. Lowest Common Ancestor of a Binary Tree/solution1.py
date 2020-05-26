# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def __init__(self):
            self.ans = None
        
        def recurse_tree(current_node: 'TreeNode') -> 'boolean':
            if current_node == None:
                return False
            
            mid = current_node.val == p.val or current_node.val == q.val
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            
            if mid + left + right == 2:
                self.ans = current_node
            
            return mid or left or right
        
        recurse_tree(root)
        return self.ans            
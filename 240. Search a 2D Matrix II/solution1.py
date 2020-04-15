# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(root, lower, upper) -> bool:
            if root == None:
                return True
            if root.val >= upper or root.val <= lower:
                return False    
            if helper(root.right, root.val, upper) == False:
                return False    
            if helper(root.left, lower, root.val) == False:
                return False
            return True
        
        return helper(root, float('-inf'), float('inf'))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(i: TreeNode, j: TreeNode) -> bool:
            if i == None and j == None:
                return True
            elif i == None or j == None or i.val != j. val:
                return False
            else:
                return isSame(i.left, j.left) and isSame(i.right, j.right)
        
        if s == None:
            return False
        elif isSame(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(s: TreeNode, t: TreeNode) -> bool:
            if s == None and t == None:
                return True
            elif s == None or t == None:
                return False
            else:
                return s.val == t.val and isMirror(s.left, t.right) and isMirror(s.right, t.left)
            
        return isMirror(root, root)
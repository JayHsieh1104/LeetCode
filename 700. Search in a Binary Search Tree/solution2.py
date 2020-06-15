# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root != None and root.val != val:
            if root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
        return root
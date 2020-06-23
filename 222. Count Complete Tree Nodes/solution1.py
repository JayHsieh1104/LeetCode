# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = []
        count = 0
        stack.append(root)
        
        while stack:
            count += 1
            curr = stack.pop()
            if curr.right != None:
                stack.append(curr.right)
            if curr.left != None:
                stack.append(curr.left)
        return count
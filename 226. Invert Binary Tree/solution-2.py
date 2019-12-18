# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.right, node.left = node.left, node.right
                stack += node.right, node.left
        return root
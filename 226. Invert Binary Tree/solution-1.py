# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            """
			if you write the following code, this will cause wrong answer 
			because the two node should exchange at the same time
				root.left = self.invertTree(root.right)
				root.right = self.invertTree(root.left)
            """
        return root
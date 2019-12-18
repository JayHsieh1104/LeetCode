# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                node.right, node.left = node.left, node.right
                queue += node.right, node.left
        return root
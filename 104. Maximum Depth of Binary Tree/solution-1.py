# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        stack = []
        if root is not None:
            stack.append((root, 1))
        
        max_depth = 0
        while stack != []:
            current_node, current_depth = stack.pop()
            if current_node is not None:
                stack.append((current_node.left, current_depth + 1))
                stack.append((current_node.right, current_depth + 1))
                max_depth = max(max_depth, current_depth)
        
        return max_depth
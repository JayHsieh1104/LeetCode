# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def has_target(curr_node):
            if curr_node == None:
                return False

            mid = curr_node == p or curr_node == q
            left = has_target(curr_node.left)
            right = has_target(curr_node.right)

            if mid + left + right == 2:
                self.ans = curr_node

            return mid or left or right

        has_target(root)
        return self.ans

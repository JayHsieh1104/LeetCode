# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(node):
            nonlocal max_sum
            if node == None:
                return 0
            
            left_gain = max(0, max_gain(node.left))
            right_gain = max(0, max_gain(node.right))
            max_sum = max(max_sum, left_gain + right_gain + node.val)
            
            return node.val + max(left_gain, right_gain)
            
        max_sum = -math.inf
        max_gain(root)
        return max_sum
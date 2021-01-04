# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        
        stack = [(root, 0)]
        
        while stack:
            curr_node, curr_sum = stack.pop()
            curr_sum += curr_node.val
            if curr_node.left == curr_node.right == None and curr_sum == sum:
                return True
            if curr_node.left:
                stack.append((curr_node.left, curr_sum))
            if curr_node.right:
                stack.append((curr_node.right, curr_sum))
        
        return False

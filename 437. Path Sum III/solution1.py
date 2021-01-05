# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def helper(root, curr_sum):
            nonlocal counter
            
            curr_sum += root.val
            counter += prefix_sum[curr_sum - sum]
            prefix_sum[curr_sum] += 1
            if root.left:
                helper(root.left, curr_sum)
            if root.right:
                helper(root.right, curr_sum)
            prefix_sum[curr_sum] -= 1
            
        if root == None:
            return 0
        
        prefix_sum = collections.defaultdict(int)
        prefix_sum[0] = 1
        counter = 0    
        
        helper(root, 0)
        
        return counter
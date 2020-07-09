# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(left_pos = 0, right_pos = len(inorder)):
            if left_pos == right_pos:
                return None
            
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            
            index = idx_map[root_val]
            
            self.pre_idx += 1
            root.left = helper(left_pos, index)
            root.right = helper(index+1, right_pos)
            return root
            
        self.pre_idx = 0
        idx_map = {val: i for i, val in enumerate(inorder)}
        return helper()
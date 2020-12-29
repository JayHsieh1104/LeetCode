# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def depth(node):
            if node == None:
                return 0
            else:
                left_subtree_length = depth(node.left)
                right_subtree_length = depth(node.right)
                if left_subtree_length + right_subtree_length > self.ans:
                    self.ans = left_subtree_length + right_subtree_length
                return max(left_subtree_length, right_subtree_length) + 1
        
        depth(root)
        return self.ans
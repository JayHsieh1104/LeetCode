# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        min_max_col_in_level = {}
        stack = [(root, 0, 0)]
        
        while stack:
            current_node, current_level, current_col = stack.pop()
            if current_level in min_max_col_in_level:
                if current_col < min_max_col_in_level[current_level][0]:
                    min_max_col_in_level[current_level][0] = current_col
                elif current_col > min_max_col_in_level[current_level][1]:
                    min_max_col_in_level[current_level][1] = current_col
            else:
                min_max_col_in_level[current_level] = [current_col, current_col]
            
            if current_node.left:
                stack.append((current_node.left, current_level+1, 2*current_col))
            if current_node.right:
                stack.append((current_node.right, current_level+1, 2*current_col+1))
                
        max_width = [j[1] - j[0] for i, j in min_max_col_in_level.items()]
        return max(max_width)+1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if node == None:
                return (None, 0)
            else:
                left_child, right_child = dfs(node.left), dfs(node.right)
                if left_child[1] == right_child[1]:
                    return (node, left_child[1] + 1)
                elif left_child[1] > right_child[1]:
                    return (left_child[0], left_child[1] + 1)
                elif right_child[1] > left_child[1]:
                    return (right_child[0], right_child[1] + 1)

        return dfs(root)[0]
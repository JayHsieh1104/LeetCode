# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        depth = {None: -1}
        def dfs(node, parent = None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        
        max_depth = max(depth.values())
        
        def answer(node):
            if node == None or depth[node] == max_depth:
                return node
            
            left_child, right_child = answer(node.left), answer(node.right)
            if left_child and right_child:
                return node
            elif left_child:
                return left_child
            elif right_child:
                return right_child
            else:
                return None
            
        return answer(root)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        rightmost_value_at_depth = dict() # dictionary for storing (level, rightmost value)
        max_depth = -1
        
        stack = [(root, 0)] # stack for DFS search
        while stack:
            node, depth = stack.pop()
            
            if node is not None:
                # maintain knowledge of the number of levels in the tree
                max_depth = max(max_depth, depth)
                
                # only insert into dict if the depth is not already present
                rightmost_value_at_depth.setdefault(depth, node.val)
                
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
                
        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]
            
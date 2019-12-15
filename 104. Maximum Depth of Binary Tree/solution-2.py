# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        rightmost_value_at_depth = dict() # dictionary for storing (depth, rightmost value)
        max_depth = -1
        
        queue = deque([(root, 0)]) # stack for DFS search
        while queue:
            node, depth = queue.popleft()
            
            if node is not None:
                # maintain knowledge of the number of levels in the tree
                max_depth = max(max_depth, depth)
                
                # overwrite rightmost value when visiting the nodes at the current depth
                rightmost_value_at_depth[depth] = node.val
                
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
                
        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]
            
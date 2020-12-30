# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = collections.deque()
        queue.append(root)
        queue.append(root)
        
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            
            if node1 == None and node2 == None:
                continue
            elif node1 == None or node2 == None or node1.val != node2.val:
                return False
            
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        
        return True
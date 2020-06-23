# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def computeDepth(self, node):
        depth = 0
        while node.left:
            node = node.left
            depth += 1
        return depth
    
    def isExisted(self, idx, depth, root):
        lo = 1
        hi = 2**depth

        for _ in range(depth):
            pivot = lo + (hi - lo) // 2
            if pivot <= idx:
                root = root.right
                lo = pivot + 1
            else:
                root = root.left
                hi = pivot
                
        if root == None:
            return False
        else:
            return True    
    
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth = self.computeDepth(root)
        
        if depth == 0:
            return 1
        
        lo = 1
        hi = 2**depth
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.isExisted(mid, depth, root):
                lo = mid + 1
            else:
                hi = mid
        
        return 2**depth - 1 + lo
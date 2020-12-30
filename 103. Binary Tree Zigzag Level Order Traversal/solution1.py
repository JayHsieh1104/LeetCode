# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        ret = []
        isLeftToRight = True
        queue = collections.deque([root])
        
        while queue:
            level_list = []
            n = len(queue)
            for _ in range(n):
                curr_node = queue.popleft()
                level_list.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            if isLeftToRight:
                ret.append(level_list)
            else:
                ret.append(level_list[::-1])
            isLeftToRight = not isLeftToRight
        
        return ret
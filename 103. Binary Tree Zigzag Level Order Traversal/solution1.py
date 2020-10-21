# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        isLeftToRight = True
        stack = [root]
        ret = []
        
        while stack:
            temp_stack = []
            ret.append([])
            if isLeftToRight:
                for i in range(len(stack)):
                    current_node = stack.pop()
                    ret[-1].append(current_node.val)
                    if current_node.left:
                        temp_stack.append(current_node.left)
                    if current_node.right:
                        temp_stack.append(current_node.right)
            else:
                for i in range(len(stack)):
                    current_node = stack.pop()
                    ret[-1].append(current_node.val)
                    if current_node.right:
                        temp_stack.append(current_node.right)
                    if current_node.left:
                        temp_stack.append(current_node.left)
            stack = temp_stack
            isLeftToRight = not isLeftToRight
            
        return ret
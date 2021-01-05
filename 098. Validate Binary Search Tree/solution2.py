# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = [(root, -math.inf, math.inf)]

        while stack:
            curr_node, low, high = stack.pop()

            if curr_node == None:
                continue
            if curr_node.val <= low or curr_node.val >= high:
                return False

            stack.append((curr_node.left, low, curr_node.val))
            stack.append((curr_node.right, curr_node.val, high))

        return True

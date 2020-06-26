# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        total = 0
        stack = [(root, root.val)]
        
        while stack:
            currentNode, currentNum = stack.pop()
            if currentNode.left == currentNode.right == None:
                total += currentNum
                continue
            if currentNode.right:
                stack.append((currentNode.right, 10 * currentNum + currentNode.right.val))
            if currentNode.left:
                stack.append((currentNode.left, 10 * currentNum + currentNode.left.val))
        return total
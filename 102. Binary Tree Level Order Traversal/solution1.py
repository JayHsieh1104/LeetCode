# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        stack = []
        stack.append((root, 1))
        mDict = defaultdict(list)
        maxLayer = 1
        while stack:
            currNode, layer = stack.pop()
            mDict[layer].append(currNode.val)
            if layer > maxLayer:
                maxLayer = layer
            if currNode.right:
                stack.append((currNode.right, layer + 1))
            if currNode.left:
                stack.append((currNode.left, layer + 1))
        
        ret = []
        for layer in range(1, maxLayer+1):
            ret.append(mDict[layer])
        
        return ret
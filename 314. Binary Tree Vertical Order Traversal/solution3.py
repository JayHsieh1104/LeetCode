# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(0, root)])
        columnTable = defaultdict(list)
        minColumn = float('inf')
        maxColumn = 0
        
        while queue:
            column, currentNode = queue.popleft()
            if currentNode:
                columnTable[column].append(currentNode.val)

                if column < minColumn:
                    minColumn = column
                if column > maxColumn:
                    maxColumn = column

                if currentNode.left:
                    queue.append((column-1, currentNode.left))
                if currentNode.right:
                    queue.append((column+1, currentNode.right))
            
        
        _ret = []
        for i in range(minColumn, maxColumn+1):
            if i in columnTable:
                _ret.append(columnTable[i])
        
        return _ret
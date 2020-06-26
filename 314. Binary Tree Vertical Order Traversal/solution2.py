# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(0, root)])
        columnTable = defaultdict(list)

        while queue:
            column, currentNode = queue.popleft()
            
            if currentNode:
                columnTable[column].append(currentNode.val)
                queue.append((column-1, currentNode.left))
                queue.append((column+1, currentNode.right))
        
        return [columnTable[x] for x in sorted(columnTable.keys())]
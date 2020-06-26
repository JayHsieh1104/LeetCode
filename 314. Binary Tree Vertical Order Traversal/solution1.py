# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
import heapq

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        inputOrder = 0
        queue = deque([(0, root)])
        hq = [(0, inputOrder, root.val)]
        heapq.heapify(hq)
        
        while queue:
            column, currentNode = queue.popleft()
            if currentNode.left:
                inputOrder += 1
                queue.append((column-1, currentNode.left))
                heapq.heappush(hq, (column-1, inputOrder, currentNode.left.val))
            if currentNode.right:
                inputOrder += 1
                queue.append((column+1, currentNode.right))
                heapq.heappush(hq, (column+1, inputOrder, currentNode.right.val))
            
        
        _ret = []
        _listColumn = None
        _list = []
        while hq:
            currColumn, inputOrder, currNodeVal = heapq.heappop(hq)
            if _listColumn == None:
                _listColumn = currColumn
                _list.append(currNodeVal)
            elif _listColumn != currColumn:
                _ret.append(_list)
                _list = [currNodeVal]
                _listColumn = currColumn
            else:
                _list.append(currNodeVal)
        _ret.append(_list)
        
        return _ret
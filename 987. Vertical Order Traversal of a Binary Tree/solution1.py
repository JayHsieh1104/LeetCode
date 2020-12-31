# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []
        
        def BFS(root):
            queue = collections.deque([(root, 0, 0)])
            while queue:
                node, row, col = queue.popleft()
                if node != None:
                    node_list.append((col, row, node.val))
                    queue.append((node.left, row + 1, col - 1))
                    queue.append((node.right, row + 1, col + 1))

        BFS(root)
        
        node_list.sort()
        
        ret = {}
        for col, row, value in node_list:
            if col in ret:
                ret[col].append(value)
            else:
                ret[col] = [value]
        
        return ret.values()
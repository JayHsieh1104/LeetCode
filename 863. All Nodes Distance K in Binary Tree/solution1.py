# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(node, parent_node):
            if node:
                node.parent = parent_node
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root, None)
        
        curr_distance = 0
        queue = collections.deque([target])
        seen = set()
        
        while queue:
            n = len(queue)
            if curr_distance == K:
                return [node.val for node in queue]
            else:
                for _ in range(n):
                    curr_node = queue.popleft()
                    seen.add(curr_node)
                    for nei in (curr_node.left, curr_node.right, curr_node.parent):
                        if nei and nei not in seen:
                            queue.append(nei)
            curr_distance += 1
            
        return []
        
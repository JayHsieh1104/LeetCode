# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ret = []
        queue = collections.deque()
        queue.append(root)
        curr_depth = 0

        while queue:
            n = len(queue)
            curr_depth += 1
            for i in range(n):
                curr_node = queue.popleft()
                if len(ret) == curr_depth:
                    ret[curr_depth - 1] = curr_node.val
                else:
                    ret.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

        return ret

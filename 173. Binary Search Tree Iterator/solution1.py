# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue

class BSTIterator:

    def __init__(self, root: TreeNode):
        def DFS(root: TreeNode):
            if root == None:
                return
            else:
                DFS(root.left)
                self.q.put(root.val)
                DFS(root.right)
        
        self.q = queue.Queue()
        DFS(root)

    def next(self) -> int:
        return self.q.get()
        

    def hasNext(self) -> bool:
        return not self.q.empty()
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
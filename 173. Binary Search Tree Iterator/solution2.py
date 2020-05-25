# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = [root]
        self.seen = set()

    def next(self) -> int:
        cur_node = self.stack[-1]
        while cur_node.left != None and cur_node.left.val not in self.seen:
            self.stack.append(cur_node.left)
            cur_node = cur_node.left
        ret_node = self.stack.pop()
        if ret_node.right != None:
            self.stack.append(ret_node.right)
        self.seen.add(ret_node.val)
        return ret_node.val

    def hasNext(self) -> bool:
        if len(self.stack) == 0 or not self.stack[0]:
            return False
        else:
            return True     

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
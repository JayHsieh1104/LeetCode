# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []

        self.leftmost_inorder(root)

    def leftmost_inorder(self, root):
        while root != None:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        next_node = self.stack.pop()
        if next_node.right != None:
            self.leftmost_inorder(next_node.right)
        return next_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.sorted_list = []
        self.stack = []
        self.current_node = root
        self.node_index = 0

        while self.current_node != None or self.stack:
            while self.current_node != None:
                self.stack.append(self.current_node)
                self.current_node = self.current_node.left
            self.current_node = self.stack.pop()
            self.sorted_list.append(self.current_node.val)
            self.current_node = self.current_node.right

    def next(self) -> int:
        ret = self.sorted_list[self.node_index]
        self.node_index += 1
        return ret

    def hasNext(self) -> bool:
        if self.node_index >= len(self.sorted_list):
            return False
        else:
            return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

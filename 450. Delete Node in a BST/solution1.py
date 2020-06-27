# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPredecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root
    
    def findSuccessor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return root
        
        # delete from the left subtree
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        # delete from the right subtree
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # delte the current node
        else:
            # the node is not a leaf and has a right child
            if root.right:
                root.val = self.findSuccessor(root).val
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            elif root.left:
                root.val = self.findPredecessor(root).val
                root.left = self.deleteNode(root.left, root.val)
            # the node is a left
            else:
                root = None
        return root
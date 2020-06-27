# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def reserialize(root, string):
            if root == None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = reserialize(root.left, string)
                string = reserialize(root.right, string)
            return string
        
        return reserialize(root, '')
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def redeserialize(data):
            if data[0] == 'None':
                data.pop(0)
                return None
            else:
                root = TreeNode(data.pop(0))
                root.left = redeserialize(data)
                root.right = redeserialize(data)
                return root
            
        data_list = data.split(',')
        return redeserialize(data_list)
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
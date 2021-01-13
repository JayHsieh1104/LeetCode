# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mapLinkedListToList(self, head: ListNode) -> list:
        ret = []
        while head:
            ret.append(head.val)
            head = head.next
        return ret

    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        
        values = self.mapLinkedListToList(head)
        
        def convertListToBST(lo: int, hi:int) -> TreeNode:
            if lo > hi:
                return None
            
            mid = lo + (hi - lo) // 2
            root = TreeNode(values[mid])
            root.left = convertListToBST(lo, mid - 1)
            root.right = convertListToBST(mid + 1, hi)
            return root
            
        return convertListToBST(0, len(values) - 1)
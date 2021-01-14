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
    
    def findLinkedListSize(self, head: ListNode) -> int:
        ptr = head
        length = 0
        while ptr:
            length += 1
            ptr = ptr.next
        return length
        
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        size = self.findLinkedListSize(head)
        
        def convert(lo: int, hi: int) -> TreeNode:
            nonlocal head
            
            if lo > hi:
                return None
            
            mid = lo + (hi - lo) // 2
            
            left = convert(lo, mid - 1)
            node = TreeNode(head.val, left)
            head = head.next
            node.right = convert(mid + 1, hi)
            
            return node
        
        return convert(0, size - 1)
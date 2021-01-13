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
    def findMiddle(self, head: ListNode) -> ListNode:
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        if prev:
            prev.next = None
            
        return slow
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        
        mid_node = self.findMiddle(head)
        root = TreeNode(mid_node.val)
        
        if mid_node == head:
            return root
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid_node.next)
        
        return root
        
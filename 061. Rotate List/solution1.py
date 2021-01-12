# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head
        
        length = 1
        old_tail = head
        while old_tail.next:
            length += 1
            old_tail = old_tail.next
        old_tail.next = head
        
        new_tail = head
        for i in range(length - k % length - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        new_tail.next = None
        
        return new_head
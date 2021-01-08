# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        beforePointer = beforeHead = ListNode(0)
        afterPointer = afterHead = ListNode(0)
        
        while head:
            if head.val < x:
                beforePointer.next = head
                beforePointer = beforePointer. next
            else:
                afterPointer.next = head
                afterPointer = afterPointer.next
            head = head.next
        
        afterPointer.next = None
        beforePointer.next = afterHead.next
        
        return beforeHead.next
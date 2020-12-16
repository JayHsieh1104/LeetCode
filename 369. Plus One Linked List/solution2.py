# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        not_nine_pointer = dummyHead
        
        while head:
            if head.val != 9:
                not_nine_pointer = head
            head = head.next
        
        not_nine_pointer.val += 1
        not_nine_pointer = not_nine_pointer.next
        
        while not_nine_pointer:
            not_nine_pointer.val = 0
            not_nine_pointer = not_nine_pointer.next
        
        if dummyHead.val:
            return dummyHead
        else:
            return dummyHead.next

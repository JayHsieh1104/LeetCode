# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_pointer = None
        cur_pointer = head
        
        while(cur_pointer != None):
            next_pointer = cur_pointer.next
            cur_pointer.next = prev_pointer
            prev_pointer = cur_pointer
            cur_pointer = next_pointer
        
        return prev_pointer
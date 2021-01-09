# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        
        prev, curr = None, head
        
        while m > 1:
            prev, curr = curr, curr.next
            m, n = m - 1, n - 1
        
        unReversedTail, reversedHead = prev, curr
        
        while n > 0:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
            n -= 1
            
        if unReversedTail:
            unReversedTail.next = prev
        else:
            head = prev
        
        reversedHead.next = curr
            
        return head
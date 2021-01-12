# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        prev, curr = head, head.next
        
        while curr and curr.next:
            if prev == curr:
                return True
            prev = prev.next
            curr = curr.next.next
        
        return False
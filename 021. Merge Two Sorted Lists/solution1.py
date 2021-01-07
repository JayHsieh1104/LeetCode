# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:    
        dummyHead = ListNode(0)
        curr = dummyHead
        
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = ListNode(l2.val)
                curr, l2 = curr.next, l2.next
            else:
                curr.next = ListNode(l1.val)
                curr, l1 = curr.next, l1.next
        
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        
        return dummyHead.next
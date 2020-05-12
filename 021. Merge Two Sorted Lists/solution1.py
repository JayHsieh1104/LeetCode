# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode()
        pointer = dummyHead
        
        while l1 and l2:
            if l1.val < l2.val:
                pointer.next = ListNode(l1.val)
                l1 = l1.next
            else:
                pointer.next = ListNode(l2.val)
                l2 = l2.next
            pointer = pointer.next
        
        if l1 == None:
            pointer.next = l2
        else:
            pointer.next = l1
        
        return dummyHead.next
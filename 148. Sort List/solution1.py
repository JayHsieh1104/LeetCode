# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def getMid(self, head: ListNode) -> ListNode:
        midPrev = None
        while head and head.next:
            if midPrev == None:
                midPrev = head
            else:
                midPrev = midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid
        
        
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        curr = dummyHead
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
                
        if list1:
            curr.next = list1
        else:
            curr.next = list2
                
        return dummyHead.next
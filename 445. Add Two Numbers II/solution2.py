# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None
        while head:
            next_node = head.next
            head.next, prev_node = prev_node, head
            head = next_node
            
        return prev_node
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
            
        dummyHead = ListNode(0)
        carry = 0
        
        while l1 or l2:
            if l1:
                x = l1.val
                l1 = l1.next
            else:
                x = 0
            if l2:
                y = l2.val
                l2 = l2.next
            else:
                y = 0
            sum = x + y + carry
            carry = sum // 10
            dummyHead.next = ListNode(sum % 10, dummyHead.next)
        
        if carry > 0:
            dummyHead.next = ListNode(carry % 10, dummyHead.next)
        
        return dummyHead.next
            
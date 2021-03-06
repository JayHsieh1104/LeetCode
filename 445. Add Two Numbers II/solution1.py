# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        while l1:
            stack1.append(l1)
            l1 = l1.next
            
        stack2 = []
        while l2:
            stack2.append(l2)
            l2 = l2.next
            
        dummyHead = ListNode(0)
        carry = 0
        
        while stack1 or stack2:
            if stack1:
                x = stack1.pop().val
            else:
                x = 0
            if stack2:
                y = stack2.pop().val
            else:
                y = 0
            sum = x + y + carry
            carry = sum // 10
            dummyHead.next = ListNode(sum % 10, dummyHead.next)
        
        if carry > 0:
            dummyHead.next = ListNode(carry % 10, dummyHead.next)
        
        return dummyHead.next
            
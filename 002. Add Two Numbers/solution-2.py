# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        dummy_head = res
        while l1 != None or l2 != None:
            res.val += l1.val + l2.val            
            if res.val > 9:
                res.next = ListNode(int(res.val / 10))
                res.val %= 10
            else:
                if l1.next == None and l2.next == None:
                    return dummy_head
                res.next = ListNode(0)
            res = res.next
            
            if l1.next != None:
                l1 = l1.next
            else:
                l1.val = 0
                
            if l2.next != None:
                l2 = l2.next
            else:
                l2.val = 0
            
        return dummy_head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp = headA
        length_A = 0
        while temp:
            length_A += 1
            temp = temp.next
        
        temp = headB
        length_B = 0
        while temp:
            length_B += 1
            temp = temp.next
        
        if length_A > length_B:
            for _ in range(length_A - length_B):
                headA = headA.next
        else:
            for _ in range(length_B - length_A):
                headB = headB.next
        
        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        
        return None

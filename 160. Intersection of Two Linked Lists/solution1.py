# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headA:
            temp = headB
            while temp:
                if headA == temp:
                    return headA
                temp = temp.next
            headA = headA.next
        
        return None
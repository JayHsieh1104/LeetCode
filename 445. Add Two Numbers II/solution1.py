# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            s1 = []
            s2 = []
            
            while l1 != None:
                s1.append(l1.val)
                l1 = l1.next
            while l2 != None:
                s2.append(l2.val)
                l2 = l2.next

            head = ListNode(0)
            while s1 or s2:
                temp = head.val
                tempHead = ListNode(0)
                if not s2:
                    temp += s1.pop()
                elif not s1:
                    temp += s2.pop()
                else:
                    temp += s1.pop() + s2.pop()
                    
                tempHead.val, head.val = divmod(temp, 10)
                tempHead.next, head = head, tempHead
                
            if head.val == 0:
                return head.next
            else:
                return head
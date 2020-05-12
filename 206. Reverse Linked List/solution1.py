# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        mStack = []
        while head != None:
            mStack.append(head.val)
            head = head.next
        
        dummyHead = ListNode()
        pointer = dummyHead
        while len(mStack) != 0:
            pointer.next = ListNode(mStack.pop())
            pointer = pointer.next
        
        return dummyHead.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return None
            
        stack = []
        ptr = head
        
        while ptr:
            temp = ptr.next
            ptr.next = None
            stack.append(ptr)
            ptr = temp
        
        dummyHead = ListNode()
        ptr = dummyHead
        while len(stack) > 1:
            ptr.next = stack.pop(0)
            ptr = ptr.next
            ptr.next = stack.pop()
            ptr = ptr.next

        if stack:
            ptr.next = stack.pop()
        
        return dummyHead.next
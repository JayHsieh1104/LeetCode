# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return head
        
        stack = []
        cnt = 0
        pointer = head
        while pointer != None:
            stack.append(pointer.val)
            cnt += 1
            pointer = pointer.next
        
        while cnt > 2:
            next_node = ListNode(stack.pop())
            next_node.next = head.next
            head.next = next_node
            head = head.next.next
            cnt -= 2
        
        if cnt == 2:
            head.next.next = None
        else:
            head.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        stack = []
        pointer = head
        while pointer != None:
            stack.append(pointer)
            pointer = pointer.next
        
        while stack:
            current_node = stack.pop()
            if current_node.val == 9:
                current_node.val = 0
            else:
                current_node.val += 1
                return head
        
        return ListNode(1, head)
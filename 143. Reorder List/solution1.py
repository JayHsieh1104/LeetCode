# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        def popFinalNode(node: ListNode) -> ListNode:
            while node.next.next != None:
                node = node.next
            ret = node.next
            node.next = None
            return ret
        
        if not head:
            return head
        
        pointer = head
        while pointer.next != None and pointer.next.next != None:
            next_node = popFinalNode(pointer)
            next_node.next = pointer.next
            pointer.next = next_node
            pointer = pointer.next.next
        return head
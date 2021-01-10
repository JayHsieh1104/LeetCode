# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, head: ListNode, k: int) -> ListNode:
        prev, curr = None, head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        return prev
        
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        
        counter = 0
        while counter < k and curr:
            curr = curr.next
            counter += 1
        
        if counter == k:
            revseresd_head = self.reverseLinkedList(head, k)
            head.next = self.reverseKGroup(curr, k)
            return revseresd_head
        
        return head
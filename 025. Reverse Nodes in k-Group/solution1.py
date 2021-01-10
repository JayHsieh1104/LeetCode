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
        new_head = None
        last_list_tail = None
        curr = head
        
        while curr:
            counter = 0
            while counter < k and curr:
                curr = curr.next
                counter += 1
            
            if counter == k:
                revseresd_head = self.reverseLinkedList(head, k)
            
                if not new_head:
                    new_head = revseresd_head

                if last_list_tail:
                    last_list_tail.next = revseresd_head

                last_list_tail = head
                head = curr

        if head:
            last_list_tail.next = head
        
        if new_head:
            return new_head
        else:
            return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        
        cnt = 0
        dummyHead = ListNode(0, head)
        pointer = dummyHead
        
        while cnt < m - 1:
            cnt += 1
            pointer = pointer.next
            
        start_node = pointer
        end_node = pointer.next
        prev_node = pointer.next
        pointer = prev_node.next
        cnt += 2
        
        while True:
            next_node = pointer.next
            pointer.next = prev_node
            if cnt == n:
                start_node.next = pointer
                end_node.next = next_node
                return dummyHead.next
            else:
                prev_node = pointer
                pointer = next_node
                cnt += 1
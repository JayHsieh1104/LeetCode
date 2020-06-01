# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:   
        dummyHead = ListNode(-1)
        dummyHead.next = head
    
        prev_round_tail = dummyHead
        
        while head and head.next:
            first_node = head
            second_node = head.next
            
            first_node.next = second_node.next
            second_node.next = first_node
            prev_round_tail.next = second_node
            
            prev_round_tail = first_node
            head = first_node.next
                
        return dummyHead.next
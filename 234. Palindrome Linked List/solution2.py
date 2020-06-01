# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head. next is None:
            return True
        
        first_half_end = self.get_end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        
        result = True
        pointer = second_half_start
        while result and pointer:
            if head.val != pointer.val:
                result = False
            head = head.next
            pointer = pointer.next
        
        # Restore the sceond half list
        self.reverse_list(second_half_start)
        
        return result
        
    def get_end_of_first_half(self, head):
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse_list(self, head):
        previous = None
        current = head
        while current != None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
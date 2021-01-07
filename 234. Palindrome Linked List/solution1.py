# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def is_next_same(node: ListNode) -> bool:
            nonlocal head
            if node == None:
                return True
            
            if is_next_same(node.next) and head.val == node.val:
                head = head.next
                return True
            else:
                return False
        
        return is_next_same(head)
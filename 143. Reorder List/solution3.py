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
        def get_mid_node(head: ListNode) -> ListNode:
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        
        def reverse_linked_list(head: ListNode) -> ListNode:
            prev, curr = None, head
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev
        
        
        def merge_linked_list(list1: ListNode, list2: ListNode) -> ListNode:
            while list2.next:
                list1.next, list1 = list2, list1.next
                list2.next, list2 = list1, list2.next
        
        
        if head == None:
            return None
        
        mid_node = get_mid_node(head)
        new_head = reverse_linked_list(mid_node)
        merge_linked_list(head, new_head)
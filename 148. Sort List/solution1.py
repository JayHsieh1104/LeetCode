# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        def merge(head1, head2):
            dummyHead = ListNode()
            pointer = dummyHead
            
            while head1 != None and head2 != None:
                if head1.val > head2.val:
                    pointer.next = ListNode(head2.val)
                    head2 = head2.next
                else:
                    pointer.next = ListNode(head1.val)
                    head1 = head1.next
                pointer = pointer.next
            
            while head1 != None:
                pointer.next = ListNode(head1.val)
                pointer = pointer.next
                head1 = head1.next

            while head2 != None:
                pointer.next = ListNode(head2.val)
                pointer = pointer.next
                head2 = head2.next

            return dummyHead.next

        if head == None or head.next == None:
            return head

        # 1. Cut the list to two sublists
        prev, slow, fast = None, head, head
        
        while fast != None and fast.next != None:
            prev, slow, fast = slow, slow.next, fast.next.next
        
        prev.next = None

        # 2. Sort the two sublists
        L1 = self.sortList(head)
        L2 = self.sortList(slow)

        # 3. Merge the two sublists
        return merge(L1, L2)
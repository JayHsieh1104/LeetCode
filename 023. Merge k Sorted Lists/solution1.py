# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        
        for list in lists:
            while list:
                nodes.append(list.val)
                list = list.next
        
        nodes.sort()
        
        dummyHead = ListNode()
        curr = dummyHead
        
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next
        
        return dummyHead.next
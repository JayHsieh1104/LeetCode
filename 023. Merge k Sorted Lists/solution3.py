# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        dummyHead = ListNode(0)
        curr = dummyHead
        queue = PriorityQueue()
        
        for list in lists:
            if list:
                queue.put(Wrapper(list))
        
        while not queue.empty():
            node = queue.get().node
            curr.next = node
            node, curr = node.next, curr.next
            if node:
                queue.put(Wrapper(node))
        
        return dummyHead.next
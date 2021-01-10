# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummyHead = ListNode(0)
        curr = dummyHead
        
        while True:
            min_node = (math.inf, 0)
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_node[0]:
                    min_node = (lists[i].val, i)
            if min_node[0] == math.inf:
                break
            curr.next = lists[min_node[1]]
            lists[min_node[1]] = lists[min_node[1]].next
            curr = curr.next
        
        curr.next = None
        return dummyHead.next
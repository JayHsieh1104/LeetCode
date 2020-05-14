# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        mList = []
        for i in range(len(lists)):
            while lists[i] != None:
                mList.append(lists[i].val)
                lists[i] = lists[i].next
        
        mList.sort()
        dummyHead = ListNode()
        pointer = dummyHead
        for num in mList:
            pointer.next = ListNode(num)
            pointer = pointer.next
            
        return dummyHead.next
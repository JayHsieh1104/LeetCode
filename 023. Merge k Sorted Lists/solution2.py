# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:        
        dummyHead = ListNode()
        pointer = dummyHead

        isAllVisited = False
        while not isAllVisited:
            isAllVisited = True
            for i in range(len(lists)):
                if lists[i] != None:
                    isAllVisited = False
                    nextNum = (lists[i].val, i)
                    break
            
            for i in range(len(lists)):
                if lists[i] == None:
                    continue
                else:
                    if lists[i].val < nextNum[0]:
                        nextNum = (lists[i].val, i)
            pointer.next = ListNode(nextNum[0])
            pointer = pointer.next
            lists[nextNum[1]] = lists[nextNum[1]].next
        
        return dummyHead.next
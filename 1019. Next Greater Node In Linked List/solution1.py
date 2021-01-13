# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head == None:
            return []
        
        ret = []
        first = head
        while first:
            ret.append(first.val)
            second = first.next
            while second:
                if second.val > ret[-1]:
                    ret[-1] = second.val
                    break
                second = second.next 
            if first.val == ret[-1]:
                ret[-1] = 0 
            first = first.next
                
        return ret
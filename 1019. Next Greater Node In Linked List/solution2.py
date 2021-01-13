# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head == None:
            return []
        
        answer_array = []
        stack = []
        while head:
            answer_array.append(0)
            
            while stack and stack[-1][0] < head.val:
                val, pos = stack.pop()
                answer_array[pos] = head.val
            
            stack.append((head.val, len(answer_array) - 1))
            head = head.next
              
        return answer_array
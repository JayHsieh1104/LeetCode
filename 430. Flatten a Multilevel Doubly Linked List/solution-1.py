"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        dummyHead = Node(0, None, head, None)
        prev = dummyHead
        
        stack = []
        stack.append(head)
        
        while stack:
            curr = stack.pop()
            
            prev.next = curr
            curr.prev = prev
            
            if curr.next:
                stack.append(curr.next)
            
            if curr.child:
                stack.append(curr.child)
                curr.child = None
                
            prev = prev.next
        
        dummyHead.next.prev = None
        return dummyHead.next        
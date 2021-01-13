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
        if head == None:
            return None
        
        dummyHead = Node(0, None, None, None)
        ptr = dummyHead
        stack = [head]
        while stack:
            curr = stack.pop()
            
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
                
            ptr.next, curr.prev= curr, ptr
            ptr = ptr.next
        
        dummyHead.next.prev = None
        
        return dummyHead.next
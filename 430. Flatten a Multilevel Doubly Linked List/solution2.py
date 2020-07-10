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
        
        stack = []
        stack.append(head)
        dummyHead = Node(0, None, None, None)
        pointer = dummyHead
        prev_node = None
        
        while stack:
            current_node = stack.pop()
            current_node.prev, prev_node = prev_node, current_node
            pointer.next = current_node
            pointer = pointer.next
            
            if current_node.next:
                stack.append(current_node.next)
                
            if current_node.child:
                stack.append(current_node.child)
                current_node.child = None
        
        return dummyHead.next
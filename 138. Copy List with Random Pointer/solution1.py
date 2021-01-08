"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visitedHash = {}
    
    def getClonedNode(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        
        if node not in self.visitedHash:
            self.visitedHash[node] = ListNode(node.val)
        return self.visitedHash[node] 
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        
        old_node = head
        new_node = ListNode(old_node.val)
        self.visitedHash[old_node] = new_node
        
        while old_node:
            new_node.next = self.getClonedNode(old_node.next)
            new_node.random = self.getClonedNode(old_node.random)
            
            old_node = old_node.next
            new_node = new_node.next

        return self.visitedHash[head]
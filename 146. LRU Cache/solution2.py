class ListNode:
    
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    
    def __init__(self, capacity: int):
        self.hashTable = {}
        self.currentSize = 0
        self.capacity = capacity
        self.listHead = ListNode(-1, -1)
        self.listTail = ListNode(-1, -1)
        self.listHead.next = self.listTail
        self.listTail.prev = self.listHead

    def _add_to_tail(self, key: int, val: int):
        newNode = ListNode(key, val, self.listTail.prev, self.listTail)
        self.listTail.prev.next = newNode
        self.listTail.prev = newNode
        self.hashTable[key] = newNode

    def _remove_node(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.hashTable[node.key]

    def _move_to_tail(self, node: ListNode):
        self._remove_node(node)
        self._add_to_tail(node.key, node.val)

    def get(self, key: int) -> int:
        if key in self.hashTable:
            self._move_to_tail(self.hashTable[key])
            return self.hashTable[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashTable:
            self._remove_node(self.hashTable[key])
            self.currentSize -= 1
        self._add_to_tail(key, value)

        if self.currentSize < self.capacity:
            self.currentSize += 1
        else:
            self._remove_node(self.listHead.next)
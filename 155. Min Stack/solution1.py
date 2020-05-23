class MinStack:

    def __init__(self):
        self.stack = []
        self.pq = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.pq and x < self.pq[0]:
            self.pq.append(self.pq[0])
            self.pq[0] = x
        else:
            self.pq.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.pq[0]:
            self.pq.remove(self.stack[-1])
            self.pq.sort(reverse=False)
        else:
            self.pq.remove(self.stack[-1])
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pq[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
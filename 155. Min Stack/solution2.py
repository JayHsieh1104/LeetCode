class MinStack:

    def __init__(self):
        self.stack = []
        self.pq = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.pq:
            if x >= self.pq[-1]:
                self.pq.append(x)
            else:
                for i in range(len(self.pq)):
                    if self.pq[i] >= x:
                        self.pq.insert(i, x)
                        break
        else:
            self.pq.append(x)

    def pop(self) -> None:
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
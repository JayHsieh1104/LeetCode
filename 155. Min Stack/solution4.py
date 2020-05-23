class MinStack:

    def __init__(self):
        self.value_stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.value_stack.append(x)
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.min_stack[-1] == self.value_stack[-1]:
            self.min_stack.pop()
        self.value_stack.pop()
        
    def top(self) -> int:
        return self.value_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MinStack:

    def __init__(self):
        self.stack = collections.deque()
        self.minValues = collections.deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minValues: self.minValues.append(val)
        else: self.minValues.append(min(self.minValues[-1],val))

    def pop(self) -> None:
        self.stack.pop()
        self.minValues.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minValues[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
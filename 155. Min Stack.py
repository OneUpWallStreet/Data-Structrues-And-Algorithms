class MinStack:

    def __init__(self):
        self.s = collections.deque()
        self.minVals = collections.deque()

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.minVals or self.minVals[-1] > val: self.minVals.append(val)
        else: self.minVals.append(self.minVals[-1])

    def pop(self) -> None:
        self.minVals.pop()
        self.s.pop()

    def top(self) -> int: return self.s[-1]
    def getMin(self) -> int:  return self.minVals[-1]
        



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
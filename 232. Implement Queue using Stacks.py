class MyQueue:
    def __init__(self): self.s1, self.s2 = collections.deque(), collections.deque()
    def push(self, x: int) -> None: self.s1.append(x)
    def s1Tos2(self,remove: bool) -> int:        
        while len(self.s1) > 1: self.s2.append(self.s1.pop())
        val = self.s1.pop()
        if not remove: self.s2.append(val)
        while self.s2: self.s1.append(self.s2.pop())
        return val
    def pop(self) -> int: return self.s1Tos2(True)
    def peek(self) -> int: return self.s1Tos2(False)
    def empty(self) -> bool: return len(self.s1) == 0
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
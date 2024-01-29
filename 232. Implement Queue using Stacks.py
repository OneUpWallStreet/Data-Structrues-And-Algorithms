import collections

class MyQueue:

    def __init__(self):
        self.s1, self.s2 = collections.deque(), collections.deque()
        

    def push(self, x: int) -> None: self.s1.append(x)
        

    def pop(self) -> int:
        self.s2.clear()
        while len(self.s1) > 1: self.s2.append(self.s1.pop())
        result = self.s1.pop()
        while self.s2: self.s1.append(self.s2.pop())
        return result

    def peek(self) -> int:
        self.s2.clear()
        while len(self.s1) > 1: self.s2.append(self.s1.pop())
        result = self.s1.pop()
        self.s2.append(result)
        while self.s2: self.s1.append(self.s2.pop())
        return result

    def empty(self) -> bool: return not self.s1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
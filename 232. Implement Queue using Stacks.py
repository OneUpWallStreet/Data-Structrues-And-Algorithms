class MyQueue:

    def __init__(self):
        self.s1, self.s2 = collections.deque(), collections.deque()

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:

        # Fill S2 with S1 expect for last element
        # Shift S2 back into S1 
        self.s2.clear()
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop()) 
        ele = self.s1.pop()
        
        while self.s2: self.s1.append(self.s2.pop())
        return ele

    def peek(self) -> int:
        
        self.s2.clear()
        print(self.s1)
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop()) 
        print(self.s1)
        ele = self.s1.pop()
        self.s2.append(ele)
        while self.s2: self.s1.append(self.s2.pop())
        return ele
        

    def empty(self) -> bool:
        return len(self.s1) == 0

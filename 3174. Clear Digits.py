class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = collections.deque()

        for ch in s:
            if ch.isnumeric(): stack.pop()
            else: stack.append(ch)
        
        return "".join(stack)
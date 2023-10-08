class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def createNewString(stri):
            stack = collections.deque()
            for ch in stri:
                if ch == "#":
                    if stack: stack.pop()
                else:
                    stack.append(ch)
            return stack
        return createNewString(s) == createNewString(t)
 



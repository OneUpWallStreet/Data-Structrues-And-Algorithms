class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = collections.deque()

        for ch in s:
            if ch == "(": stack.append(")")
            elif ch == "[": stack.append("]")
            elif ch == "{": stack.append("}")
            else: 
                if not stack or stack.pop() != ch: return False 
    
        return not stack
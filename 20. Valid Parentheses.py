class Solution:
    def isValid(self, s: str) -> bool:

        stack = collections.deque()
        hashset = ("{", "[","(")

        def match(p1,p2):
            if p1 == "{"  and p2 == "}": return True
            elif p1 == "("  and p2 == ")": return True
            elif p1 == "["  and p2 == "]": return True
            else: return False
        
        for ch in s:
            if ch in hashset: stack.append(ch) 
            elif len(stack) == 0 or match(stack.pop(),ch) == False: return False

        return len(stack) == 0
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def back(val: str):
            s = collections.deque()
            for ch in val:
                if ch != "#": s.append(ch)
                elif s: s.pop()
            return "".join(s)
        return back(s) == back(t)
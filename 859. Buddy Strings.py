class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal): return False

        if s == goal:
            hashset = set()
            for ch in s:
                hashset.add(ch)
            
            if len(hashset) < len(s): return True
            else: return False

        dif = []

        for index in range(len(s)): 
            if s[index] != goal[index]: dif.append(index)

        if len(dif) != 2: return False
        if s[dif[0]] == goal[dif[1]] and s[dif[1]] == goal[dif[0]]: return True


        return False
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        rad = collections.deque()
        dire = collections.deque()

        for i, ch in enumerate(senate): 
            if ch == "R": rad.append(i)
            else: dire.append(i)

        n = len(senate)

        while rad and dire:            
            if rad[0] < dire[0]: rad.append(n)
            else: dire.append(n)
            
            rad.popleft()
            dire.popleft()
            n += 1
        
        return "Radiant" if rad else "Dire"

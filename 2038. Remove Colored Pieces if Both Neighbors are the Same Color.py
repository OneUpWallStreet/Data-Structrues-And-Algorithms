class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        aCounter, bCounter = 0, 0 

        p1,p2,p3 = 0,1,2

        if len(colors) < 3: return False

        while p3< len(colors):
            if colors[p1] == colors[p2] == colors[p3]:
                if colors[p1] == "A": aCounter += 1
                else: bCounter += 1

            p1 += 1
            p2 += 1
            p3 += 1
        
        return aCounter > bCounter
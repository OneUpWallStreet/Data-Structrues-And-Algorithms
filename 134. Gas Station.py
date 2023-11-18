class Solution:


    def greedyCanCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost): return -1         

        total = 0
        cur = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if cur == None: cur = i
            if total < 0: 
                total = 0
                cur = None
            
        if total >= 0 and cur != None: return cur
        return -1

    # Brute Force Solution
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost): return -1

        diff = [-1] * len(gas)

        for i in range(len(gas)): diff[i] = gas[i] - cost[i]

        def getNextIndex(index):
            if index + 1 == len(gas): return 0
            else: return index + 1 

        for i in range(len(diff)):
            if diff[i] < 0: continue
            
            cur = diff[i]
            nextIndex = getNextIndex(i)
            
            while True:

                cur += diff[nextIndex]
                if cur < 0: break
                if nextIndex == i and cur>= 0: return i
                nextIndex = getNextIndex(nextIndex)            

        return -1
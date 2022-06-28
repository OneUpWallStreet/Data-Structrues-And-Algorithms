class Solution:
    def minDeletions(self, s: str) -> int:

        freqMap = dict()
        for c in s:
            if c in freqMap:
                freqMap[c] += 1
            else:
                freqMap[c] = 1


        mySet = set()
        result = 0

        for key,value in freqMap.items():
            while value > 0 and value in mySet:
                value -= 1
                result += 1
            mySet.add(value)

        return result

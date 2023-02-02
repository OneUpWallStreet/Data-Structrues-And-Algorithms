class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alienDict = dict()
        for index in range(len(order)):
            alienDict[order[index]] = index

        def compareStrings(s1,s2) -> True:
            s1Len,s2Len = len(s1),len(s2)
            for index in range(max(s1Len,s2Len)):
                if index >= s1Len and index < s2Len:
                    return True
                elif index < s1Len and index >= s2Len:
                    return False
                if alienDict[s1[index]] < alienDict[s2[index]]:
                    return True
                elif alienDict[s1[index]] == alienDict[s2[index]]:
                    continue
                elif alienDict[s1[index]] > alienDict[s2[index]]:
                    return False
            return True
        for index in range(len(words)-1):
            if compareStrings(words[index],words[index+1]) == False:
                return False
        return True

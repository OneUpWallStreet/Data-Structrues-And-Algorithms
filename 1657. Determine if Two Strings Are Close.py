class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        hashmap1 = Counter(word1)
        hashmap2 = Counter(word2)

        if hashmap1.keys() != hashmap2.keys():
            return False

        if sorted(hashmap1.values()) != sorted(hashmap2.values()):
            return False

        return True
    
    # Not a good solution but came up with it lol 
    # forgot my old solution. 
    # Although I had to look at this line if w1FM.keys() != w2FM.keys(): return False
    def mySolutionCloseStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False


        w1FM, w2FM = collections.Counter(word1), collections.Counter(word2)

        f1, f2 = collections.defaultdict(int), collections.defaultdict(int)

        for k, v in w1FM.items(): f1[v] += 1
        for k, v in w2FM.items(): f2[v] += 1

        if w1FM.keys() != w2FM.keys(): return False

        if len(f1) != len(f2): return False

        for k,v in f1.items():
            if k not in f2 or v != f2[k]: return False
         
        for k,v in f2.items():
            if k not in f1 or v != f1[k]: return False
         
        return True
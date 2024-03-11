class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ""
        hm = Counter(s)
        for ch in order: 
            result += ch*hm[ch]
            del hm[ch]
        for k,v in hm.items(): result += k*v
        return result
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        mMap = defaultdict(int)

        for ch in magazine:  mMap[ch] += 1

        for ch in ransomNote:
            if ch not in mMap or mMap[ch] <= 0: return False
            mMap[ch] -= 1
        
        return True
        


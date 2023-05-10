class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        hashmap1 = Counter(word1)
        hashmap2 = Counter(word2)

        if hashmap1.keys() != hashmap2.keys():
            return False

        if sorted(hashmap1.values()) != sorted(hashmap2.values()):
            return False

        return True
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        result = []
        for i in range(len(words)-1,-1,-1):
            if len(words[i]) == 0: continue
            result.append(words[i])
        return " ".join(result)
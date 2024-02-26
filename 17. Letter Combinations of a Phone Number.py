class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0: return []
        result = []
        
        hm = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i, cur):
            if i >= len(digits): 
                result.append(cur)
                return
            for ch in hm[digits[i]]: dfs(i+1,cur+ch)

        dfs(0,"")
        return result
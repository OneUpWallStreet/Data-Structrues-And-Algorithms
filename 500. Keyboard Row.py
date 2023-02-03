class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        row1Set = set()
        row2Set = set()
        row3Set = set()
        result = []
        counter = 0

        for row in rows:
            for ch in row:
                if counter == 0:
                    row1Set.add(ch)
                elif counter == 1:
                    row2Set.add(ch)
                elif counter == 2:
                    row3Set.add(ch)

            counter += 1

        def checkWord(word,wordSet):
            nonlocal result
            for ch in word:
                if ch.lower() not in wordSet:
                    return
            result.append(word)

        for word in words:
            if word[0].lower() in row1Set:
                checkWord(word,row1Set)
            elif word[0].lower() in row2Set:
                checkWord(word,row2Set)
            elif word[0].lower() in row3Set:
                checkWord(word,row3Set)
        
        return result
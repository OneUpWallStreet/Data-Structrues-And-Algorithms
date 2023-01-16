class Solution:
    def reverseWords(self, s: str) -> str:

        words = []
        cur = ""
        for i in s:
            if i == " ":
                if len(cur) == 0:
                    continue
                else:
                    words.append(cur)
                    cur = ""
            else:
                cur = cur + i

        if len(cur) > 0:
            words.append(cur)

        output = ""

        for index in range(len(words)-1,-1,-1):
            if index != 0:
                output = output + words[index] + " "
            else:
                output = output + words[index]

        return output
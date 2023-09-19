from typing import List

class Node:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False

class TrieSolution:

    def __init__(self):
        self.result = ""
        self.root = Node()

    def insertIntoTrie(self,word: str):
        cur = self.root
        for ch in word:
            if ch in cur.children: 
                cur = cur.children[ch]
                continue
            else: cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.isEnd = True

    def longestCommonPrefix(self, strs: List[str]) -> str:

        for word in strs:
            if word == "": return ""
            self.insertIntoTrie(word)
        
        # Traverse trie root and find answer
        cur = self.root
        while len(cur.children) == 1:
            val = list(cur.children)[0]
            if cur.isEnd: break
            self.result += val
            cur = cur.children[val]
        
        return self.result


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""
        cur = ""
        minStr = 200
        for s in strs:
            minStr = min(minStr,len(s))

        for i in range(minStr):
            cur = strs[0][i]
            for word in strs:
                if word[i] != cur:
                    return result
            
            result = result + cur
        return result
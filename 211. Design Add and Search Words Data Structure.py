class Node:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

class WordDictionary:

    def __init__(self): self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children: cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.isEnd = True

    def search(self, word: str) -> bool:

        def rcr(node,index):
            if index == len(word): return node.isEnd            
            if word[index] == ".":
                for ch in node.children.keys():
                    if rcr(node.children[ch],index+1): return True
            if word[index] in node.children:  return rcr(node.children[word[index]],index+1)
            return False
        return rcr(self.root,0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
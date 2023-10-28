class Node:

    def __init__(self):
        self.children = dict()
        self.isEnd = False

class Trie:

    def __init__(self): self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children: cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root 
        for ch in word:
            if ch not in cur.children: return False
            cur = cur.children[ch]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root 
        for ch in prefix:
            if ch not in cur.children: return False
            cur = cur.children[ch]
        return True

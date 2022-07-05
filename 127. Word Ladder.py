import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList.append(beginWord)
        
        graph = collections.defaultdict(list)
        
        for word in wordList:
            for i in range(len(beginWord)):
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)
        
        q = collections.deque()
        
        visited = set([beginWord])
        q.append((beginWord,1))
        
        
        while q:
            
            cur,step = q.popleft()
            
            if cur == endWord:
                return step
            
            step += 1
            
            for i in range(len(cur)):
                pattern = cur[:i] + "*" + cur[i+1:]
                for nextWord in graph[pattern]:
                    if nextWord not in visited:
                        visited.add(nextWord)
                        q.append((nextWord,step))
                        
        return 0
            
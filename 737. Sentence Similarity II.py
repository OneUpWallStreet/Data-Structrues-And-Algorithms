import collections


def sentenceSimilarity(words1: list,words2: list,pairs: list) -> bool:

    if len(words1) != len(words2):
        return False

    graph = collections.defaultdict(list)

    for pair in pairs:
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])

    visited = set()

    def isSynonym(curWord,target) -> bool:
        nonlocal visited
        if curWord == target:
            return True
        for nextWord in graph[curWord]:
            if nextWord not in visited:
                visited.add(nextWord)
                if isSynonym(nextWord,target):
                    return True        
        return False

    for i in range(len(words1)):
        visited = set()
        if isSynonym(words1[i],words2[i]) == False:
            return False

    return True

# True
# words2 = ["fine", "drama", "talent"]
# words1 = ["great", "acting", "skills"]
# pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]

# False
# words2 = ["fine", "drama", "talent"]
# words1 = ["great", "acting", "skills"]
# pairs = [["great", "good"],["acting","drama"], ["skills","talent"]]

# True
words1 = ["great"]
words2 = ["great"]
pairs = []

print(sentenceSimilarity(words1,words2,pairs))

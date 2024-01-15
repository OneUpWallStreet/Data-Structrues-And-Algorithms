class Node: 
    def __init__(self):
        self.win = 0
        self.loss = 0
        
class Solution:

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        hm = collections.defaultdict(Node)
        result = [[],[]]
        # winners, one_loss

        for match in matches:
            hm[match[0]].win += 1
            hm[match[1]].loss += 1

        for k,v in hm.items():
            if v.loss == 0: result[0].append(k)
            elif v.loss == 1: result[1].append(k)
            
        return [sorted(sub) for sub in result]
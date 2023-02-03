class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        heapq.heapify(heap)
        result = [""]*len(score)
        for index in range(len(score)):
            heapq.heappush(heap,[-1*score[index],index])
        counter = 1
        while heap:
            index = heapq.heappop(heap)[1]
            if counter == 1:
                result[index] = "Gold Medal"
            elif counter == 2:
                result[index] = "Silver Medal"
            elif counter == 3:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(counter)
            counter += 1
        return result
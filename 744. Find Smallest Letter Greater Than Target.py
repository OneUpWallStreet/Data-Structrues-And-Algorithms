class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        heapq.heapify(letters)
        firstChar = letters[0]

        while letters:
            cur = heapq.heappop(letters)
            if cur > target:
                return cur   
        
        return firstChar
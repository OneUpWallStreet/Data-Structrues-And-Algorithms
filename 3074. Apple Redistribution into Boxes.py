class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse=True)
        result = 0
        for cur in capacity:
            apples -= cur
            result += 1
            print(apples)
            if apples <= 0: return result
        
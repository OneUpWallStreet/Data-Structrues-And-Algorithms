class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = -1

        def calculateWater(first,last):
            curHeight = min(height[first],height[last])
            curWidth = last - first
            return curHeight*curWidth

        first,last = 0,len(height)-1

        while first<last:
            result = max(calculateWater(first,last),result)
            if height[first] < height[last]:
                first += 1
            else:
                last -= 1
        
        return result
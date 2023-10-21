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

    # Simpler Code 
    def maxArea2023(self, height: List[int]) -> int:
        l, r, area = 0, len(height) - 1, float('-inf')
        while l < r:
            area = max(area, min(height[l],height[r])*(r-l))
            if height[l] < height[r]: l += 1
            else: r -= 1
        return area
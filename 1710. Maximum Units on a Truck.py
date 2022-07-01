from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        result = 0
        boxTypes.sort(key =lambda x : -x[1])
        for box in boxTypes:
            if truckSize == 0:
                break
            if box[0] <= truckSize:
                result += box[0]*box[1]
                truckSize -= box[0]
            else:
                result += truckSize*box[1]
                truckSize = 0
        return result
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # Solved within like 5 mins cool lol according to discussion this is kinda hard! 
        # Cool :D 

        for i in range(len(flowerbed)):
            
            if i > 0 and i < len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == 0:
                if flowerbed[i] == 0 and len(flowerbed) > 1 and flowerbed[i+1] == 0: 
                    flowerbed[i] = 1
                    n-= 1
                if len(flowerbed) == 1 and flowerbed[i] == 0: 
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] != 1:
                    flowerbed[i] = 1
                    n -= 1 
            
        return n <= 0
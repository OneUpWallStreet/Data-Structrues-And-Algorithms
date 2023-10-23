class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        result = []

        def rcr(index, curSum, arr):

            if curSum == target:
                result.append(deepcopy(arr))
                return
            elif index >= len(candidates): return
            elif curSum > target: return

            # Use current index
            arr.append(candidates[index])
            
            rcr(index+1,curSum + candidates[index],deepcopy(arr))

            arr.pop()

            index += 1
        
            while index < len(candidates) and candidates[index] == candidates[index-1]: index += 1

            rcr(index,curSum,deepcopy(arr))
            
        rcr(0,0,[])
        return result
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        result = []

        ptr,begin,end = 0, None, None

        while ptr < len(nums):
            if begin == None: 
                begin = int(nums[ptr])
            elif int(nums[ptr]) - 1 == int(nums[ptr-1]):
                end = nums[ptr]
            else:
                if end != None: result.append('{}->{}'.format(begin,end))
                else: result.append('{}'.format(begin))
                begin, end = nums[ptr], None
            
            ptr += 1
        if end != None and begin!=None: result.append('{}->{}'.format(begin,end))
        elif begin != None: result.append('{}'.format(begin))

        return result
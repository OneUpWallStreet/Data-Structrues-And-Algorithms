class Solution:

    # Brute Force Solution (On^2)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hm = collections.defaultdict(int)
        result = [-1] * len(nums1)
        for index,num in enumerate(nums2): hm[num] = index 

        for index, num in enumerate(nums1):
            
            for i in range(hm[num],len(nums2)):
                if nums2[i] > num: 
                    result[index] = nums2[i]
                    break
            
        return result
        
    # Monotonic Stack Solution
    def nextGreaterElementMonoStack(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = [-1] * len(nums1)
        hm = collections.defaultdict(int)

        for i in range(len(nums1)): hm[nums1[i]] = i

        stack = collections.deque()

        for num in nums2:
            while stack and num > stack[-1]:
                if stack[-1] in hm: result[hm[stack.pop()]] = num
                else: stack.pop()
            if num in hm: stack.append(num)

        return result
class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
        
        
        var currentSum = 0
        var result: Int = nums[0]
        
        for num in nums {
            if currentSum < 0 {
                currentSum = 0
            }
            currentSum += num
            result = max(result,currentSum)
        }
        
 
        return result
    }
}
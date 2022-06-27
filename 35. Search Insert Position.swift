import Foundation

class Solution {
    
    var nums: Array<Int> = []
    
    private func binarySearch(_ left: Int,_ right: Int,_ target: Int) -> Int {
        
        if left <= right {
            let mid = left + (right - left)/2
            
            if nums[mid] == target {
                return mid
            }
            
            if nums[mid] > target {
                return binarySearch(left, mid-1, target)
            }else{
                return binarySearch(mid+1, right, target)
            }
        }
    
        return left
    }
    
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {
        self.nums = nums
        return binarySearch(0, nums.count-1, target)
    }
}
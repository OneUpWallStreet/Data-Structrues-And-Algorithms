class Solution {
    
    var nums: Array<Int> = []
    
    private func binarySearch(_ left: Int,_ right: Int) -> Int{
        
        if left <= right {
            
            let mid = left + (right-left)/2
                            
            if mid != 0 && mid+1 != nums.count {
                if nums[mid] > nums[mid-1] && nums[mid] > nums[mid+1] {
                    return mid
                }
                else if nums[mid] < nums[mid-1] {
                    return binarySearch(left, mid)
                }else{
                    return binarySearch(mid+1, right)
                }
            }
        }
        return left
    }
    
    func peakIndexInMountainArray(_ arr: Array<Int>) -> Int {
        self.nums = arr
        return binarySearch(0, arr.count-1)
    }
}
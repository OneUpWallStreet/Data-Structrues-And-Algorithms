class Solution {
    
    var result: Array<Array<Int>> = []
    var nums: Array<Int> = []
    
    var array: Array<Int> = []
    
    func backtrackingDFS(_ index: Int) {
        
        if index >= nums.count {
            result.append(array)
            return
        }
        
        array.append(nums[index])
        
        // Use The current element
        backtrackingDFS(index+1)
		
		// Backtrack
        array.popLast()
        backtrackingDFS(index+1)
        
    }
    
    func subsets(_ nums: Array<Int>) -> Array<Array<Int>> {
        self.nums = nums
        backtrackingDFS(0)
        return result
    }
}

class Solution {
    
    
    var result: Array<Array<Int>> = []
    var nums: Array<Int> = []
    var set = Set<Array<Int>>()
    
    
    func backtrackingDFS(_ index: Int,_ array: Array<Int>) {
        
        if !set.contains(array){
            set.insert(array)
            result.append(array)
        }
        
        if index >= nums.count {
            return
        }
        
        // Use The current element
        var newArray = array
        newArray.append(nums[index])
        backtrackingDFS(index+1,newArray)
        
        // Backtrack
        newArray.popLast()
        backtrackingDFS(index+1,newArray)
        
    }
    
    func subsets(_ nums: Array<Int>) -> Array<Array<Int>> {
        self.nums = nums
        backtrackingDFS(0, [])
        return result
    }
}

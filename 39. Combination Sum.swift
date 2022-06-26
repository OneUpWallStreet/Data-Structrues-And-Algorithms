class Solution {
    
    var result: Array<Array<Int>> = []
    var candidates: Array<Int> = []
    var target: Int = -1
    
    func backtrackingDFS(_ index: Int,_ sum: Int,_ array: Array<Int>) {
        
        if sum == target {
            result.append(array)
            return
        }
        
        if sum > target || index >= candidates.count {
            return
        }
        
        let current = candidates[index]
                
        var nextArray = array
        nextArray.append(current)
        
        // Keep using the current value
        backtrackingDFS(index,sum+current,nextArray)
        
        
        // Backtracking, notice that we pass the
        // array that does not append current element
        backtrackingDFS(index+1, sum, array)
        
    }
    
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        self.candidates = candidates
        self.target = target
        backtrackingDFS(0, 0, [])
        return result
    }
}


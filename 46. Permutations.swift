class Solution {

    // Arbitary init value
    var nums: Array<Int> = []
    var result: Array<Array<Int>> = []
    
    private func backtrackingDFS(_ value: Int,_ set: Set<Int>,_ array: Array<Int>){
                
        if array.count == nums.count {
            result.append(array)
            return
        }
        
        var newSet = set
        newSet.insert(value)
        
        for num in nums {
            if !newSet.contains(num){
                var newArray = array
                newArray.append(num)
                backtrackingDFS(num, newSet, newArray)
                newArray.popLast()
                backtrackingDFS(num, newSet, newArray)
            }
        }
        
    }

    func permute(_ nums: [Int]) -> [[Int]] {
        self.nums = nums
        for num in nums {
            let set = Set<Int>()
            backtrackingDFS(num, set, [num])
        }
        return result
    }
}

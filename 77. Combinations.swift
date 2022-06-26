class Solution {
    
    // arbitrary init values
    var n: Int = -1
    var k: Int = -1
    var result: Array<Array<Int>> = []
    
    func backtrackingDFS(_ index: Int,_ array: Array<Int>) {
        
        if array.count == k {
            result.append(array)
            return
        }
        
        if index > n {
            return
        }
        
        // Recursive Backtracking
        var newArray = array
        newArray.append(index)
        backtrackingDFS(index+1, newArray)

        // Backtrack
        newArray.popLast()
        // We choose to ignore current element
        backtrackingDFS(index+1, newArray)
        
    }
    
    func combine(_ n: Int, _ k: Int) -> Array<Array<Int>>{
        self.n = n
        self.k = k
        backtrackingDFS(1, [])
        return result
    }
}
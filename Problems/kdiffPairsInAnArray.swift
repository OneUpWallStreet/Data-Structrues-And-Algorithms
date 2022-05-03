import Foundation


struct KDiffStruct: Hashable {
    let value: Int
    let index: Int
}


struct Pair: Hashable{
    let val1: Int
    let val2: Int
}

class Solution {
    
    var hashMap: [Int: KDiffStruct] = [:]
    
    func findPairs(_ nums: Array<Int>, _ k: Int) -> Int {
            
        for (index,value) in nums.enumerated() {
            let kDiffStruct = KDiffStruct(value: value, index: index)
            hashMap[value] = kDiffStruct
        }
        
        var counter: Int = 0
        
        var hashSetUsedPairs: Set<Pair> = []
        
        for (index,value) in nums.enumerated() {
            let diffValue = value - k

            if(hashMap[diffValue] != nil && hashMap[diffValue]!.index != index && hashSetUsedPairs.contains(Pair(val1: diffValue, val2: value)) == false){
                hashSetUsedPairs.insert(Pair(val1: diffValue, val2: value))
                counter += 1
                
            }
        }
        
        
        return counter;
    }
}




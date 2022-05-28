import Foundation


class Solution {
    
    private var hashMap: [[String.Element: Int] : Array<String>] = [:]
    

    
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        
        for str in strs {
            
            var singleStringHashMap: [String.Element: Int] = [:]
            
            for singleChar in str {
                
//              Key Exists
                if singleStringHashMap[singleChar] != nil {
                    singleStringHashMap[singleChar]! += 1
                }
//              Key Does not exist, so this is the first time we are
//              storing this char
                else{
                    singleStringHashMap[singleChar] = 1
                }
            }
            
            if(hashMap[singleStringHashMap] != nil) {
                hashMap[singleStringHashMap]!.append(str)
            }
            else{
                hashMap[singleStringHashMap] = [str]
            }
        }
        
        var answer: Array<Array<String>> = []
        
        for (_,value) in hashMap {
            answer.append(value)
        }
        
        return answer
    }
}

let solution = Solution()
let input: Array<String> = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(input))
//Output: [["bat"],["nat","tan"],["ate","eat","tea"]]




import Foundation

class Solution {
    
    private func initGraph(connections: Array<Array<Int>>, ignore: Array<Int>) -> [Int: Array<Int>] {
        
        var graph: [Int: Array<Int>] = [:]

        for connection in connections {
                        
            if(connection == ignore){
                continue
            }
                        
            if graph[connection[0]] == nil {
                graph[connection[0]] = [connection[1]]
            }
            else{
                graph[connection[0]]!.append(connection[1])
            }
            
            if graph[connection[1]] == nil {
                graph[connection[1]] = [connection[0]]
            }
            else{
                graph[connection[1]]!.append(connection[0])
            }

        }
        
        return graph
    }
    
    
    private func depthFirstSearch(_ node: Int,graph: [Int: Array<Int>]) -> Int{
        
        var stack: Array<Int> = []
        var alreadyVisited: Set<Int> = []

        //
        alreadyVisited.insert(node)
        stack.append(node)
        
        var count: Int = 1
        
        while(stack.count > 0){
            
            let current = stack.removeLast()
            
            let edges = graph[current]!
            
            
            for edge in edges {
                
                if(!alreadyVisited.contains(edge)){
                    alreadyVisited.insert(edge)
                    stack.append(edge)
                    count += 1
                    
                }
                
            }
            
        }
        
        return count
    }
    
    
    func criticalConnections(_ n: Int, _ connections: [[Int]]) -> [[Int]] {
        
        var result: Array<Array<Int>> = []
        
        if(n == 2){
            return connections
        }

        for connection in connections {
            let graph = initGraph(connections: connections,ignore: connection)
            if(depthFirstSearch(0, graph: graph) != n){
                result.append(connection)
            }
        }
        
        return result
        
    }
}


var solution = Solution()

let edges = [[0,1],[1,2],[2,0],[1,3]]

var result = solution.criticalConnections(2, edges)

print(result)















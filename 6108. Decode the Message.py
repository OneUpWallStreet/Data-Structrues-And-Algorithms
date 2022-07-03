class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        hashmap = dict()
        
        values = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        counter = 0
        
        for c in key:       
            if c == " ":
                continue
            if c not in hashmap:
                hashmap[c] = values[counter]
                counter += 1
            
        result = ""
        for c in message:
            if c == " ":
                result = result + c
                continue
            result = result + hashmap[c]
        
        return result
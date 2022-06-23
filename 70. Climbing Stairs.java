import java.util.HashMap;

class Solution {
    HashMap<Integer,Integer> cache = new HashMap<>();
    public int climbStairs(int n) {
        if(n==0){
            return 1;
        } else  if(n<0){
            return 0;
        } else if(cache.containsKey(n)){
            return cache.get(n);
        }
        cache.put(n,climbStairs(n-1) + climbStairs(n-2));
        return cache.get(n);
    }
}
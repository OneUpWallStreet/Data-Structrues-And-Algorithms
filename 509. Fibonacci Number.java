import java.util.HashMap;

class Solution {
    HashMap<Integer,Integer> map = new HashMap<>();
    public int fib(int n) {
        if(map.containsKey(n)){
            return map.get(n);
        }else if(n == 0){
            return 0;
        }else if(n==1 || n==2){
            return 1;
        }else{
            int a1 = fib(n-1);
            int a2 = fib(n-2);
            map.put(n-1,a1);
            map.put(n-2,a2);
            return a1+a2;
        }
    }
}
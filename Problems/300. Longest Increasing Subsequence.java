import java.util.*;



class Solution {

    private int longestCount = 1;
    private HashMap<Integer,Integer> cache = new HashMap<>();


    private int depthFirstTraversal(int index,int currentValue, int pathCount){


        if(cache.containsKey(index)){
            return pathCount + cache.get(index);
        }
        int oldPathCount = pathCount;

        for(int i = index+1;i<numbers.length;i++){
            if(numbers[i] > currentValue){
                pathCount = Math.max(pathCount,depthFirstTraversal(i,numbers[i],oldPathCount));
            }
        }

        cache.put(index,pathCount);

        return pathCount;
    }

    public int lengthOfLIS(int[] nums) {

        numbers = nums;
        for(int i = nums.length-1;i>=0;i--){
            longestCount = Math.max(depthFirstTraversal(i,numbers[i],1),longestCount);
        }

        return longestCount;
    }

    private int[] numbers;
}


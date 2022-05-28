import java.util.*;


class Solution {

    private int longestCount = 1;
    private HashMap<Integer,Integer> cache = new HashMap<>();


    private int depthFirstTraversal(int[] nums,int index,int currentValue, int pathCount){

        if(cache.containsKey(index)){
            return pathCount + cache.get(index);
        }
        int oldPathCount = pathCount;

        for(int i = index+1;i<nums.length;i++){
            if(nums[i] > currentValue){
                pathCount = Math.max(pathCount,depthFirstTraversal(nums,i,nums[i],oldPathCount));
            }
        }

        cache.put(index,pathCount);

        return pathCount;
    }

    public int lengthOfLIS(int[] nums) {

        for(int i = nums.length-1;i>=0;i--){
            longestCount = Math.max(depthFirstTraversal(nums,i,nums[i],1),longestCount);
        }

        return longestCount;
    }

}

